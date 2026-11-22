'''
The Calagopus Minecraft Version Changer panel extension (dev.0x7d8.minecraftversionchanger).

    server.versions.getTypes()
    build = server.versions.getLatestBuild('PAPER', '1.21.11')
    server.versions.install(build)

    panel.minecraft.versionChanger.getSettings()     # admin
'''
from calagoapi.api.client import segment
from calagoapi.utils.exceptions import InvalidActionError, NotFoundError
from calagoapi.utils.model import idOf

from calagoapi_minecraft.config import settings


# identifier of the panel extension
PANEL_EXTENSION = 'dev.0x7d8.minecraftversionchanger'


class VersionChangerAPI:
    '''
    HTTP calls of the Version Changer. Uses the panel's client, so authentication,
    retries and errors behave like the rest of CalagoAPI.
    '''
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, suffix=''):
        return f'/api/client/servers/{server_id}/minecraft/versions{suffix}'

    # client endpoints
    def installed(self, server_id):
        return self.client.get(self._path(server_id, '/installed'))['build']

    def types(self, server_id):
        return self.client.get(self._path(server_id, '/types'))['types']

    def versions(self, server_id, type, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, f'/types/{segment(type)}'), 'versions', {'search': search},
                                page, per_page)

    def builds(self, server_id, type, version, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, f'/types/{segment(type)}/{segment(version)}'), 'builds',
                                {'search': search}, page, per_page)

    def install(self, server_id, build_uuid, truncate_directory=False, accept_eula=True):
        return self.client.post(self._path(server_id, '/install'), json={
            'build_uuid': build_uuid,
            'truncate_directory': truncate_directory,
            'accept_eula': accept_eula,
        })

    # admin endpoints
    def _admin(self, suffix, method='GET', json=None):
        return self.client.request(method, f'/api/admin/extensions/{PANEL_EXTENSION}/{suffix}', json=json)

    def settings(self):
        return self._admin('settings')['settings']

    def updateSettings(self, values):
        return self._admin('settings', 'PUT', json=values)

    def statistics(self):
        return self._admin('statistics/total')

    def defaultOrder(self):
        return self._admin('default-order')['mcjars_type_order']


def _buildId(build):
    return build.get('uuid') if isinstance(build, dict) else idOf(build)


