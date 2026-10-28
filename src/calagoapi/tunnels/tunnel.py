from calagoapi.utils.model import idOf


class TunnelManager:
    '''
    The server's network tunnel, available as `server.tunnel`.

    A tunnel exposes server ports through the node's tunnel without opening
    them publicly, and lets servers reach each other privately.

    Example:
        if server.tunnel.isSupported() and not server.tunnel.exists():
            server.tunnel.createTunnel('survival')
        server.tunnel.setPorts([25565])
        server.tunnel.connect(proxy_server)
        print(server.tunnel.getAddress())
    '''
    def __init__(self, server):
        self.server = server
        self.api = server.panel.api.network

    @property
    def server_id(self):
        return self.server.server_id

    def getInfo(self) -> dict:
        '''
        Returns the full tunnel state.

        Returns:
            dict with supported, tunnel, ports, allocation_ports, outgoing and incoming.
        '''
        return self.api.tunnel(self.server_id)

    def getTunnel(self) -> dict:
        '''Returns the tunnel (name, alias, address), or None if none exists.'''
        return self.getInfo().get('tunnel')

    def isSupported(self) -> bool:
        '''Returns True if the server's node supports tunnels.'''
        return bool(self.getInfo().get('supported'))

    def exists(self) -> bool:
        '''Returns True if the server has a tunnel.'''
        return self.getTunnel() is not None

    def getName(self) -> str:
        '''Returns the tunnel name.'''
        return (self.getTunnel() or {}).get('name')

    def getAlias(self) -> str:
        '''Returns the tunnel alias (the hostname other servers use).'''
        return (self.getTunnel() or {}).get('alias')

    def getAddress(self) -> str:
        '''Returns the public tunnel address, if any.'''
        return (self.getTunnel() or {}).get('address')

    def getPorts(self) -> list:
        '''Returns the ports exposed through the tunnel.'''
        return self.getInfo().get('ports', [])

    def getOutgoing(self) -> list:
        '''Returns the servers this server can reach through the tunnel.'''
        return self.getInfo().get('outgoing', [])

    def getIncoming(self) -> list:
        '''Returns the servers that can reach this server through the tunnel.'''
        return self.getInfo().get('incoming', [])

    def createTunnel(self, name: str = None) -> dict:
        '''Creates the tunnel. Returns the tunnel info.'''
        return self.api.createTunnel(self.server_id, name)

    def rename(self, name: str) -> dict:
        '''Renames the tunnel.'''
        return self.api.renameTunnel(self.server_id, name)

    def deleteTunnel(self) -> None:
        '''Deletes the tunnel.'''
        return self.api.deleteTunnel(self.server_id)

    def setPorts(self, ports: list) -> None:
        '''
        Sets the exposed ports.

        Args:
            ports: List of port numbers (tcp + udp), or {'port': 25565, 'protocols': ['tcp']} dicts.

        Example:
            server.tunnel.setPorts([25565, {'port': 19132, 'protocols': ['udp']}])
        '''
        ports = [p if isinstance(p, dict) else {'port': p, 'protocols': ['tcp', 'udp']} for p in ports]
        return self.api.setTunnelPorts(self.server_id, ports)

    def getConnectableServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns servers this tunnel can connect to.'''
        return self.api.tunnelConnectable(self.server_id, search, None, page, per_page)

    def connect(self, server) -> None:
        '''Lets this server reach another server (object or id) through the tunnel.'''
        return self.api.connectTunnel(self.server_id, idOf(server))

    def disconnect(self, server, incoming: bool = False) -> None:
        '''
        Removes a tunnel connection.

        Args:
            server: The connected server (object or id).
            incoming: Remove the connection that reaches this server instead of the outgoing one.
        '''
        return self.api.disconnectTunnel(self.server_id, idOf(server), incoming or None)
