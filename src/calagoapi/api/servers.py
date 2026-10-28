# Internal Calagopus ServersAPI
class ServersAPI:
    def __init__(self, client):
        self.client = client

    # listing
    def list(self, search=None, other=None, page=None, per_page=None):
        return self.client.list('/api/client/servers', 'servers', {'search': search, 'other': other}, page, per_page)

    def get(self, server_id):
        return self.client.get(f'/api/client/servers/{server_id}')['server']

    def eggs(self, search=None, page=None, per_page=None):
        return self.client.list('/api/client/servers/eggs', 'nest_eggs', {'search': search}, page, per_page)

    def eggCommandSnippets(self, egg_id):
        return self.client.get(f'/api/client/servers/eggs/{egg_id}/command-snippets')['command_snippets']

    def nodeResources(self, node_id):
        return self.client.get(f'/api/client/servers/nodes/{node_id}/resources')['resources']

    # status and console
    def resources(self, server_id):
        return self.client.get(f'/api/client/servers/{server_id}/resources')['resources']

    def power(self, server_id, action):
        return self.client.post(f'/api/client/servers/{server_id}/power', json={'action': action})

    def command(self, server_id, command):
        return self.client.post(f'/api/client/servers/{server_id}/command', json={'command': command})

    def logs(self, server_id, lines=None):
        return self.client.get(f'/api/client/servers/{server_id}/logs', params={'lines': lines})

    def websocket(self, server_id):
        return self.client.get(f'/api/client/servers/{server_id}/websocket')

    def activity(self, server_id, user=None, search=None, page=None, per_page=None):
        return self.client.list(
            f'/api/client/servers/{server_id}/activity', 'activities',
            {'user': user, 'search': search}, page, per_page
        )

    def announcements(self, server_id):
        return self.client.get(f'/api/client/servers/{server_id}/announcements')['announcements']

    # settings
    def rename(self, server_id, name=None, description=None):
        return self.client.post(
            f'/api/client/servers/{server_id}/settings/rename',
            json={'name': name, 'description': description}
        )

    def setTimezone(self, server_id, timezone):
        return self.client.put(f'/api/client/servers/{server_id}/settings/timezone', json={'timezone': timezone})

    def setAutoKill(self, server_id, enabled, seconds=None):
        payload = {'enabled': enabled}
        if seconds is not None:
            payload['seconds'] = seconds
        return self.client.put(f'/api/client/servers/{server_id}/settings/auto-kill', json=payload)

    def setAutoStart(self, server_id, behavior):
        return self.client.put(f'/api/client/servers/{server_id}/settings/auto-start', json={'behavior': behavior})

    def reinstall(self, server_id, truncate_directory=False, start_on_completion=None):
        payload = {'truncate_directory': truncate_directory}
        if start_on_completion is not None:
            payload['start_on_completion'] = start_on_completion
        return self.client.post(f'/api/client/servers/{server_id}/settings/install', json=payload)

    def cancelInstall(self, server_id):
        return self.client.post(f'/api/client/servers/{server_id}/settings/install/cancel')

    def unlockInstall(self, server_id):
        return self.client.post(f'/api/client/servers/{server_id}/settings/install/unlock')

    # startup
    def startupVariables(self, server_id):
        return self.client.get(f'/api/client/servers/{server_id}/startup/variables')['variables']

    def updateStartupVariables(self, server_id, variables):
        return self.client.put(f'/api/client/servers/{server_id}/startup/variables', json={'variables': variables})

    def setStartupCommand(self, server_id, command):
        return self.client.put(f'/api/client/servers/{server_id}/startup/command', json={'command': command})

    def setDockerImage(self, server_id, image):
        return self.client.put(f'/api/client/servers/{server_id}/startup/docker-image', json={'image': image})

    # server groups
    def groups(self):
        return self.client.get('/api/client/servers/groups')['server_groups']

    def groupServers(self, group_id, search=None, page=None, per_page=None):
        return self.client.list(f'/api/client/servers/groups/{group_id}', 'servers', {'search': search}, page, per_page)

    def createGroup(self, name, server_order=None):
        return self.client.post(
            '/api/client/servers/groups',
            json={'name': name, 'server_order': server_order or []}
        )['server_group']

    def updateGroup(self, group_id, name, server_order=None):
        payload = {'name': name}
        if server_order is not None:
            payload['server_order'] = server_order
        return self.client.patch(f'/api/client/servers/groups/{group_id}', json=payload)

    def deleteGroup(self, group_id):
        return self.client.delete(f'/api/client/servers/groups/{group_id}')

    def orderGroups(self, group_order):
        return self.client.put('/api/client/servers/groups/order', json={'server_group_order': group_order})
