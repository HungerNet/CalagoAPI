import re
from dataclasses import dataclass

from calagoapi.extensions.exceptions import ExtensionDefinitionError, ExtensionNotEnabledError


# metadata schema versions this CalagoAPI understands
SUPPORTED_SCHEMAS = (1,)

MODES = ('direct', 'namespace')

ID_PATTERN = re.compile(r'^[a-z][a-z0-9_]*$')


@dataclass(frozen=True)
class ExtensionMetadata:
    '''
    Describes an extension.

    Args:
        author: Who maintains the extension.
        version: The extension's own version, e.g. '1.0.0'.
        schema: Metadata schema version. Only 1 exists today; a newer CalagoAPI
            may add fields under a higher schema number.
        description: One line describing what the extension adds.
        package: PyPI distribution name, shown in "pip install ..." hints.
        homepage: Project or documentation URL.

    Example:
        metadata = ExtensionMetadata(author='iFamished', version='1.0.0', schema=1)
    '''
    author: str = None
    version: str = '0.0.0'
    schema: int = 1
    description: str = None
    package: str = None
    homepage: str = None


@dataclass(frozen=True)
class Alias:
    '''
    Another name an extension can be enabled with, usually its old id after a rename.

    Args:
        name: The alias.
        deprecated: Emit an ExtensionDeprecationWarning when the alias is used.
        message: Optional text appended to the warning.

    Example:
        aliases = ['version_changer', Alias('mc_versions', deprecated=True)]
    '''
    name: str
    deprecated: bool = False
    message: str = None


@dataclass(frozen=True)
class Dependency:
    '''
    An extension this extension needs. Plain strings in `dependencies` are turned into
    Dependency objects; use the class directly for options.

    Args:
        extension_id: Id or alias of the required extension.
        optional: Enable it if installed, skip it silently otherwise.

    Example:
        dependencies = ['version_changer', Dependency('metrics', optional=True)]
    '''
    extension_id: str
    optional: bool = False


class Extension:
    '''
    Base class for every CalagoAPI extension.

    Subclass it, set the class attributes, and expose the class through the
    "calagoapi" entry point group (or call `register()` for local extensions).
    CalagoAPI creates the instance itself when the extension is enabled.

    Class attributes:
        extension_id: Public, globally unique id, used with enable(). Lowercase
            letters, digits and underscores, starting with a letter.
        metadata: ExtensionMetadata (author, version, schema).
        aliases: Other names the extension can be enabled with (strings or Alias).
        dependencies: Extensions enabled automatically first (strings or Dependency).
        default_mode: 'direct' (members appear on the object) or 'namespace'
            (members appear under `obj.<namespace>`).
        namespace: Attribute name used in namespace mode. Defaults to extension_id.
        default_config: Default configuration, merged with the user's config.
        allow_unknown_config: Accept config keys missing from default_config.
        secret_config: Config keys holding secrets (tokens, passwords); shown as
            *** in describe() and error messages.
        members: Explicit list of decorated members. None collects every decorated
            member found in the module that defines the Extension class.

    Instance attributes (set when enabled):
        config: The effective configuration (read-only mapping).
        mode: 'direct' or 'namespace'.
        namespace: The namespace attribute name.
        enabled_by: Id of the extension that enabled this one as a dependency, or None.

    Example:
        class VersionChangerExtension(Extension):
            extension_id = 'version_changer'
            metadata = ExtensionMetadata(author='iFamished', version='1.0.0', schema=1)
            default_mode = 'direct'
            default_config = {'auto_backup': False}

            def on_enable(self):
                print('version changer ready, config:', dict(self.config))
    '''
    extension_id = None
    metadata = ExtensionMetadata()
    aliases = ()
    dependencies = ()
    default_mode = 'direct'
    namespace = None
    default_config = {}
    allow_unknown_config = False
    secret_config = ()
    members = None

    def __init__(self):
        self.config = None
        self.mode = None
        self.enabled_by = None

    def __repr__(self):
        state = f'mode={self.mode!r}' if self.mode else 'not enabled'
        return f'<Extension {self.extension_id!r} {state}>'

    # lifecycle hooks, override what you need
    def validate_config(self, config: dict) -> dict:
        '''
        Checks the merged configuration before anything is installed.

        Return the (optionally normalized) config, or raise ConfigurationError.
        Called once per enable, before on_enable().
        '''
        return config

    def on_enable(self) -> None:
        '''Called once after every member is installed. Raising here undoes the enable.'''

    @classmethod
    def get(cls) -> 'Extension':
        '''
        Returns the enabled instance of this extension class.

        Handy inside extension members to read the configuration:

            @method(MinecraftServer)
            def installVersion(self, build):
                config = VersionChangerExtension.get().config
        '''
        instance = cls.__dict__.get('_enabled_instance')
        if instance is None:
            raise ExtensionNotEnabledError(
                f'Extension {cls.extension_id!r} is not enabled. Call enable({cls.extension_id!r}) first.')
        return instance


