# calagoapi-minecraft

Minecraft servers for [CalagoAPI](https://github.com/HungerNet/CalagoAPI), the Calagopus
panel SDK. `MinecraftServer` is a `calagoapi.Server` with Minecraft features:

- **commands with output** and **live console streaming** through
  [HungerBridge](https://modrinth.com/project/hungerbridge), the plugin/mod inside the game,
  using [HungerBridgePy](https://github.com/HungerNet/HungerBridgePy) (`server.bridge`);
- installing HungerBridge from Modrinth and creating its tokens through the panel;
- `server.properties`, EULA, chat and moderation helpers.

Version 2 needs HungerBridge 5 and HungerBridgePy 2 (protocol v2). Upgrading from 1.x:
[docs/migrating-minecraft-2.0.md](../../../docs/migrating-minecraft-2.0.md).

```bash
pip install calagoapi calagoapi-minecraft      # also installs hungerbridge (HungerBridgePy)
```

```python
from calagoapi import Panel
from calagoapi.extensions import enable

enable('minecraft', config={'bridge_token_id': 'calagoapi', 'bridge_token_secret': '9f2c...'})

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

    print(server.sendCommand('list'))                 # the command's output (not printed on the console)
    for line in server.streamConsole(history=10, timeout=30):
        print(line)
    print(f'{server.bridge.getPlayerCount()} online, TPS {server.bridge.getTPS("1m")}')
    print(f'container {server.getRAM()} MiB, heap {server.bridge.getMemoryStats()["heap_used"]:.0f} MiB')
```

Learn it step by step in the [Minecraft tutorials](../../../docs/tutorials/README.md#track-3-minecraft);
runnable code is in [examples/minecraft/](../../../examples/minecraft/README.md).

## Two channels

| Channel | Used by |
| --- | --- |
| **Panel / daemon** (CalagoAPI) | everything inherited from `Server`: `start()`, `stop()`, `restart()`, `getRAM()`, `getCPU()`, `getStatus()`, files, backups, ...; plus `server.properties`, EULA, `installBridge()`, `createBridgeToken()`, `sendPanelCommand()`, `server.console` |
| **HungerBridge** (HungerBridgePy) | `sendCommand()`, `sendCommands()`, `streamConsole()`, `onConsoleLine()`, the chat and moderation helpers, and everything on `server.bridge` |

`server.bridge` is a `hungerbridge.BridgeClient`: players, TPS/MSPT, world, JVM metrics,
`log()`, `streamLogs()`, `broadcast()`, ... are used with HungerBridgePy's own names (see its
[API table](https://github.com/HungerNet/HungerBridgePy#api)); CalagoAPI does not add aliases.
`MinecraftServer` itself only adds what combines the panel with the bridge, or what replaces
a `Server` method with its bridge version.

Nothing falls back silently. Bridge methods without a token raise
`BridgeNotConfiguredError`; HungerBridge errors are raised as HungerBridgePy's
`hungerbridge.HungerBridgeError` subclasses (`HungerBridgeAuthError` with `.reason`,
`HungerBridgeForbidden`, `HungerBridgeNotFound`, `HungerBridgeRateLimit`,
`HungerBridgeConnectionError`, `HungerBridgeProtocolError`).

## Getting a server

```python
server = panel.minecraft.getServer('abc123')                       # after enable('minecraft')
server = panel.minecraft.getServer('abc123', address='play.example.com', bridge_url=...,
                                   bridge_token_id=..., bridge_token_secret=...)
server = panel.minecraft.fromServer(panel.servers.getServerByName('Survival'))
servers = panel.minecraft.getServers()                             # every visible server, as MinecraftServer

from calagoapi_minecraft import MinecraftServer                    # works without enable() too
server = MinecraftServer(panel, 'abc123', bridge_token_id='calagoapi', bridge_token_secret='9f2c...')
```

The token id and secret are always separate values: give both or neither
(`ConfigurationError` otherwise, also for a secret that is not 64 hex characters).

## Connecting HungerBridge

| Method | Description |
| --- | --- |
| `installBridge(minecraft_version, loader, *, version=None, replace=True)` | download the HungerBridge jar for that Minecraft version and loader (`paper`, `purpur`, `folia`, `fabric`) from Modrinth into `/plugins` or `/mods`; both arguments required, nothing is detected; returns a `hungerbridge.BridgeRelease` |
| `createBridgeToken(token_id='calagoapi', policy='admin', expiry=None, timeout=30, url=None)` | run `hb token create` on the console, redeem the pickup, connect; returns `hungerbridge.Credentials` |
| `redeemBridgePickup(pickup_url)` | redeem a pickup URL (or its `/pickup/...` part) and connect |
| `connectBridge(url=None, *, token_id=None, token_secret=None, **options)` | set URL/token (and `BridgeClient` options such as `timeout`) for this server |
| `setBridge(client)`, `closeBridge()` | use your own `BridgeClient`; close connections |
| `bridge` | the `hungerbridge.BridgeClient` |
| `getBridgeUrl()`, `hasBridge()`, `isBridgeReachable()`, `waitForBridge(timeout=120)` | |

The bridge URL is `bridge_url`, else the `bridge_url` config, else the server's address
with `bridge_port` (1913). HungerBridge binds `127.0.0.1` by default. Set its
`bind-address` and `security.yaml` `ips` so your code can reach it.

## Commands and console

| Method | Description |
| --- | --- |
| `sendCommand(command, *, show_console=False)` | HungerBridgePy `runCommand()`: returns the output text; it reaches the server console only with `show_console=True` |
| `sendCommands(commands, *, show_console=False)` | list of outputs |
| `sendPanelCommand(command)` | through the panel (`Server.sendCommand`), no output |
| `streamConsole(history=0, timeout=None, *, reconnect=None)` | yields plain console lines `[HH:mm:ss] [thread/LEVEL]: [logger] message`; `history=True` = everything HungerBridge keeps (1000) |
| `onConsoleLine(callback, history=0, *, reconnect=None)` | background callbacks; returns the `hungerbridge.Stream` (`.disconnect()`) |
| `say`, `tellraw`, `kick`, `ban`, `pardon`, `op`, `deop`, `whitelistAdd`, `whitelistRemove`, `saveAll` | chat and moderation (return the command output) |

For structured events (`level`, `thread`, `logger`, `message`) use
`server.bridge.streamLogs()`; to write your own log lines, `server.bridge.log(message,
level, thread, logger, normalize)`.

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
| `bridge_token_id`, `bridge_token_secret` | `None` | token for every server (the secret is masked in diagnostics) |
| `bridge_timeout` | `None` | seconds or `(connect, read)`; `None` = HungerBridgePy's `(5, 30)` |
| `bridge_max_retries` | `2` | retries after HTTP 429 |
| `stream_reconnect` | `True` | default `reconnect` of `streamConsole()` / `onConsoleLine()` |

Without `enable()`, `MinecraftServer` uses these defaults (`calagoapi_minecraft.settings()`).

## Async

```python
async with AsyncPanel(url=..., api_key=...) as panel:
    server = await panel.minecraft.getServer('abc123')
    print(await server.sendCommand('list'), await server.bridge.getTPS())
    async for line in server.streamConsole(history=10):
        print(line)
```

`AsyncMinecraftServer` runs HungerBridgePy in worker threads (one per open stream);
`onConsoleLine()` accepts coroutine callbacks.

## Package layout

| Module | Responsibility |
| --- | --- |
| `server.py` | `MinecraftServer` |
| `bridge.py` | client creation, pickup line parsing |
| `properties.py` | `server.properties` text handling |
| `manager.py` | `MinecraftManager` (`panel.minecraft`) |
| `extension.py`, `config.py` | `MinecraftExtension`, defaults, validation, `settings()` |
| `aio.py` | `AsyncMinecraftServer`, async type registrations |
| `exceptions.py` | `MinecraftError`, `BridgeNotConfiguredError` |
