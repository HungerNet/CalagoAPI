import os

from calagoapi.utils.model import Model, idOf
from calagoapi.utils.convert import formatBytes
from calagoapi.databases.explorer import DatabaseExplorer


class Database(Model):
    '''
    A database on a database host, attached to a server.

    Args:
        server: The owning server.
        data: Raw database data from Calagopus.

    Example:
        db = server.createDatabase('stats')
        print(db.getHost(), db.getPort(), db.getUsername(), db.getPassword())
        print(db.getConnectionString())
        db.explorer.query('SELECT 1')
    '''
    def __init__(self, server, data: dict):
        super().__init__(server.panel, data)
        self.server = server
        self.explorer = DatabaseExplorer(self.panel, self.panel.api.databases.databasePath(server.server_id, self.getUUID()))

    # getters
    def getName(self) -> str:
        '''Returns the database name.'''
        return self.data.get('name')

    def getType(self) -> str:
        '''Returns the database type: mysql, postgres or mongodb.'''
        return self.data.get('type')

    def getHost(self) -> str:
        '''Returns the hostname to connect to.'''
        return self.data.get('host')

    def getPort(self) -> int:
        '''Returns the port to connect to.'''
        return self.data.get('port')

    def getAddress(self) -> str:
        '''Returns "host:port".'''
        return f'{self.getHost()}:{self.getPort()}'

    def getUsername(self) -> str:
        '''Returns the database username.'''
        return self.data.get('username')

    def getPassword(self) -> str:
        '''
        Returns the password.

        Only available when the database was fetched with include_password=True,
        right after creation, or after rotatePassword().
        '''
        return self.data.get('password')

    def getConnectionString(self) -> str:
        '''
        Returns a connection URI like "mysql://user:pass@host:3306/name".

        The password is omitted if it is not known.
        '''
        scheme = {'postgres': 'postgresql'}.get(self.getType(), self.getType())
        auth = self.getUsername()
        if self.getPassword():
            auth = f'{auth}:{self.getPassword()}'
        return f'{scheme}://{auth}@{self.getAddress()}/{self.getName()}'

    def getSize(self, formatted: bool = False):
        '''Returns the current database size in bytes (or formatted with formatted=True).'''
        size = self.panel.api.databases.size(self.server.server_id, self.getUUID())
        return formatBytes(size) if formatted else size

    def isLocked(self) -> bool:
        '''Returns True if the database is locked against deletion.'''
        return bool(self.data.get('is_locked'))

    # actions
    def refresh(self, include_password: bool = False) -> 'Database':
        '''Re-fetches the database from the panel.'''
        self.data = self.panel.api.databases.get(self.server.server_id, self.getUUID(), include_password or None)
        return self

    def rotatePassword(self) -> str:
        '''
        Generates a new password.

        Returns:
            The new password.
        '''
        password = self.panel.api.databases.rotatePassword(self.server.server_id, self.getUUID())
        self.data['password'] = password
        return password

    def lock(self) -> 'Database':
        '''Locks the database against deletion.'''
        self.panel.api.databases.update(self.server.server_id, self.getUUID(), locked=True)
        return self._update({'is_locked': True})

    def unlock(self) -> 'Database':
        '''Unlocks the database.'''
        self.panel.api.databases.update(self.server.server_id, self.getUUID(), locked=False)
        return self._update({'is_locked': False})

    def recreate(self) -> None:
        '''Drops and recreates the database, deleting all of its data.'''
        return self.panel.api.databases.recreate(self.server.server_id, self.getUUID())

    def delete(self) -> None:
        '''Deletes the database.'''
        return self.panel.api.databases.delete(self.server.server_id, self.getUUID())


