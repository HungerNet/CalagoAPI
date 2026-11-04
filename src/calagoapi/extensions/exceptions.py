# Extension system exceptions
from calagoapi.utils.exceptions import CalagoAPIError


class ExtensionError(CalagoAPIError):
    '''
    Base class for every extension system error.

    Example:
        from calagoapi.extensions import enable, ExtensionError

        try:
            enable('hungerbridge')
        except ExtensionError as e:
            print(e)
    '''
    def __init__(self, message):
        super().__init__(message)


class ExtensionNotFoundError(ExtensionError, LookupError):
    '''No installed or registered extension has this id or alias.'''
    def __init__(self, message, extension_id=None):
        super().__init__(message)
        self.extension_id = extension_id


class ExtensionLoadError(ExtensionError):
    '''An extension entry point could not be imported, or does not point to an Extension class.'''


class ExtensionDefinitionError(ExtensionError, TypeError):
    '''An Extension class or one of its members is invalid (bad id, bad mode, bad member name, ...).'''


class ExtensionConflictError(ExtensionError):
    '''
    Two things want the same name: two extensions with the same id or alias, or an
    extension member that would replace something that already exists.

    Attributes:
        extension: Id of the extension being loaded.
        owner: Who already provides the name (an extension id, or 'calagoapi' for built-ins).
        target: The class the member was going to be added to, or None.
        member: The conflicting attribute name, id or alias.
    '''
    def __init__(self, message, extension=None, owner=None, target=None, member=None):
        super().__init__(message)
        self.extension = extension
        self.owner = owner
        self.target = target
        self.member = member


class DependencyError(ExtensionError):
    '''A dependency is missing or could not be enabled.'''


class CircularDependencyError(DependencyError):
    '''
    Extensions depend on each other in a loop.

    Attributes:
        cycle: The extension ids forming the loop, e.g. ['a', 'b', 'a'].
    '''
    def __init__(self, message, cycle=None):
        super().__init__(message)
        self.cycle = cycle or []


class ConfigurationError(ExtensionError, ValueError):
    '''Invalid configuration, or an attempt to re-enable an extension with a different configuration or mode.'''


class ExtensionNotEnabledError(ExtensionError):
    '''The extension exists but enable() has not been called for it.'''


class ExtensionDeprecationWarning(DeprecationWarning):
    '''Warns about a deprecated extension alias or a built-in feature that moved to an extension.'''
