# calagoapi-version-changer

A [CalagoAPI](https://github.com/HungerNet/CalagoAPI) extension for the Calagopus
**Minecraft Version Changer** panel extension: list server types, versions and
builds, and install any Paper, Purpur, Fabric, Forge, ... build.

```bash
pip install calagoapi calagoapi-version-changer
```

```python
from calagoapi import Panel
from calagoapi.extensions import enable

enable('version_changer')

panel = Panel(url='https://panel.example.com', api_key='...')
server = panel.servers.getMinecraftServer('abc123')

print(server.installedVersion)                 # installed build, or None
builds = server.getBuilds('PAPER', '1.21.11', page=1, per_page=1)
server.installVersion(builds[0])

if server.isUpToDate() is False:
    server.updateVersion()                     # newest build of the installed version
```

You never import this package yourself; `enable('version_changer')` finds it
through its entry point.

## What it adds

`MinecraftServer`:

| Member | Kind |
| --- | --- |
| `getInstalledVersion()` | method, `{'build': ..., 'latest': ...}` or None |
| `installedVersion` | property, the installed build or None |
| `isUpToDate()` | method |
| `getVersionTypes()` | method |
| `getVersions(type, search=None, page=None, per_page=None)` | method |
| `getBuilds(type, version, search=None, page=None, per_page=None)` | method |
| `installVersion(build, truncate_directory=False, accept_eula=True)` | method |
| `updateVersion(truncate_directory=False)` | method |

`panel.admin.extensions` (admin API key): `getVersionChangerSettings()`,
`updateVersionChangerSettings(**settings)`, `getVersionChangerStatistics()`,
`getVersionChangerDefaultOrder()`.

## Configuration

```python
enable('version_changer', config={
    'auto_backup': True,                    # back up before every installVersion()
    'backup_name': 'Before version change',
    'backup_timeout': 3600,                 # seconds to wait for that backup
})
```

## Namespace mode

```python
enable('version_changer', mode='namespace')
server.version_changer.installVersion(build)
```

## Compatibility

Before this package existed, these methods were built into `MinecraftServer`.
The built-in versions still work but emit an `ExtensionDeprecationWarning`;
enabling the extension replaces them.
