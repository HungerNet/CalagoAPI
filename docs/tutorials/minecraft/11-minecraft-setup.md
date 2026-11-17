# 11 · Minecraft setup

This builds on tracks 1 and 2: `Server`, extensions and `enable()`. From here on you
need a Minecraft server on your panel (Paper, Purpur, Folia or Fabric).

## What you will build

A connection check that gets a `MinecraftServer`, creates its own HungerBridge token
through the server console if it has none, and prints what both channels report.
Code: [examples/minecraft/01_connect.py](../../../examples/minecraft/01_connect.py).

## The pieces

| Piece | What it is | Package |
| --- | --- | --- |
| CalagoAPI | the panel SDK; `Server` is game-agnostic | `calagoapi` |
| calagoapi-minecraft | `MinecraftServer(Server)`, `panel.minecraft`, Version Changer | `calagoapi-minecraft` |
| HungerBridge | a plugin/mod **inside** the Minecraft server: an authenticated HTTP API | jar in `plugins/` or `mods/` |
| HungerBridgePy | the Python client for HungerBridge (`hungerbridge.BridgeClient`) | `hungerbridge`, installed with calagoapi-minecraft |

```
                   ┌────────────── panel / daemon ──────────────┐
MinecraftServer ───┤  power, getRAM/getCPU, files, backups,      │──► Calagopus
(calagoapi_        │  server.properties, server.versions          │
 minecraft)        └──────────────────────────────────────────────┘
                   ┌────────────── HungerBridge ─────────────────┐
                   │  sendCommand (with output), streamConsole,  │──► HungerBridgePy ──► HungerBridge
                   │  players, TPS/MSPT, JVM info, writeLog      │        (server.bridge)    (in the game)
                   └──────────────────────────────────────────────┘
```

Every `MinecraftServer` method uses exactly one channel, and nothing falls back silently
from one to the other.

## Step 1: install and enable

```bash
pip install calagoapi calagoapi-minecraft
```

```python
from calagoapi import Panel
from calagoapi.extensions import enable

enable('minecraft')                      # adds panel.minecraft, sets process-wide defaults
panel = Panel(url='https://panel.example.com', api_key='c7sp_...')
server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')
```

`panel.minecraft.getServer()` is `panel.servers.getServer(..., server_class=MinecraftServer)`.
Everything from track 1 works on it unchanged.

## Step 2: install HungerBridge (once)

If the plugin is not on the server yet:

```python
asset = server.installBridge()           # detects Paper/Fabric and the Minecraft version
print(f'installed {asset.name} into {asset.directory}')
server.restart()
```

HungerBridge listens on port 1913, bound to `127.0.0.1` by default. Set `bind-address`
in its `config.yaml` (and `ips` in `security.yaml`) so the machine running your code can
reach it, then pass that address as `bridge_url`.

## Step 3: a token

HungerBridge only answers signed requests. Tokens are created on the **server console**
(`/hb token create <id> <policy>`), which prints a one-time pickup URL. CalagoAPI can
do all of that for you:

```python
token = server.createBridgeToken(token_id='calagoapi', policy='admin')
print(token)                             # 'calagoapi:9f2c...' - store it somewhere safe
```

The `admin` policy must exist in HungerBridge's `policies.yaml`. Next time, pass the
stored token instead:

```python
enable('minecraft', config={'bridge_token': 'calagoapi:9f2c...'})   # every server
server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')
# or per server: panel.minecraft.getServer(..., bridge_token='...') / server.connectBridge(url, token)
```

## Complete program

```python
from calagoapi import Panel
from calagoapi.extensions import enable

enable('minecraft')

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

    # the panel channel works without HungerBridge
    print(f'{server.name}: {server.getStatus()}, egg {server.getEggName()}, address {server.getAddress()}')

    if not server.hasBridge():
        token = server.createBridgeToken(token_id='calagoapi', policy='admin')
        print(f'created bridge token {token.split(":")[0]}:<secret> - store it')

    info = server.getBridgeInfo()
    print(f'HungerBridge {info["bridge_version"]} on {info["platform"]} {info["minecraft_version"]} '
          f'at {server.getBridgeUrl()}')
```

## How it works

- `server.bridge` **is** a `hungerbridge.BridgeClient`. CalagoAPI does not reimplement
  the HungerBridge protocol (HMAC signing, canonical JSON, typed errors). HungerBridgePy
  is the single source of truth, and everything it offers is available on `server.bridge`.
- `createBridgeToken()` uses the **panel** channel (the daemon console) to bootstrap the
  **bridge** channel. It sends `hb token create`, waits for the line containing
  `/pickup/<id>?passkey=<hex>`, and redeems it with HungerBridgePy. The passkey only
  appears on the console. HungerBridge redacts it from its own log stream.
- Without a token, bridge methods raise `BridgeNotConfiguredError` with the fix in the
  message; HungerBridge's own errors arrive as `hungerbridge.HungerBridgeError`
  subclasses (`HungerBridgeAuthError` with a `reason`, `HungerBridgeForbidden`, ...).
- Config precedence: per-server arguments > `enable('minecraft', config=...)` >
  defaults. `calagoapi_minecraft.settings()` shows the effective values. The token is a
  secret and never appears in `registry.describe()`.

## Next

[12 · Commands and console](12-commands-and-console.md).
