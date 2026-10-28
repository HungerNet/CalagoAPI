from calagoapi.databases.database import Database, DatabaseInstance
from calagoapi.utils.model import idOf
from calagoapi.utils.exceptions import InvalidActionError


class DatabaseManager:
    '''
    Database management for one server, available as `server.databases`.

    Calagopus offers two kinds of databases:
    - databases on a shared database host (`getDatabases()`, `createDatabase()`)
    - dedicated database instances the server runs itself (`getInstances()`, `createInstance()`)

    Args:
        server: The server to manage databases for.

    Example:
        db = server.databases.createDatabase('stats')
        print(db.getConnectionString())
    '''
    def __init__(self, server):
        self.server = server
        self.api = server.panel.api.databases

    @property
    def server_id(self):
        return self.server.server_id

    def _wrap(self, data):
        return Database(self.server, data)

    # hosted databases
    def getDatabases(self, search: str = None, include_password: bool = False, page: int = None, per_page: int = None):
        '''
        Lists the server's databases.

        Args:
            search: Filter by name.
            include_password: Include each database password.

        Returns:
            A Page (list) of Database objects.
        '''
        return self.api.list(self.server_id, search, include_password or None, page, per_page).map(self._wrap)

    def getDatabase(self, database_id: str, include_password: bool = False) -> Database:
        '''Returns a single database by UUID.'''
        return self._wrap(self.api.get(self.server_id, database_id, include_password or None))

    def getDatabaseByName(self, name: str, include_password: bool = False) -> Database:
        '''Returns a database by name, or None.'''
        for database in self.getDatabases(include_password=include_password):
            if database.getName() == name:
                return database
        return None

    def getDatabaseHosts(self) -> list:
        '''Returns the database hosts this server can create databases on.'''
        return self.api.hosts(self.server_id)

    def createDatabase(self, name: str, host=None) -> Database:
        '''
        Creates a database.

        Args:
            name: Database name.
            host: Database host UUID (or dict from getDatabaseHosts()). Defaults to the first available host.

        Returns:
            The new Database, including its password.

        Example:
            db = server.databases.createDatabase('luckperms')
        '''
        if host is None:
            hosts = self.getDatabaseHosts()
            if not hosts:
                raise InvalidActionError('No database hosts are available for this server')
            host = hosts[0]
        host_id = host.get('uuid') if isinstance(host, dict) else idOf(host)
        return self._wrap(self.api.create(self.server_id, host_id, name))

    def rotateDatabasePassword(self, database_id: str) -> str:
        '''Generates a new password for a database and returns it.'''
        return self.api.rotatePassword(self.server_id, idOf(database_id))

    def deleteDatabase(self, database_id: str) -> None:
        '''Deletes a database.'''
        return self.api.delete(self.server_id, idOf(database_id))

    # database instances
    def getInstances(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists the server's database instances.'''
        return self.api.instances(self.server_id, search, page, per_page).map(lambda data: DatabaseInstance(self.server, data))

    def getInstance(self, instance_id: str) -> DatabaseInstance:
        '''Returns a database instance, including live state.'''
        return DatabaseInstance(self.server, self.api.instance(self.server_id, instance_id))

    def getTemplates(self) -> list:
        '''Returns the database instance templates (engines) available to this server.'''
        return self.api.templates(self.server_id)

    def createInstance(self, template, name: str, image: str = None) -> DatabaseInstance:
        '''
        Creates a database instance.

        Args:
            template: Template UUID or dict from getTemplates().
            name: Instance name.
            image: Optional docker image from the template's allowed images.

        Example:
            template = server.databases.getTemplates()[0]
            instance = server.databases.createInstance(template, 'main-db')
        '''
        template_id = template.get('uuid') if isinstance(template, dict) else template
        return DatabaseInstance(self.server, self.api.createInstance(self.server_id, template_id, name, image))

    def deleteInstance(self, instance_id: str, force: bool = None) -> None:
        '''Deletes a database instance.'''
        return self.api.deleteInstance(self.server_id, idOf(instance_id), force)