def normalizeAliases(extension_class):
    '''Returns the extension's aliases as Alias objects'''
    aliases = extension_class.aliases or ()
    if isinstance(aliases, (str, Alias)):
        aliases = [aliases]
    result = []
    for alias in aliases:
        if isinstance(alias, str):
            alias = Alias(alias)
        if not isinstance(alias, Alias):
            raise ExtensionDefinitionError(
                f'{extension_class.__name__}.aliases must contain strings or Alias objects, got {alias!r}')
        result.append(alias)
    return result


def normalizeDependencies(extension_class):
    '''Returns the extension's dependencies as Dependency objects'''
    dependencies = extension_class.dependencies or ()
    if isinstance(dependencies, (str, Dependency)):
        dependencies = [dependencies]
    result = []
    for dependency in dependencies:
        if isinstance(dependency, str):
            dependency = Dependency(dependency)
        if not isinstance(dependency, Dependency):
            raise ExtensionDefinitionError(
                f'{extension_class.__name__}.dependencies must contain strings or Dependency objects, got {dependency!r}')
        result.append(dependency)
    return result


def validateExtensionClass(extension_class):
    '''Raises ExtensionDefinitionError if an Extension subclass is not usable'''
    if not (isinstance(extension_class, type) and issubclass(extension_class, Extension)):
        raise ExtensionDefinitionError(f'{extension_class!r} is not a subclass of calagoapi.extensions.Extension')
    name = extension_class.__name__
    extension_id = extension_class.extension_id

    if not isinstance(extension_id, str) or not ID_PATTERN.match(extension_id):
        raise ExtensionDefinitionError(
            f'{name}.extension_id must be lowercase letters, digits and underscores, starting with a letter '
            f'(e.g. "version_changer"), got {extension_id!r}')
    for alias in normalizeAliases(extension_class):
        if not ID_PATTERN.match(alias.name):
            raise ExtensionDefinitionError(f'{name}: alias {alias.name!r} is not a valid extension id')
        if alias.name == extension_id:
            raise ExtensionDefinitionError(f'{name}: alias {alias.name!r} is the same as the extension id')
    normalizeDependencies(extension_class)

    metadata = extension_class.metadata
    if not isinstance(metadata, ExtensionMetadata):
        raise ExtensionDefinitionError(f'{name}.metadata must be an ExtensionMetadata, got {metadata!r}')
    if metadata.schema not in SUPPORTED_SCHEMAS:
        raise ExtensionDefinitionError(
            f'{name} uses metadata schema {metadata.schema}, this CalagoAPI supports {list(SUPPORTED_SCHEMAS)}. '
            f'Upgrade calagoapi.')

    if extension_class.default_mode not in MODES:
        raise ExtensionDefinitionError(f'{name}.default_mode must be "direct" or "namespace", got {extension_class.default_mode!r}')
    namespace = extension_class.namespace
    if namespace is not None and (not isinstance(namespace, str) or not namespace.isidentifier() or namespace.startswith('_')):
        raise ExtensionDefinitionError(f'{name}.namespace must be a public Python identifier, got {namespace!r}')
    if not isinstance(extension_class.default_config, dict):
        raise ExtensionDefinitionError(f'{name}.default_config must be a dict')
    if extension_class.members is not None and not isinstance(extension_class.members, (list, tuple)):
        raise ExtensionDefinitionError(f'{name}.members must be a list or None')
