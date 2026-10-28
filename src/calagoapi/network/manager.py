from calagoapi.network.allocation import Allocation, Subdomain
from calagoapi.utils.model import idOf
from calagoapi.utils.exceptions import InvalidActionError


class NetworkManager:
    '''
    Allocations, subdomains and firewall for one server, available as `server.network`.

    Example:
        print(server.network.getPrimaryAllocation().getAddress())
        server.network.addFirewallRule('allow', ports=[25565], sources=['0.0.0.0/0'])
    '''
    def __init__(self, server):
        self.server = server
        self.api = server.panel.api.network

    @property
    def server_id(self):
        return self.server.server_id

    # allocations
    def getAllocations(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists the server's allocations as a Page of Allocation objects.'''
        return self.api.allocations(self.server_id, search, page, per_page).map(lambda data: Allocation(self.server, data))

    def getPrimaryAllocation(self) -> Allocation:
        '''Returns the primary allocation, or None.'''
        return next((a for a in self.getAllocations() if a.isPrimary()), None)

    def createAllocation(self) -> Allocation:
        '''
        Assigns a new allocation from the node's free pool.

        Only works if the server's allocation limit allows it.
        '''
        return Allocation(self.server, self.api.createAllocation(self.server_id))

    def setPrimaryAllocation(self, allocation) -> None:
        '''Makes an allocation the primary one.'''
        return self.api.updateAllocation(self.server_id, idOf(allocation), primary=True)

    def deleteAllocation(self, allocation) -> None:
        '''Removes an allocation from the server.'''
        return self.api.deleteAllocation(self.server_id, idOf(allocation))

    # subdomains
    def getSubdomains(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists the server's subdomains as a Page of Subdomain objects.'''
        return self.api.subdomains(self.server_id, search, page, per_page).map(lambda data: Subdomain(self.server, data))

    def getAvailableDomains(self) -> list:
        '''Returns the domains subdomains can be created on.'''
        return self.api.subdomainDomains(self.server_id)

    def createSubdomain(self, subdomain: str, domain=None, allocation=None) -> Subdomain:
        '''
        Creates a subdomain.

        Args:
            subdomain: Subdomain part, e.g. "survival".
            domain: Domain name or UUID. Defaults to the first available domain.
            allocation: Allocation to point to. Defaults to the primary allocation.

        Example:
            server.network.createSubdomain('survival', 'example.com')
        '''
        domains = self.getAvailableDomains()
        if domain is None:
            if not domains:
                raise InvalidActionError('No subdomain domains are available for this server')
            domain_id = domains[0]['uuid']
        else:
            match = next((d for d in domains if domain in (d.get('uuid'), d.get('domain'))), None)
            domain_id = match['uuid'] if match else domain
        if allocation is None:
            allocation = self.getPrimaryAllocation()
        return Subdomain(self.server, self.api.createSubdomain(self.server_id, domain_id, idOf(allocation), subdomain))

    def deleteSubdomain(self, subdomain) -> None:
        '''Deletes a subdomain.'''
        return self.api.deleteSubdomain(self.server_id, idOf(subdomain))

    # firewall
    def getFirewall(self) -> dict:
        '''
        Returns the firewall state.

        Returns:
            dict with `supported` (bool), `rules` (list) and `allocation_ports`.
        '''
        return self.api.firewall(self.server_id)

    def isFirewallSupported(self) -> bool:
        '''Returns True if the node supports per-server firewalls.'''
        return bool(self.getFirewall().get('supported'))

    def getFirewallRules(self) -> list:
        '''Returns the firewall rules.'''
        return self.getFirewall().get('rules', [])

    def setFirewallRules(self, rules: list) -> None:
        '''
        Replaces every firewall rule.

        Args:
            rules: List of {'action': 'allow'|'deny', 'protocols': ['tcp', 'udp'],
                'sources': ['1.2.3.4/32'], 'ports': [25565]} dicts.
        '''
        return self.api.setFirewallRules(self.server_id, rules)

    def addFirewallRule(self, action: str, ports: list = None, sources: list = None, protocols: list = None) -> None:
        '''
        Appends a firewall rule.

        Args:
            action: 'allow' or 'deny'.
            ports: Ports the rule applies to. All ports when omitted.
            sources: Source IPs/CIDRs. Everyone when omitted.
            protocols: ['tcp'], ['udp'] or both (default).

        Example:
            server.network.addFirewallRule('deny', sources=['203.0.113.7/32'])
        '''
        rule = {'action': action, 'protocols': protocols or ['tcp', 'udp'], 'sources': sources or []}
        if ports:
            rule['ports'] = ports
        return self.setFirewallRules(self.getFirewallRules() + [rule])

    def clearFirewallRules(self) -> None:
        '''Removes every firewall rule.'''
        return self.setFirewallRules([])
