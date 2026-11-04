'''
The Calagopus Minecraft Version Changer as a CalagoAPI extension.

    from calagoapi.extensions import enable

    enable('version_changer')
    build = server.getBuilds('PAPER', '1.21.11', page=1, per_page=1)[0]
    server.installVersion(build)
    print(server.installedVersion['name'])
'''
from calagoapi import MinecraftServer
from calagoapi.admin.admin import ExtensionManager
from calagoapi.extensions import (
    ConfigurationError,
    Extension,
    ExtensionMetadata,
    method,
    property_extension,
)
from calagoapi.utils.exceptions import InvalidActionError
from calagoapi.utils.model import idOf

from calagoapi_version_changer import __version__
from calagoapi_version_changer.api import VersionChangerAPI


def _api(obj) -> VersionChangerAPI:
    return VersionChangerAPI(obj.panel.client)


# MinecraftServer methods
@method(MinecraftServer)
def getInstalledVersion(self) -> dict:
    '''
    Returns what the Version Changer knows about the installed build:
    `{'build': {...}, 'latest': {...}}`, or None if the server was not installed with it.

    Example:
        info = server.getInstalledVersion()
        if info:
            print(info['build']['name'], 'latest:', info['latest']['name'])
    '''
    return _api(self).installed(self.server_id)


@property_extension(MinecraftServer)
def installedVersion(self) -> dict:
    '''
    The installed build (type, name, version_id, ...), or None. Makes a request each
    time it is read; in async code prefer `await server.getInstalledVersion()`.

    Example:
        print(server.installedVersion['name'])
    '''
    installed = getInstalledVersion(self)
    return installed.get('build') if installed else None


@method(MinecraftServer)
def isUpToDate(self) -> bool:
    '''
    Returns True if the installed build is the newest build of its version, None if unknown.

    Example:
        if server.isUpToDate() is False:
            server.updateVersion()
    '''
    installed = getInstalledVersion(self)
    if not installed or not installed.get('build') or not installed.get('latest'):
        return None
    return installed['build'].get('uuid') == installed['latest'].get('uuid')


@method(MinecraftServer)
def getVersionTypes(self) -> dict:
    '''Returns the available server types (PAPER, PURPUR, FABRIC, VANILLA, ...).'''
    return _api(self).types(self.server_id)


@method(MinecraftServer)
def getVersions(self, type: str, search: str = None, page: int = None, per_page: int = None):
    '''
    Returns the Minecraft versions available for a server type.

    Example:
        server.getVersions('PAPER', page=1, per_page=10)
    '''
    return _api(self).versions(self.server_id, type, search, page, per_page)


@method(MinecraftServer)
def getBuilds(self, type: str, version: str, search: str = None, page: int = None, per_page: int = None):
    '''
    Returns the builds of a version, newest first.

    Example:
        latest = server.getBuilds('PAPER', '1.21.11', page=1, per_page=1)[0]
    '''
    return _api(self).builds(self.server_id, type, version, search, page, per_page)


@method(MinecraftServer)
def installVersion(self, build, truncate_directory: bool = False, accept_eula: bool = True) -> None:
    '''
    Installs a server build.

    With `auto_backup` enabled in the extension config, a backup is made first and
    the install only starts once it succeeded.

    Args:
        build: Build dict from getBuilds() or build UUID.
        truncate_directory: Delete every file first.
        accept_eula: Accept the Minecraft EULA.

    Example:
        latest = server.getBuilds('PAPER', '1.21.11', page=1, per_page=1)[0]
        server.installVersion(latest)
    '''
    config = VersionChangerExtension.get().config
    build_id = build.get('uuid') if isinstance(build, dict) else idOf(build)
    if config['auto_backup']:
        backup = self.backups.createBackup(name=config['backup_name'])
        backup.waitUntilComplete(timeout=config['backup_timeout'])
        if not backup.isSuccessful():
            raise InvalidActionError(f'The backup before installing {build_id} failed; nothing was installed.')
    return _api(self).install(self.server_id, build_id, truncate_directory, accept_eula)


@method(MinecraftServer)
def updateVersion(self, truncate_directory: bool = False) -> bool:
    '''
    Installs the newest build of the installed version. Returns False if already up to date.

    Example:
        server.updateVersion()
    '''
    # sibling members are called directly so this works in direct and namespace mode
    installed = getInstalledVersion(self)
    if not installed or not installed.get('latest'):
        raise InvalidActionError('The installed version is unknown, use installVersion() instead.')
    if isUpToDate(self):
        return False
    installVersion(self, installed['latest'], truncate_directory=truncate_directory)
    return True


# panel.admin.extensions methods (admin API key required)
@method(ExtensionManager)
def getVersionChangerSettings(self) -> dict:
    '''Returns the Minecraft Version Changer settings.'''
    return _api(self).settings()


@method(ExtensionManager)
def updateVersionChangerSettings(self, **settings) -> None:
    '''Changes Version Changer settings (mcjars_url, mcjars_api_key, type_egg_assignments, ...).'''
    return _api(self).updateSettings(settings)


@method(ExtensionManager)
def getVersionChangerStatistics(self) -> dict:
    '''Returns install statistics by server type and version.'''
    return _api(self).statistics()


@method(ExtensionManager)
def getVersionChangerDefaultOrder(self) -> list:
    '''Returns the default order of server types in the version picker.'''
    return _api(self).defaultOrder()


class VersionChangerExtension(Extension):
    '''
    Calagopus Minecraft Version Changer: list and install Paper, Purpur, Fabric,
    Forge, ... builds on Minecraft servers.

    Config:
        auto_backup: Make a backup before every installVersion() (default False).
        backup_name: Name of that backup.
        backup_timeout: Seconds to wait for the backup.
    '''
    extension_id = 'version_changer'
    aliases = ['minecraft_version_changer']
    metadata = ExtensionMetadata(
        author='iFamished',
        version=__version__,
        schema=1,
        description='Calagopus Minecraft Version Changer for CalagoAPI',
        package='calagoapi-version-changer',
        homepage='https://github.com/HungerNet/CalagoAPI',
    )
    default_mode = 'direct'
    default_config = {
        'auto_backup': False,
        'backup_name': 'Before version change',
        'backup_timeout': 3600,
    }

    def validate_config(self, config):
        if not isinstance(config['auto_backup'], bool):
            raise ConfigurationError('version_changer: auto_backup must be True or False')
        if not isinstance(config['backup_timeout'], (int, float)) or config['backup_timeout'] <= 0:
            raise ConfigurationError('version_changer: backup_timeout must be a positive number of seconds')
        return config
