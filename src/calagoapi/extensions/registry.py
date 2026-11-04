import ast
import copy
import difflib
import inspect
import sys
import textwrap
import threading
import warnings
import weakref
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType

from calagoapi.extensions.base import (
    MODES,
    Extension,
    normalizeAliases,
    normalizeDependencies,
    validateExtensionClass,
)
from calagoapi.extensions.compat import migratedTo
from calagoapi.extensions.discovery import FIRST_PARTY, describeEntryPoint, entryPoints
from calagoapi.extensions.exceptions import (
    CircularDependencyError,
    ConfigurationError,
    DependencyError,
    ExtensionConflictError,
    ExtensionDefinitionError,
    ExtensionDeprecationWarning,
    ExtensionError,
    ExtensionLoadError,
    ExtensionNotEnabledError,
    ExtensionNotFoundError,
)
from calagoapi.extensions.members import (
    ExtensionProperty,
    NamespaceDescriptor,
    ServiceDescriptor,
    specsOf,
    supportsInstanceDict,
)


BUILTIN_OWNER = 'calagoapi'


@dataclass
class Registration:
    '''
    One member installed by an extension. The registry keeps one per installed
    attribute, plus one per member placed inside a namespace.

    Attributes:
        owner: Id of the extension that installed it.
        target: The class it was added to.
        name: Attribute name (for namespace members: the name inside the namespace).
        kind: 'method', 'property', 'service' or 'namespace'.
        member: The MemberSpec declared by the extension (None for namespaces).
        namespace: Namespace name, for members placed in a namespace, else None.
        replaced: The built-in this member took over (migration handover), else None.
    '''
    owner: str
    target: type
    name: str
    kind: str
    member: object = None
    namespace: str = None
    replaced: object = None

    def __str__(self):
        where = f'{self.target.__name__}.{self.namespace}.{self.name}' if self.namespace else f'{self.target.__name__}.{self.name}'
        return f'{where} ({self.kind}, from {self.owner!r})'


@dataclass
class _Planned:
    target: type
    name: str
    kind: str
    value: object
    member: object = None
    replaced: object = None


def _externalStacklevel() -> int:
    '''Stack level of the first frame outside calagoapi.extensions, for warnings'''
    frame = sys._getframe(1)
    level = 1
    while frame is not None and frame.f_globals.get('__name__', '').startswith('calagoapi.extensions'):
        frame = frame.f_back
        level += 1
    return level


def _allSubclasses(cls) -> list:
    result, stack = [], list(type.__subclasses__(cls))
    while stack:
        sub = stack.pop()
        if sub not in result:
            result.append(sub)
            stack.extend(type.__subclasses__(sub))
    return result


_instance_attribute_cache = weakref.WeakKeyDictionary()


def instanceAttributes(cls) -> frozenset:
    '''
    Names assigned as `self.<name> = ...` anywhere in a class body.

    Instance attributes shadow class attributes, so an extension member with one of
    these names would never be reached. Read from the class source; classes without
    source (C extensions, exec'd code) report nothing.
    '''
    try:
        return _instance_attribute_cache[cls]
    except (KeyError, TypeError):
        pass
    names = set()
    try:
        tree = ast.parse(textwrap.dedent(inspect.getsource(cls)))
    except (OSError, TypeError, SyntaxError, IndentationError):
        tree = None
    if tree is not None:
        for node in ast.walk(tree):
            if (isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Store)
                    and isinstance(node.value, ast.Name) and node.value.id == 'self'):
                names.add(node.attr)
    result = frozenset(names)
    try:
        _instance_attribute_cache[cls] = result
    except TypeError:
        pass
    return result


_async_reserved = None


def asyncReservedNames() -> frozenset:
    '''Public names defined by the async wrappers; members with these names would be unreachable on AsyncPanel'''
    global _async_reserved
    if _async_reserved is None:
        from calagoapi.aio.panel import AsyncWrapper, AsyncServer, AsyncPanel
        names = {'target'}
        for cls in (AsyncWrapper, AsyncServer, AsyncPanel):
            names.update(n for n in vars(cls) if not n.startswith('_'))
        _async_reserved = frozenset(names)
    return _async_reserved


