from calagoapi.utils.resource import AdminManager
from calagoapi.admin.resources import (
    Location,
    Nest,
    Egg,
    Mount,
    Device,
    Role,
    Announcement,
    OAuthProvider,
    DatabaseHost,
    DatabaseAgentHost,
    DatabaseAgentTemplate,
    BackupConfiguration,
    BackupPolicy,
    EggRepository,
    EggConfiguration,
    SubdomainDomain,
)
from calagoapi.utils.model import idOf


class LocationManager(AdminManager):
    '''Location management, available as `panel.admin.locations`.'''
    model = Location

    def getLocations(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists locations.'''
        return self._list(search, page, per_page)

    def getLocation(self, location_id: str) -> Location:
        '''Returns a location by UUID.'''
        return self._get(location_id)

    def getLocationByName(self, name: str) -> Location:
        '''Returns a location by exact name, or None.'''
        return self._find(name)

    def createLocation(self, name: str, description: str = None, flag: str = None, backup_configuration=None) -> Location:
        '''
        Creates a location.

        Example:
            panel.admin.locations.createLocation('Frankfurt', flag='de')
        '''
        return self._create(name=name, description=description, flag=flag, backup_configuration_uuid=idOf(backup_configuration))

    def deleteLocation(self, location) -> None:
        '''Deletes a location. It must not contain nodes.'''
        return self._delete(location)


class NestManager(AdminManager):
    '''Nest and egg management, available as `panel.admin.nests`.'''
    model = Nest

    def getNests(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists nests.'''
        return self._list(search, page, per_page)

    def getNest(self, nest_id: str) -> Nest:
        '''Returns a nest by UUID.'''
        return self._get(nest_id)

    def getNestByName(self, name: str) -> Nest:
        '''Returns a nest by exact name, or None.'''
        return self._find(name)

    def createNest(self, name: str, author: str, description: str = None) -> Nest:
        '''Creates a nest.'''
        return self._create(name=name, author=author, description=description)

    def deleteNest(self, nest, delete_eggs: bool = False) -> None:
        '''Deletes a nest, optionally with its eggs.'''
        return self._delete(nest, delete_eggs=delete_eggs)

    def getAllEggs(self) -> list:
        '''
        Returns every egg grouped by nest.

        Returns:
            List of {'nest': {...}, 'eggs': [...]} dicts.
        '''
        return self.admin.allEggs()

    def findEgg(self, egg_id_or_name: str):
        '''
        Finds an egg in any nest by UUID or name.

        Example:
            paper = panel.admin.nests.findEgg('Paper')
        '''
        for entry in self.admin.allEggs():
            for egg in entry.get('eggs', []):
                if egg_id_or_name in (egg.get('uuid'), egg.get('name')):
                    return Egg(self.panel, egg, self.admin.eggs(entry['nest']['uuid']))
        return None


class MountManager(AdminManager):
    '''Mount management, available as `panel.admin.mounts`.'''
    model = Mount

    def getMounts(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists mounts.'''
        return self._list(search, page, per_page)

    def getMount(self, mount_id: str) -> Mount:
        '''Returns a mount by UUID.'''
        return self._get(mount_id)

    def createMount(self, name: str, source: str, target: str, read_only: bool = False,
                    user_mountable: bool = False, description: str = None) -> Mount:
        '''
        Creates a mount.

        Args:
            source: Path on the node.
            target: Path inside servers.
        '''
        return self._create(name=name, source=source, target=target, read_only=read_only,
                            user_mountable=user_mountable, description=description)

    def deleteMount(self, mount) -> None:
        '''Deletes a mount.'''
        return self._delete(mount)


class DeviceManager(AdminManager):
    '''Device management, available as `panel.admin.devices`.'''
    model = Device

    def getDevices(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists devices.'''
        return self._list(search, page, per_page)

    def getDevice(self, device_id: str) -> Device:
        '''Returns a device by UUID.'''
        return self._get(device_id)

    def createDevice(self, name: str, source: str, target: str, permissions: str = 'rwm',
                     user_attachable: bool = False, description: str = None) -> Device:
        '''Creates a device passthrough.'''
        return self._create(name=name, source=source, target=target, permissions=permissions,
                            user_attachable=user_attachable, description=description)

    def deleteDevice(self, device) -> None:
        '''Deletes a device.'''
        return self._delete(device)


class RoleManager(AdminManager):
    '''Role management, available as `panel.admin.roles`.'''
    model = Role

    def getRoles(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists roles.'''
        return self._list(search, page, per_page)

    def getRole(self, role_id: str) -> Role:
        '''Returns a role by UUID.'''
        return self._get(role_id)

    def getRoleByName(self, name: str) -> Role:
        '''Returns a role by exact name, or None.'''
        return self._find(name)

    def createRole(self, name: str, admin_permissions: list = None, server_permissions: list = None,
                   require_two_factor: bool = False, description: str = None) -> Role:
        '''Creates a role.'''
        return self._create(name=name, admin_permissions=admin_permissions or [], server_permissions=server_permissions or [],
                            require_two_factor=require_two_factor, description=description)

    def deleteRole(self, role) -> None:
        '''Deletes a role.'''
        return self._delete(role)


class AnnouncementManager(AdminManager):
    '''Announcement management, available as `panel.admin.announcements`.'''
    model = Announcement

    def getAnnouncements(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists announcements.'''
        return self._list(search, page, per_page)

    def getAnnouncement(self, announcement_id: str) -> Announcement:
        '''Returns an announcement by UUID.'''
        return self._get(announcement_id)

    def createAnnouncement(self, title: str, content: str, type: str = 'info', enabled: bool = True, dismissible: bool = True,
                           locations: list = None, nodes: list = None, eggs: list = None, backup_configurations: list = None,
                           enabled_start: str = None, enabled_end: str = None, dismissible_end: str = None) -> Announcement:
        '''
        Creates an announcement.

        Args:
            title: Title.
            content: Markdown content.
            type: info, success, warning or error.
            locations, nodes, eggs, backup_configurations: Limit who sees it. Everyone when all are empty.
            enabled_start, enabled_end: Optional ISO-8601 time window.

        Example:
            panel.admin.announcements.createAnnouncement('Maintenance', 'Reboot at 02:00 UTC', type='warning')
        '''
        return self._create(
            type=type,
            title=title,
            content=content,
            enabled=enabled,
            dismissible=dismissible,
            title_translations={},
            content_translations={},
            locations=[idOf(x) for x in locations or []],
            nodes=[idOf(x) for x in nodes or []],
            eggs=[idOf(x) for x in eggs or []],
            backup_configurations=[idOf(x) for x in backup_configurations or []],
            enabled_start=enabled_start,
            enabled_end=enabled_end,
            dismissible_end=dismissible_end,
        )

    def deleteAnnouncement(self, announcement) -> None:
        '''Deletes an announcement.'''
        return self._delete(announcement)


class OAuthProviderManager(AdminManager):
    '''OAuth provider management, available as `panel.admin.oauth`.'''
    model = OAuthProvider

    def getProviders(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists OAuth providers.'''
        return self._list(search, page, per_page)

    def getProvider(self, provider_id: str) -> OAuthProvider:
        '''Returns a provider by UUID.'''
        return self._get(provider_id)

    def createProvider(self, **fields) -> OAuthProvider:
        '''
        Creates an OAuth provider. Accepts every Calagopus provider field
        (name, client_id, client_secret, auth_url, token_url, info_url, scopes,
        identifier_path, email_path, username_path, enabled, ...).

        Tip: `discover()` fills most fields from an OpenID issuer URL.
        '''
        defaults = {
            'enabled': True,
            'login_only': False,
            'login_bypass_two_factor': False,
            'link_viewable': True,
            'user_manageable': True,
            'basic_auth': False,
            'scopes': [],
        }
        return self._create(**{**defaults, **fields})

    def discover(self, url: str) -> dict:
        '''Reads an OpenID Connect discovery document and returns suggested provider settings.'''
        return self.admin.discoverOauthProvider(url)

    def deleteProvider(self, provider) -> None:
        '''Deletes an OAuth provider.'''
        return self._delete(provider)


class DatabaseHostManager(AdminManager):
    '''Database host management, available as `panel.admin.database_hosts`.'''
    model = DatabaseHost

    def getDatabaseHosts(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists database hosts.'''
        return self._list(search, page, per_page)

    def getDatabaseHost(self, host_id: str) -> DatabaseHost:
        '''Returns a database host by UUID.'''
        return self._get(host_id)

    def createDatabaseHost(self, name: str, type: str, credentials: dict, public_host: str = None, public_port: int = None,
                           deployment_enabled: bool = True, maintenance_enabled: bool = False) -> DatabaseHost:
        '''
        Creates a database host.

        Args:
            type: mysql, postgres or mongodb.
            credentials: Connection credentials (host, port, username, password, ...).
        '''
        return self._create(name=name, type=type, credentials=credentials, public_host=public_host, public_port=public_port,
                            deployment_enabled=deployment_enabled, maintenance_enabled=maintenance_enabled)

    def deleteDatabaseHost(self, host, force: bool = False) -> None:
        '''Deletes a database host.'''
        return self._delete(host, force=force)


class DatabaseAgentHostManager(AdminManager):
    '''Database agent host management, available as `panel.admin.database_agent_hosts`.'''
    model = DatabaseAgentHost

    def getDatabaseAgentHosts(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists database agent hosts.'''
        return self._list(search, page, per_page)

    def getDatabaseAgentHost(self, host_id: str) -> DatabaseAgentHost:
        '''Returns a database agent host by UUID.'''
        return self._get(host_id)

    def createDatabaseAgentHost(self, name: str, url: str, memory: int, disk: int, types: list = None,
                                deployment_enabled: bool = True, maintenance_enabled: bool = False,
                                description: str = None) -> DatabaseAgentHost:
        '''Creates a database agent host.'''
        return self._create(name=name, url=url, memory=memory, disk=disk, types=types, description=description,
                            deployment_enabled=deployment_enabled, maintenance_enabled=maintenance_enabled)

    def deleteDatabaseAgentHost(self, host, force: bool = False) -> None:
        '''Deletes a database agent host.'''
        return self._delete(host, force=force)

    def getCapacities(self) -> dict:
        '''Returns allocated resources of every host.'''
        return self.admin.databaseAgentCapacities()

    def updateConfigs(self, hosts: list, config: dict) -> dict:
        '''Applies the same configuration change to several hosts.'''
        return self.admin.updateDatabaseAgentHostsConfig([idOf(h) for h in hosts], config)


class DatabaseAgentTemplateManager(AdminManager):
    '''Database instance template management, available as `panel.admin.database_templates`.'''
    model = DatabaseAgentTemplate

    def getTemplates(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists templates.'''
        return self._list(search, page, per_page)

    def getTemplate(self, template_id: str) -> DatabaseAgentTemplate:
        '''Returns a template by UUID.'''
        return self._get(template_id)

    def createTemplate(self, **fields) -> DatabaseAgentTemplate:
        '''
        Creates a template. Accepts every Calagopus template field (name, type,
        docker_images, env, image_uid, image_gid, volumes, socket_path, memory,
        swap, disk, cpu, deployment_enabled, ...).
        '''
        return self._create(**fields)

    def deleteTemplate(self, template) -> None:
        '''Deletes a template.'''
        return self._delete(template)


class BackupConfigurationManager(AdminManager):
    '''Backup configuration management, available as `panel.admin.backup_configurations`.'''
    model = BackupConfiguration

    def getBackupConfigurations(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists backup configurations.'''
        return self._list(search, page, per_page)

    def getBackupConfiguration(self, configuration_id: str) -> BackupConfiguration:
        '''Returns a backup configuration by UUID.'''
        return self._get(configuration_id)

    def createBackupConfiguration(self, name: str, backup_disk: str, backup_configs: dict, shared: bool = False,
                                  maintenance_enabled: bool = False, description: str = None) -> BackupConfiguration:
        '''
        Creates a backup configuration.

        Args:
            backup_disk: local, s3, ddup-bak, btrfs, zfs, restic, proxmox-backup-server or kopia.
            backup_configs: Driver settings.
        '''
        return self._create(name=name, backup_disk=backup_disk, backup_configs=backup_configs, shared=shared,
                            maintenance_enabled=maintenance_enabled, description=description)

    def testBackupConfiguration(self, node, backup_disk: str, backup_configs: dict) -> dict:
        '''Tests storage settings from a node before saving them.'''
        return self.admin.testBackupConfiguration(idOf(node), backup_disk, backup_configs)

    def deleteBackupConfiguration(self, configuration) -> None:
        '''Deletes a backup configuration.'''
        return self._delete(configuration)


class BackupPolicyManager(AdminManager):
    '''Panel-wide backup policies, available as `panel.admin.backup_policies`.'''
    model = BackupPolicy

    def getBackupPolicies(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists backup policies.'''
        return self._list(search, page, per_page)

    def getBackupPolicy(self, policy_id: str) -> BackupPolicy:
        '''Returns a backup policy by UUID.'''
        return self._get(policy_id)

    def createBackupPolicy(self, name: str, cron: str, enabled: bool = True, parallelism: int = 1, retention: dict = None,
                           backup_configuration=None, kind: str = None, description: str = None) -> BackupPolicy:
        '''
        Creates a backup policy.

        Args:
            cron: 6-field cron expression (seconds first).
            parallelism: How many backups run at the same time.
        '''
        return self._create(name=name, cron=cron, enabled=enabled, parallelism=parallelism, retention=retention,
                            backup_configuration_uuid=idOf(backup_configuration), kind=kind, description=description)

    def deleteBackupPolicy(self, policy, delete_backups: bool = False) -> None:
        '''Deletes a backup policy.'''
        return self._delete(policy, delete_backups=delete_backups)


class EggRepositoryManager(AdminManager):
    '''Egg repository management, available as `panel.admin.egg_repositories`.'''
    model = EggRepository

    def getEggRepositories(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists egg repositories.'''
        return self._list(search, page, per_page)

    def getEggRepository(self, repository_id: str) -> EggRepository:
        '''Returns an egg repository by UUID.'''
        return self._get(repository_id)

    def createEggRepository(self, name: str, git_repository: str, description: str = None, credentials: dict = None) -> EggRepository:
        '''Adds an egg repository.'''
        return self._create(name=name, git_repository=git_repository, description=description, credentials=credentials)

    def deleteEggRepository(self, repository) -> None:
        '''Deletes an egg repository.'''
        return self._delete(repository)


class EggConfigurationManager(AdminManager):
    '''Egg configuration rules, available as `panel.admin.egg_configurations`.'''
    model = EggConfiguration

    def getEggConfigurations(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists egg configurations.'''
        return self._list(search, page, per_page)

    def getEggConfiguration(self, configuration_id: str) -> EggConfiguration:
        '''Returns an egg configuration by UUID.'''
        return self._get(configuration_id)

    def createEggConfiguration(self, name: str, matcher: dict, order: int = 0, **fields) -> EggConfiguration:
        '''Creates an egg configuration. Extra fields: config_allocations, config_startup, config_routes, config_features.'''
        return self._create(name=name, matcher=matcher, order=order, **fields)

    def deleteEggConfiguration(self, configuration) -> None:
        '''Deletes an egg configuration.'''
        return self._delete(configuration)


class SubdomainDomainManager(AdminManager):
    '''Subdomain Manager domains, available as `panel.admin.subdomain_domains`.'''
    model = SubdomainDomain

    def getDomains(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists domains.'''
        return self._list(search, page, per_page)

    def getDomain(self, domain_id_or_name: str) -> SubdomainDomain:
        '''Returns a domain by UUID or domain name, or None.'''
        for domain in self.getDomains():
            if domain_id_or_name in (domain.getUUID(), domain.getDomain()):
                return domain
        return None

    def createDomain(self, domain: str, provider: str, provider_config: dict, eggs: list = None,
                     disallowed_subdomains_regexes: list = None) -> SubdomainDomain:
        '''
        Adds a domain.

        Args:
            domain: e.g. "example.com".
            provider: cloudflare or powerdns.
            provider_config: Provider credentials.
            eggs: Eggs allowed to use the domain. All when empty.
        '''
        return self._create(domain=domain, provider=provider, provider_config=provider_config,
                            eggs=[idOf(e) for e in eggs or []], disallowed_subdomains_regexes=disallowed_subdomains_regexes or [])

    def deleteDomain(self, domain) -> None:
        '''Deletes a domain.'''
        return self._delete(domain)
