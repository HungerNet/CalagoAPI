from calagoapi.utils.resource import AdminResource
from calagoapi.utils.model import idOf
from calagoapi.utils.exceptions import InvalidActionError
from calagoapi.nodes.node import Node
from calagoapi.users.user import User


class Location(AdminResource):
    '''
    A location groups nodes, e.g. by region.

    Example:
        location = panel.admin.locations.createLocation('Frankfurt', flag='de')
        print([node.getName() for node in location.getNodes()])
    '''
    collection = 'locations'

    def duplicate(self, name: str) -> 'Location':
        '''Creates a copy under a new name.'''
        return self._duplicate(name=name)

    def getFlag(self) -> str:
        '''Returns the country flag code.'''
        return self.data.get('flag')

    def getBackupConfiguration(self) -> dict:
        '''Returns the default backup configuration of the location.'''
        return self.data.get('backup_configuration')

    def getNodes(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the nodes in this location.'''
        return self._api().related(self.getUUID(), 'nodes', 'nodes', search, page, per_page).map(lambda d: Node(self.panel, d))

    def getDatabaseHosts(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns database hosts linked to this location.'''
        return self._api().related(self.getUUID(), 'database-hosts', 'database_hosts', search, page, per_page)

    def attachDatabaseHost(self, database_host) -> None:
        '''Links a database host to this location.'''
        return self._api().attach(self.getUUID(), 'database-hosts', 'database_host_uuid', idOf(database_host))

    def detachDatabaseHost(self, database_host) -> None:
        '''Unlinks a database host.'''
        return self._api().detach(self.getUUID(), 'database-hosts', idOf(database_host))

    def getDatabaseAgentHosts(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns database agent hosts linked to this location.'''
        return self._api().related(self.getUUID(), 'database-agent-hosts', 'database_agent_hosts', search, page, per_page)

    def attachDatabaseAgentHost(self, host) -> None:
        '''Links a database agent host to this location.'''
        return self._api().attach(self.getUUID(), 'database-agent-hosts', 'database_agent_host_uuid', idOf(host))

    def detachDatabaseAgentHost(self, host) -> None:
        '''Unlinks a database agent host.'''
        return self._api().detach(self.getUUID(), 'database-agent-hosts', idOf(host))


class Nest(AdminResource):
    '''
    A nest is a category of eggs (server types).

    Example:
        nest = panel.admin.nests.getNestByName('Minecraft')
        for egg in nest.getEggs():
            print(egg.getName())
        nest.importEggsFromUrls(['https://example.com/egg-paper.json'])
    '''
    collection = 'nests'

    def getAuthor(self) -> str:
        '''Returns the nest author.'''
        return self.data.get('author')

    def _eggs(self):
        return self.panel.api.admin.eggs(self.getUUID())

    def getEggs(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the eggs in this nest.'''
        return self._eggs().list(search, page, per_page).map(lambda d: Egg(self.panel, d, self._eggs()))

    def getEgg(self, egg_id_or_name: str) -> 'Egg':
        '''Returns an egg by UUID or name, or None.'''
        for egg in self.getEggs():
            if egg_id_or_name in (egg.getUUID(), egg.getName()):
                return egg
        return None

    def createEgg(self, **fields) -> 'Egg':
        '''
        Creates an egg. Accepts every Calagopus egg field (name, author,
        config_files, config_startup, config_stop, config_script, startup_commands,
        docker_images, features, file_denylist, force_outgoing_ip, separate_port, ...).
        '''
        return Egg(self.panel, self._eggs().create(**fields), self._eggs())

    def importEgg(self, data: dict) -> 'Egg':
        '''Imports an egg from exported egg JSON (as a dict).'''
        return Egg(self.panel, self._api().action(self.getUUID(), 'eggs/import', json=data)['egg'], self._eggs())

    def importEggsFromUrls(self, urls: list) -> dict:
        '''Imports eggs from URLs. Returns the created eggs and failures.'''
        return self._api().action(self.getUUID(), 'eggs/import/url', json={'urls': urls})

    def deleteEggs(self, eggs: list) -> int:
        '''Deletes several eggs. Returns how many were deleted.'''
        return self._api().action(self.getUUID(), 'eggs/delete', json={'egg_uuids': [idOf(e) for e in eggs]})['deleted']

    def moveEggs(self, eggs: list, nest) -> int:
        '''Moves eggs into another nest. Returns how many were moved.'''
        return self._api().action(self.getUUID(), 'eggs/move', json={
            'egg_uuids': [idOf(e) for e in eggs],
            'destination_nest_uuid': idOf(nest),
        })['moved']

    def updateEggsFromRepository(self) -> int:
        '''Updates every egg that came from an egg repository.'''
        return self._api().action(self.getUUID(), 'eggs/update/repository')['updated']

    def delete(self, delete_eggs: bool = False) -> None:
        '''Deletes the nest, optionally together with its eggs.'''
        return self._api().delete(self.getUUID(), delete_eggs=delete_eggs)


class Egg(AdminResource):
    '''
    An egg defines a server type: its install script, startup command, images and variables.

    Example:
        egg = nest.getEgg('Paper')
        print(egg.getDockerImages())
        egg.updateFromUrl('https://example.com/egg-paper.json')
    '''
    collection = None

    def getNestId(self) -> str:
        '''Returns the UUID of the nest the egg belongs to.'''
        return self.resource.parent

    def getAuthor(self) -> str:
        '''Returns the egg author.'''
        return self.data.get('author')

    def getStartupCommands(self) -> dict:
        '''Returns the startup commands as {name: command}.'''
        return self.data.get('startup_commands', {})

    def getDockerImages(self) -> dict:
        '''Returns the docker images as {name: image}.'''
        return self.data.get('docker_images', {})

    def getFeatures(self) -> list:
        '''Returns the egg features, e.g. ["eula", "java_version"].'''
        return self.data.get('features', [])

    def getFileDenylist(self) -> list:
        '''Returns files users may not edit.'''
        return self.data.get('file_denylist', [])

    def _variables(self):
        return self.panel.api.admin.eggVariables(self.getNestId(), self.getUUID())

    def getVariables(self) -> list:
        '''Returns the egg's variables.'''
        return [EggVariable(self.panel, d, self._variables()) for d in self._variables().listAll()]

    def createVariable(self, name: str, env_variable: str, default_value: str = '', description: str = None,
                       rules: list = None, user_viewable: bool = True, user_editable: bool = True,
                       secret: bool = False, order: int = None) -> 'EggVariable':
        '''
        Adds a variable.

        Example:
            egg.createVariable('Server Jar', 'SERVER_JARFILE', 'server.jar', rules=['required', 'string'])
        '''
        if order is None:
            order = len(self.getVariables()) + 1
        return EggVariable(self.panel, self._variables().create(
            name=name,
            env_variable=env_variable,
            default_value=default_value,
            description=description,
            rules=rules or [],
            user_viewable=user_viewable,
            user_editable=user_editable,
            secret=secret,
            order=order,
            name_translations={},
            description_translations={},
        ), self._variables())

    def orderVariables(self, variables: list) -> None:
        '''Sets the variable order.'''
        return self.panel.api.admin.orderEggVariables(self.getNestId(), self.getUUID(), [idOf(v) for v in variables])

    def export(self) -> dict:
        '''Exports the egg as JSON (dict).'''
        return self._api().action(self.getUUID(), 'export', 'GET')

    def updateFromImport(self, data: dict) -> None:
        '''Overwrites the egg with exported egg JSON.'''
        return self._api().action(self.getUUID(), 'update/import', json=data)

    def updateFromUrl(self, url: str) -> None:
        '''Overwrites the egg with egg JSON downloaded from a URL.'''
        return self._api().action(self.getUUID(), 'update/import/url', json={'url': url})

    def updateFromRepository(self) -> None:
        '''Updates the egg from its egg repository.'''
        return self._api().action(self.getUUID(), 'update/repository')

    def move(self, nest) -> None:
        '''Moves the egg into another nest.'''
        return self._api().action(self.getUUID(), 'move', json={'destination_nest_uuid': idOf(nest)})

    def duplicate(self, name: str, nest=None) -> 'Egg':
        '''Copies the egg, into `nest` or the same nest.'''
        return self._duplicate(name=name, nest_uuid=idOf(nest) or self.getNestId())

    def getServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns servers using this egg.'''
        return self._api().related(self.getUUID(), 'servers', 'servers', search, page, per_page)

    def getMounts(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns mounts attached to this egg.'''
        return self._api().related(self.getUUID(), 'mounts', 'mounts', search, page, per_page)

    def attachMount(self, mount) -> None:
        '''Attaches a mount to the egg.'''
        return self._api().attach(self.getUUID(), 'mounts', 'mount_uuid', idOf(mount))

    def detachMount(self, mount) -> None:
        '''Detaches a mount from the egg.'''
        return self._api().detach(self.getUUID(), 'mounts', idOf(mount))

    def getDevices(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns devices attached to this egg.'''
        return self._api().related(self.getUUID(), 'devices', 'devices', search, page, per_page)

    def attachDevice(self, device) -> None:
        '''Attaches a device to the egg.'''
        return self._api().attach(self.getUUID(), 'devices', 'device_uuid', idOf(device))

    def detachDevice(self, device) -> None:
        '''Detaches a device from the egg.'''
        return self._api().detach(self.getUUID(), 'devices', idOf(device))


class EggVariable(AdminResource):
    '''
    A configurable variable of an egg.

    Example:
        for variable in egg.getVariables():
            print(variable.getEnvVariable(), variable.getDefaultValue())
    '''
    collection = None

    def getEnvVariable(self) -> str:
        '''Returns the environment variable name, e.g. "SERVER_JARFILE".'''
        return self.data.get('env_variable')

    def getDefaultValue(self) -> str:
        '''Returns the default value.'''
        return self.data.get('default_value')

    def getRules(self) -> list:
        '''Returns the validation rules.'''
        return self.data.get('rules', [])

    def isUserViewable(self) -> bool:
        '''Returns True if users can see the variable.'''
        return bool(self.data.get('user_viewable'))

    def isUserEditable(self) -> bool:
        '''Returns True if users can change the variable.'''
        return bool(self.data.get('user_editable'))

    def isSecret(self) -> bool:
        '''Returns True if the value is hidden.'''
        return bool(self.data.get('secret'))

    def refresh(self) -> 'EggVariable':
        '''Re-fetches the variable from the panel.'''
        for data in self._api().listAll():
            if data.get('uuid') == self.getUUID():
                self.data = data
        return self

    def duplicate(self, name: str, env_variable: str) -> 'EggVariable':
        '''Copies the variable under a new name and environment variable.'''
        return self._duplicate(name=name, env_variable=env_variable)


class Mount(AdminResource):
    '''
    A host directory that can be mounted into servers.

    Example:
        mount = panel.admin.mounts.createMount('Shared maps', '/srv/maps', '/home/container/maps', read_only=True)
        node.attachMount(mount)
    '''
    collection = 'mounts'

    def getSource(self) -> str:
        '''Returns the path on the node.'''
        return self.data.get('source')

    def getTarget(self) -> str:
        '''Returns the path inside the server.'''
        return self.data.get('target')

    def isReadOnly(self) -> bool:
        '''Returns True if the mount is read-only.'''
        return bool(self.data.get('read_only'))

    def isUserMountable(self) -> bool:
        '''Returns True if server owners can attach it themselves.'''
        return bool(self.data.get('user_mountable'))

    def duplicate(self, name: str, source: str, target: str) -> 'Mount':
        '''Copies the mount with a new name, source and target.'''
        return self._duplicate(name=name, source=source, target=target)

    def getNodes(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns nodes the mount is attached to.'''
        return self._api().related(self.getUUID(), 'nodes', 'node_mounts', search, page, per_page)

    def getServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns servers the mount is attached to.'''
        return self._api().related(self.getUUID(), 'servers', 'server_mounts', search, page, per_page)

    def getEggs(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns eggs the mount is attached to.'''
        return self._api().related(self.getUUID(), 'nest-eggs', 'nest_egg_mounts', search, page, per_page)


class Device(AdminResource):
    '''
    A host device (e.g. a GPU) that can be passed into servers.

    Example:
        gpu = panel.admin.devices.createDevice('GPU', '/dev/dri', '/dev/dri', 'rwm')
    '''
    collection = 'devices'

    def getSource(self) -> str:
        '''Returns the device path on the node.'''
        return self.data.get('source')

    def getTarget(self) -> str:
        '''Returns the device path inside the server.'''
        return self.data.get('target')

    def getPermissions(self) -> str:
        '''Returns the cgroup permissions, e.g. "rwm".'''
        return self.data.get('permissions')

    def isUserAttachable(self) -> bool:
        '''Returns True if server owners can attach it themselves.'''
        return bool(self.data.get('user_attachable'))

    def duplicate(self, name: str, source: str, target: str) -> 'Device':
        '''Copies the device with a new name, source and target.'''
        return self._duplicate(name=name, source=source, target=target)

    def getNodes(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns nodes the device is attached to.'''
        return self._api().related(self.getUUID(), 'nodes', 'node_devices', search, page, per_page)

    def getServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns servers the device is attached to.'''
        return self._api().related(self.getUUID(), 'servers', 'server_devices', search, page, per_page)

    def getEggs(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns eggs the device is attached to.'''
        return self._api().related(self.getUUID(), 'nest-eggs', 'nest_egg_devices', search, page, per_page)


class Role(AdminResource):
    '''
    A role grants admin and server permissions to users.

    Example:
        support = panel.admin.roles.createRole('Support', admin_permissions=['servers.read'])
        user.setRole(support)
    '''
    collection = 'roles'

    def duplicate(self, name: str) -> 'Role':
        '''Creates a copy under a new name.'''
        return self._duplicate(name=name)

    def getAdminPermissions(self) -> list:
        '''Returns the admin permissions.'''
        return self.data.get('admin_permissions', [])

    def getServerPermissions(self) -> list:
        '''Returns the server permissions granted on every server.'''
        return self.data.get('server_permissions', [])

    def requiresTwoFactor(self) -> bool:
        '''Returns True if members must use two-factor authentication.'''
        return bool(self.data.get('require_two_factor'))

    def getUsers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns users with this role.'''
        return self._api().related(self.getUUID(), 'users', 'users', search, page, per_page).map(lambda d: User(self.panel, d))


class Announcement(AdminResource):
    '''
    A panel announcement banner.

    Example:
        panel.admin.announcements.createAnnouncement('Maintenance', 'Nodes reboot at 02:00 UTC', type='warning')
    '''
    collection = 'announcements'

    def getName(self) -> str:
        '''Returns the title.'''
        return self.data.get('title')

    def getType(self) -> str:
        '''Returns info, success, warning or error.'''
        return self.data.get('type')

    def getTitle(self) -> str:
        '''Returns the title.'''
        return self.data.get('title')

    def getContent(self) -> str:
        '''Returns the content (markdown).'''
        return self.data.get('content')

    def isEnabled(self) -> bool:
        '''Returns True if the announcement is shown.'''
        return bool(self.data.get('enabled'))

    def isDismissible(self) -> bool:
        '''Returns True if users can dismiss it.'''
        return bool(self.data.get('dismissible'))

    def enable(self) -> 'Announcement':
        '''Shows the announcement.'''
        return self.update(enabled=True)

    def disable(self) -> 'Announcement':
        '''Hides the announcement.'''
        return self.update(enabled=False)

    def getDescription(self) -> str:
        '''Returns the content (announcements have no separate description).'''
        return self.getContent()

    def rename(self, title: str) -> 'Announcement':
        '''Changes the title.'''
        return self.update(title=title)

    def setName(self, title: str) -> 'Announcement':
        '''Changes the title.'''
        return self.update(title=title)

    def setTitle(self, title: str) -> 'Announcement':
        '''Changes the title.'''
        return self.update(title=title)

    def setContent(self, content: str) -> 'Announcement':
        '''Changes the content.'''
        return self.update(content=content)

    def setDescription(self, content: str) -> 'Announcement':
        '''Changes the content.'''
        return self.update(content=content)

    def duplicate(self) -> 'Announcement':
        '''Copies the announcement.'''
        return self._duplicate()


class OAuthProvider(AdminResource):
    '''
    An OAuth login provider (Discord, GitHub, Google, Keycloak, ...).

    Example:
        provider = panel.admin.oauth.discover('https://accounts.google.com')
        for mapping in provider.getMappings():
            print(mapping)
    '''
    collection = 'oauth_providers'

    def duplicate(self, name: str) -> 'OAuthProvider':
        '''Creates a copy under a new name.'''
        return self._duplicate(name=name)

    def getClientId(self) -> str:
        '''Returns the OAuth client id.'''
        return self.data.get('client_id')

    def getScopes(self) -> list:
        '''Returns the requested scopes.'''
        return self.data.get('scopes', [])

    def isEnabled(self) -> bool:
        '''Returns True if users can log in with this provider.'''
        return bool(self.data.get('enabled'))

    def enable(self) -> 'OAuthProvider':
        '''Enables the provider.'''
        return self.update(enabled=True)

    def disable(self) -> 'OAuthProvider':
        '''Disables the provider.'''
        return self.update(enabled=False)

    def _mappings(self):
        return self.panel.api.admin.oauthMappings(self.getUUID())

    def getMappings(self, page: int = None, per_page: int = None):
        '''Returns rules that map OAuth claims to roles/permissions.'''
        return self._mappings().list(page=page, per_page=per_page)

    def createMapping(self, matcher: dict, mapping: dict) -> dict:
        '''Adds a claim mapping rule.'''
        return self._mappings().create(matcher=matcher, mapping=mapping)

    def updateMapping(self, mapping_id: str, matcher: dict = None, mapping: dict = None) -> None:
        '''Changes a claim mapping rule.'''
        return self._mappings().update(mapping_id, matcher=matcher, mapping=mapping)

    def deleteMapping(self, mapping_id: str) -> None:
        '''Deletes a claim mapping rule.'''
        return self._mappings().delete(mapping_id)

    def getUsers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns users linked through this provider.'''
        return self._api().related(self.getUUID(), 'users', 'user_oauth_links', search, page, per_page)

    def getUserLink(self, identifier: str) -> dict:
        '''Returns the user linked to an OAuth identifier.'''
        return self.panel.api.admin.oauthProviderUserLink(self.getUUID(), identifier)

    def getMapping(self, mapping_id: str) -> dict:
        '''Returns one claim mapping rule.'''
        return self._mappings().get(mapping_id)


class DatabaseHost(AdminResource):
    '''
    An external database server (MySQL, PostgreSQL, MongoDB) servers can create databases on.

    Example:
        host = panel.admin.database_hosts.getDatabaseHost('...')
        print(host.test())
    '''
    collection = 'database_hosts'

    def setDescription(self, description: str):
        '''Database hosts have no description.'''
        raise InvalidActionError('Database hosts have no description')

    def getType(self) -> str:
        '''Returns mysql, postgres or mongodb.'''
        return self.data.get('type')

    def getPublicHost(self) -> str:
        '''Returns the host shown to users.'''
        return self.data.get('public_host')

    def getPublicPort(self) -> int:
        '''Returns the port shown to users.'''
        return self.data.get('public_port')

    def isDeploymentEnabled(self) -> bool:
        '''Returns True if new databases can be created on it.'''
        return bool(self.data.get('deployment_enabled'))

    def isInMaintenance(self) -> bool:
        '''Returns True if the host is in maintenance mode.'''
        return bool(self.data.get('maintenance_enabled'))

    def test(self) -> dict:
        '''Tests the connection.'''
        return self.panel.api.admin.testDatabaseHost(self.getUUID())

    def getDatabases(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns databases on the host.'''
        return self._api().related(self.getUUID(), 'databases', 'databases', search, page, per_page)

    def deleteDatabase(self, database, force: bool = False) -> None:
        '''Deletes a database on the host.'''
        return self.panel.api.admin.deleteHostDatabase(self.getUUID(), idOf(database), force)

    def delete(self, force: bool = False) -> None:
        '''Deletes the host.'''
        return self._api().delete(self.getUUID(), force=force)


class DatabaseAgentHost(AdminResource):
    '''
    A machine running the Calagopus database agent, which hosts database instances.

    Example:
        host = panel.admin.database_agent_hosts.getDatabaseAgentHost('...')
        print(host.getSystemOverview())
    '''
    collection = 'database_agent_hosts'

    def _admin(self):
        return self.panel.api.admin

    def getURL(self) -> str:
        '''Returns the agent URL.'''
        return self.data.get('url')

    def getMemory(self) -> int:
        '''Returns memory available for instances, in MiB.'''
        return self.data.get('memory')

    def getDisk(self) -> int:
        '''Returns disk available for instances, in MiB.'''
        return self.data.get('disk')

    def getTypes(self) -> list:
        '''Returns the database engines the agent supports.'''
        return self.data.get('types', [])

    def test(self) -> dict:
        '''Tests the connection to the agent.'''
        return self._admin().databaseAgentHostPost(self.getUUID(), 'test')

    def getCapacity(self) -> dict:
        '''Returns limits and allocated resources.'''
        return self._admin().databaseAgentHostGet(self.getUUID(), 'capacity')

    def getToken(self) -> dict:
        '''Returns the agent token.'''
        return self._admin().databaseAgentHostGet(self.getUUID(), 'token')

    def resetToken(self) -> dict:
        '''Generates a new agent token.'''
        return self._admin().databaseAgentHostPost(self.getUUID(), 'reset-token')

    def getSystemOverview(self) -> dict:
        '''Returns agent version, CPU, memory and instance counts.'''
        return self._admin().databaseAgentHostGet(self.getUUID(), 'system/overview')

    def getSystemStats(self) -> dict:
        '''Returns live system statistics.'''
        return self._admin().databaseAgentHostGet(self.getUUID(), 'system/stats')['stats']

    def getConfig(self) -> dict:
        '''Returns the agent configuration.'''
        return self._admin().databaseAgentHostGet(self.getUUID(), 'config')

    def updateConfig(self, config: dict) -> bool:
        '''Applies changes to the agent configuration.'''
        return self._admin().updateDatabaseAgentHostConfig(self.getUUID(), config)

    def getInstances(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns database instances on this host.'''
        return self._api().related(self.getUUID(), 'instances', 'instances', search, page, per_page)

    def getInstance(self, instance_id: str) -> dict:
        '''Returns one database instance.'''
        return self._admin().databaseAgentInstance(self.getUUID(), instance_id)['instance']

    def updateInstance(self, instance_id: str, **fields) -> None:
        '''Changes an instance (name, locked, image, env, memory, swap, disk, io_weight, cpu).'''
        return self._admin().databaseAgentInstance(self.getUUID(), instance_id, 'PATCH', fields)

    def deleteInstance(self, instance_id: str, force: bool = False) -> None:
        '''Deletes an instance.'''
        return self._admin().databaseAgentInstance(self.getUUID(), instance_id, 'DELETE', {'force': force})

    def getBackups(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns database backups stored by this agent.'''
        return self._api().related(self.getUUID(), 'backups', 'backups', search, page, per_page)

    def deleteFailedBackups(self, force: bool = False) -> int:
        '''Deletes failed backups.'''
        return self._admin().deleteFailedBackups('database-agent-hosts', self.getUUID(), force)

    def delete(self, force: bool = False) -> None:
        '''Deletes the host.'''
        return self._api().delete(self.getUUID(), force=force)


class DatabaseAgentTemplate(AdminResource):
    '''A template defining how database instances are created (engine, images, limits).'''
    collection = 'database_agent_templates'

    def duplicate(self, name: str) -> 'DatabaseAgentTemplate':
        '''Creates a copy under a new name.'''
        return self._duplicate(name=name)

    def getType(self) -> str:
        '''Returns the engine type.'''
        return self.data.get('type')

    def getDockerImages(self) -> dict:
        '''Returns the allowed images.'''
        return self.data.get('docker_images', {})

    def getInstances(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns instances created from this template.'''
        return self._api().related(self.getUUID(), 'instances', 'instances', search, page, per_page)

    def updateInstances(self, instances) -> int:
        '''Applies template changes to existing instances.'''
        return self.panel.api.admin.updateTemplateInstances(self.getUUID(), instances)


class BackupConfiguration(AdminResource):
    '''
    Where and how backups are stored (local, S3, restic, kopia, ...).

    Example:
        config = panel.admin.backup_configurations.getBackupConfiguration('...')
        print(config.getStats()['all_time'])
    '''
    collection = 'backup_configurations'

    def duplicate(self, name: str) -> 'BackupConfiguration':
        '''Creates a copy under a new name.'''
        return self._duplicate(name=name)

    def getBackupDisk(self) -> str:
        '''Returns the storage driver, e.g. "s3" or "local".'''
        return self.data.get('backup_disk')

    def getBackupConfigs(self) -> dict:
        '''Returns the driver configuration.'''
        return self.data.get('backup_configs')

    def isShared(self) -> bool:
        '''Returns True if the configuration is shared.'''
        return bool(self.data.get('shared'))

    def isInMaintenance(self) -> bool:
        '''Returns True if backups are paused.'''
        return bool(self.data.get('maintenance_enabled'))

    def getStats(self) -> dict:
        '''Returns backup counts and sizes for today, this week, this month and all time.'''
        return self.panel.api.admin.backupConfigurationStats(self.getUUID())

    def getBackups(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns backups stored with this configuration.'''
        return self._api().related(self.getUUID(), 'backups', 'backups', search, page, per_page)

    def deleteFailedBackups(self, force: bool = False) -> int:
        '''Deletes failed backups.'''
        return self.panel.api.admin.deleteFailedBackups('backup-configurations', self.getUUID(), force)

    def getLocations(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns locations using this configuration.'''
        return self._api().related(self.getUUID(), 'locations', 'locations', search, page, per_page)

    def getNodes(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns nodes using this configuration.'''
        return self._api().related(self.getUUID(), 'nodes', 'nodes', search, page, per_page)

    def getServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns servers using this configuration.'''
        return self._api().related(self.getUUID(), 'servers', 'servers', search, page, per_page)


class BackupPolicy(AdminResource):
    '''
    A panel-wide backup policy that backs up servers on a cron schedule.

    Example:
        policy = panel.admin.backup_policies.createBackupPolicy('Nightly', '0 0 3 * * *')
        policy.attachLocation(location)
        policy.trigger()
    '''
    collection = 'system_backup_policies'

    def getCron(self) -> str:
        '''Returns the cron expression.'''
        return self.data.get('cron')

    def getRetention(self) -> dict:
        '''Returns the retention policy.'''
        return self.data.get('retention')

    def isEnabled(self) -> bool:
        '''Returns True if the policy is active.'''
        return bool(self.data.get('enabled'))

    def enable(self) -> 'BackupPolicy':
        '''Activates the policy.'''
        return self.update(enabled=True)

    def disable(self) -> 'BackupPolicy':
        '''Deactivates the policy.'''
        return self.update(enabled=False)

    def trigger(self) -> None:
        '''Runs the policy now.'''
        return self.panel.api.admin.triggerSystemBackupPolicy(self.getUUID())

    def getBackups(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns backups created by the policy.'''
        return self._api().related(self.getUUID(), 'backups', 'backups', search, page, per_page)

    def deleteFailedBackups(self, force: bool = False) -> int:
        '''Deletes failed backups.'''
        return self.panel.api.admin.deleteFailedBackups('system-backup-policies', self.getUUID(), force)

    def _targets(self, suffix, key, search, page, per_page):
        return self._api().related(self.getUUID(), suffix, key, search, page, per_page)

    def getLocations(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns locations covered by the policy.'''
        return self._targets('locations', 'locations', search, page, per_page)

    def getNodes(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns nodes covered by the policy.'''
        return self._targets('nodes', 'nodes', search, page, per_page)

    def getServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns servers covered by the policy.'''
        return self._targets('servers', 'servers', search, page, per_page)

    def getDatabaseAgentHosts(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns database agent hosts covered by the policy.'''
        return self._targets('database-agent-hosts', 'database_agent_hosts', search, page, per_page)

    def attachLocation(self, location) -> None:
        '''Adds a location to the policy.'''
        return self._api().attach(self.getUUID(), 'locations', 'location_uuid', idOf(location))

    def detachLocation(self, location) -> None:
        '''Removes a location from the policy.'''
        return self._api().detach(self.getUUID(), 'locations', idOf(location))

    def attachNode(self, node) -> None:
        '''Adds a node to the policy.'''
        return self._api().attach(self.getUUID(), 'nodes', 'node_uuid', idOf(node))

    def detachNode(self, node) -> None:
        '''Removes a node from the policy.'''
        return self._api().detach(self.getUUID(), 'nodes', idOf(node))

    def attachServer(self, server) -> None:
        '''Adds a server to the policy.'''
        return self._api().attach(self.getUUID(), 'servers', 'server_uuid', idOf(server))

    def detachServer(self, server) -> None:
        '''Removes a server from the policy.'''
        return self._api().detach(self.getUUID(), 'servers', idOf(server))

    def attachDatabaseAgentHost(self, host) -> None:
        '''Adds a database agent host to the policy.'''
        return self._api().attach(self.getUUID(), 'database-agent-hosts', 'database_agent_host_uuid', idOf(host))

    def detachDatabaseAgentHost(self, host) -> None:
        '''Removes a database agent host from the policy.'''
        return self._api().detach(self.getUUID(), 'database-agent-hosts', idOf(host))

    def delete(self, delete_backups: bool = False) -> None:
        '''Deletes the policy, optionally with its backups.'''
        return self._api().delete(self.getUUID(), delete_backups=delete_backups)


class EggRepository(AdminResource):
    '''
    A git repository of eggs that can be synced and installed from.

    Example:
        repo = panel.admin.egg_repositories.createEggRepository('Pelican eggs', 'https://github.com/pelican-eggs/minecraft')
        repo.sync()
        repo.installEggs(repo.getEggs(), nest)
    '''
    collection = 'egg_repositories'

    def getGitRepository(self) -> str:
        '''Returns the git URL.'''
        return self.data.get('git_repository')

    def sync(self) -> int:
        '''Pulls the repository. Returns the number of eggs found.'''
        return self.panel.api.admin.syncEggRepository(self.getUUID())

    def getEggs(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the eggs available in the repository.'''
        return self._api().related(self.getUUID(), 'eggs', 'egg_repository_eggs', search, page, per_page)

    def installEgg(self, egg, nest) -> dict:
        '''Installs one repository egg into a nest.'''
        egg_id = egg.get('uuid') if isinstance(egg, dict) else idOf(egg)
        return self.panel.api.admin.installRepositoryEgg(self.getUUID(), egg_id, idOf(nest))

    def installEggs(self, eggs: list, nest) -> int:
        '''Installs several repository eggs into a nest. Returns how many were installed.'''
        egg_ids = [e.get('uuid') if isinstance(e, dict) else idOf(e) for e in eggs]
        return self.panel.api.admin.installRepositoryEggs(self.getUUID(), egg_ids, idOf(nest))


class EggConfiguration(AdminResource):
    '''Rules that apply extra configuration (allocations, startup, routes, features) to matching eggs.'''
    collection = 'egg_configurations'

    def duplicate(self, name: str) -> 'EggConfiguration':
        '''Creates a copy under a new name.'''
        return self._duplicate(name=name)

    def getOrder(self) -> int:
        '''Returns the priority order.'''
        return self.data.get('order')

    def getMatcher(self) -> dict:
        '''Returns the rule deciding which eggs match.'''
        return self.data.get('matcher')


class SubdomainDomain(AdminResource):
    '''
    A domain users can create subdomains on (Subdomain Manager extension).

    Example:
        domain = panel.admin.subdomain_domains.createDomain('example.com', 'cloudflare', {'api_token': '...'})
        print(domain.test())
    '''
    collection = 'subdomain_domains'

    def getName(self) -> str:
        '''Returns the domain.'''
        return self.data.get('domain')

    def getDomain(self) -> str:
        '''Returns the domain.'''
        return self.data.get('domain')

    def getProvider(self) -> str:
        '''Returns the DNS provider: cloudflare or powerdns.'''
        return self.data.get('provider')

    def getEggs(self) -> list:
        '''Returns the eggs allowed to use the domain. Empty means all.'''
        return self.data.get('eggs', [])

    def refresh(self) -> 'SubdomainDomain':
        '''Re-fetches the domain from the panel.'''
        for data in self._api().list():
            if data.get('uuid') == self.getUUID():
                self.data = data
        return self

    def rename(self, domain: str) -> 'SubdomainDomain':
        '''Changes the domain name.'''
        return self.update(domain=domain)

    def setName(self, domain: str) -> 'SubdomainDomain':
        '''Changes the domain name.'''
        return self.update(domain=domain)

    def setDescription(self, description: str):
        '''Domains have no description.'''
        raise InvalidActionError('Subdomain domains have no description')

    def test(self) -> dict:
        '''Tests the DNS provider credentials.'''
        return self.panel.api.admin.testSubdomainDomain(self.getUUID())

    def getSubdomains(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns subdomains created on this domain.'''
        return self._api().related(self.getUUID(), 'subdomains', 'subdomains', search, page, per_page)
