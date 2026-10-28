# CalagoAPI

The Python SDK for [Calagopus](https://calagopus.com).

CalagoAPI wraps the whole Calagopus API (servers, files, backups, databases,
schedules, networking, your account, and full panel administration) in a
small, hand-written API that reads like plain Python.

```python
from calagoapi import Panel

panel = Panel(
    url='https://panel.example.com',
    api_key='c7sp_...'
)

server = panel.servers.getServer('abc123')
server.sendCommand('say Hello')
server.restart()

if server.isOnline():
    print(server.getStatus(), server.getRAM(), server.getUptime(formatted=True))

backup = server.createBackup('before-update')
```

If you have used [HungerLib](https://github.com/iFamished/HungerLib), you
already know CalagoAPI. The same objects and method names
(`Panel`, `GenericServer`, `MinecraftServer`, `getStatus()`, `isOnline()`,
`createBackup()`, `listFiles()`, ...) work here, backed by Calagopus.

## Installation

```bash
pip install calagoapi
```

CalagoAPI needs Python 3.9+ and depends on `requests` and `websockets`.

## Features

| Area | What you can do |
| --- | --- |
| **Servers** | Power actions, console commands, logs, live resources, status checks, rename, reinstall, timezone, auto-start, auto-kill, startup variables, docker image, server groups |
| **Live console** | Stream console output over the daemon websocket, wait for a line, callbacks for output, status, stats and every daemon event, automatic token renewal and reconnects |
| **Files** | List, read, write, upload, download, rename, move, copy (also to other servers), compress, decompress, chmod, search, pull from URL, file revisions, SQLite queries, directory sizes |
| **Backups** | Create, restore, download, lock, rename, bulk delete, backup groups with retention policies, usage |
| **Databases** | Hosted databases, dedicated database instances (PostgreSQL, MariaDB, MongoDB, Redis), database users and grants, import/export, a full **database explorer** (tables, columns, rows, queries) |
| **Schedules** | Triggers (cron, crash, console line, resource usage, ...), conditions, 30+ step actions, import/export, live status, with builder helpers |
| **Network** | Allocations, subdomains, per-server firewall, tunnels between servers |
| **Subusers** | Invite, permissions, ignored files |
| **Minecraft** | Version changer (install any Paper/Purpur/Fabric/... build), `server.properties` editing, EULA, console helpers |
| **Account** | Profile, password, email, two-factor, API keys, SSH keys, passkeys, sessions, OAuth links, command snippets, activity |
| **Admin** | Users, servers (create, deploy, transfer, suspend, limits), nodes, allocations, locations, nests and eggs, egg repositories, mounts, devices, roles, announcements, OAuth providers, database hosts, backup configurations and policies, settings, email templates, extensions, system health and updates |
| **Async** | `AsyncPanel`: the whole API with `await`, plus a native asyncio live console |
| **Reliability** | Automatic retries on rate limits (and on transient errors for reads), typed exceptions, automatic pagination |

## Quick tour

### Status and resources

```python
status = server.getStatus()        # 'running', 'offline', 'starting' or 'stopping'

if server.isOnline():
    print(server.getCPU(), '%')
    print(server.getRAM(), '/', server.getRAMLimit(), 'MiB')
    print(server.getUptime(formatted=True))  # '3h 12m'

server.isInstalled()
server.isSuspended()
```

Every important value has a getter *and* convenience checks, so you can
inspect the exact state or just branch on it.

### Live console

```python
for line in server.streamConsole():
    if 'joined the game' in line:
        print(line)

with server.console as console:
    console.sendCommand('save-all')
    console.waitFor('Saved the game')

server.onConsoleLine(print)   # callbacks in a background thread
```

### Async

```python
from calagoapi import AsyncPanel

async with AsyncPanel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    servers = await panel.servers.getServers()
    statuses = await asyncio.gather(*(server.getStatus() for server in servers))

    async for line in servers[0].streamConsole():
        print(line)
```

### Files

```python
for file in server.files.listFiles('/plugins'):
    print(file.getName(), file.getSize(formatted=True))

properties = server.readFile('/server.properties')
server.writeFile('/eula.txt', 'eula=true')
server.files.uploadFile('/plugins', 'build/MyPlugin.jar')
server.files.downloadFile('/world.zip', 'world.zip')
```

### Backups

```python
backup = server.createBackup('before-update')
backup.waitUntilComplete()

if backup.isSuccessful():
    print(backup.getSize(formatted=True))

backup.lock()
backup.restore(truncate_directory=True)
```

### Schedules

```python
from calagoapi import triggers, conditions, actions

server.schedules.createSchedule(
    'Nightly restart',
    triggers=[triggers.cron('0 0 4 * * *')],
    condition=conditions.serverState('running'),
    steps=[
        actions.sendCommand('say Restarting in 1 minute'),
        actions.sleep(60_000),
        actions.createBackup('nightly', foreground=True),
        actions.sendPower('restart'),
    ],
)
```

### Databases

```python
db = server.createDatabase('stats')
print(db.getConnectionString())

db.explorer.createTable('players', [
    {'name': 'id', 'type': 'INT', 'primary_key': True, 'auto_increment': True},
    {'name': 'name', 'type': 'VARCHAR(32)'},
])
db.explorer.insertRow('players', {'name': 'Steve'})
print(db.explorer.query('SELECT COUNT(*) FROM players'))
```

### Minecraft

```python
server = panel.servers.getMinecraftServer('abc123')

server.say('Server update in 5 minutes!')
server.setProperties({'max-players': 100, 'motd': 'Welcome!'})

latest = server.getBuilds('PAPER', '1.21.1', page=1, per_page=1)[0]
server.installVersion(latest)
```

### Administration

```python
user = panel.admin.users.createUser('steve', 'steve@example.com')

server = panel.admin.servers.deployServer(
    'Steve SMP', owner=user, egg=panel.admin.nests.findEgg('Paper'),
    locations=[panel.admin.locations.getLocationByName('Frankfurt')],
    memory=4096, disk=20480,
)

for node in panel.admin.nodes.getNodes():
    print(node.getName(), node.getSystemOverview()['version'])
```

### Errors

```python
from calagoapi import NotFoundError, PermissionDeniedError, CalagoAPIError

try:
    panel.servers.getServer('missing')
except NotFoundError:
    print('No such server')
except CalagoAPIError as e:
    print(e.status_code, e.errors)
```

## Documentation

The [docs](docs/) folder has a guide for every area:

- [Getting started](docs/getting-started.md)
- [Servers](docs/servers.md), [Minecraft servers](docs/minecraft.md), [Live console](docs/console.md)
- [Files](docs/files.md), [Backups](docs/backups.md), [Databases](docs/databases.md)
- [Schedules](docs/schedules.md)
- [Network, subusers and tunnels](docs/network.md)
- [Account and authentication](docs/account.md)
- [Administration](docs/admin.md)
- [Async](docs/async.md)
- [Errors, pagination and utilities](docs/errors-and-utilities.md)
- [Migrating from HungerLib](docs/migrating-from-hungerlib.md)
- [Architecture](docs/architecture.md)

Every public class and method also has a docstring with parameters and an
example, so `help(server.files)` works from a Python shell.

## Development

```bash
pip install -e .[dev]
pytest
```

The tests run offline against `openapi.json` and a fake daemon. See
[Architecture](docs/architecture.md#tests).

## License

GPL-3.0, see [LICENSE](LICENSE).
