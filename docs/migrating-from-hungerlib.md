# Migrating from HungerLib

CalagoAPI is the Calagopus counterpart of HungerLib's panel layer. Most
scripts only need new imports and a new `Panel(...)` call.

## What stays the same

- `Panel`, `GenericServer`, `MinecraftServer`
- camelCase methods, snake_case variables
- Status and resources: `getStatus()`, `isOnline()`, `isOffline()`, `refresh()`,
  `resources()`, `getRAM()`, `getCPU()`, `getDisk()`, `getNetworkIn()`,
  `getNetworkOut()`, `getUptime(formatted=True)`
- Power: `powerAction()`, `start()`, `stop()`, `restart()`, `kill()`
- Server shortcuts: `listFiles`, `downloadFile`, `uploadFile`, `deleteFiles`,
  `renameFiles`, `copyFiles`, `moveFiles`, `createFolder`, `compress`,
  `decompress`, `listBackups`, `createBackup`, `deleteBackup`, `downloadBackup`,
  `listDatabases`, `createDatabase`, `rotateDatabasePassword`, `deleteDatabase`,
  `getStartupVariables`, `updateStartupVariable`, `listSchedules`,
  `createSchedule`, `updateSchedule`, `deleteSchedule`, `runSchedule`,
  `enableSchedule`, `disableSchedule`, `getSchedule`
- `panel.ping()`, `panel.validateAPI()`
- `utils.waitForOnline()`, `utils.waitForOffline()`, `utils.secsUntil()`,
  `utils.minsUntil()`, `convert.time()`, `convert.byte()`

## What changed

| HungerLib | CalagoAPI | Why |
| --- | --- | --- |
| `Panel(name, url, api_key)` | `Panel(url, api_key, name=None)` | `name` is optional now |
| `GenericServer(name, panel, server_id)` | `panel.servers.getServer(server_id)` or `GenericServer(panel, server_id, name=None)` | details are loaded from the panel |
| methods return `requests.Response` / `(status, text)` | methods return objects, dicts or `None`, and raise exceptions on errors | no more checking status codes |
| `listBackups()` returned the raw response | returns a list of `Backup` objects | |
| `createSchedule(payload)` | `createSchedule(name, triggers, condition, steps)` | Calagopus schedules are trigger/step based, see [Schedules](schedules.md) |
| `createDatabase(name, remote, host)` | `createDatabase(name, host=None)` | Calagopus has no remote pattern |
| `MinecraftServer(..., bridge)` | `MinecraftServer(panel, server_id, ...)` | HungerBridge is not part of CalagoAPI |
| `server.stream` (via HungerBridge) | `server.streamConsole()`, `server.onConsoleLine(callback)`, `server.console` | console streaming comes from the Calagopus daemon, see [Live console](console.md) |
| `panel.files.list(server_id, ...)` (internal API) | `server.files.listFiles(...)` | internal modules live in `panel.api` |

## Before and after

HungerLib:

```python
from hungerlib import Panel, GenericServer

panel = Panel('main', 'https://panel.example.com', 'ptla_...')
server = GenericServer('Survival', panel, 'abc123')

code, text = server.restart()
response = server.listBackups()
for item in response.json()['data']:
    print(item['attributes']['name'])
```

CalagoAPI:

```python
from calagoapi import Panel

panel = Panel(url='https://panel.example.com', api_key='c7sp_...')
server = panel.servers.getServer('abc123')

server.restart()
for backup in server.listBackups():
    print(backup.getName())
```

## Things CalagoAPI adds

A live console with callbacks, an async API (`AsyncPanel`), automatic retries,
server settings, subusers, allocations, subdomains, firewall, tunnels,
database instances and the database explorer, backup groups, file search
and revisions, schedule builders, Minecraft version changer, account
management (API keys, SSH keys, passkeys, sessions, 2FA) and the complete
admin API.
