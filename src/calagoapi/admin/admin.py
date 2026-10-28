import os

from calagoapi.admin.managers import (
    LocationManager,
    NestManager,
    MountManager,
    DeviceManager,
    RoleManager,
    AnnouncementManager,
    OAuthProviderManager,
    DatabaseHostManager,
    DatabaseAgentHostManager,
    DatabaseAgentTemplateManager,
    BackupConfigurationManager,
    BackupPolicyManager,
    EggRepositoryManager,
    EggConfigurationManager,
    SubdomainDomainManager,
)
from calagoapi.nodes import NodeManager
from calagoapi.servers.admin import AdminServerManager
from calagoapi.users import UserManager, Activity
from calagoapi.utils.model import idOf


class SystemManager:
    '''
    Panel health, updates and diagnostics, available as `panel.admin.system`.

    Example:
        overview = panel.admin.system.getOverview()
        print(overview['version'])
        if panel.admin.system.getUpdates():
            print('An update is available')
    '''
    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.admin

    def getOverview(self) -> dict:
        '''Returns panel version, CPU, memory, cache and database information.'''
        return self.api.system('overview')

    def getHealth(self) -> dict:
        '''Returns time sync and pending migration information.'''
        return self.api.system('health/general')

    def getNodeHealth(self, page: int = None, per_page: int = None) -> dict:
        '''Returns nodes whose clock is out of sync or that cannot be reached.'''
        return self.api.system('health/nodes', params={'page': page, 'per_page': per_page})

    def getTelemetry(self) -> dict:
        '''Returns the anonymous telemetry the panel would send.'''
        return self.api.system('telemetry')['telemetry']

    def getUpdates(self) -> dict:
        '''Returns available panel update information.'''
        return self.api.system('updates')['update_information']

    def recheckUpdates(self) -> dict:
        '''Checks for updates now.'''
        return self.api.system('updates/recheck', 'POST')['update_information']

    def getUpdateHistory(self) -> dict:
        '''Returns the panel version history.'''
        return self.api.system('updates/history')['version_history']

    def getOutdatedNodes(self, page: int = None, per_page: int = None) -> dict:
        '''Returns nodes running an outdated daemon.'''
        return self.api.system('updates/nodes', params={'page': page, 'per_page': per_page})

    def getOutdatedDatabaseAgentHosts(self, page: int = None, per_page: int = None) -> dict:
        '''Returns database agent hosts running an outdated agent.'''
        return self.api.system('updates/database-agent-hosts', params={'page': page, 'per_page': per_page})

    def isDebugEnabled(self) -> bool:
        '''Returns True if debug logging is enabled.'''
        return bool(self.api.system('debug').get('enabled'))

    def setDebug(self, enabled: bool) -> None:
        '''Turns debug logging on or off.'''
        return self.api.system('debug', 'POST', json={'enabled': enabled})


class EmailManager:
    '''
    Email templates and variables, available as `panel.admin.email`.

    Example:
        panel.admin.email.sendTestEmail('me@example.com')
        panel.admin.email.updateTemplate('password_reset', subject='Reset your password')
    '''
    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.admin

    def sendTestEmail(self, email: str) -> None:
        '''Sends a test email using the current mail settings.'''
        return self.api.sendTestEmail(email)

    def getTemplates(self) -> list:
        '''Returns every email template.'''
        return self.api.emailTemplates()

    def getTemplate(self, identifier: str) -> dict:
        '''Returns one email template.'''
        return self.api.emailTemplate(identifier)

    def updateTemplate(self, identifier: str, subject: str = None, content: str = None, enabled: bool = None) -> None:
        '''Changes an email template.'''
        return self.api.updateEmailTemplate(identifier, subject, content, enabled)

    def getTemplateVariables(self, identifier: str) -> list:
        '''Returns variables defined for one template.'''
        return self.api.emailVariables(identifier)

    def createTemplateVariable(self, identifier: str, name: str, value: str, value_translations: dict = None) -> None:
        '''Defines a variable for one template.'''
        return self.api.createEmailVariable(name, value, value_translations, identifier)

    def updateTemplateVariable(self, identifier: str, name: str, value: str = None, value_translations: dict = None) -> None:
        '''Changes a template variable.'''
        return self.api.updateEmailVariable(name, value, value_translations, identifier)

    def deleteTemplateVariable(self, identifier: str, name: str) -> None:
        '''Deletes a template variable.'''
        return self.api.deleteEmailVariable(name, identifier)

    def getVariables(self) -> list:
        '''Returns global email variables.'''
        return self.api.emailVariables()

    def createVariable(self, name: str, value: str, value_translations: dict = None) -> None:
        '''Defines a global email variable.'''
        return self.api.createEmailVariable(name, value, value_translations)

    def updateVariable(self, name: str, value: str = None, value_translations: dict = None) -> None:
        '''Changes a global email variable.'''
        return self.api.updateEmailVariable(name, value, value_translations)

    def deleteVariable(self, name: str) -> None:
        '''Deletes a global email variable.'''
        return self.api.deleteEmailVariable(name)


