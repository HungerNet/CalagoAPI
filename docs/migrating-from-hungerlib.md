# Migrating from HungerLib

CalagoAPI is the Calagopus counterpart of HungerLib's panel layer. Most
scripts only need new imports and a new `Panel(...)` call.

## What stays the same

- `Panel` and the server class (HungerLib's `GenericServer` is `Server`; `MinecraftServer` is in the
  `calagoapi-minecraft` package)
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
- `calagoapi.utils.waitForOnline()`, `waitForOffline()`, `secsUntil()`, `minsUntil()`,
  `convert.time()`, `convert.byte()`

## What changed

| HungerLib | CalagoAPI | Why |
| --- | --- | --- |
| `Panel(name, url, api_key)` | `Panel(url, api_key, name=None)` | `name` is optional now |
| `GenericServer(name, panel, server_id)` | `panel.servers.getServer(server_id)` or `Server(panel, server_id, name=None)` | details are loaded from the panel |
| methods return `requests.Response` / `(status, text)` | methods return objects, dicts or `None`, and raise exceptions on errors | no more checking status codes |
| `listBackups()` returned the raw response | returns a list of `Backup` objects | |
| `createSchedule(payload)` | `createSchedule(name, triggers, condition, steps)` | Calagopus schedules are trigger/step based, see [Schedules](schedules.md) |
| `createDatabase(name, remote, host)` | `createDatabase(name, host=None)` | Calagopus has no remote pattern |
| `MinecraftServer(..., bridge)` | `pip install calagoapi-minecraft`, then `panel.minecraft.getServer(server_id, bridge_url=..., bridge_token=...)` | Minecraft lives in its own package; HungerBridge is used through HungerBridgePy (`server.bridge`) |
| `server.sendCommand()` via HungerBridge | `MinecraftServer.sendCommand(command, silent=False, showConsole=False)` returns the output | `Server.sendCommand()` (any game) goes through the panel and returns `None` |
| `server.installVersion(...)` | `server.versions.install(build)` | the Version Changer is part of `calagoapi-minecraft` |
| `server.stream` (via HungerBridge) | `MinecraftServer.streamConsole(history=...)` / `onConsoleLine()`; `Server.streamConsole()` for other games | see [Live console](console.md) and [tutorial 12](tutorials/minecraft/12-commands-and-console.md) |
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
and revisions, schedule builders, account
management (API keys, SSH keys, passkeys, sessions, 2FA) and the complete
admin API. Minecraft users additionally get, through `calagoapi-minecraft`, the Version
Changer, JVM and game metrics, bridge installation and token setup.