class DatabaseInstance(Model):
    '''
    A dedicated database server (container) owned by a server.

    Database instances run their own engine (PostgreSQL, MariaDB, MongoDB or Redis)
    and can hold several databases and users.

    Example:
        instance = server.databases.createInstance(template, 'main-db')
        instance.start()
        db = instance.createDatabase('players')
        user = instance.createUser('app', databases={db: 'read_write'})
    '''
    def __init__(self, server, data: dict):
        super().__init__(server.panel, data.get('instance', data))
        self.server = server
        self.live = data.get('live')

    @property
    def instance_id(self):
        return self.getUUID()

    def _api(self):
        return self.panel.api.databases

    # getters
    def getName(self) -> str:
        '''Returns the instance name.'''
        return self.data.get('name')

    def getType(self) -> str:
        '''Returns the engine type, e.g. postgres, mariadb, mongodb, redis.'''
        return self.data.get('type')

    def getHost(self) -> str:
        '''Returns the hostname to connect to.'''
        return self.data.get('host')

    def getPort(self) -> int:
        '''Returns the port to connect to.'''
        return self.data.get('port')

    def getStatus(self) -> str:
        '''Returns the instance status as reported by the panel.'''
        return self.data.get('status')

    def getMemory(self) -> int:
        '''Returns the memory limit in MiB.'''
        return self.data.get('memory')

    def getDisk(self) -> int:
        '''Returns the disk limit in MiB.'''
        return self.data.get('disk')

    def getCPU(self) -> int:
        '''Returns the CPU limit in percent.'''
        return self.data.get('cpu')

    def getLiveData(self) -> dict:
        '''Returns live state information, if it was included when fetching.'''
        return self.live

    def isLocked(self) -> bool:
        '''Returns True if the instance is locked against deletion.'''
        return bool(self.data.get('is_locked'))

    def hasUpdate(self) -> bool:
        '''Returns True if a newer image is available, see upgrade().'''
        return bool(self.data.get('update_available'))

    # actions
    def refresh(self) -> 'DatabaseInstance':
        '''Re-fetches the instance from the panel.'''
        result = self._api().instance(self.server.server_id, self.instance_id)
        self.data = result['instance']
        self.live = result.get('live')
        return self

    def powerAction(self, action: str) -> None:
        '''Sends a power action: start, stop, restart or kill.'''
        return self._api().instancePower(self.server.server_id, self.instance_id, action)

    def start(self) -> None:
        '''Starts the instance.'''
        return self.powerAction('start')

    def stop(self) -> None:
        '''Stops the instance.'''
        return self.powerAction('stop')

    def restart(self) -> None:
        '''Restarts the instance.'''
        return self.powerAction('restart')

    def kill(self) -> None:
        '''Kills the instance.'''
        return self.powerAction('kill')

    def getResources(self) -> dict:
        '''Returns live resource usage of the instance.'''
        return self._api().instanceResources(self.server.server_id, self.instance_id)

    def getLogs(self, lines: int = None) -> str:
        '''Returns the instance console log.'''
        return self._api().instanceLogs(self.server.server_id, self.instance_id, lines)

    def rename(self, name: str) -> 'DatabaseInstance':
        '''Renames the instance.'''
        self._api().updateInstance(self.server.server_id, self.instance_id, name=name)
        return self._update({'name': name})

    def lock(self) -> 'DatabaseInstance':
        '''Locks the instance against deletion.'''
        self._api().updateInstance(self.server.server_id, self.instance_id, locked=True)
        return self._update({'is_locked': True})

    def unlock(self) -> 'DatabaseInstance':
        '''Unlocks the instance.'''
        self._api().updateInstance(self.server.server_id, self.instance_id, locked=False)
        return self._update({'is_locked': False})

    def upgrade(self) -> 'DatabaseInstance':
        '''Updates the instance to the latest image.'''
        self.data = self._api().upgradeInstance(self.server.server_id, self.instance_id)
        return self

    def export(self, destination: str = None):
        '''
        Exports a dump of the whole instance.

        Args:
            destination: Optional local file to write the dump to.
        '''
        dump = self._api().exportInstance(self.server.server_id, self.instance_id)
        return _save(dump, destination)

    def importDump(self, dump, wipe: bool = False) -> None:
        '''
        Imports a dump into the instance.

        Args:
            dump: Local file path, bytes or str.
            wipe: Delete existing data first.
        '''
        return self._api().importInstance(self.server.server_id, self.instance_id, _load(dump), wipe)

    def cancelOperation(self, operation_id: str) -> None:
        '''Cancels a running import/export operation.'''
        return self._api().cancelInstanceOperation(self.server.server_id, self.instance_id, operation_id)

    def delete(self, force: bool = None) -> None:
        '''Deletes the instance and all its databases.'''
        return self._api().deleteInstance(self.server.server_id, self.instance_id, force)

    # databases
    def getDatabases(self) -> list:
        '''Returns the databases inside this instance.'''
        return [InstanceDatabase(self, data) for data in self._api().instanceDatabases(self.server.server_id, self.instance_id)]

    def getDatabase(self, name_or_id: str) -> 'InstanceDatabase':
        '''Returns a database by name or UUID, or None.'''
        for database in self.getDatabases():
            if name_or_id in (database.getUUID(), database.getName()):
                return database
        return None

    def createDatabase(self, name: str) -> 'InstanceDatabase':
        '''Creates a database inside the instance.'''
        return InstanceDatabase(self, self._api().createInstanceDatabase(self.server.server_id, self.instance_id, name))

    # users
    def getUsers(self) -> list:
        '''Returns the database users of this instance.'''
        return [InstanceUser(self, data) for data in self._api().instanceUsers(self.server.server_id, self.instance_id)]

    def createUser(self, username: str, databases: dict = None) -> 'InstanceUser':
        '''
        Creates a database user.

        Args:
            username: The username.
            databases: Optional {database: permission} grants, permission is
                'none', 'read_only' or 'read_write'.

        Returns:
            The new user. `user.getPassword()` holds the generated password.

        Example:
            user = instance.createUser('app', databases={db: 'read_write'})
        '''
        grants = _grants(databases)
        return InstanceUser(self, self._api().createInstanceUser(self.server.server_id, self.instance_id, username, grants))


