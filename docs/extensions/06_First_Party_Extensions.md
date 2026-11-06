# First-party extensions

CalagoAPI's own extensions live in this repository under `src/extensions/` and
are published to PyPI as separate packages. They use exactly the same public API
as third-party extensions (`calagoapi.extensions`), so they double as reference
implementations.

| Package | Id | Adds | Default mode |
| --- | --- | --- | --- |
| `calagoapi-version-changer` | `version_changer` | Minecraft Version Changer methods on `MinecraftServer` and `panel.admin.extensions` | direct |
| `calagoapi-hungerbridge` | `hungerbridge` | `server.hungerbridge` service for the HungerBridge mod | namespace |

```bash
pip install calagoapi-version-changer
pip install calagoapi-hungerbridge      # also installs calagoapi-version-changer
```

## version_changer

Wraps the Calagopus **Minecraft Version Changer** panel extension
(`dev.0x7d8.minecraftversionchanger`), which must be installed on your panel.

```python
from calagoapi.extensions import enable

enable('version_changer')

server = panel.servers.getMinecraftServer('abc123')
print(server.installedVersion)                     # installed build, or None
print(server.getVersionTypes())                    # PAPER, PURPUR, FABRIC, ...
builds = server.getBuilds('PAPER', '1.21.11', page=1, per_page=1)
server.installVersion(builds[0])

if server.isUpToDate() is False:
    server.updateVersion()
```

| Member on `MinecraftServer` | Kind |
| --- | --- |
| `getInstalledVersion()` | method: `{'build': ..., 'latest': ...}` or None |
| `installedVersion` | property: the installed build or None |
| `isUpToDate()` | method: True / False / None (unknown) |
| `getVersionTypes()` | method |
| `getVersions(type, search=None, page=None, per_page=None)` | method |
| `getBuilds(type, version, search=None, page=None, per_page=None)` | method |
| `installVersion(build, truncate_directory=False, accept_eula=True)` | method |
| `updateVersion(truncate_directory=False)` | method: newest build of the installed version |

On `panel.admin.extensions` (admin API key): `getVersionChangerSettings()`,
`updateVersionChangerSettings(**settings)`, `getVersionChangerStatistics()`,
`getVersionChangerDefaultOrder()`.

Config:

| Key | Default | Meaning |
| --- | --- | --- |
| `auto_backup` | `False` | Create a backup before every `installVersion()`; nothing is installed if it fails |
| `backup_name` | `'Before version change'` | Name of that backup |
| `backup_timeout` | `3600` | Seconds to wait for it |

Alias: `minecraft_version_changer`.

**Compatibility.** These methods used to be built into `MinecraftServer`. The
built-in versions still work (with an `ExtensionDeprecationWarning`), and
`enable('version_changer')` replaces them with the extension's versions. See
[Migrating built-in features](Migrating_Builtins.md).

## hungerbridge

A client for [HungerBridge](https://github.com/hungernet/hungerbridge), the
Paper/Fabric mod that exposes an HMAC-signed HTTP API inside the Minecraft
server: run commands without RCON, read players, TPS, memory and more.

```python
enable('hungerbridge', config={'token': 'bot:9f2c...'})

server.hungerbridge.players()           # ['Steve', 'Alex']
server.hungerbridge.playerCount()       # 2
server.hungerbridge.run('list')         # console output lines
server.hungerbridge.tps()               # {'tps': 20.0, 'tps_1m': ..., ...}
server.hungerbridge.memory()            # heap / JVM / process bytes
```

Tokens are created in the server console (`hb token create <id> <policy>`) and
picked up once from the URL it prints. Pass them as `"tokenId:secret"`.

The bridge URL defaults to the server's address with port 1913. Set `url` in the
config for every server, or per server:

```python
server.hungerbridge.connect('http://10.0.0.6:1913', 'other:41ab...')
```

| Area | Methods |
| --- | --- |
| Health | `ping()`, `isReachable()`, `authCheck()`, `status()`, `info()`, `meta()` |
| Players | `players()`, `playerCount()` |
| Console | `run(command, silent=False, show_console=False)`, `log(message, level='INFO', thread=None)`, `stop()` |
| World | `tps()`, `mspt()`, `chunks()`, `entities()`, `time()`, `weather()` |
| System | `uptime()`, `cpu()`, `memory()`, `gc()`, `threads()`, `network()`, `disk()` |
| Install | `install(mc_version=None, loader=None, release=None)`, `findRelease(...)` |
| Connection | `connect(url=None, token=None)`, `getUrl()`, `client`, `close()` |

`install()` downloads the matching HungerBridge jar from GitHub releases into
`/plugins` (Paper, Purpur, Folia, ...) or `/mods` (Fabric, Quilt). It asks the
version changer for the server type and Minecraft version, which is why
`hungerbridge` depends on `version_changer`. Restart the server afterwards.

Config:

| Key | Default | Meaning |
| --- | --- | --- |
| `url` | `None` | Bridge URL for every server; `None` = server address + `port` |
| `port` | `1913` | Bridge port |
| `token` | `None` | `"tokenId:secret"` (masked in diagnostics) |
| `timeout` | `10` | Seconds |
| `verify` | `True` | Verify TLS certificates |
| `mc_version` | `'auto'` | For `install()`: `'auto'`, `'latest'` or e.g. `'1.21.11'` |
| `release` | `'latest'` | HungerBridge release tag |
| `repository` | `'hungernet/hungerbridge'` | GitHub repository |
| `github_api` | `'https://api.github.com'` | GitHub API URL |

Errors raise `calagoapi_hungerbridge.HungerBridgeError` (a `CalagoAPIError`) with
`status_code` and HungerBridge's `error` code (`'unauthorized'`, `'forbidden'`, ...).

Alias: `hunger_bridge`. The default mode is `namespace`; since everything lives
in the `hungerbridge` service, the mode makes no visible difference.

## Repository layout

```text
src/extensions/
├── conftest.py                       shared test fixtures (fake panel, fresh registry)
├── calagoapi-version-changer/
│   ├── pyproject.toml                package metadata + "calagoapi" entry point
│   ├── version.yaml                  run / version / release notes
│   ├── README.md                     the PyPI page
│   ├── calagoapi_version_changer/
│   │   ├── api.py                    HTTP calls
│   │   └── extension.py              members + VersionChangerExtension
│   └── tests/
└── calagoapi-hungerbridge/
    └── (same layout; client.py signs requests)
```

## Adding a first-party extension

1. Create `src/extensions/calagoapi-<name>/` following the layout above.
2. Depend on `calagoapi>=<first version with the APIs you use>`.
3. Add the id and package to `FIRST_PARTY` in
   `src/calagoapi/extensions/discovery.py`, so "not installed" errors suggest
   the right `pip install`.
4. Write tests in `tests/` using the `extensions`, `fake` and `panel` fixtures
   from `src/extensions/conftest.py`.
5. Add a `version.yaml`. The release workflow finds every
   `src/extensions/*/pyproject.toml` automatically, publishes packages whose tag
   (`<package>-v<version>`) does not exist yet, and orders them so dependencies
   are published first.
6. Configure PyPI trusted publishing for the new project (repository
   `HungerNet/CalagoAPI`, workflow `release.yml`).
7. Document it on this page.
