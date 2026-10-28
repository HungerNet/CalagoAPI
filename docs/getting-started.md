# Getting started

## Install

```bash
pip install calagoapi
```

## Create an API key

In your Calagopus panel open **Account → API Keys** and create a key.

- For managing your own servers, grant the server permissions you need
  (for example `control.*`, `file.*`, `backup.*`).
- For administration (`panel.admin`), the key must belong to an admin
  and include the admin permissions you need.

You can also create keys from code with
[`panel.account.createApiKey()`](account.md#api-keys).

## Connect

```python
from calagoapi import Panel

panel = Panel(
    url='https://panel.example.com',
    api_key='c7sp_...'
)

print(panel.ping())         # True if the panel answers
print(panel.validateAPI())  # True if the API key works
```

`Panel` options:

| Argument | Default | Description |
| --- | --- | --- |
| `url` | required | Panel URL. A trailing `/` is fine. |
| `api_key` | required | API key. |
| `name` | the URL | Label shown in `repr()`, handy with several panels. |
| `timeout` | `10` | Request timeout in seconds. Uploads and downloads use at least 300. |
| `verify` | `True` | Verify TLS certificates. Use `False` for self-signed test panels. |
| `max_retries` | `3` | Retries for rate limited requests, and for reads that hit a connection error or 502/503/504. `0` disables retries. |

Close the connections when you are done, or use a `with` block:

```python
with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    ...
```

For asyncio applications use [`AsyncPanel`](async.md), which has the same API with `await`.

## The object model

```
Panel
├── servers   ServerManager      getServer(), getServers(), getMinecraftServer(), groups
├── account   Account            your profile, API keys, SSH keys, sessions, 2FA, ...
├── auth      Auth               public login/registration endpoints
├── admin     Admin              panel administration
└── api       internal API layer (raw access when you need it)

GenericServer  (panel.servers.getServer())
├── power, console, status, resources, settings, startup variables
├── files      FileManager
├── backups    BackupManager
├── databases  DatabaseManager
├── schedules  ScheduleManager
├── users      SubuserManager
├── network    NetworkManager    allocations, subdomains, firewall
├── tunnel     TunnelManager
└── console    Console           live console over websocket
```

Managers return objects (`Backup`, `File`, `Schedule`, ...) with getters,
state checks and actions:

```python
backup = server.backups.getBackup('5f0c...')
backup.getName()       # getter
backup.isLocked()      # state check
backup.lock()          # action
backup['checksum']     # raw panel data is always available
backup.toDict()
```

Anywhere a method needs an id you can pass the object instead:

```python
server.backups.deleteBackup(backup)          # same as deleteBackup(backup.getUUID())
panel.admin.servers.createServer(..., owner=user, node=node, egg=egg)
```

## Your first script

```python
from calagoapi import Panel

panel = Panel(url='https://panel.example.com', api_key='c7sp_...')

for server in panel.servers.getServers():
    status = server.getStatus()
    print(f'{server.getName():30} {status:10} {server.getRAM()} MiB')

    if status == 'offline':
        server.start()
```

Next: [Servers](servers.md).