class ExtensionManager:
    '''
    Panel extensions, available as `panel.admin.extensions`.

    Example:
        for extension in panel.admin.extensions.getExtensions():
            print(extension['identifier'])
        panel.admin.extensions.disable('dev.0x7d8.subdomainmanager')
        panel.admin.extensions.restart()
    '''
    VERSION_CHANGER = 'dev.0x7d8.minecraftversionchanger'

    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.admin

    def getInfo(self) -> dict:
        '''Returns installed, disabled and pending extensions.'''
        return self.api.extensions()

    def getExtensions(self) -> list:
        '''Returns installed extensions.'''
        return self.getInfo().get('extensions', [])

    def setEnabled(self, extension: str, enabled: bool) -> bool:
        '''Enables or disables an extension. Returns True if a restart is needed.'''
        return self.api.setExtensionEnabled(extension, enabled)

    def enable(self, extension: str) -> bool:
        '''Enables an extension.'''
        return self.setEnabled(extension, True)

    def disable(self, extension: str) -> bool:
        '''Disables an extension.'''
        return self.setEnabled(extension, False)

    def getStatus(self) -> dict:
        '''Returns build status, running version and pending changes.'''
        return self.api.manageExtensions('status')

    def install(self, file, accept_license: bool = False) -> dict:
        '''
        Uploads and installs an extension package.

        Args:
            file: Local path or bytes of the extension archive.
            accept_license: Accept the extension's license.
        '''
        if isinstance(file, (str, os.PathLike)):
            with open(file, 'rb') as f:
                file = f.read()
        return self.api.manageExtensions('add', 'PUT', params={'accept_license': accept_license}, data=file,
                                         headers={'Content-Type': 'application/octet-stream'})

    def remove(self, extension: str, remove_migrations: bool = False) -> None:
        '''Uninstalls an extension.'''
        return self.api.removeExtension(extension, remove_migrations)

    def rebuild(self, force: bool = False) -> str:
        '''Rebuilds the panel with the current extensions. Returns the build id.'''
        return self.api.manageExtensions('rebuild', 'POST', params={'force': force})['build_id']

    def cancelRebuild(self, build_id: str = None) -> str:
        '''Cancels a running rebuild.'''
        return self.api.manageExtensions('rebuild/cancel', 'POST', params={'build_id': build_id})['build_id']

    def getBuildLogs(self, build_id: str = None, from_offset: int = None) -> dict:
        '''Returns build output (offset, data, eof).'''
        return self.api.manageExtensions('logs', params={'build_id': build_id, 'from_offset': from_offset})

    def restart(self) -> None:
        '''Restarts the panel to apply extension changes.'''
        return self.api.manageExtensions('restart', 'POST')

    # Minecraft Version Changer
    def getVersionChangerSettings(self) -> dict:
        '''Returns the Minecraft Version Changer settings.'''
        return self.api.extension(self.VERSION_CHANGER, 'settings')['settings']

    def updateVersionChangerSettings(self, **settings) -> None:
        '''Changes Minecraft Version Changer settings (mcjars_url, mcjars_api_key, type_egg_assignments, ...).'''
        return self.api.extension(self.VERSION_CHANGER, 'settings', 'PUT', json=settings)

    def getVersionChangerStatistics(self) -> dict:
        '''Returns install statistics by server type and version.'''
        return self.api.extension(self.VERSION_CHANGER, 'statistics/total')

    def getVersionChangerDefaultOrder(self) -> list:
        '''Returns the default order of server types in the version picker.'''
        return self.api.extension(self.VERSION_CHANGER, 'default-order')['mcjars_type_order']


