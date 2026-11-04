import functools
import warnings

from calagoapi.extensions.exceptions import ExtensionDeprecationWarning


# attribute marking a built-in member that an extension may take over
MIGRATED_ATTRIBUTE = '_calagoapi_migrated_to_'


def migrated_to(extension_id: str, package: str):
    '''
    Marks a built-in method that moved to an extension.

    The method keeps working, but warns (ExtensionDeprecationWarning) that it now
    lives in an extension package. When that extension is enabled in direct mode it
    replaces the built-in under the same name; any other extension trying to use the
    name still gets an ExtensionConflictError.

    Args:
        extension_id: Id of the extension that now provides the method.
        package: PyPI package of that extension, used in the warning.

    Example:
        class MinecraftServer(GenericServer):
            @migrated_to('version_changer', 'calagoapi-version-changer')
            def installVersion(self, build, ...):
                ...
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f'{func.__qualname__}() moved to the {package} extension. '
                f'Run "pip install {package}" and call calagoapi.extensions.enable({extension_id!r}); '
                f'the built-in version will be removed in a future major release.',
                ExtensionDeprecationWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)

        setattr(wrapper, MIGRATED_ATTRIBUTE, extension_id)
        return wrapper

    return decorator


def migratedTo(value):
    '''Returns the extension id a built-in member was handed to, or None'''
    return getattr(value, MIGRATED_ATTRIBUTE, None)
