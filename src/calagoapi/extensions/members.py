import threading
import types
import weakref

from calagoapi.extensions.exceptions import ExtensionDefinitionError


# attribute holding the MemberSpec list on decorated functions, properties and classes
SPEC_ATTRIBUTE = '_calagoapi_members_'

KINDS = ('method', 'property', 'service')

# service classes installed by any registry, so the async layer can recognise service instances
_service_classes = weakref.WeakSet()


class MemberSpec:
    '''
    What a decorator declared: "add this function/property/class to these classes
    under this name". Specs have no effect until an extension that owns them is enabled.

    Attributes:
        kind: 'method', 'property' or 'service'.
        targets: Tuple of classes the member is added to.
        name: Attribute name on the target (for services: the service name).
        value: The decorated function, property or class.
    '''
    def __init__(self, kind, targets, name, value):
        self.kind = kind
        self.targets = targets
        self.name = name
        self.value = value

    def __repr__(self):
        targets = ', '.join(t.__name__ for t in self.targets)
        return f'<{self.kind} {self.name!r} on {targets}>'

    @property
    def source(self) -> str:
        '''Where the member was defined, e.g. "calagoapi_version_changer.extension.installVersion".'''
        value = self.value.fget if isinstance(self.value, property) else self.value
        module = getattr(value, '__module__', None) or '?'
        qualname = getattr(value, '__qualname__', None) or self.name
        return f'{module}.{qualname}'


class ExtensionProperty(property):
    '''A property declared with @property_extension (a property that can carry a MemberSpec).'''


def _targets(target, decorator):
    targets = tuple(target) if isinstance(target, (list, tuple)) else (target,)
    if not targets:
        raise ExtensionDefinitionError(f'@{decorator}() needs at least one target class')
    for t in targets:
        if not isinstance(t, type):
            hint = f' Use @{decorator}(TargetClass), not bare @{decorator}.' if callable(t) else ''
            raise ExtensionDefinitionError(f'@{decorator}() targets must be classes, got {t!r}.{hint}')
    return targets


def _checkName(name, decorator):
    if not isinstance(name, str) or not name.isidentifier():
        raise ExtensionDefinitionError(f'@{decorator}(): member name must be a Python identifier, got {name!r}')
    if name.startswith('__') and name.endswith('__'):
        raise ExtensionDefinitionError(f'@{decorator}(): dunder names like {name!r} cannot be added by extensions')
    return name


def _attach(value, spec):
    specs = vars(value).get(SPEC_ATTRIBUTE)
    if specs is None:
        specs = []
        setattr(value, SPEC_ATTRIBUTE, specs)
    specs.append(spec)
    return value


def specsOf(value) -> list:
    '''Returns the MemberSpecs attached to a decorated object (not inherited ones)'''
    try:
        return list(vars(value).get(SPEC_ATTRIBUTE) or ())
    except TypeError:
        return []


def method(target, name: str = None):
    '''
    Declares a method an extension adds to one or more CalagoAPI classes.

    The function works like a normal method: `self` is the object it is called on.
    Both `def` and `async def` work; plain `def` is recommended, it is awaitable
    automatically on AsyncPanel objects.

    Args:
        target: The class (or a list of classes) to extend.
        name: Attribute name, defaults to the function name.

    Example:
        @method(MinecraftServer)
        def installVersion(self, build):
            ...
    '''
    targets = _targets(target, 'method')

    def decorator(func):
        if isinstance(func, (staticmethod, classmethod)):
            raise ExtensionDefinitionError('@method() cannot be used on staticmethod or classmethod objects')
        if not callable(func) or isinstance(func, type):
            raise ExtensionDefinitionError(f'@method() decorates functions, got {func!r}. Use @class_extension() for classes.')
        return _attach(func, MemberSpec('method', targets, _checkName(name or func.__name__, 'method'), func))

    return decorator


def property_extension(target, name: str = None):
    '''
    Declares a read-only property an extension adds to one or more CalagoAPI classes.

    Decorate a getter function, or pass a `property` object (for setters).

    Args:
        target: The class (or a list of classes) to extend.
        name: Attribute name, defaults to the function name.

    Example:
        @property_extension(MinecraftServer)
        def installedVersion(self):
            return self.getInstalledVersion()
    '''
    targets = _targets(target, 'property_extension')

    def decorator(value):
        if isinstance(value, ExtensionProperty):
            prop = value
        elif isinstance(value, property):
            prop = ExtensionProperty(value.fget, value.fset, value.fdel, value.__doc__)
        elif callable(value) and not isinstance(value, type):
            prop = None
        else:
            raise ExtensionDefinitionError(f'@property_extension() decorates a getter function or a property, got {value!r}')

        getter = prop.fget if prop is not None else value
        member_name = _checkName(name or getattr(getter, '__name__', None), 'property_extension')
        if prop is None:
            # keep the getter a plain function, the property is built when installed
            return _attach(value, MemberSpec('property', targets, member_name, value))
        return _attach(prop, MemberSpec('property', targets, member_name, prop))

    return decorator


