# Internal Calagopus DatabasesAPI
class DatabasesAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, suffix=''):
        return f'/api/client/servers/{server_id}/databases{suffix}'

    def _instance(self, server_id, instance_id, suffix=''):
        return self._path(server_id, f'/instances/{instance_id}{suffix}')

    # hosted databases
    def list(self, server_id, search=None, include_password=None, page=None, per_page=None):
        return self.client.list(self._path(server_id), 'databases', {
            'search': search,
            'include_password': include_password,
        }, page, per_page)

    def get(self, server_id, database_id, include_password=None):
        return self.client.get(
            self._path(server_id, f'/{database_id}'),
            params={'include_password': include_password}
        )['database']

    def create(self, server_id, database_host_uuid, name):
        return self.client.post(self._path(server_id), json={
            'database_host_uuid': database_host_uuid,
            'name': name,
        })['database']

    def update(self, server_id, database_id, locked=None):
        return self.client.patch(self._path(server_id, f'/{database_id}'), json={'locked': locked})

    def delete(self, server_id, database_id):
        return self.client.delete(self._path(server_id, f'/{database_id}'))

    def rotatePassword(self, server_id, database_id):
        return self.client.post(self._path(server_id, f'/{database_id}/rotate-password'))['password']

    def recreate(self, server_id, database_id):
        return self.client.post(self._path(server_id, f'/{database_id}/recreate'))

    def size(self, server_id, database_id):
        return self.client.get(self._path(server_id, f'/{database_id}/size'))['size']

    def hosts(self, server_id):
        return self.client.get(self._path(server_id, '/hosts'))['database_hosts']

    # database explorer, `base` is the database path from databasePath() / instanceDatabasePath()
    def databasePath(self, server_id, database_id):
        return self._path(server_id, f'/{database_id}')

    def instanceDatabasePath(self, server_id, instance_id, database_id):
        return self._instance(server_id, instance_id, f'/databases/{database_id}')

    def schema(self, base):
        return self.client.get(f'{base}/explorer/schema')

    def tableTypes(self, base):
        return self.client.get(f'{base}/explorer/tables/types')['types']

    def query(self, base, query, rows=None, read_only=None):
        return self.client.post(f'{base}/explorer/query', json={
            'query': query,
            'rows': rows,
            'read_only': read_only,
        })['results']

    def rows(self, base, table, schema=None, order_by=None, descending=None, limit=None, offset=None, filters=None):
        return self.client.post(f'{base}/explorer/rows', json={
            'table': table,
            'schema': schema,
            'order_by': order_by,
            'descending': descending,
            'limit': limit,
            'offset': offset,
            'filters': filters,
        })['result']

    def insertRows(self, base, table, rows, schema=None):
        return self.client.post(f'{base}/explorer/rows/insert', json={'table': table, 'rows': rows, 'schema': schema})['affected']

    def updateRows(self, base, table, rows, schema=None):
        return self.client.post(f'{base}/explorer/rows/update', json={'table': table, 'rows': rows, 'schema': schema})['affected']

    def deleteRows(self, base, table, rows, schema=None):
        return self.client.post(f'{base}/explorer/rows/delete', json={'table': table, 'rows': rows, 'schema': schema})['affected']

    def createTable(self, base, table, columns, schema=None):
        return self.client.post(f'{base}/explorer/tables', json={'table': table, 'columns': columns, 'schema': schema})

    def renameTable(self, base, table, name, schema=None):
        return self.client.post(f'{base}/explorer/tables/rename', json={'table': table, 'name': name, 'schema': schema})

    def deleteTable(self, base, table, schema=None):
        return self.client.post(f'{base}/explorer/tables/delete', json={'table': table, 'schema': schema})

    def addColumn(self, base, table, column, schema=None):
        return self.client.post(f'{base}/explorer/tables/columns', json={'table': table, 'column': column, 'schema': schema})

    def renameColumn(self, base, table, column, name, schema=None):
        return self.client.post(f'{base}/explorer/tables/columns/rename', json={
            'table': table,
            'column': column,
            'name': name,
            'schema': schema,
        })

    def deleteColumn(self, base, table, column, schema=None):
        return self.client.post(f'{base}/explorer/tables/columns/delete', json={'table': table, 'column': column, 'schema': schema})

    # database instances
    def instances(self, server_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, '/instances'), 'instances', {'search': search}, page, per_page)

    def instance(self, server_id, instance_id):
        return self.client.get(self._instance(server_id, instance_id))

    def templates(self, server_id):
        return self.client.get(self._path(server_id, '/instances/templates'))['templates']

    def createInstance(self, server_id, template_uuid, name, image=None):
        return self.client.post(self._path(server_id, '/instances'), json={
            'template_uuid': template_uuid,
            'name': name,
            'image': image,
        })['instance']

    def updateInstance(self, server_id, instance_id, name=None, locked=None):
        return self.client.patch(self._instance(server_id, instance_id), json={'name': name, 'locked': locked})

    def deleteInstance(self, server_id, instance_id, force=None):
        return self.client.delete(self._instance(server_id, instance_id), params={'force': force})

    def instancePower(self, server_id, instance_id, action):
        return self.client.post(self._instance(server_id, instance_id, '/power'), json={'action': action})

    def instanceResources(self, server_id, instance_id):
        return self.client.get(self._instance(server_id, instance_id, '/resources'))['resources']

    def instanceLogs(self, server_id, instance_id, lines=None):
        return self.client.get(self._instance(server_id, instance_id, '/logs'), params={'lines': lines})

    def upgradeInstance(self, server_id, instance_id):
        return self.client.post(self._instance(server_id, instance_id, '/update'))['instance']

    def exportInstance(self, server_id, instance_id):
        return self.client.get(self._instance(server_id, instance_id, '/export'))

    def importInstance(self, server_id, instance_id, content, wipe=None):
        return self.client.postText(
            self._instance(server_id, instance_id, '/import'), content,
            params={'wipe': wipe}, content_type='application/octet-stream'
        )

    def cancelInstanceOperation(self, server_id, instance_id, operation_id):
        return self.client.delete(self._instance(server_id, instance_id, f'/operations/{operation_id}'))

    # databases inside an instance
    def instanceDatabases(self, server_id, instance_id):
        return self.client.get(self._instance(server_id, instance_id, '/databases'))['databases']

    def createInstanceDatabase(self, server_id, instance_id, name):
        return self.client.post(self._instance(server_id, instance_id, '/databases'), json={'name': name})['database']

    def deleteInstanceDatabase(self, server_id, instance_id, database_id):
        return self.client.delete(self.instanceDatabasePath(server_id, instance_id, database_id))

    def recreateInstanceDatabase(self, server_id, instance_id, database_id):
        return self.client.post(f'{self.instanceDatabasePath(server_id, instance_id, database_id)}/recreate')

    def instanceDatabaseSize(self, server_id, instance_id, database_id):
        return self.client.get(f'{self.instanceDatabasePath(server_id, instance_id, database_id)}/size')['size']

    def exportInstanceDatabase(self, server_id, instance_id, database_id):
        return self.client.get(f'{self.instanceDatabasePath(server_id, instance_id, database_id)}/export')

    def importInstanceDatabase(self, server_id, instance_id, database_id, content, source_db=None, wipe=None):
        return self.client.postText(
            f'{self.instanceDatabasePath(server_id, instance_id, database_id)}/import', content,
            params={'source_db': source_db, 'wipe': wipe}, content_type='application/octet-stream'
        )

    def importInstanceDatabaseRemote(self, server_id, instance_id, database_id, url, source_db=None, wipe=None):
        return self.client.post(f'{self.instanceDatabasePath(server_id, instance_id, database_id)}/import/remote', json={
            'url': url,
            'source_db': source_db,
            'wipe': wipe,
        })['operation']

    # instance users
    def instanceUsers(self, server_id, instance_id):
        return self.client.get(self._instance(server_id, instance_id, '/users'))['users']

    def createInstanceUser(self, server_id, instance_id, username, databases=None):
        return self.client.post(self._instance(server_id, instance_id, '/users'), json={
            'username': username,
            'databases': databases,
        })['user']

    def deleteInstanceUser(self, server_id, instance_id, user_id):
        return self.client.delete(self._instance(server_id, instance_id, f'/users/{user_id}'))

    def rotateInstanceUserPassword(self, server_id, instance_id, user_id):
        return self.client.post(self._instance(server_id, instance_id, f'/users/{user_id}/rotate-password'))['password']

    def setInstanceUserDatabases(self, server_id, instance_id, user_id, databases):
        return self.client.put(
            self._instance(server_id, instance_id, f'/users/{user_id}/databases'),
            json={'databases': databases}
        )['databases']

    def setInstanceUserPermission(self, server_id, instance_id, user_id, database_id, permission):
        return self.client.put(
            self._instance(server_id, instance_id, f'/users/{user_id}/databases/{database_id}'),
            json={'permission': permission}
        )['database']