def _ownerLabel(cls) -> str:
    module = getattr(cls, '__module__', '') or ''
    return BUILTIN_OWNER if module == 'calagoapi' or module.startswith('calagoapi.') else module


def _shortConfig(config, extension_class=None) -> str:
    '''Config as text for messages, with the extension's secret_config values masked'''
    secret = set(getattr(extension_class, 'secret_config', ()) or ())
    return repr({k: ('***' if k in secret and v is not None else v) for k, v in dict(config).items()})


class ExtensionRegistry:
    '''
    The authoritative record of extension state: discovery, known extensions, aliases,
    enabled extensions and their configuration, dependencies, and every member each
    extension installed (ownership).

    There is one process-global instance, `calagoapi.extensions.registry`; the
    module-level functions (`enable`, `register`, ...) use it.

    Example:
        from calagoapi.extensions import registry

        registry.enable('version_changer')
        print(registry.owner_of(MinecraftServer, 'installVersion'))   # 'version_changer'
        print(registry.describe())
    '''
    def __init__(self):
        self._lock = threading.RLock()
        self._entry_points = None        # entry point name -> [EntryPoint]
        self._loaded_entry_points = set()
        self._failed_entry_points = {}   # entry point name -> the ExtensionError it raised
        self._classes = {}               # extension id -> Extension subclass
        self._origins = {}               # extension id -> where it came from
        self._aliases = {}               # alias -> (extension id, Alias)
        self._enabled = {}               # extension id -> Extension instance, in enable order
        self._registrations = {}         # (target class, attribute name) -> Registration
        self._namespaced = []            # Registrations of members placed inside namespaces
        self._claimed = {}               # MemberSpec -> extension id

    def __repr__(self):
        return f'<ExtensionRegistry known={len(self._classes)} enabled={list(self._enabled)}>'

    # discovery
    def _entryPointIndex(self) -> dict:
        if self._entry_points is None:
            index = {}
            for entry_point in entryPoints():
                index.setdefault(entry_point.name, []).append(entry_point)
            self._entry_points = index
        return self._entry_points

    def discover(self) -> list:
        '''
        Rescans installed packages for "calagoapi" entry points (e.g. after a pip install
        at runtime) and returns the entry point names. Nothing is imported.
        '''
        with self._lock:
            self._entry_points = None
            self._failed_entry_points.clear()
            self._loaded_entry_points.clear()
            return sorted(self._entryPointIndex())

    def _loadEntryPoint(self, name):
        if name in self._failed_entry_points:
            raise self._failed_entry_points[name]
        if name in self._loaded_entry_points:
            return
        candidates = self._entryPointIndex().get(name, [])
        if not candidates:
            return
        self._loaded_entry_points.add(name)
        try:
            values = sorted({ep.value for ep in candidates})
            if len(values) > 1:
                sources = ', '.join(describeEntryPoint(ep) for ep in candidates)
                raise ExtensionConflictError(
                    f'Several installed packages provide the calagoapi extension {name!r}: {sources}. '
                    f'Uninstall one of them.', extension=name, member=name)
            entry_point = candidates[0]
            try:
                extension_class = entry_point.load()
            except Exception as e:
                raise ExtensionLoadError(
                    f'Could not load {describeEntryPoint(entry_point)}: {type(e).__name__}: {e}') from e
            if not (isinstance(extension_class, type) and issubclass(extension_class, Extension)):
                raise ExtensionLoadError(f'{describeEntryPoint(entry_point)} must point to a '
                                         f'calagoapi.extensions.Extension subclass, got {extension_class!r}')
            self._register(extension_class, describeEntryPoint(entry_point))
        except ExtensionError as e:
            # remembered: raised again when this name is asked for, listed when a lookup fails
            self._failed_entry_points[name] = e
            raise

    def _loadAll(self):
        for name in list(self._entryPointIndex()):
            try:
                self._loadEntryPoint(name)
            except ExtensionError:
                pass  # a broken or conflicting package must not block the others

    # registration
    def register(self, extension_class):
        '''
        Makes an Extension class known without an entry point (scripts, tests, examples).

        Registering the same class again is a no-op. Returns the class, so it can be
        used as a decorator.

        Example:
            @register
            class MyExtension(Extension):
                extension_id = 'my_extension'
        '''
        with self._lock:
            self._register(extension_class, f'registered from {extension_class.__module__}')
        return extension_class

    def _register(self, extension_class, origin):
        validateExtensionClass(extension_class)
        extension_id = extension_class.extension_id
        existing = self._classes.get(extension_id)
        if existing is extension_class:
            return
        if existing is not None:
            raise ExtensionConflictError(
                f'Two extensions use the id {extension_id!r}: {existing.__module__}.{existing.__qualname__} '
                f'({self._origins[extension_id]}) and {extension_class.__module__}.{extension_class.__qualname__} '
                f'({origin}). Extension ids must be globally unique.',
                extension=extension_id, owner=extension_id, member=extension_id)
        if extension_id in self._aliases:
            other = self._aliases[extension_id][0]
            raise ExtensionConflictError(
                f'The id of extension {extension_id!r} ({origin}) is already an alias of extension {other!r}. '
                f'Ids and aliases must be globally unique.',
                extension=extension_id, owner=other, member=extension_id)
        aliases = normalizeAliases(extension_class)
        for alias in aliases:
            if alias.name in self._classes:
                raise ExtensionConflictError(
                    f'Extension {extension_id!r} declares the alias {alias.name!r}, which is the id of another '
                    f'extension. Ids and aliases must be globally unique.',
                    extension=extension_id, owner=alias.name, member=alias.name)
            if alias.name in self._aliases:
                other = self._aliases[alias.name][0]
                raise ExtensionConflictError(
                    f'Extension {extension_id!r} declares the alias {alias.name!r}, already used by extension '
                    f'{other!r}. Ids and aliases must be globally unique.',
                    extension=extension_id, owner=other, member=alias.name)
        self._classes[extension_id] = extension_class
        self._origins[extension_id] = origin
        for alias in aliases:
            self._aliases[alias.name] = (extension_id, alias)

    # lookup
    def _find(self, name):
        if name in self._classes:
            return name, None
        if name in self._aliases:
            return self._aliases[name]
        return None, None

    def resolve(self, name: str):
        '''
        Returns `(extension_id, extension_class)` for an id or alias, loading the entry
        point if needed. Deprecated aliases emit an ExtensionDeprecationWarning.

        Raises:
            ExtensionNotFoundError: Nothing installed or registered has this name.
        '''
        if not isinstance(name, str):
            raise ExtensionNotFoundError(f'Extension ids are strings, got {name!r}', name)
        with self._lock:
            extension_id, alias = self._find(name)
            if extension_id is None:
                self._loadEntryPoint(name)
                extension_id, alias = self._find(name)
            if extension_id is None:
                # the id may have been renamed, or live only in an alias: load everything once
                self._loadAll()
                extension_id, alias = self._find(name)
            if extension_id is None:
                raise ExtensionNotFoundError(self._notFoundMessage(name), name)
            extension_class = self._classes[extension_id]
        if alias is not None and alias.deprecated:
            message = f'Extension name {name!r} is deprecated, use {extension_id!r} instead.'
            if alias.message:
                message += f' {alias.message}'
            warnings.warn(message, ExtensionDeprecationWarning, stacklevel=_externalStacklevel())
        return extension_id, extension_class

    def _notFoundMessage(self, name) -> str:
        known = sorted(set(self._classes) | set(self._aliases))
        lines = [f'Extension {name!r} is not installed.']
        close = difflib.get_close_matches(name, known, n=3)
        if close:
            lines.append(f'Did you mean: {", ".join(repr(c) for c in close)}?')
        if name in FIRST_PARTY:
            lines.append(f'Install it with: pip install {FIRST_PARTY[name]}')
        lines.append(f'Installed extensions: {", ".join(sorted(self._classes)) or "none"}.')
        for error in self._failed_entry_points.values():
            lines.append(f'Note: {error}')
        return '\n'.join(lines)

    def available(self) -> list:
        '''Ids of every installed or registered extension, sorted. Imports installed extension packages.'''
        with self._lock:
            self._loadAll()
            return sorted(self._classes)

    def get_class(self, extension_id: str):
        '''Returns the Extension class for an id or alias (enabled or not).'''
        return self.resolve(extension_id)[1]

    def is_enabled(self, extension_id: str) -> bool:
        '''True if the extension (id or alias) is enabled. Never imports anything.'''
        with self._lock:
            resolved, _ = self._find(extension_id)
            return resolved in self._enabled

    def get(self, extension_id: str) -> Extension:
        '''
        Returns the enabled Extension instance for an id or alias.

        Raises:
            ExtensionNotFoundError: The extension is not installed.
            ExtensionNotEnabledError: It is installed but not enabled.
        '''
        resolved, _ = self.resolve(extension_id)
        with self._lock:
            instance = self._enabled.get(resolved)
        if instance is None:
            raise ExtensionNotEnabledError(f'Extension {resolved!r} is not enabled. Call enable({resolved!r}) first.')
        return instance

    def enabled(self) -> list:
        '''Enabled Extension instances, in the order they were enabled.'''
        with self._lock:
            return list(self._enabled.values())

    # enabling
    def enable(self, extension_id: str, mode: str = None, config: dict = None) -> Extension:
        '''
        Enables an extension process-wide, after enabling its dependencies.

        Existing objects gain the extension's members immediately, future objects
        automatically. Calling it again is safe; changing the configuration or mode of
        an enabled extension raises ConfigurationError.

        Args:
            extension_id: Extension id or alias.
            mode: 'direct' or 'namespace'. None uses the extension's default_mode.
            config: Overrides for the extension's default_config.

        Returns:
            The Extension instance.
        '''
        with self._lock:
            return self._enable(extension_id, mode, config, None, ())

    def _enable(self, name, mode, config, enabled_by, path):
        extension_id, extension_class = self.resolve(name)
        if extension_id in path:
            cycle = list(path[path.index(extension_id):]) + [extension_id]
            raise CircularDependencyError(
                f'Circular extension dependency: {" -> ".join(cycle)}', cycle=cycle)
        if mode is not None and mode not in MODES:
            raise ConfigurationError(f'mode must be "direct" or "namespace", got {mode!r}')
        if config is not None and not isinstance(config, Mapping):
            raise ConfigurationError(f'config must be a dict, got {type(config).__name__}')

        current = self._enabled.get(extension_id)
        if current is not None:
            self._checkReenable(current, mode, config)
            return current

        for dependency in normalizeDependencies(extension_class):
            try:
                self.resolve(dependency.extension_id)
            except ExtensionNotFoundError as e:
                if dependency.optional:
                    continue
                hint = f' Install it with: pip install {FIRST_PARTY[dependency.extension_id]}' \
                    if dependency.extension_id in FIRST_PARTY else ''
                raise DependencyError(
                    f'Extension {extension_id!r} requires {dependency.extension_id!r}, which is not installed.{hint}'
                ) from e
            try:
                self._enable(dependency.extension_id, None, None, extension_id, path + (extension_id,))
            except DependencyError:
                raise
            except ExtensionError as e:
                raise DependencyError(
                    f'Extension {extension_id!r} could not enable its dependency {dependency.extension_id!r}: {e}'
                ) from e

        return self._activate(extension_id, extension_class, mode, config, enabled_by)

    def _mergeConfig(self, extension_class, config) -> dict:
        merged = copy.deepcopy(dict(extension_class.default_config))
        if config:
            unknown = sorted(set(config) - set(merged))
            if unknown and not extension_class.allow_unknown_config:
                known = ', '.join(sorted(merged)) or 'none'
                raise ConfigurationError(
                    f'Unknown config key(s) for extension {extension_class.extension_id!r}: '
                    f'{", ".join(unknown)}. Known keys: {known}.')
            merged.update(copy.deepcopy(dict(config)))
        return merged

    def _checkReenable(self, current, mode, config):
        extension_id = current.extension_id
        hint = ''
        if current.enabled_by:
            hint = (f' It was enabled automatically as a dependency of {current.enabled_by!r}; to choose its '
                    f'mode or configuration, enable {extension_id!r} before {current.enabled_by!r}.')
        if mode is not None and mode != current.mode:
            raise ConfigurationError(
                f'Extension {extension_id!r} is already enabled in {current.mode!r} mode and cannot be '
                f're-enabled in {mode!r} mode.{hint}')
        if config is not None:
            requested = self._mergeConfig(type(current), config)
            if requested != current._merged_config:
                raise ConfigurationError(
                    f'Extension {extension_id!r} is already enabled with a different configuration.\n'
                    f'  enabled with: {_shortConfig(current._merged_config, type(current))}\n'
                    f'  requested:    {_shortConfig(requested, type(current))}\n'
                    f'Extensions cannot be reconfigured once enabled.{hint}')

    def _activate(self, extension_id, extension_class, mode, config, enabled_by):
        merged = self._mergeConfig(extension_class, config)
        try:
            instance = extension_class()
        except Exception as e:
            raise ExtensionLoadError(f'Could not create extension {extension_id!r}: {type(e).__name__}: {e}') from e
        instance.mode = mode or extension_class.default_mode
        instance.namespace = extension_class.namespace or extension_id
        instance.enabled_by = enabled_by
        instance._merged_config = merged

        try:
            validated = instance.validate_config(copy.deepcopy(merged))
        except ConfigurationError:
            raise
        except Exception as e:
            raise ConfigurationError(f'Invalid configuration for extension {extension_id!r}: {e}') from e
        if validated is None:
            validated = merged
        if not isinstance(validated, Mapping):
            raise ExtensionDefinitionError(f'{extension_class.__name__}.validate_config() must return a dict')
        instance.config = MappingProxyType(dict(validated))

        specs = self._collectMembers(extension_class)
        plan, namespaced = self._plan(instance, specs)

        installed = []
        try:
            for item in plan:
                try:
                    setattr(item.target, item.name, item.value)
                except (TypeError, AttributeError) as e:
                    raise ExtensionDefinitionError(
                        f'Extension {extension_id!r} cannot add {item.name!r} to {item.target.__name__}: {e}') from e
                registration = Registration(extension_id, item.target, item.name, item.kind, item.member,
                                            replaced=item.replaced)
                self._registrations[(item.target, item.name)] = registration
                installed.append(registration)
            self._namespaced.extend(namespaced)
            for spec in specs:
                self._claimed[spec] = extension_id
            self._enabled[extension_id] = instance
            setattr(extension_class, '_enabled_instance', instance)
            try:
                instance.on_enable()
            except ExtensionError:
                raise
            except Exception as e:
                raise ExtensionError(f'on_enable() of extension {extension_id!r} failed: {type(e).__name__}: {e}') from e
        except BaseException:
            self._rollback(extension_id, installed)
            raise
        return instance

    def _collectMembers(self, extension_class) -> list:
        explicit = extension_class.members is not None
        if explicit:
            values = list(extension_class.members)
        else:
            module = sys.modules.get(extension_class.__module__)
            values = list(vars(module).values()) if module is not None else []
        package = extension_class.__module__.split('.')[0]

        specs = []
        for value in values:
            found = specsOf(value)
            if explicit and not found:
                raise ExtensionDefinitionError(
                    f'{extension_class.__name__}.members contains {value!r}, which is not decorated with '
                    f'@method, @property_extension or @class_extension')
            for spec in found:
                # module scanning only picks up members from the extension's own package
                if not explicit and spec.source.split('.')[0] != package:
                    continue
                if spec not in specs:
                    specs.append(spec)

        for spec in specs:
            owner = self._claimed.get(spec)
            if owner is not None and owner != extension_class.extension_id:
                raise ExtensionDefinitionError(
                    f'{spec} ({spec.source}) already belongs to extension {owner!r}. A member can belong to one '
                    f'extension only; if several extensions live in one module, give each an explicit `members` list.')
        return specs

    def _plan(self, instance, specs):
        extension_id = instance.extension_id
        plan, namespaced, seen = [], [], set()
        namespace_members = {}

        for spec in specs:
            for target in spec.targets:
                value = spec.value
                if spec.kind == 'property' and not isinstance(value, property):
                    value = ExtensionProperty(value, doc=value.__doc__)

                if spec.kind == 'service' or instance.mode == 'direct':
                    if (target, spec.name) in seen:
                        raise ExtensionDefinitionError(
                            f'Extension {extension_id!r} declares {spec.name!r} on {target.__name__} twice')
                    seen.add((target, spec.name))
                    if spec.kind == 'service':
                        value = ServiceDescriptor(spec.name, extension_id, spec.value)
                    plan.append(_Planned(target, spec.name, spec.kind, value, spec))
                else:
                    members = namespace_members.setdefault(target, {})
                    if spec.name in members:
                        raise ExtensionDefinitionError(
                            f'Extension {extension_id!r} declares {spec.name!r} on {target.__name__} twice')
                    members[spec.name] = (spec.kind, value)
                    namespaced.append(Registration(extension_id, target, spec.name, spec.kind, spec,
                                                   namespace=instance.namespace))

        if namespace_members:
            descriptor = NamespaceDescriptor(instance.namespace, extension_id, namespace_members)
            targets = list(namespace_members)
            for target in targets:
                # one descriptor on the most general classes is enough, lookups walk the MRO
                if any(other is not target and issubclass(target, other) for other in targets):
                    continue
                if (target, instance.namespace) in seen:
                    raise ExtensionDefinitionError(
                        f'Extension {extension_id!r} uses {instance.namespace!r} both as its namespace and as a '
                        f'service name on {target.__name__}')
                plan.append(_Planned(target, instance.namespace, 'namespace', descriptor))

        for item in plan:
            self._checkConflicts(instance, item)
        return plan, namespaced

    def _checkConflicts(self, instance, item):
        extension_id = instance.extension_id
        target, name = item.target, item.name
        label = f'{item.kind} {name!r}'

        def conflict(owner, detail):
            raise ExtensionConflictError(
                f'Extension {extension_id!r} cannot add {label} to {target.__name__}: {detail}',
                extension=extension_id, owner=owner, target=target, member=name)

        if item.kind in ('service', 'namespace') and not supportsInstanceDict(target):
            raise ExtensionDefinitionError(
                f'Extension {extension_id!r} cannot add {label} to {target.__name__}: its instances have no '
                f'__dict__ (__slots__), so the {item.kind} cannot be cached')

        # other extensions: same name on this class, a base class or a subclass
        for (other_target, other_name), registration in self._registrations.items():
            if other_name != name or registration.owner == extension_id:
                continue
            if issubclass(target, other_target) or issubclass(other_target, target):
                conflict(registration.owner,
                         f'it is already provided by extension {registration.owner!r} '
                         f'({registration.kind} on {other_target.__name__}).')

        # built-ins: defined in the MRO or on a subclass, or set as an instance attribute
        aliases = {extension_id} | {a.name for a in normalizeAliases(type(instance))}
        for cls in target.__mro__:
            if name in vars(cls) and (cls, name) not in self._registrations:
                existing = vars(cls)[name]
                if (cls is target and item.kind == 'method' and migratedTo(existing) in aliases):
                    item.replaced = existing  # migration handover from core
                    break
                conflict(_ownerLabel(cls), f'{cls.__name__} already defines {name!r} '
                                           f'({_ownerLabel(cls)} built-in). Extensions never replace existing members.')
        for sub in _allSubclasses(target):
            if name in vars(sub) and (sub, name) not in self._registrations:
                conflict(_ownerLabel(sub), f'the subclass {sub.__name__} already defines {name!r}, which would hide '
                                           f'the extension member there.')
        for cls in list(target.__mro__) + _allSubclasses(target):
            if cls is not object and name in instanceAttributes(cls):
                conflict(_ownerLabel(cls), f'{cls.__name__} sets the instance attribute self.{name}, which would '
                                           f'hide the extension member.')

        if name in asyncReservedNames():
            conflict(BUILTIN_OWNER, f'{name!r} is used by the async wrappers (AsyncPanel), so the member would '
                                    f'be unreachable there.')

    def _rollback(self, extension_id, installed):
        '''Undo a failed enable. Internal: extensions cannot be disabled once enabled.'''
        for registration in reversed(installed):
            if registration.replaced is not None:
                setattr(registration.target, registration.name, registration.replaced)
            else:
                try:
                    delattr(registration.target, registration.name)
                except AttributeError:
                    pass
            self._registrations.pop((registration.target, registration.name), None)
        self._namespaced = [r for r in self._namespaced if r.owner != extension_id]
        for spec, owner in list(self._claimed.items()):
            if owner == extension_id:
                del self._claimed[spec]
        instance = self._enabled.pop(extension_id, None)
        extension_class = self._classes.get(extension_id)
        if extension_class is not None and extension_class.__dict__.get('_enabled_instance') is instance:
            try:
                delattr(extension_class, '_enabled_instance')
            except AttributeError:
                pass

    def _reset_for_tests(self):
        '''Removes everything this registry installed. For test suites only; there is no public disable().'''
        with self._lock:
            for extension_id in reversed(list(self._enabled)):
                installed = [r for r in self._registrations.values() if r.owner == extension_id]
                self._rollback(extension_id, installed)

    # introspection
    def registrations(self, owner: str = None, target: type = None, namespaced: bool = True) -> list:
        '''
        Returns installed members as Registration records.

        Args:
            owner: Only members of this extension (id or alias).
            target: Only members added to this class.
            namespaced: Include members placed inside namespaces.

        Example:
            for r in registry.registrations(owner='version_changer'):
                print(r)    # MinecraftServer.installVersion (method, from 'version_changer')
        '''
        with self._lock:
            if owner is not None:
                owner = self._find(owner)[0] or owner
            items = list(self._registrations.values()) + (list(self._namespaced) if namespaced else [])
        return [r for r in items
                if (owner is None or r.owner == owner) and (target is None or r.target is target)]

    def owner_of(self, target: type, name: str) -> str:
        '''
        Returns which extension provides `name` on `target` (or a base class), or None
        for built-ins and unknown names.

        Example:
            registry.owner_of(MinecraftServer, 'installVersion')   # 'version_changer'
        '''
        with self._lock:
            for cls in target.__mro__:
                registration = self._registrations.get((cls, name))
                if registration is not None:
                    return registration.owner
        return None

    def describe(self) -> str:
        '''A readable summary of every enabled extension, its configuration and members.'''
        with self._lock:
            if not self._enabled:
                return 'No extensions enabled.'
            lines = []
            for extension_id, instance in self._enabled.items():
                meta = instance.metadata
                origin = f', enabled by {instance.enabled_by!r}' if instance.enabled_by else ''
                lines.append(f'{extension_id} {meta.version} by {meta.author or "unknown"} '
                             f'[{instance.mode}{origin}] ({self._origins.get(extension_id)})')
                lines.append(f'  config: {_shortConfig(instance.config, type(instance))}')
                for registration in self.registrations(owner=extension_id):
                    lines.append(f'  {registration}')
            return '\n'.join(lines)