class VersionManager:
    '''
    The Version Changer of one server, available as `server.versions`.

    Needs the Minecraft Version Changer panel extension on the panel; without it the
    calls raise NotFoundError (check with isAvailable()).

    Example:
        build = server.versions.getLatestBuild('PAPER', '1.21.11')
        server.versions.install(build)                   # backs up first with auto_backup
        if server.versions.isUpToDate() is False:
            server.versions.update()
    '''
    def __init__(self, server):
        self.server = server

    def __repr__(self):
        return f'<VersionManager of {self.server!r}>'

    @property
    def api(self) -> VersionChangerAPI:
        return VersionChangerAPI(self.server.panel.client)

    def isAvailable(self) -> bool:
        '''Returns True if the Version Changer panel extension answers for this server.'''
        try:
            self.getTypes()
            return True
        except NotFoundError:
            return False

    def getInstalled(self) -> dict:
        '''
        Returns what the Version Changer knows about the installed build:
        `{'build': {...}, 'latest': {...}}`, or None if it was not installed with it.

        Example:
            installed = server.versions.getInstalled()
            if installed:
                print(f'{installed["build"]["name"]}, latest: {installed["latest"]["name"]}')
        '''
        return self.api.installed(self.server.server_id)

    def getInstalledBuild(self) -> dict:
        '''Returns the installed build (type, name, version_id, ...), or None.'''
        installed = self.getInstalled()
        return installed.get('build') if installed else None

    def isUpToDate(self) -> bool:
        '''Returns True if the installed build is the newest of its version, None if unknown.'''
        installed = self.getInstalled()
        if not installed or not installed.get('build') or not installed.get('latest'):
            return None
        return installed['build'].get('uuid') == installed['latest'].get('uuid')

    def getTypes(self) -> dict:
        '''Returns the available server types (PAPER, PURPUR, FABRIC, VANILLA, ...).'''
        return self.api.types(self.server.server_id)

    def getVersions(self, type: str, search: str = None, page: int = None, per_page: int = None):
        '''
        Returns the Minecraft versions available for a server type.

        Example:
            server.versions.getVersions('PAPER', page=1, per_page=10)
        '''
        return self.api.versions(self.server.server_id, type, search, page, per_page)

    def getBuilds(self, type: str, version: str, search: str = None, page: int = None, per_page: int = None):
        '''
        Returns the builds of a version, newest first.

        Example:
            builds = server.versions.getBuilds('PAPER', '1.21.11', page=1, per_page=5)
        '''
        return self.api.builds(self.server.server_id, type, version, search, page, per_page)

    def getLatestBuild(self, type: str, version: str) -> dict:
        '''Returns the newest build of a version, or None.'''
        builds = self.getBuilds(type, version, page=1, per_page=1)
        return builds[0] if builds else None

    def install(self, build, truncate_directory: bool = False, accept_eula: bool = True, backup: bool = None) -> None:
        '''
        Installs a server build.

        Args:
            build: Build dict from getBuilds() or a build UUID.
            truncate_directory: Delete every file first.
            accept_eula: Accept the Minecraft EULA.
            backup: Make a backup first and only install if it succeeded. None uses the
                `auto_backup` config (default False).

        Raises:
            InvalidActionError: The backup failed; nothing was installed.

        Example:
            server.versions.install(server.versions.getLatestBuild('FABRIC', '26.2'), backup=True)
        '''
        config = settings()
        build_id = _buildId(build)
        if config['auto_backup'] if backup is None else backup:
            created = self.server.backups.createBackup(name=config['backup_name'])
            created.waitUntilComplete(timeout=config['backup_timeout'])
            if not created.isSuccessful():
                raise InvalidActionError(f'The backup before installing {build_id} failed; nothing was installed.')
        return self.api.install(self.server.server_id, build_id, truncate_directory, accept_eula)

    def update(self, truncate_directory: bool = False, backup: bool = None) -> bool:
        '''
        Installs the newest build of the installed version. Returns False if already up to date.

        Raises:
            InvalidActionError: The installed version is unknown (use install()).
        '''
        installed = self.getInstalled()
        if not installed or not installed.get('latest'):
            raise InvalidActionError('The installed version is unknown, use server.versions.install() instead.')
        if installed.get('build') and installed['build'].get('uuid') == installed['latest'].get('uuid'):
            return False
        self.install(installed['latest'], truncate_directory=truncate_directory, backup=backup)
        return True


class VersionChangerAdmin:
    '''
    Admin settings of the Version Changer panel extension, available as
    `panel.minecraft.versionChanger` (admin API key required).

    Example:
        settings = panel.minecraft.versionChanger.getSettings()
        panel.minecraft.versionChanger.updateSettings(mcjars_url='https://mcjars.app')
    '''
    def __init__(self, panel):
        self.panel = panel

    def __repr__(self):
        return '<VersionChangerAdmin>'

    @property
    def api(self) -> VersionChangerAPI:
        return VersionChangerAPI(self.panel.client)

    def getSettings(self) -> dict:
        '''Returns the Version Changer settings.'''
        return self.api.settings()

    def updateSettings(self, **values) -> None:
        '''Changes settings (mcjars_url, mcjars_api_key, type_egg_assignments, ...).'''
        return self.api.updateSettings(values)

    def getStatistics(self) -> dict:
        '''Returns install statistics by server type and version.'''
        return self.api.statistics()

    def getDefaultOrder(self) -> list:
        '''Returns the default order of server types in the version picker.'''
        return self.api.defaultOrder()
