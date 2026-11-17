# Migrating to CalagoAPI 2.0

CalagoAPI 2.0 makes the core package game-agnostic and moves every Minecraft feature into
one extension package, `calagoapi-minecraft`. It is a breaking release: 1.x shims were
removed instead of deprecated. This page lists every change. The full inventory and the
reasoning are in [PLAN.md](../PLAN.md#11-method-inventory).

## Install

```bash
pip install -U calagoapi                    # 2.0
pip install calagoapi-minecraft             # if you use Minecraft features
pip uninstall calagoapi-hungerbridge calagoapi-version-changer
```

## Core

| 1.x | 2.0 |
| --- | --- |
| `from calagoapi import GenericServer` | `from calagoapi import Server` |
| `calagoapi.servers.generic` | `calagoapi.servers.server` |
| `calagoapi.servers.Generic` / `.Minecraft` / `.Panel` (namespace) | import the classes; `calagoapi.servers` is the real subpackage |
| `calagoapi.utils.*`, `calagoapi.schedules.*` namespaces | unchanged names, now the real subpackages |
| `panel.servers.getMinecraftServer(id, name, server_domain, server_port)` | `panel.minecraft.getServer(id, name, address=...)` (calagoapi-minecraft) |
| — | `panel.servers.getServer(id, server_class=Cls, **options)`, `getServers(server_class=...)` |
| `panel.api.versions` | `calagoapi_minecraft.VersionChangerAPI` |
| `panel.admin.extensions.getVersionChangerSettings()` etc. | `panel.minecraft.versionChanger.getSettings()` etc. |
| — | `panel.admin.extensions.call(extension, path, method='GET', json=None)` |
| `AsyncPanel` wrapped only `calagoapi.*` objects | `calagoapi.aio.registerAsyncType(cls, wrapper)`; generator methods are async generators |

## Extension API (camelCase)

| 1.x | 2.0 |
| --- | --- |
| `get_extension()` | `getExtension()` |
| `is_enabled()` | `isEnabled()` |
| `enabled_extensions()` | `enabledExtensions()` |
| `@property_extension` | `@propertyExtension` |
| `@class_extension` | `@classExtension` |
| `@migrated_to` | `@migratedTo` |
| `Extension.on_enable()` / `validate_config()` | `onEnable()` / `validateConfig()` |
| `registry.owner_of()` / `get_class()` / `is_enabled()` | `ownerOf()` / `getClass()` / `isEnabled()` |
| `enable('hungerbridge')`, `enable('version_changer')` | `enable('minecraft')` (the old ids raise `ExtensionNotFoundError` naming the replacement) |

Class attributes (`extension_id`, `default_config`, `default_mode`, `secret_config`, ...)
are unchanged.

## Minecraft

| 1.x | 2.0 (`calagoapi_minecraft`) |
| --- | --- |
| `from calagoapi import MinecraftServer` | `from calagoapi_minecraft import MinecraftServer` |
| `MinecraftServer(panel, id, name, server_domain, server_port, data)` | `MinecraftServer(panel, id, name, data, *, address=None, bridge_url=None, bridge_token=None)` |
| `server.sendCommand(cmd)` → panel, `None` | `server.sendCommand(cmd, *, silent=False, showConsole=False)` → HungerBridge, output text; panel: `server.sendPanelCommand(cmd)` |
| `server.streamConsole(history=True)` → daemon | `server.streamConsole(history=0, timeout=None, *, reconnect=None, sanitize=True)` → HungerBridge (`history` = number of lines) |
| `server.onConsoleLine(cb)` → `Console` | `server.onConsoleLine(cb, history=0)` → `hungerbridge.Stream` (`.disconnect()`) |
| `server.broadcast(msg)` (alias of `say`) | `server.broadcast(msg, prefix=None)` (tellraw to everyone) |
| `getRAM()`, `getCPU()`, `stop()` | unchanged (panel) |

### calagoapi-version-changer

| 1.x | 2.0 |
| --- | --- |
| `server.getInstalledVersion()` | `server.versions.getInstalled()` |
| `server.installedVersion` | `server.versions.getInstalledBuild()` |
| `server.isUpToDate()` | `server.versions.isUpToDate()` |
| `server.getVersionTypes()` | `server.versions.getTypes()` |
| `server.getVersions(type, ...)` / `getBuilds(type, version, ...)` | `server.versions.getVersions(...)` / `getBuilds(...)`; new `getLatestBuild(type, version)` |
| `server.installVersion(build, ...)` | `server.versions.install(build, ..., backup=None)` |
| `server.updateVersion()` | `server.versions.update()` |
| config `auto_backup`, `backup_name`, `backup_timeout` | same keys on `enable('minecraft', config=...)` |

### calagoapi-hungerbridge

| 1.x (`server.hungerbridge.`) | 2.0 (`server.`) |
| --- | --- |
| `connect(url, token)` | `connectBridge(url, token, **options)` |
| `client`, `getUrl()`, `close()` | `bridge` (a `hungerbridge.BridgeClient`), `getBridgeUrl()`, `closeBridge()` |
| `isReachable()`, `authCheck()`, `meta()` | `isBridgeReachable()`, `getBridgeTokenInfo()`, `getBridgeInfo()` |
| `ping()` | `bridge.getServerTime()` / `bridge.getPing()` |
| `status()`, `info()`, `disk()` | removed: not HungerBridge protocol v1 endpoints (use `getBridgeInfo()`, `getDisk()`) |
| `players()`, `playerCount()` | `getPlayers()`, `getPlayerCount()`, new `getMaxPlayers()` |
| `run(cmd, silent, show_console)` | `sendCommand(cmd, silent=..., showConsole=...)` |
| `log(message, level, thread)` | `writeLog(message, level='info', thread=None)` |
| `stop()` | `bridge.stopServer()` (`server.stop()` is the panel's) |
| `tps()` (dict), `mspt()` | `getTPS(mode)` (float), `getMSPT()`, `getPerformance()` |
| `chunks()`, `entities()`, `time()`, `weather()` | `getLoadedChunks()`, `getLoadedEntities()`, `getWorldTime()`, `getWeather()` |
| `uptime()`, `cpu()`, `memory()`, `gc()`, `threads()`, `network()` | `getJVMUptime()`, `getProcessorInfo()`, `getMemoryInfo()`, `getGarbageCollectorInfo()`, `getThreadInfo()`, `getNetworkInfo()`; new `getProcessInfo()` |
| `findRelease(mc_version, loader, release)`, `install(...)` | `findBridgeRelease(minecraft_version, loader, release)`, `installBridge(...)` |
| — | `createBridgeToken()`, `redeemBridgePickup()`, `waitForBridge()`, `setBridge()`, `hasBridge()` |
| `HungerBridgeClient`, `HungerBridgeError` (CalagoAPI) | `hungerbridge.BridgeClient`, `hungerbridge.HungerBridgeError` (HungerBridgePy) |
| config `url`, `port`, `token`, `timeout`, `verify`, `mc_version` | `bridge_url`, `bridge_port`, `bridge_token`, `bridge_timeout`, `bridge_max_retries`, `stream_reconnect`; versions are arguments of `installBridge()` |

## Example

```python
# 1.x
from calagoapi.extensions import enable
enable('hungerbridge', config={'token': 'bot:9f2c...'})
server = panel.servers.getMinecraftServer('abc123', server_domain='play.example.com')
print(server.hungerbridge.run('list'), server.hungerbridge.tps()['tps'])
server.installVersion(server.getBuilds('PAPER', '1.21.11')[0])

# 2.0
from calagoapi.extensions import enable
enable('minecraft', config={'bridge_token': 'bot:9f2c...'})
server = panel.minecraft.getServer('abc123', address='play.example.com')
print(server.sendCommand('list'), server.getTPS())
server.versions.install(server.versions.getLatestBuild('PAPER', '1.21.11'))
```

## HungerBridge and HungerBridgePy

- HungerBridgePy ≥ 1.0.dev2 is required (`streamLogs()`, `getTPSStats()`,
  `getPlayerStats()`, `hungerbridge.releases`, typed stream errors).
- HungerBridge release jars are now named `HungerBridge-<loader>-<minecraft>-<version>.jar`.
  `installBridge()` still recognises the older `<minecraft>-<loader>-<version>.jar` names.