class InstanceDatabase(Model):
    '''
    A database inside a DatabaseInstance.

    Example:
        db = instance.getDatabase('players')
        db.explorer.getTables()
        db.export('players.sql')
    '''
    def __init__(self, instance: DatabaseInstance, data: dict):
        super().__init__(instance.panel, data)
        self.instance = instance
        self.server = instance.server
        self.explorer = DatabaseExplorer(
            self.panel,
            self.panel.api.databases.instanceDatabasePath(self.server.server_id, instance.instance_id, self.getUUID())
        )

    def _args(self):
        return self.server.server_id, self.instance.instance_id, self.getUUID()

    def getName(self) -> str:
        '''Returns the database name.'''
        return self.data.get('name')

    def getSize(self, formatted: bool = False):
        '''Returns the current size in bytes (or formatted with formatted=True).'''
        size = self.panel.api.databases.instanceDatabaseSize(*self._args())
        return formatBytes(size) if formatted else size

    def export(self, destination: str = None):
        '''Exports a dump of this database, optionally saving it to `destination`.'''
        return _save(self.panel.api.databases.exportInstanceDatabase(*self._args()), destination)

    def importDump(self, dump, source_db: str = None, wipe: bool = False) -> None:
        '''
        Imports a dump into this database.

        Args:
            dump: Local file path, bytes or str.
            source_db: Name of the database inside the dump to import, if it contains several.
            wipe: Delete existing data first.
        '''
        return self.panel.api.databases.importInstanceDatabase(*self._args(), _load(dump), source_db, wipe)

    def importFromUrl(self, url: str, source_db: str = None, wipe: bool = False) -> dict:
        '''Imports a dump from a remote URL. Returns the background operation.'''
        return self.panel.api.databases.importInstanceDatabaseRemote(*self._args(), url, source_db, wipe)

    def recreate(self) -> None:
        '''Drops and recreates the database, deleting all of its data.'''
        return self.panel.api.databases.recreateInstanceDatabase(*self._args())

    def delete(self) -> None:
        '''Deletes the database.'''
        return self.panel.api.databases.deleteInstanceDatabase(*self._args())


class InstanceUser(Model):
    '''
    A database user inside a DatabaseInstance.

    Example:
        user = instance.createUser('app')
        user.setPermission(db, 'read_only')
        new_password = user.rotatePassword()
    '''
    def __init__(self, instance: DatabaseInstance, data: dict):
        super().__init__(instance.panel, data)
        self.instance = instance
        self.server = instance.server

    def _args(self):
        return self.server.server_id, self.instance.instance_id, self.getUUID()

    def getUsername(self) -> str:
        '''Returns the username.'''
        return self.data.get('username')

    def getPassword(self) -> str:
        '''Returns the password, only known right after creation or rotation.'''
        return self.data.get('password')

    def getDatabases(self) -> list:
        '''Returns the database grants of this user.'''
        return self.data.get('databases', [])

    def setDatabases(self, databases: dict) -> list:
        '''
        Replaces every grant of this user.

        Args:
            databases: {database: permission}, permission is 'none', 'read_only' or 'read_write'.
        '''
        result = self.panel.api.databases.setInstanceUserDatabases(*self._args(), _grants(databases))
        self.data['databases'] = result
        return result

    def setPermission(self, database, permission: str) -> dict:
        '''Sets the permission on one database: 'none', 'read_only' or 'read_write'.'''
        return self.panel.api.databases.setInstanceUserPermission(*self._args(), idOf(database), permission)

    def rotatePassword(self) -> str:
        '''Generates and returns a new password.'''
        password = self.panel.api.databases.rotateInstanceUserPassword(*self._args())
        self.data['password'] = password
        return password

    def delete(self) -> None:
        '''Deletes the user.'''
        return self.panel.api.databases.deleteInstanceUser(*self._args())


# helpers
def _grants(databases):
    if not databases:
        return None
    return [{'database_uuid': idOf(db), 'permission': permission} for db, permission in databases.items()]


def _load(dump):
    # a local file path, otherwise the dump contents themselves
    if isinstance(dump, (str, os.PathLike)) and os.path.isfile(dump):
        with open(dump, 'rb') as f:
            return f.read()
    return dump


def _save(dump, destination):
    if destination is None:
        return dump
    with open(destination, 'w', encoding='utf-8') as f:
        f.write(dump)
    return destination
