# Internal Calagopus UsersAPI (server subusers)
class UsersAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, suffix=''):
        return f'/api/client/servers/{server_id}/subusers{suffix}'

    def list(self, server_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id), 'subusers', {'search': search}, page, per_page)

    def create(self, server_id, email, permissions, ignored_files=None, captcha=None):
        return self.client.post(self._path(server_id), json={
            'email': email,
            'permissions': permissions,
            'ignored_files': ignored_files or [],
            'captcha': captcha,
        })['subuser']

    def update(self, server_id, subuser_id, permissions=None, ignored_files=None):
        return self.client.patch(self._path(server_id, f'/{subuser_id}'), json={
            'permissions': permissions,
            'ignored_files': ignored_files,
        })

    def delete(self, server_id, subuser_id):
        return self.client.delete(self._path(server_id, f'/{subuser_id}'))
