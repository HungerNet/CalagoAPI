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
| `panel.api.versions`, `panel.admin.extensions.getVersionChangerSettings()` etc. | removed: the Minecraft Version Changer is no longer supported |
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

Minecraft moved into `calagoapi-minecraft`. The tables below map 1.x straight to the
current `calagoapi-minecraft` 2.0 API (HungerBridge 5, HungerBridgePy 2); the changes between
calagoapi-minecraft 1.x and 2.0 are in [migrating-minecraft-2.0.md](migrating-minecraft-2.0.md).

| 1.x | now (`calagoapi_minecraft`) |
| --- | --- |
| `from calagoapi import MinecraftServer` | `from calagoapi_minecraft import MinecraftServer` |
| `MinecraftServer(panel, id, name, server_domain, server_port, data)` | `MinecraftServer(panel, id, name, data, *, address=None, bridge_url=None, bridge_token_id=None, bridge_token_secret=None)` |
| `server.sendCommand(cmd)` → panel, `None` | `server.sendCommand(cmd, *, show_console=False)` → HungerBridge, output text; panel: `server.sendPanelCommand(cmd)` |
| `server.streamConsole(history=True)` → daemon | `server.streamConsole(history=0, timeout=None, *, reconnect=None)` → HungerBridge |
| `server.onConsoleLine(cb)` → `Console` | `server.onConsoleLine(cb, history=0)` → `hungerbridge.Stream` (`.disconnect()`) |
| `server.broadcast(msg)` (alias of `say`) | `server.say(msg)`, or `server.bridge.broadcast(msg, prefix=None)` (tellraw to everyone) |
| `getRAM()`, `getCPU()`, `stop()` | unchanged (panel) |

### calagoapi-version-changer

Removed. The Minecraft Version Changer panel extension is no longer supported; change the
server software with the panel or your egg, and install HungerBridge with
`server.installBridge(minecraft_version=..., loader=...)`.

### calagoapi-hungerbridge

| 1.x (`server.hungerbridge.`) | now |
| --- | --- |
| `connect(url, token)` | `server.connectBridge(url, token_id=..., token_secret=..., **options)` |
| `client`, `getUrl()`, `close()` | `server.bridge` (a `hungerbridge.BridgeClient`), `server.getBridgeUrl()`, `server.closeBridge()` |
| `isReachable()`, `authCheck()`, `meta()` | `server.isBridgeReachable()`, `server.bridge.getTokenInfo()`, `server.bridge.getServerMeta()` |
| `ping()` | `server.bridge.getServerTime()` / `getPing()` |
| `status()`, `info()`, `disk()` | removed (not HungerBridge endpoints; use `getServerMeta()`, the panel's `getDisk()`) |
| `players()`, `playerCount()` | `server.bridge.getPlayers()`, `getPlayerCount()`, `getMaxPlayers()` |
| `run(cmd, silent, show_console)` | `server.sendCommand(cmd, show_console=...)` |
| `log(message, level, thread)` | `server.bridge.log(message, level='INFO', thread=None, logger=None, normalize=False)` |
| `stop()` | `server.bridge.stopServer()` (`server.stop()` is the panel's) |
| `tps()` (dict), `mspt()` | `server.bridge.getTPSStats()`, `getTPS(window)`, `getMSPT()` |
| `chunks()`, `entities()`, `time()`, `weather()` | `server.bridge.getLoadedChunks()`, `getLoadedEntities()`, `getWorldTime()`, `getWorldWeather()` |
| `uptime()`, `cpu()`, `memory()`, `gc()`, `threads()`, `network()` | `server.bridge.getUptime()`, `getCPUStats()`, `getMemoryStats()`, `getGCStats()`, `getThreadStats()`, `getNetworkStats()` |
| `findRelease(mc_version, loader, release)`, `install(...)` | `hungerbridge.findRelease(minecraft_version=..., loader=...)`, `server.installBridge(minecraft_version, loader)` |
| — | `createBridgeToken()`, `redeemBridgePickup()`, `waitForBridge()`, `setBridge()`, `hasBridge()` |
| `HungerBridgeClient`, `HungerBridgeError` (CalagoAPI) | `hungerbridge.BridgeClient`, `hungerbridge.HungerBridgeError` (HungerBridgePy) |
| config `url`, `port`, `token`, `timeout`, `verify`, `mc_version` | `bridge_url`, `bridge_port`, `bridge_token_id`, `bridge_token_secret`, `bridge_timeout`, `bridge_max_retries`, `stream_reconnect`; versions are arguments of `installBridge()` |

## Example

```python
# 1.x
from calagoapi.extensions import enable
enable('hungerbridge', config={'token': 'bot:9f2c...'})
server = panel.servers.getMinecraftServer('abc123', server_domain='play.example.com')
print(server.hungerbridge.run('list'), server.hungerbridge.tps()['tps'])

# now
from calagoapi.extensions import enable
enable('minecraft', config={'bridge_token_id': 'bot', 'bridge_token_secret': '9f2c...'})
server = panel.minecraft.getServer('abc123', address='play.example.com')
print(server.sendCommand('list'), server.bridge.getTPS())
server.installBridge(minecraft_version='1.21.11', loader='paper')
```

## HungerBridge and HungerBridgePy

- calagoapi-minecraft 2 requires HungerBridgePy ≥ 2.0.dev1 and HungerBridge 5 on the server
  (protocol v2).
- HungerBridge is released on [Modrinth](https://modrinth.com/project/hungerbridge) only;
  `installBridge()` selects the jar by Modrinth's loader and game-version metadata.