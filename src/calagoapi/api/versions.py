from calagoapi.api.client import segment


# Internal Calagopus VersionsAPI (Minecraft Version Changer extension)
class VersionsAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, suffix=''):
        return f'/api/client/servers/{server_id}/minecraft/versions{suffix}'

    def installed(self, server_id):
        return self.client.get(self._path(server_id, '/installed'))['build']

    def types(self, server_id):
        return self.client.get(self._path(server_id, '/types'))['types']

    def versions(self, server_id, type, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, f'/types/{segment(type)}'), 'versions', {'search': search}, page, per_page)

    def builds(self, server_id, type, version, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, f'/types/{segment(type)}/{segment(version)}'), 'builds', {'search': search}, page, per_page)

    def install(self, server_id, build_uuid, truncate_directory=False, accept_eula=True):
        return self.client.post(self._path(server_id, '/install'), json={
            'build_uuid': build_uuid,
            'truncate_directory': truncate_directory,
            'accept_eula': accept_eula,
        })
