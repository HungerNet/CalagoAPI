# Internal Calagopus BackupsAPI
class BackupsAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, suffix=''):
        return f'/api/client/servers/{server_id}/backups{suffix}'

    # backups
    def list(self, server_id, search=None, ungrouped=None, kind=None, database_instance_uuid=None, database_type=None, page=None, per_page=None):
        return self.client.list(self._path(server_id), 'backups', {
            'search': search,
            'ungrouped': ungrouped,
            'kind': kind,
            'database_instance_uuid': database_instance_uuid,
            'database_type': database_type,
        }, page, per_page)

    def system(self, server_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, '/system'), 'backups', {'search': search}, page, per_page)

    def get(self, server_id, backup_id):
        return self.client.get(self._path(server_id, f'/{backup_id}'))['backup']

    def create(self, server_id, name=None, ignored_files=None, backup_group_uuid=None, database_instance_uuid=None):
        return self.client.post(self._path(server_id), json={
            'name': name,
            'ignored_files': ignored_files or [],
            'backup_group_uuid': backup_group_uuid,
            'database_instance_uuid': database_instance_uuid,
        })['backup']

    def update(self, server_id, backup_id, name=None, backup_group_uuid=None, locked=None):
        return self.client.patch(self._path(server_id, f'/{backup_id}'), json={
            'name': name,
            'backup_group_uuid': backup_group_uuid,
            'locked': locked,
        })

    def delete(self, server_id, backup_id):
        return self.client.delete(self._path(server_id, f'/{backup_id}'))

    def deleteMany(self, server_id, backup_ids):
        return self.client.delete(self._path(server_id), json={'selector': {'type': 'uuids', 'uuids': backup_ids}})

    def updateMany(self, server_id, backup_ids, backup_group_uuid=None, locked=None):
        return self.client.patch(self._path(server_id), json={
            'selector': {'type': 'uuids', 'uuids': backup_ids},
            'backup_group_uuid': backup_group_uuid,
            'locked': locked,
        })

    def downloadUrl(self, server_id, backup_id, archive_format=None):
        return self.client.get(
            self._path(server_id, f'/{backup_id}/download'),
            params={'archive_format': archive_format}
        )['url']

    def query(self, server_id, backup_id):
        return self.client.get(self._path(server_id, f'/{backup_id}/query'))

    def export(self, server_id, backup_id, path, archive_format=None, foreground=None):
        return self.client.post(self._path(server_id, f'/{backup_id}/export'), json={
            'path': path,
            'archive_format': archive_format,
            'foreground': foreground,
        })

    def restore(self, server_id, backup_id, truncate_directory=None, restore_startup=None, database_instance_uuid=None):
        return self.client.post(self._path(server_id, f'/{backup_id}/restore'), json={
            'truncate_directory': truncate_directory,
            'restore_startup': restore_startup,
            'database_instance_uuid': database_instance_uuid,
        })

    def unlock(self, server_id):
        return self.client.post(self._path(server_id, '/unlock'))

    def usage(self, server_id):
        return self.client.get(self._path(server_id, '/usage'))['usage']

    # backup groups
    def groups(self, server_id):
        return self.client.get(self._path(server_id, '/groups'))['backup_groups']

    def groupBackups(self, server_id, group_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, f'/groups/{group_id}'), 'backups', {'search': search}, page, per_page)

    def createGroup(self, server_id, name, retention=None):
        return self.client.post(self._path(server_id, '/groups'), json={'name': name, 'retention': retention})['backup_group']

    def updateGroup(self, server_id, group_id, name=None, retention=None):
        return self.client.patch(self._path(server_id, f'/groups/{group_id}'), json={'name': name, 'retention': retention})

    def deleteGroup(self, server_id, group_id, lock_backups=None):
        return self.client.delete(self._path(server_id, f'/groups/{group_id}'), json={'lock_backups': lock_backups})

    def orderGroups(self, server_id, group_order):
        return self.client.put(self._path(server_id, '/groups/order'), json={'backup_group_order': group_order})