def class_extension(target, name: str = None):
    '''
    Declares a service: a class attached to CalagoAPI objects under a name.

    The service is created on first access as `ServiceClass(obj)` and cached on the
    object, so `server.hungerbridge is server.hungerbridge`.

    Args:
        target: The class (or a list of classes) to extend.
        name: Attribute name, defaults to the class name in lowercase.

    Example:
        @class_extension(MinecraftServer, 'hungerbridge')
        class HungerBridge:
            def __init__(self, server):
                self.server = server

            def players(self):
                ...
    '''
    targets = _targets(target, 'class_extension')

    def decorator(cls):
        if not isinstance(cls, type):
            raise ExtensionDefinitionError(f'@class_extension() decorates classes, got {cls!r}')
        member_name = _checkName(name or cls.__name__.lower(), 'class_extension')
        return _attach(cls, MemberSpec('service', targets, member_name, cls))

    return decorator


def supportsInstanceDict(cls) -> bool:
    '''True if instances of cls have a __dict__ (needed to cache services and namespaces)'''
    return getattr(cls, '__dictoffset__', 0) != 0


class _CachedDescriptor:
    '''Creates a value on first access and stores it in the instance __dict__ under the same name'''
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.lock = threading.RLock()

    def create(self, obj):
        raise NotImplementedError

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        cache = obj.__dict__
        try:
            return cache[self.name]
        except KeyError:
            pass
        with self.lock:
            if self.name not in cache:
                cache[self.name] = self.create(obj)
            return cache[self.name]


class ServiceDescriptor(_CachedDescriptor):
    '''Installed on a class for every service. Builds `service_class(obj)` once per object.'''
    def __init__(self, name, owner, service_class):
        super().__init__(name, owner)
        self.service_class = service_class
        self.__doc__ = service_class.__doc__
        _service_classes.add(service_class)

    def create(self, obj):
        return self.service_class(obj)

    def __repr__(self):
        return f'<service {self.name!r} ({self.service_class.__name__}) from extension {self.owner!r}>'


class NamespaceDescriptor(_CachedDescriptor):
    '''Installed on a class for an extension enabled in namespace mode.'''
    def __init__(self, name, owner, members):
        super().__init__(name, owner)
        # shared {target class: {member name: (kind, value)}} for the whole extension
        self.members = members
        self.__doc__ = f'Members added by the {owner!r} extension.'

    def create(self, obj):
        return ExtensionNamespace(obj, self.name, self.owner, self.members)

    def __repr__(self):
        return f'<namespace {self.name!r} from extension {self.owner!r}>'


class ExtensionNamespace:
    '''
    The object behind `obj.<namespace>` for extensions enabled in namespace mode.

    Methods are bound to the original object, so inside them `self` is still the
    server (or whatever was extended), exactly as in direct mode.

    Example:
        enable('version_changer', mode='namespace')
        server.version_changer.installVersion(build)
    '''
    def __init__(self, obj, name, owner, members):
        object.__setattr__(self, '_obj', obj)
        object.__setattr__(self, '_name', name)
        object.__setattr__(self, '_owner', owner)
        object.__setattr__(self, '_members', members)

    def _lookup(self, name):
        for cls in type(self._obj).__mro__:
            member = self._members.get(cls, {}).get(name)
            if member is not None:
                return member
        return None

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        member = self._lookup(name)
        if member is None:
            raise AttributeError(
                f'{type(self._obj).__name__}.{self._name} (extension {self._owner!r}) has no member {name!r}. '
                f'Available: {", ".join(dir(self)) or "none"}')
        kind, value = member
        if kind == 'method':
            return types.MethodType(value, self._obj)
        return value.__get__(self._obj, type(self._obj))

    def __setattr__(self, name, value):
        member = self._lookup(name)
        if member is None or member[0] != 'property' or member[1].fset is None:
            raise AttributeError(f'cannot set {name!r} on the {self._name!r} namespace')
        member[1].__set__(self._obj, value)

    def __dir__(self):
        names = set()
        for cls in type(self._obj).__mro__:
            names.update(self._members.get(cls, {}))
        return sorted(names)

    def __repr__(self):
        return f'<namespace {self._name!r} of {self._obj!r} (extension {self._owner!r})>'


def isExtensionObject(value) -> bool:
    '''True for service instances and namespace objects (the async layer wraps these)'''
    return isinstance(value, ExtensionNamespace) or type(value) in _service_classes
