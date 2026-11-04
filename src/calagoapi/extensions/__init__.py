'''
CalagoAPI extensions: add methods, properties and services to CalagoAPI classes
from separately installed packages.

Example:
    from calagoapi.extensions import enable

    enable('version_changer')
    server.installVersion(build)
    print(server.installedVersion)

    enable('hungerbridge', config={'token': 'id:secret'})
    server.hungerbridge.players()

See docs/learning/extensions.md for the full guide.
'''
from .base import Extension, ExtensionMetadata, Alias, Dependency
from .members import method, property_extension, class_extension, MemberSpec, ExtensionNamespace
from .registry import ExtensionRegistry, Registration
from .compat import migrated_to
from .discovery import ENTRY_POINT_GROUP
from .exceptions import (
    ExtensionError,
    ExtensionNotFoundError,
    ExtensionLoadError,
    ExtensionDefinitionError,
    ExtensionConflictError,
    DependencyError,
    CircularDependencyError,
    ConfigurationError,
    ExtensionNotEnabledError,
    ExtensionDeprecationWarning,
)


# the process-global registry
registry = ExtensionRegistry()


def enable(extension_id: str, mode: str = None, config: dict = None) -> Extension:
    '''
    Enables an extension for the whole process.

    Dependencies are enabled first. Objects that already exist gain the extension's
    members immediately, objects created later get them automatically. Calling it
    again is safe; re-enabling with a different config or mode raises ConfigurationError.

    Args:
        extension_id: The extension id or one of its aliases.
        mode: 'direct' (members on the object) or 'namespace' (members under
            `obj.<namespace>`). Defaults to the extension's default_mode.
        config: Values overriding the extension's default_config.

    Returns:
        The enabled Extension instance.

    Raises:
        ExtensionNotFoundError: The extension is not installed.
        DependencyError: A dependency is missing or circular.
        ExtensionConflictError: A member would replace something that already exists.
        ConfigurationError: Invalid config, or a different config/mode than before.

    Example:
        enable('version_changer')
        enable('hungerbridge', mode='namespace', config={'mc_version': '1.21.11'})
    '''
    return registry.enable(extension_id, mode=mode, config=config)


def register(extension_class):
    '''
    Registers an Extension class without an entry point, for scripts, notebooks and
    tests. Can be used as a class decorator. Published packages should use entry points.

    Example:
        @register
        class GreeterExtension(Extension):
            extension_id = 'greeter'

        enable('greeter')
    '''
    return registry.register(extension_class)


def get_extension(extension_id: str) -> Extension:
    '''
    Returns the enabled Extension instance (for its config, mode and metadata).

    Example:
        get_extension('hungerbridge').config['port']
    '''
    return registry.get(extension_id)


def is_enabled(extension_id: str) -> bool:
    '''Returns True if the extension (id or alias) is enabled.'''
    return registry.is_enabled(extension_id)


def available() -> list:
    '''Returns the ids of every installed or registered extension.'''
    return registry.available()


def enabled_extensions() -> list:
    '''Returns the enabled Extension instances, in the order they were enabled.'''
    return registry.enabled()


__all__ = [
    'enable',
    'register',
    'get_extension',
    'is_enabled',
    'available',
    'enabled_extensions',
    'registry',
    'ExtensionRegistry',
    'Registration',

    # defining extensions
    'Extension',
    'ExtensionMetadata',
    'Alias',
    'Dependency',
    'method',
    'property_extension',
    'class_extension',
    'MemberSpec',
    'ExtensionNamespace',
    'migrated_to',
    'ENTRY_POINT_GROUP',

    # errors
    'ExtensionError',
    'ExtensionNotFoundError',
    'ExtensionLoadError',
    'ExtensionDefinitionError',
    'ExtensionConflictError',
    'DependencyError',
    'CircularDependencyError',
    'ConfigurationError',
    'ExtensionNotEnabledError',
    'ExtensionDeprecationWarning',
]
