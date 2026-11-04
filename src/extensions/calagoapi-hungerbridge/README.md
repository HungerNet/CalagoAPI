# calagoapi-hungerbridge

A [CalagoAPI](https://github.com/HungerNet/CalagoAPI) extension for
[HungerBridge](https://github.com/hungernet/hungerbridge), the Paper/Fabric mod
that exposes a signed HTTP API inside a Minecraft server (commands without RCON,
players, TPS, memory, ...).

```bash
pip install calagoapi calagoapi-hungerbridge
```

```python
from calagoapi import Panel
from calagoapi.extensions import enable

enable('hungerbridge', config={'token': 'bot:9f2c...'})   # "tokenId:secret"

panel = Panel(url='https://panel.example.com', api_key='...')
server = panel.servers.getMinecraftServer('abc123')

print(server.hungerbridge.players())       # ['Steve', 'Alex']
print(server.hungerbridge.tps())           # {'tps': 20.0, 'tps_1m': ..., ...}
server.hungerbridge.run('say Hello from Python')
```

`enable('hungerbridge')` also enables its dependency, `version_changer`
(installed automatically with this package), which `install()` uses to detect
the server type and Minecraft version.

## Connecting

The bridge URL defaults to the server's address (from the panel) with port 1913.
Override it for every server through the config, or per server:

```python
enable('hungerbridge', config={'url': 'http://10.0.0.5:1913', 'token': 'bot:9f2c...'})

server.hungerbridge.connect('http://10.0.0.6:1913', 'other:41ab...')
```

Tokens come from the server console: `hb token create <tokenId> <policyId>`
prints a one-time pickup URL that returns the secret.

## Methods

| Area | Methods |
| --- | --- |
| Health | `ping()`, `isReachable()`, `authCheck()`, `status()`, `info()`, `meta()` |
| Players | `players()`, `playerCount()` |
| Console | `run(command, silent=False, show_console=False)`, `log(message, level='INFO')`, `stop()` |
| World | `tps()`, `mspt()`, `chunks()`, `entities()`, `time()`, `weather()` |
| System | `uptime()`, `cpu()`, `memory()`, `gc()`, `threads()`, `network()`, `disk()` |
| Install | `install(mc_version=None, loader=None, release=None)`, `findRelease(...)` |

Errors raise `calagoapi_hungerbridge.HungerBridgeError` (a `CalagoAPIError`).

## Configuration

| Key | Default | Meaning |
| --- | --- | --- |
| `url` | `None` | Bridge URL for every server; `None` uses the server address + `port` |
| `port` | `1913` | Bridge port |
| `token` | `None` | `"tokenId:secret"` |
| `timeout` | `10` | Seconds |
| `verify` | `True` | Verify TLS certificates |
| `mc_version` | `'auto'` | For `install()`: `'auto'` (installed version), `'latest'` or e.g. `'1.21.11'` |
| `release` | `'latest'` | HungerBridge release tag for `install()` |
| `repository` | `'hungernet/hungerbridge'` | GitHub repository |
| `github_api` | `'https://api.github.com'` | GitHub API URL |

## Async

```python
from calagoapi import AsyncPanel

async with AsyncPanel(url=..., api_key=...) as panel:
    server = await panel.servers.getMinecraftServer('abc123')
    print(await server.hungerbridge.players())
```
