# Internal Calagopus NetworkAPI (allocations, subdomains, tunnels, firewall)
class NetworkAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, suffix=''):
        return f'/api/client/servers/{server_id}{suffix}'

    # allocations
    def allocations(self, server_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, '/allocations'), 'allocations', {'search': search}, page, per_page)

    def createAllocation(self, server_id):
        return self.client.post(self._path(server_id, '/allocations'))['allocation']

    def updateAllocation(self, server_id, allocation_id, notes=None, primary=None):
        return self.client.patch(
            self._path(server_id, f'/allocations/{allocation_id}'),
            json={'notes': notes, 'primary': primary}
        )

    def deleteAllocation(self, server_id, allocation_id):
        return self.client.delete(self._path(server_id, f'/allocations/{allocation_id}'))

    # subdomains
    def subdomains(self, server_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, '/subdomains'), 'subdomains', {'search': search}, page, per_page)

    def subdomainDomains(self, server_id):
        return self.client.get(self._path(server_id, '/subdomains/domains'))['domains']

    def createSubdomain(self, server_id, domain_uuid, allocation_uuid, subdomain):
        return self.client.post(self._path(server_id, '/subdomains'), json={
            'domain_uuid': domain_uuid,
            'allocation_uuid': allocation_uuid,
            'subdomain': subdomain,
        })['subdomain']

    def updateSubdomain(self, server_id, subdomain_id, allocation_uuid):
        return self.client.patch(
            self._path(server_id, f'/subdomains/{subdomain_id}'),
            json={'allocation_uuid': allocation_uuid}
        )

    def deleteSubdomain(self, server_id, subdomain_id):
        return self.client.delete(self._path(server_id, f'/subdomains/{subdomain_id}'))

    # tunnel
    def tunnel(self, server_id):
        return self.client.get(self._path(server_id, '/tunnel'))

    def createTunnel(self, server_id, name=None):
        return self.client.post(self._path(server_id, '/tunnel'), json={'name': name})['tunnel']

    def renameTunnel(self, server_id, name):
        return self.client.patch(self._path(server_id, '/tunnel'), json={'name': name})['tunnel']

    def deleteTunnel(self, server_id):
        return self.client.delete(self._path(server_id, '/tunnel'))

    def setTunnelPorts(self, server_id, ports):
        return self.client.put(self._path(server_id, '/tunnel/ports'), json={'ports': ports})

    def tunnelConnectable(self, server_id, search=None, other=None, page=None, per_page=None):
        return self.client.list(
            self._path(server_id, '/tunnel/connections/available'), 'servers',
            {'search': search, 'other': other}, page, per_page
        )

    def connectTunnel(self, server_id, target_server):
        return self.client.post(self._path(server_id, '/tunnel/connections'), json={'server': target_server})

    def disconnectTunnel(self, server_id, connection_id, incoming=None):
        return self.client.delete(
            self._path(server_id, f'/tunnel/connections/{connection_id}'),
            params={'incoming': incoming}
        )

    # firewall
    def firewall(self, server_id):
        return self.client.get(self._path(server_id, '/firewall'))

    def setFirewallRules(self, server_id, rules):
        return self.client.put(self._path(server_id, '/firewall'), json={'rules': rules})
