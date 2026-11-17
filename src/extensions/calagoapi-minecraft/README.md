# calagoapi-minecraft

Minecraft servers for [CalagoAPI](https://github.com/HungerNet/CalagoAPI), the Calagopus
panel SDK. `MinecraftServer` is a `calagoapi.Server` with Minecraft features:

- **commands with output** and **live console streaming** through
  [HungerBridge](https://github.com/HungerNet/HungerBridge), the plugin/mod inside the
  game, using [HungerBridgePy](https://github.com/HungerNet/HungerBridgePy);
- players, TPS/MSPT, world data and JVM information;
- the Calagopus **Minecraft Version Changer** (`server.versions`);
- `server.properties`, EULA, chat and moderation helpers;
- installing HungerBridge and creating its tokens through the panel.

```bash
pip install calagoapi calagoapi-minecraft      # also installs hungerbridge (HungerBridgePy)
```

```python
from calagoapi import Panel
from calagoapi.extensions import enable

enable('minecraft', config={'bridge_token': 'calagoapi:9f2c...'})

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

    print(server.sendCommand('list'))                 # the command's output
    for line in server.streamConsole(history=10, timeout=30):
        print(line)
    print(f'{server.getPlayerCount()} online, TPS {server.getTPS("1m")}')
    print(f'container {server.getRAM()} MiB, heap {server.getMemoryInfo()["used"]:.0f} MiB')
```

Learn it step by step in the [Minecraft tutorials](../../../docs/tutorials/README.md#track-3-minecraft);
runnable code is in [examples/minecraft/](../../../examples/minecraft/README.md).

## Two channels

| Channel | Used by |
| --- | --- |
| **Panel / daemon** (CalagoAPI) | everything inherited from `Server`: `start()`, `stop()`, `restart()`, `getRAM()`, `getCPU()`, `getStatus()`, files, backups, ...; plus `server.properties`, EULA, `server.versions`, `sendPanelCommand()`, `installBridge()`, `createBridgeToken()`, `server.console` |
| **HungerBridge** (HungerBridgePy, `server.bridge`) | `sendCommand()`, `streamConsole()`, `onConsoleLine()`, chat helpers, players, TPS/MSPT, world, JVM info, `writeLog()` |

Nothing falls back silently. Bridge methods without a token raise
`BridgeNotConfiguredError`; HungerBridge errors are raised as HungerBridgePy's
`hungerbridge.HungerBridgeError` subclasses (`HungerBridgeAuthError` with `.reason`,
`HungerBridgeForbidden`, `HungerBridgeNotFound`, `HungerBridgeRateLimit`,
`HungerBridgeConnectionError`).

## Getting a server

```python
server = panel.minecraft.getServer('abc123')                       # after enable('minecraft')
server = panel.minecraft.getServer('abc123', address='play.example.com', bridge_url=..., bridge_token=...)
server = panel.minecraft.fromServer(panel.servers.getServerByName('Survival'))
servers = panel.minecraft.getServers()                             # every visible server, as MinecraftServer

from calagoapi_minecraft import MinecraftServer                    # works without enable() too
server = MinecraftServer(panel, 'abc123', bridge_token='calagoapi:9f2c...')
```

## Connecting HungerBridge

| Method | Description |
| --- | --- |
| `installBridge(minecraft_version=None, loader=None, release=None, replace=True)` | download the right jar into `/plugins` or `/mods` (detects loader and version); returns a `hungerbridge.ReleaseAsset` |
| `findBridgeRelease(minecraft_version, loader, release=None)` | the jar without installing it |
| `createBridgeToken(token_id='calagoapi', policy='admin', expiry=None, timeout=30, url=None)` | run `hb token create` on the console, redeem the pickup, connect; returns `'id:secret'` |
| `redeemBridgePickup(pickup_url)` | redeem a pickup URL (or its `/pickup/...` part) and connect |
| `connectBridge(url=None, token=None, **options)` | set URL/token (and `BridgeClient` options such as `timeout`) for this server |
| `setBridge(client)`, `closeBridge()` | use your own `BridgeClient`; close connections |
| `bridge` | the `hungerbridge.BridgeClient` (the full HungerBridgePy API) |
| `getBridgeUrl()`, `hasBridge()`, `isBridgeReachable()`, `waitForBridge(timeout=120)` | |
| `getBridgeInfo()`, `getBridgeTokenInfo()`, `getPlatform()`, `getMinecraftVersion()` | `/server/meta`, `/auth/check` |

The bridge URL is `bridge_url`, else the `bridge_url` config, else the server's address
with `bridge_port` (1913). HungerBridge binds `127.0.0.1` by default. Set its
`bind-address` and `security.yaml` `ips` so your code can reach it.

## Commands and console

| Method | Description |
| --- | --- |
| `sendCommand(command, *, silent=False, showConsole=False)` | HungerBridgePy `runCommand()`: returns the output text, `None` when silent |
| `sendCommands(commands, *, silent=False, showConsole=False)` | list of outputs |
| `sendPanelCommand(command)` | through the panel (`Server.sendCommand`), no output |
| `streamConsole(history=0, timeout=None, *, reconnect=None, sanitize=True)` | HungerBridgePy `streamLogs()`: yields `[HH:mm:ss LEVEL]: message` lines; `history` ≤ 200 (`True` = 200) |
| `onConsoleLine(callback, history=0, *, reconnect=None, sanitize=True)` | background callbacks; returns the `hungerbridge.Stream` (`.disconnect()`) |
| `writeLog(message, level='info', thread=None)` | write a line to the server log |
| `say`, `broadcast(message, prefix=None)`, `tellraw`, `kick`, `ban`, `pardon`, `op`, `deop`, `whitelistAdd`, `whitelistRemove`, `saveAll` | chat and moderation (return the command output) |

## Game and JVM information

These are **additional** to the panel's `getRAM()`, `getCPU()`, `getUptime()`, which stay
unchanged (the container as the panel sees it).

| Method | Returns |
| --- | --- |
| `getPlayers()`, `getPlayerCount()`, `getMaxPlayers()` | names, online count, slots |
| `getTPS(mode='current')` | `'current'`, `'1m'`, `'5m'`, `'15m'`; `-1` if unavailable |
| `getMSPT()` | milliseconds per tick |
| `getPerformance()` | `{'tps': {...}, 'mspt', 'players', 'max_players'}` |
| `getWorldTime()`, `getWorldTimeInfo()`, `getWeather()` | tick of day, time info, `clear`/`rain`/`thunder` |
| `getLoadedChunks()`, `getLoadedEntities()` | per dimension and total |
| `getMemoryInfo(unit='mib')` | heap, non-heap, JVM, process + `used`, `total`, `free`, `max` |
| `getProcessInfo(unit='mib')` | `process_used`, `process_virtual`, `uptime_ms` |
| `getProcessorInfo()` | `load` (JVM process, 0–1), `processors` |
| `getThreadInfo()` | `current`, `peak`, `daemon` |
| `getGarbageCollectorInfo()` | `gc_type`, `gc_count`, `gc_time_ms`, `last_gc_pause_ms`, `avg_gc_pause_ms` |
| `getNetworkInfo()` | `bytes_in_per_sec`, `bytes_out_per_sec`, `total_bytes_in`, `total_bytes_out` |
| `getJVMUptime(formatted=False)` | ms, or `'3h 12m'` |

## Version Changer

Needs the Calagopus Minecraft Version Changer panel extension.

| `server.versions.` | |
| --- | --- |
| `isAvailable()` | is the panel extension installed? |
| `getInstalled()`, `getInstalledBuild()`, `isUpToDate()` | the installed build and the newest build of its version |
| `getTypes()`, `getVersions(type, ...)`, `getBuilds(type, version, ...)`, `getLatestBuild(type, version)` | |
| `install(build, truncate_directory=False, accept_eula=True, backup=None)` | `backup=None` uses `auto_backup`; a failed backup installs nothing |
| `update(truncate_directory=False, backup=None)` | newest build of the installed version; `False` if up to date |

Admin (`panel.minecraft.versionChanger.`): `getSettings()`, `updateSettings(**values)`,
`getStatistics()`, `getDefaultOrder()`.

## server.properties and EULA

`getProperties()`, `getProperty(key, default=None)`, `setProperty(key, value)`,
`setProperties(values)` (comments and order are kept; booleans become `true`/`false`),
`getMOTD()`, `setMOTD(motd)`, `acceptEula()`, `isEulaAccepted()`.

## Configuration

`enable('minecraft', config={...})`, all optional:

| Key | Default | Meaning |
| --- | --- | --- |
| `bridge_url` | `None` | HungerBridge URL for every server; `None` uses the server's address + `bridge_port` |
| `bridge_port` | `1913` | |
| `bridge_token` | `None` | `'tokenId:secret'` (secret: masked in diagnostics) |
| `bridge_timeout` | `None` | seconds or `(connect, read)`; `None` = HungerBridgePy's `(5, 30)` |
| `bridge_max_retries` | `2` | retries after HTTP 429 |
| `stream_reconnect` | `True` | default `reconnect` of `streamConsole()` / `onConsoleLine()` |
| `auto_backup` | `False` | back up before `server.versions.install()` |
| `backup_name`, `backup_timeout` | `'Before version change'`, `3600` | |
| `release` | `'latest'` | HungerBridge release for `installBridge()` |
| `repository`, `github_api` | `'HungerNet/HungerBridge'`, `'https://api.github.com'` | where releases are published |

Without `enable()`, `MinecraftServer` uses these defaults (`calagoapi_minecraft.settings()`).

## Async

```python
async with AsyncPanel(url=..., api_key=...) as panel:
    server = await panel.minecraft.getServer('abc123')
    print(await server.sendCommand('list'))
    async for line in server.streamConsole(history=10):
        print(line)
```

`AsyncMinecraftServer` runs HungerBridgePy in worker threads (one per open stream);
`onConsoleLine()` accepts coroutine callbacks.

## Package layout

| Module | Responsibility |
| --- | --- |
| `server.py` | `MinecraftServer` |
| `bridge.py` | client creation, pickup parsing, loader/version detection |
| `versions.py` | `VersionManager`, `VersionChangerAdmin`, `VersionChangerAPI` |
| `properties.py` | `server.properties` text handling |
| `manager.py` | `MinecraftManager` (`panel.minecraft`) |
| `extension.py`, `config.py` | `MinecraftExtension`, defaults, validation, `settings()` |
| `aio.py` | `AsyncMinecraftServer`, async type registrations |
| `exceptions.py` | `MinecraftError`, `BridgeNotConfiguredError` |

Replaces the CalagoAPI 1.x packages `calagoapi-hungerbridge` and `calagoapi-version-changer`;
see [Migrating to 2.0](../../../docs/migrating-to-2.0.md).
