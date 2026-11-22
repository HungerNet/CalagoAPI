from calagoapi import Panel
from calagoapi.extensions import classExtension

from calagoapi_minecraft.server import MinecraftServer


@classExtension(Panel, 'minecraft')
class MinecraftManager:
    '''
    Minecraft servers of a panel, available as `panel.minecraft` after `enable('minecraft')`.

    Example:
        from calagoapi.extensions import enable
        enable('minecraft', config={'bridge_token_id': 'bot', 'bridge_token_secret': '9f2c...'})

        server = panel.minecraft.getServer('abc123')
        server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913', address='play.example.com')
    '''
    def __init__(self, panel):
        self.panel = panel

    def __repr__(self):
        return f'<MinecraftManager of {self.panel!r}>'

    def getServer(self, server_id: str, name: str = None, **options) -> MinecraftServer:
        '''
        Returns a server as a MinecraftServer.

        Args:
            server_id: Server UUID or short id.
            name: Optional display name.
            **options: MinecraftServer options: address, bridge_url, bridge_token_id, bridge_token_secret.
        '''
        return self.panel.servers.getServer(server_id, name, server_class=MinecraftServer, **options)

    def getServers(self, search: str = None, page: int = None, per_page: int = None, all_servers: bool = False,
                   **options):
        '''
        Returns every server the API key can see as MinecraftServer objects
        (the panel does not mark which servers run Minecraft; filter as you need).
        '''
        return self.panel.servers.getServers(search, page, per_page, all_servers, server_class=MinecraftServer,
                                             **options)

    def fromServer(self, server, **options) -> MinecraftServer:
        '''
        Turns a Server (e.g. from panel.servers.getServer()) into a MinecraftServer,
        reusing its fetched details.

        Example:
            server = panel.minecraft.fromServer(panel.servers.getServerByName('Survival'))
        '''
        return MinecraftServer(server.panel, server.server_id, server.name, dict(server.data), **options)
