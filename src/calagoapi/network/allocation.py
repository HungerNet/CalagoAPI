from calagoapi.utils.model import Model, idOf


class Allocation(Model):
    '''
    An IP and port assigned to a server.

    Example:
        primary = server.network.getPrimaryAllocation()
        print(primary.getAddress())  # 'play.example.com:25565'
        extra = server.network.createAllocation()
        extra.setNotes('Dynmap')
    '''
    def __init__(self, server, data: dict):
        super().__init__(server.panel, data)
        self.server = server

    def __repr__(self):
        return f'<Allocation {self.getAddress()!r}>'

    def getIP(self) -> str:
        '''Returns the IP address.'''
        return self.data.get('ip')

    def getAlias(self) -> str:
        '''Returns the IP alias (usually a hostname), or None.'''
        return self.data.get('ip_alias')

    def getPort(self) -> int:
        '''Returns the port.'''
        return self.data.get('port')

    def getAddress(self) -> str:
        '''Returns "alias:port", or "ip:port" when there is no alias.'''
        return f'{self.getAlias() or self.getIP()}:{self.getPort()}'

    def getNotes(self) -> str:
        '''Returns the allocation notes.'''
        return self.data.get('notes')

    def isPrimary(self) -> bool:
        '''Returns True for the server's primary allocation.'''
        return bool(self.data.get('is_primary'))

    def setNotes(self, notes: str) -> 'Allocation':
        '''Sets the allocation notes.'''
        self.panel.api.network.updateAllocation(self.server.server_id, self.getUUID(), notes=notes)
        return self._update({'notes': notes})

    def makePrimary(self) -> 'Allocation':
        '''Makes this the server's primary allocation.'''
        self.panel.api.network.updateAllocation(self.server.server_id, self.getUUID(), primary=True)
        return self._update({'is_primary': True})

    def delete(self) -> None:
        '''Removes the allocation from the server.'''
        return self.panel.api.network.deleteAllocation(self.server.server_id, self.getUUID())


class Subdomain(Model):
    '''
    A subdomain pointing at one of the server's allocations (Subdomain Manager extension).

    Example:
        sub = server.network.createSubdomain('survival', domain='example.com')
        print(sub.getAddress())  # 'survival.example.com'
    '''
    def __init__(self, server, data: dict):
        super().__init__(server.panel, data)
        self.server = server

    def __repr__(self):
        return f'<Subdomain {self.getAddress()!r}>'

    def getSubdomain(self) -> str:
        '''Returns the subdomain part, e.g. "survival".'''
        return self.data.get('subdomain')

    def getDomain(self) -> str:
        '''Returns the parent domain, e.g. "example.com".'''
        return (self.data.get('domain') or {}).get('domain')

    def getAddress(self) -> str:
        '''Returns the full hostname, e.g. "survival.example.com".'''
        return f'{self.getSubdomain()}.{self.getDomain()}'

    def getAllocation(self) -> Allocation:
        '''Returns the allocation the subdomain points to, or None.'''
        data = self.data.get('allocation')
        return Allocation(self.server, data) if data else None

    def setAllocation(self, allocation) -> 'Subdomain':
        '''Points the subdomain at another allocation.'''
        self.panel.api.network.updateSubdomain(self.server.server_id, self.getUUID(), idOf(allocation))
        return self

    def delete(self) -> None:
        '''Deletes the subdomain.'''
        return self.panel.api.network.deleteSubdomain(self.server.server_id, self.getUUID())
