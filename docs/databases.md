# Databases

`server.databases` is a `DatabaseManager`. Calagopus has two kinds of
databases:

- **Hosted databases** live on a shared database host (MySQL, PostgreSQL or
  MongoDB) managed by the panel admin.
- **Database instances** are dedicated database servers (PostgreSQL,
  MariaDB, MongoDB, Redis) that belong to your server, with their own
  databases and users.

Both support the [database explorer](#database-explorer).

## Hosted databases

```python
db = server.databases.createDatabase('luckperms')       # first available host
db = server.databases.createDatabase('stats', host=host_uuid)

print(db.getHost(), db.getPort(), db.getUsername(), db.getPassword())
print(db.getConnectionString())   # mysql://user:pass@host:3306/stats

for db in server.databases.getDatabases(include_password=True):
    print(db.getName(), db.getSize(formatted=True))

server.databases.getDatabaseByName('stats')
server.databases.getDatabaseHosts()

new_password = db.rotatePassword()
db.lock()
db.unlock()
db.recreate()      # wipes all data
db.delete()
```

## Database instances

```python
template = server.databases.getTemplates()[0]
instance = server.databases.createInstance(template, 'main-db')

instance.start()
print(instance.getStatus(), instance.getResources())
print(instance.getLogs(lines=50))
instance.restart()

if instance.hasUpdate():
    instance.upgrade()

db = instance.createDatabase('players')
instance.getDatabases()
instance.getDatabase('players')

user = instance.createUser('app', databases={db: 'read_write'})
print(user.getPassword())        # only known right after creation
user.setPermission(db, 'read_only')
user.setDatabases({db: 'read_write', other_db: 'none'})
user.rotatePassword()

instance.export('instance-dump.sql')
instance.importDump('instance-dump.sql', wipe=True)
db.export('players.sql')
db.importDump('players.sql')
db.importFromUrl('https://example.com/dump.sql')
```

## Database explorer

Every hosted database and instance database has an `explorer`.

```python
explorer = db.explorer

explorer.getTables()
explorer.getTableTypes()

explorer.createTable('players', [
    {'name': 'id', 'type': 'INT', 'primary_key': True, 'auto_increment': True},
    {'name': 'name', 'type': 'VARCHAR(32)', 'nullable': False},
])
explorer.addColumn('players', 'score', 'INT')
explorer.renameColumn('players', 'score', 'points')
explorer.deleteColumn('players', 'points')
explorer.renameTable('players', 'users')
explorer.deleteTable('users')
```

### Rows

Rows are plain dicts of column -> value.

```python
explorer.insertRow('players', {'name': 'Steve'})
explorer.insertRows('players', [{'name': 'Alex'}, {'name': 'Herobrine'}])
explorer.updateRow('players', where={'id': 1}, values={'name': 'Steve2'})
explorer.deleteRow('players', where={'id': 3})

result = explorer.getRows('players', limit=50, order_by='id', descending=True,
                          filters=[{'column': 'name', 'operator': 'starts_with', 'value': 'S'}])
```

Filter operators: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `contains`,
`starts_with`, `ends_with`, `is_null`, `not_null`.

### Raw SQL

```python
explorer.query('SELECT COUNT(*) FROM players', read_only=True)
```