class AssetManager:
    '''
    Panel assets (logos, images), available as `panel.admin.assets`.

    Example:
        panel.admin.assets.upload('logo.png', directory='branding')
    '''
    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.admin

    def getAssets(self, directory: str = None, page: int = None, per_page: int = None):
        '''Lists assets.'''
        return self.api.assets(directory, page, per_page)

    def upload(self, file, directory: str = None, content_type: str = 'application/octet-stream') -> list:
        '''Uploads an asset from a local path or bytes.'''
        if isinstance(file, (str, os.PathLike)):
            with open(file, 'rb') as f:
                file = f.read()
        return self.api.uploadAsset(file, directory, content_type)

    def search(self, query: str, directory: str = None, per_page: int = None) -> list:
        '''Searches assets by name.'''
        return self.api.searchAssets(query, directory, per_page)

    def delete(self, names: list) -> int:
        '''Deletes assets by name. Returns how many were deleted.'''
        return self.api.deleteAssets(names)


class Admin:
    '''
    Panel administration, available as `panel.admin`. Requires an API key with admin permissions.

    Managers:
        users, servers, nodes, locations, nests, mounts, devices, roles,
        announcements, oauth, database_hosts, database_agent_hosts,
        database_templates, backup_configurations, backup_policies,
        egg_repositories, egg_configurations, subdomain_domains,
        system, email, extensions, assets

    Example:
        for node in panel.admin.nodes.getNodes():
            print(node.getName(), node.isInMaintenance())

        user = panel.admin.users.createUser('steve', 'steve@example.com')
        panel.admin.servers.deployServer('Steve SMP', user, paper_egg, locations=[eu])
    '''
    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.admin

        self.users = UserManager(panel)
        self.servers = AdminServerManager(panel)
        self.nodes = NodeManager(panel)
        self.locations = LocationManager(panel)
        self.nests = NestManager(panel)
        self.mounts = MountManager(panel)
        self.devices = DeviceManager(panel)
        self.roles = RoleManager(panel)
        self.announcements = AnnouncementManager(panel)
        self.oauth = OAuthProviderManager(panel)
        self.database_hosts = DatabaseHostManager(panel)
        self.database_agent_hosts = DatabaseAgentHostManager(panel)
        self.database_templates = DatabaseAgentTemplateManager(panel)
        self.backup_configurations = BackupConfigurationManager(panel)
        self.backup_policies = BackupPolicyManager(panel)
        self.egg_repositories = EggRepositoryManager(panel)
        self.egg_configurations = EggConfigurationManager(panel)
        self.subdomain_domains = SubdomainDomainManager(panel)

        self.system = SystemManager(panel)
        self.email = EmailManager(panel)
        self.extensions = ExtensionManager(panel)
        self.assets = AssetManager(panel)

    def getSettings(self) -> dict:
        '''Returns the panel settings.'''
        return self.api.settings()

    def updateSettings(self, **sections) -> None:
        '''
        Changes panel settings. Pass whole sections, e.g. app, server, user,
        activity, ratelimits, webauthn, mail_mode, captcha_provider.

        Example:
            settings = panel.admin.getSettings()
            settings['app']['name'] = 'My Hosting'
            panel.admin.updateSettings(app=settings['app'])
        '''
        return self.api.updateSettings(**sections)

    def getActivity(self, search: str = None, user=None, page: int = 1, per_page: int = 50):
        '''Returns the panel-wide admin activity log.'''
        return self.api.activity(idOf(user), search, page, per_page).map(lambda data: Activity(self.panel, data))

    def getStats(self) -> dict:
        '''Returns panel statistics (users, servers, nodes, ...).'''
        return self.api.generalStats()

    def getBackupStats(self) -> dict:
        '''Returns backup statistics for today, this week, this month and all time.'''
        return self.api.backupStats()
