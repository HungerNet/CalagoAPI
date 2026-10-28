from calagoapi.servers.generic import GenericServer
from calagoapi.servers.minecraft import MinecraftServer
from calagoapi.utils.model import Model, idOf


class ServerGroup(Model):
    '''
    A personal folder of servers in the panel sidebar.

    Example:
        group = panel.servers.createGroup('Minigames', [lobby, bedwars])
        group.addServer(skywars)
    '''
    def _api(self):
        return self.panel.api.servers

    def getName(self) -> str:
        '''Returns the group name.'''
        return self.data.get('name')

    def getOrder(self) -> int:
        '''Returns the group's position in the sidebar.'''
        return self.data.get('order')

    def getServerIds(self) -> list:
        '''Returns the UUIDs of the servers in the group, in display order.'''
        return self.data.get('server_order', [])

    def getServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the servers in the group as GenericServer objects.'''
        return self._api().groupServers(self.getUUID(), search, page, per_page).map(
            lambda data: GenericServer(self.panel, data=data)
        )

    def rename(self, name: str) -> 'ServerGroup':
        '''Renames the group.'''
        self._api().updateGroup(self.getUUID(), name)
        return self._update({'name': name})

    def setServers(self, servers: list) -> 'ServerGroup':
        '''Replaces the servers in the group (objects or ids), in display order.'''
        server_order = [idOf(s) for s in servers]
        self._api().updateGroup(self.getUUID(), self.getName(), server_order)
        return self._update({'server_order': server_order})

    def addServer(self, server) -> 'ServerGroup':
        '''Adds a server to the group.'''
        return self.setServers(self.getServerIds() + [idOf(server)])

    def removeServer(self, server) -> 'ServerGroup':
        '''Removes a server from the group.'''
        return self.setServers([s for s in self.getServerIds() if s != idOf(server)])

    def delete(self) -> None:
        '''Deletes the group (the servers are not affected).'''
        return self._api().deleteGroup(self.getUUID())


class ServerManager:
    '''
    Access to the servers the API key can see, available as `panel.servers`.

    Example:
        server = panel.servers.getServer('abc123')
        for server in panel.servers.getServers():
            print(server.getName(), server.getStatus())
    '''
    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.servers

    def getServer(self, server_id: str, name: str = None) -> GenericServer:
        '''
        Returns a server.

        Args:
            server_id: Server UUID or short id.
            name: Optional display name used in logs and repr().

        Example:
            server = panel.servers.getServer('abc123')
        '''
        server = GenericServer(self.panel, server_id, name)
        server.refreshDetails()
        if name is None:
            server.name = server.getName()
        return server

    def getMinecraftServer(self, server_id: str, name: str = None, server_domain: str = None, server_port: int = None) -> MinecraftServer:
        '''
        Returns a server with the Minecraft helpers of MinecraftServer.

        Example:
            server = panel.servers.getMinecraftServer('abc123')
            server.say('Hello')
        '''
        server = MinecraftServer(self.panel, server_id, name, server_domain, server_port)
        server.refreshDetails()
        if name is None:
            server.name = server.getName()
        return server

    def getServers(self, search: str = None, page: int = None, per_page: int = None, all_servers: bool = False):
        '''
        Lists servers.

        Args:
            search: Filter by name.
            page: Only fetch this page. By default every server is returned.
            per_page: Page size.
            all_servers: Admins only, include servers the user does not own or have access to.

        Returns:
            A Page (list) of GenericServer objects.
        '''
        return self.api.list(search, all_servers or None, page, per_page).map(
            lambda data: GenericServer(self.panel, data=data)
        )

    def listServers(self, search: str = None):
        '''Alias of getServers().'''
        return self.getServers(search)

    def getServerByName(self, name: str) -> GenericServer:
        '''Returns the first server whose name matches exactly, or None.'''
        for server in self.getServers(search=name):
            if server.getName() == name:
                return server
        return None

    def getEggs(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the eggs (server types) used by the user's servers.'''
        return self.api.eggs(search, page, per_page)

    def getCommandSnippets(self, egg) -> list:
        '''Returns the user's command snippets that apply to an egg.'''
        return self.api.eggCommandSnippets(egg.get('uuid') if isinstance(egg, dict) else idOf(egg))

    # groups
    def getGroups(self) -> list:
        '''Returns the user's server groups.'''
        return [ServerGroup(self.panel, data) for data in self.api.groups()]

    def getGroup(self, group_id_or_name: str) -> ServerGroup:
        '''Returns a server group by UUID or name, or None.'''
        for group in self.getGroups():
            if group_id_or_name in (group.getUUID(), group.getName()):
                return group
        return None

    def createGroup(self, name: str, servers: list = None) -> ServerGroup:
        '''
        Creates a server group.

        Args:
            name: Group name.
            servers: Servers (objects or ids) to put in it.
        '''
        return ServerGroup(self.panel, self.api.createGroup(name, [idOf(s) for s in servers or []]))

    def deleteGroup(self, group) -> None:
        '''Deletes a server group.'''
        return self.api.deleteGroup(idOf(group))

    def orderGroups(self, groups: list) -> None:
        '''Sets the order of the server groups.'''
        return self.api.orderGroups([idOf(g) for g in groups])
