from calagoapi.api.client import segment


# Internal Calagopus AdminAPI
class ResourceAPI:
    '''Standard CRUD calls for one admin collection, e.g. /api/admin/locations'''
    def __init__(self, client, path, key, plural, parent=None):
        self.client = client
        self.path = f'/api/admin{path}'
        self.key = key
        self.plural = plural
        # id(s) of the owning object for nested collections, e.g. the nest of an egg
        self.parent = parent

    def list(self, search=None, page=None, per_page=None, **params):
        if search is not None:
            params['search'] = search
        return self.client.list(self.path, self.plural, params, page, per_page)

    def listAll(self):
        '''For collections that are not paginated'''
        return self.client.get(self.path)[self.plural]

    def get(self, resource_id):
        return self.client.get(f'{self.path}/{resource_id}')[self.key]

    def create(self, **fields):
        return self.client.post(self.path, json=fields)[self.key]

    def update(self, resource_id, **fields):
        return self.client.patch(f'{self.path}/{resource_id}', json=fields)

    def delete(self, resource_id, **body):
        return self.client.delete(f'{self.path}/{resource_id}', json=body or None)

    def duplicate(self, resource_id, **fields):
        return self.client.post(f'{self.path}/{resource_id}/duplicate', json=fields or None)[self.key]

    # sub-collections like /locations/{id}/nodes
    def related(self, resource_id, suffix, key, search=None, page=None, per_page=None, **params):
        if search is not None:
            params['search'] = search
        return self.client.list(f'{self.path}/{resource_id}/{suffix}', key, params, page, per_page)

    def attach(self, resource_id, suffix, field, value):
        return self.client.post(f'{self.path}/{resource_id}/{suffix}', json={field: value})

    def detach(self, resource_id, suffix, child_id):
        return self.client.delete(f'{self.path}/{resource_id}/{suffix}/{child_id}')

    def action(self, resource_id, suffix, method='POST', json=None, params=None):
        return self.client.request(method, f'{self.path}/{resource_id}/{suffix}', json=json, params=params)


class AdminAPI:
    def __init__(self, client):
        self.client = client

        self.users = ResourceAPI(client, '/users', 'user', 'users')
        self.servers = ResourceAPI(client, '/servers', 'server', 'servers')
        self.nodes = ResourceAPI(client, '/nodes', 'node', 'nodes')
        self.locations = ResourceAPI(client, '/locations', 'location', 'locations')
        self.nests = ResourceAPI(client, '/nests', 'nest', 'nests')
        self.mounts = ResourceAPI(client, '/mounts', 'mount', 'mounts')
        self.devices = ResourceAPI(client, '/devices', 'device', 'devices')
        self.roles = ResourceAPI(client, '/roles', 'role', 'roles')
        self.announcements = ResourceAPI(client, '/announcements', 'announcement', 'announcements')
        self.oauth_providers = ResourceAPI(client, '/oauth-providers', 'oauth_provider', 'oauth_providers')
        self.database_hosts = ResourceAPI(client, '/database-hosts', 'database_host', 'database_hosts')
        self.database_agent_hosts = ResourceAPI(client, '/database-agent-hosts', 'database_agent_host', 'database_agent_hosts')
        self.database_agent_templates = ResourceAPI(client, '/database-agent-templates', 'database_agent_template', 'database_agent_templates')
        self.backup_configurations = ResourceAPI(client, '/backup-configurations', 'backup_configuration', 'backup_configurations')
        self.system_backup_policies = ResourceAPI(client, '/system-backup-policies', 'system_backup_policy', 'system_backup_policies')
        self.egg_repositories = ResourceAPI(client, '/egg-repositories', 'egg_repository', 'egg_repositories')
        self.egg_configurations = ResourceAPI(client, '/egg-configurations', 'egg_configuration', 'egg_configurations')
        self.subdomain_domains = ResourceAPI(client, '/extensions/dev.0x7d8.subdomainmanager/domains', 'domain', 'domains')

    # nested collections
    def eggs(self, nest_id):
        return ResourceAPI(self.client, f'/nests/{nest_id}/eggs', 'egg', 'eggs', nest_id)

    def eggVariables(self, nest_id, egg_id):
        return ResourceAPI(self.client, f'/nests/{nest_id}/eggs/{egg_id}/variables', 'variable', 'variables', (nest_id, egg_id))

    def orderEggVariables(self, nest_id, egg_id, variable_order):
        return self.client.put(f'/api/admin/nests/{nest_id}/eggs/{egg_id}/variables/order', json={'variable_order': variable_order})

    def oauthMappings(self, oauth_provider_id):
        return ResourceAPI(self.client, f'/oauth-providers/{oauth_provider_id}/mappings', 'oauth_mapping', 'oauth_mappings', oauth_provider_id)

    def userOauthLinks(self, user_id):
        return ResourceAPI(self.client, f'/users/{user_id}/oauth-links', 'oauth_link', 'oauth_links', user_id)

    # users
    def userByExternalId(self, external_id):
        return self.client.get(f'/api/admin/users/external/{segment(external_id)}')['user']

    def userServers(self, user_id, owned=None, search=None, page=None, per_page=None):
        return self.users.related(user_id, 'servers', 'servers', search, page, per_page, owned=owned)

    def userActivity(self, user_id, search=None, page=None, per_page=None):
        return self.users.related(user_id, 'activity', 'activities', search, page, per_page)

    def userDisableTwoFactor(self, user_id):
        return self.client.delete(f'/api/admin/users/{user_id}/two-factor')

    def userSendPasswordReset(self, user_id):
        return self.client.post(f'/api/admin/users/{user_id}/email/reset-password')

    def userVerifyEmail(self, user_id):
        return self.client.post(f'/api/admin/users/{user_id}/email/verify')

    # servers
    def serverByExternalId(self, external_id):
        return self.client.get(f'/api/admin/servers/external/{segment(external_id)}')['server']

    def deployServer(self, **fields):
        return self.client.post('/api/admin/servers/deploy', json=fields)['server']

    def serverLogs(self, server_id, lines=None, install=False):
        suffix = 'logs/install' if install else 'logs'
        return self.client.get(f'/api/admin/servers/{server_id}/{suffix}', params={'lines': lines})

    def serverVariables(self, server_id):
        return self.client.get(f'/api/admin/servers/{server_id}/variables')['variables']

    def setServerVariables(self, server_id, variables):
        return self.client.put(f'/api/admin/servers/{server_id}/variables', json={'variables': variables})

    def serverAllocations(self, server_id, search=None, page=None, per_page=None):
        return self.servers.related(server_id, 'allocations', 'allocations', search, page, per_page)

    def addServerAllocation(self, server_id, allocation_uuid):
        return self.client.post(f'/api/admin/servers/{server_id}/allocations', json={'allocation_uuid': allocation_uuid})['allocation']

    def updateServerAllocation(self, server_id, allocation_id, notes=None, primary=None):
        return self.client.patch(f'/api/admin/servers/{server_id}/allocations/{allocation_id}', json={'notes': notes, 'primary': primary})

    def removeServerAllocation(self, server_id, allocation_id):
        return self.client.delete(f'/api/admin/servers/{server_id}/allocations/{allocation_id}')

    def serverBackups(self, server_id, partially_detached=None, search=None, page=None, per_page=None):
        return self.servers.related(server_id, 'backups', 'backups', search, page, per_page, partially_detached=partially_detached)

    def serverDeleteFailedBackups(self, server_id, force=False, partially_detached=None):
        return self.client.post(
            f'/api/admin/servers/{server_id}/backups/delete-failed',
            json={'force': force, 'partially_detached': partially_detached}
        )['queued']

    def serverDatabases(self, server_id, search=None, page=None, per_page=None):
        return self.servers.related(server_id, 'databases', 'databases', search, page, per_page)

    def serverDatabaseInstances(self, server_id, search=None, page=None, per_page=None):
        return self.servers.related(server_id, 'databases/instances', 'instances', search, page, per_page)

    def serverMounts(self, server_id, available=False, search=None, page=None, per_page=None):
        suffix = 'mounts/available' if available else 'mounts'
        return self.servers.related(server_id, suffix, 'mounts', search, page, per_page)

    def serverDevices(self, server_id, available=False, search=None, page=None, per_page=None):
        suffix = 'devices/available' if available else 'devices'
        return self.servers.related(server_id, suffix, 'devices', search, page, per_page)

    def clearServerState(self, server_id):
        return self.client.post(f'/api/admin/servers/{server_id}/clear-state')

    def transferServer(self, server_id, **fields):
        return self.client.post(f'/api/admin/servers/{server_id}/transfer', json=fields)

    def cancelServerTransfer(self, server_id):
        return self.client.post(f'/api/admin/servers/{server_id}/transfer/cancel')

    # nodes
    def nodeAllocations(self, node_id, search=None, ip=None, port_from=None, port_to=None, assigned=None, page=None, per_page=None):
        return self.nodes.related(
            node_id, 'allocations', 'allocations', search, page, per_page,
            ip=ip, port_from=port_from, port_to=port_to, assigned=assigned
        )

    def nodeAvailableAllocations(self, node_id, search=None, page=None, per_page=None):
        return self.nodes.related(node_id, 'allocations/available', 'allocations', search, page, per_page)

    def nodeAllocationIps(self, node_id):
        return self.client.get(f'/api/admin/nodes/{node_id}/allocations/ips')['ips']

    def createNodeAllocations(self, node_id, ip, ports, ip_alias=None):
        return self.client.post(f'/api/admin/nodes/{node_id}/allocations', json={'ip': ip, 'ports': ports, 'ip_alias': ip_alias})['created']

    def updateNodeAllocations(self, node_id, selector, ip, ip_alias=None):
        return self.client.patch(f'/api/admin/nodes/{node_id}/allocations', json={'selector': selector, 'ip': ip, 'ip_alias': ip_alias})

    def deleteNodeAllocations(self, node_id, selector, force=None):
        return self.client.delete(f'/api/admin/nodes/{node_id}/allocations', json={'selector': selector, 'force': force})

    def nodeBackups(self, node_id, detached=None, search=None, page=None, per_page=None):
        return self.nodes.related(node_id, 'backups', 'backups', search, page, per_page, detached=detached)

    def nodeBackup(self, node_id, backup_id):
        return self.client.get(f'/api/admin/nodes/{node_id}/backups/{backup_id}')['backup']

    def nodeBackupAction(self, node_id, backup_id, action, method='POST', json=None):
        suffix = f'/{action}' if action else ''
        return self.client.request(method, f'/api/admin/nodes/{node_id}/backups/{backup_id}{suffix}', json=json)

    def nodeDeleteFailedBackups(self, node_id, force=False, detached=None):
        return self.client.post(f'/api/admin/nodes/{node_id}/backups/delete-failed', json={'force': force, 'detached': detached})['queued']

    def nodeConfig(self, node_id):
        return self.client.get(f'/api/admin/nodes/{node_id}/config')

    def updateNodeConfig(self, node_id, config):
        return self.client.patch(f'/api/admin/nodes/{node_id}/config', json=config)['applied']

    def updateNodesConfig(self, node_ids, config):
        return self.client.patch('/api/admin/nodes/config', json={'node_uuids': node_ids, 'config': config})

    def nodeCapacities(self):
        return self.client.get('/api/admin/nodes/capacities')['allocated']

    def probeNode(self, url, pairing_code):
        return self.client.post('/api/admin/nodes/probe', json={'url': url, 'pairing_code': pairing_code})['probe']

    def nodeGet(self, node_id, suffix, params=None):
        return self.client.get(f'/api/admin/nodes/{node_id}/{suffix}', params=params)

    def nodePost(self, node_id, suffix, json=None):
        return self.client.post(f'/api/admin/nodes/{node_id}/{suffix}', json=json)

    def nodeSystemLog(self, node_id, file, lines=None):
        return self.client.get(f'/api/admin/nodes/{node_id}/system/logs/{segment(file)}', params={'lines': lines})

    def nodeServerPower(self, node_id, action, server_ids=None):
        selector = {'type': 'uuids', 'uuids': server_ids} if server_ids else {'type': 'all'}
        return self.client.post(f'/api/admin/nodes/{node_id}/servers/power', json={'servers': selector, 'action': action})['affected']

    def nodeServerTransfer(self, node_id, **fields):
        return self.client.post(f'/api/admin/nodes/{node_id}/servers/transfer', json=fields)

    def nodeTunnel(self, node_id, method='GET', json=None, suffix=''):
        return self.client.request(method, f'/api/admin/nodes/{node_id}/tunnel{suffix}', json=json)

    # nests and eggs
    def allEggs(self):
        return self.client.get('/api/admin/nests/eggs')['nests']

    # egg repositories
    def syncEggRepository(self, repository_id):
        return self.client.post(f'/api/admin/egg-repositories/{repository_id}/sync')['found']

    def installRepositoryEggs(self, repository_id, egg_ids, nest_uuid):
        return self.client.post(
            f'/api/admin/egg-repositories/{repository_id}/eggs/install',
            json={'egg_uuids': egg_ids, 'nest_uuid': nest_uuid}
        )['installed']

    def installRepositoryEgg(self, repository_id, egg_id, nest_uuid):
        return self.client.post(
            f'/api/admin/egg-repositories/{repository_id}/eggs/{egg_id}/install',
            json={'nest_uuid': nest_uuid}
        )['egg']

    # oauth
    def discoverOauthProvider(self, url):
        return self.client.post('/api/admin/oauth-providers/discover', json={'url': url})['oauth_provider']

    def oauthProviderUserLink(self, oauth_provider_id, identifier):
        return self.client.get(f'/api/admin/oauth-providers/{oauth_provider_id}/users/identifier/{segment(identifier)}')['user_oauth_link']

    # database agent hosts
    def databaseAgentHostGet(self, host_id, suffix, params=None):
        return self.client.get(f'/api/admin/database-agent-hosts/{host_id}/{suffix}', params=params)

    def databaseAgentHostPost(self, host_id, suffix, json=None):
        return self.client.post(f'/api/admin/database-agent-hosts/{host_id}/{suffix}', json=json)

    def databaseAgentInstance(self, host_id, instance_id, method='GET', json=None):
        return self.client.request(method, f'/api/admin/database-agent-hosts/{host_id}/instances/{instance_id}', json=json)

    def updateDatabaseAgentHostConfig(self, host_id, config):
        return self.client.patch(f'/api/admin/database-agent-hosts/{host_id}/config', json=config)['applied']

    def updateDatabaseAgentHostsConfig(self, host_ids, config):
        return self.client.patch('/api/admin/database-agent-hosts/config', json={'database_agent_host_uuids': host_ids, 'config': config})

    def databaseAgentCapacities(self):
        return self.client.get('/api/admin/database-agent-hosts/capacities')['allocated']

    def updateTemplateInstances(self, template_id, instances):
        return self.client.post(
            f'/api/admin/database-agent-templates/{template_id}/instances/update',
            json={'instances': instances}
        )['updated']

    # database hosts
    def testDatabaseHost(self, host_id):
        return self.client.post(f'/api/admin/database-hosts/{host_id}/test')

    def deleteHostDatabase(self, host_id, database_id, force=False):
        return self.client.delete(f'/api/admin/database-hosts/{host_id}/databases/{database_id}', json={'force': force})

    # backup configurations
    def testBackupConfiguration(self, node_uuid, backup_disk, backup_configs):
        return self.client.post('/api/admin/backup-configurations/test', json={
            'node_uuid': node_uuid,
            'backup_disk': backup_disk,
            'backup_configs': backup_configs,
        })

    def deleteFailedBackups(self, collection, resource_id, force=False):
        return self.client.post(f'/api/admin/{collection}/{resource_id}/backups/delete-failed', json={'force': force})['queued']

    def backupConfigurationStats(self, configuration_id):
        return self.client.get(f'/api/admin/backup-configurations/{configuration_id}/stats')

    def triggerSystemBackupPolicy(self, policy_id):
        return self.client.post(f'/api/admin/system-backup-policies/{policy_id}/trigger')

    # subdomain manager
    def testSubdomainDomain(self, domain_id):
        return self.client.post(f'/api/admin/extensions/dev.0x7d8.subdomainmanager/domains/{domain_id}/test')

    # settings and stats
    def settings(self):
        return self.client.get('/api/admin/settings')['settings']

    def updateSettings(self, **fields):
        return self.client.put('/api/admin/settings', json=fields)

    def activity(self, user=None, search=None, page=None, per_page=None):
        return self.client.list('/api/admin/activity', 'activities', {'user': user, 'search': search}, page, per_page)

    def generalStats(self):
        return self.client.get('/api/admin/stats/general')['stats']

    def backupStats(self):
        return self.client.get('/api/admin/stats/backups')

    # system
    def system(self, suffix, method='GET', json=None, params=None):
        return self.client.request(method, f'/api/admin/system/{suffix}', json=json, params=params)

    # email
    def emailTemplates(self):
        return self.client.get('/api/admin/system/email/templates')['email_templates']

    def emailTemplate(self, identifier):
        return self.client.get(f'/api/admin/system/email/templates/{segment(identifier)}')['email_template']

    def updateEmailTemplate(self, identifier, subject=None, content=None, enabled=None):
        return self.client.put(f'/api/admin/system/email/templates/{segment(identifier)}', json={'subject': subject, 'content': content, 'enabled': enabled})

    def emailVariables(self, identifier=None):
        path = f'templates/{segment(identifier)}/variables' if identifier else 'variables'
        return self.client.get(f'/api/admin/system/email/{path}')['email_variables']

    def createEmailVariable(self, name, value, value_translations=None, identifier=None):
        path = f'templates/{segment(identifier)}/variables' if identifier else 'variables'
        return self.client.post(f'/api/admin/system/email/{path}', json={'name': name, 'value': value, 'value_translations': value_translations})

    def updateEmailVariable(self, name, value=None, value_translations=None, identifier=None):
        path = f'templates/{segment(identifier)}/variables' if identifier else 'variables'
        return self.client.put(f'/api/admin/system/email/{path}/{segment(name)}', json={'value': value, 'value_translations': value_translations})

    def deleteEmailVariable(self, name, identifier=None):
        path = f'templates/{segment(identifier)}/variables' if identifier else 'variables'
        return self.client.delete(f'/api/admin/system/email/{path}/{segment(name)}')

    def sendTestEmail(self, email):
        return self.client.post('/api/admin/system/email/test', json={'email': email})

    # assets
    def assets(self, directory=None, page=None, per_page=None):
        return self.client.list('/api/admin/assets', 'assets', {'directory': directory}, page, per_page)

    def uploadAsset(self, content, directory=None, content_type='application/octet-stream'):
        return self.client.request(
            'PUT', '/api/admin/assets', params={'directory': directory},
            data=content, headers={'Content-Type': content_type}
        )['assets']

    def searchAssets(self, search, directory=None, per_page=None):
        return self.client.post('/api/admin/assets/search', json={'search': search, 'directory': directory, 'per_page': per_page})['assets']

    def deleteAssets(self, names):
        return self.client.post('/api/admin/assets/delete', json={'names': names})['deleted']

    # extensions
    def extensions(self):
        return self.client.get('/api/admin/extensions')

    def setExtensionEnabled(self, extension_id, enabled):
        return self.client.patch(f'/api/admin/extensions/{segment(extension_id)}', json={'enabled': enabled})['pending_restart']

    def manageExtensions(self, suffix, method='GET', json=None, params=None, data=None, headers=None):
        return self.client.request(method, f'/api/admin/extensions/manage/{suffix}', json=json, params=params, data=data, headers=headers)

    def removeExtension(self, extension_id, remove_migrations=False):
        return self.client.delete(f'/api/admin/extensions/manage/{segment(extension_id)}', json={'remove_migrations': remove_migrations})

    def extension(self, extension_id, suffix, method='GET', json=None):
        return self.client.request(method, f'/api/admin/extensions/{extension_id}/{suffix}', json=json)
