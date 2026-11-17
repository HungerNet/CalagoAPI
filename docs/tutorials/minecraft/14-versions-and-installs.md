# 14 · Versions and installs

This builds on [11–13](../README.md#track-3-minecraft) and on the backup workflow of
[04](../basics/04-files-and-backups.md).

## What you will build

A safe upgrade: warn the players, back up, install the newest build of a Minecraft
version, reinstall the matching HungerBridge jar, restart, and wait until the bridge
answers again.

## Step 1: the Version Changer

The Calagopus **Minecraft Version Changer** panel extension installs any server build
(Paper, Purpur, Fabric, Forge, Vanilla, ...). `server.versions` wraps it:

```python
server.versions.isAvailable()                       # is the panel extension installed?
server.versions.getInstalledBuild()                 # {'type': 'PAPER', 'version_id': '1.21.11', ...}
server.versions.isUpToDate()                        # True / False / None (unknown)
server.versions.getTypes()                          # PAPER, PURPUR, FABRIC, ...
server.versions.getVersions('PAPER', page=1, per_page=10)
build = server.versions.getLatestBuild('PAPER', '1.21.11')
server.versions.install(build, backup=True)         # back up first, install only if it succeeded
server.versions.update()                            # newest build of the installed version
```

`backup=None` (the default) uses the `auto_backup` config, so
`enable('minecraft', config={'auto_backup': True})` protects every install in the process.
Admins configure the panel extension with `panel.minecraft.versionChanger.getSettings()`
and `updateSettings(...)`.

## Step 2: the matching HungerBridge jar

HungerBridge ships one jar per Minecraft version and loader. After a version change the
old jar may not load:

```python
asset = server.installBridge()        # loader + version detected, old HungerBridge jars removed
print(f'{asset.name} -> {asset.directory}')
```

Detection order: arguments → the Version Changer's installed build → a running bridge
(`/server/meta`) → the egg name and the `MINECRAFT_VERSION` startup variable. Pass
`installBridge('1.21.11', 'paper')` to skip detection, `release='v4-alpha.94'` to pin a
release.

## Complete program

```python
import time

from calagoapi import Panel
from calagoapi.extensions import enable

TYPE, VERSION = 'PAPER', '1.21.11'

enable('minecraft', config={'bridge_token': 'calagoapi:9f2c...', 'auto_backup': True})

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

    build = server.versions.getLatestBuild(TYPE, VERSION)
    installed = server.versions.getInstalledBuild() or {}
    if installed.get('uuid') == build['uuid']:
        raise SystemExit(f'{server.name} already runs {build["name"]}')

    if server.isBridgeReachable():
        server.broadcast('Updating in 60 seconds, the server will restart', prefix='[Update] ')
        time.sleep(60)
        server.saveAll()

    server.stop()                                   # the panel's stop, not HungerBridge's
    server.waitForOffline(timeout=180)
    server.versions.install(build)                  # auto_backup: backup first
    asset = server.installBridge(VERSION, TYPE)     # PAPER -> the paper jar
    server.start()

    if server.waitForBridge(timeout=300):
        print(f'{server.name}: {build["name"]} with {asset.name}, TPS {server.getTPS()}')
    else:
        print(f'{server.name} started but HungerBridge does not answer; check the console')
```

## How it works

- The Version Changer calls go through the **panel** (`/api/client/servers/{id}/minecraft/versions/...`)
  with CalagoAPI's client: same authentication, retries and errors as everything else.
  Without the panel extension they raise `NotFoundError`.
- `installBridge()` asks HungerBridgePy which jar to use (`hungerbridge.releases.find_release`).
  The jar naming (`HungerBridge-<loader>-<mc>-<version>.jar`) is a contract between
  HungerBridge's build and HungerBridgePy, so it lives there, not in CalagoAPI. The
  download itself is a panel file pull (`server.files.pullFile`) into `/plugins` or `/mods`.
- `waitForBridge()` polls an authenticated ping, so it also proves the token still works
  after the reinstall.
- `stop()` is always the panel power action. HungerBridge's own stop endpoint is
  available as `server.bridge.stopServer()` if you ever want it explicitly.

## Next

[15 · Capstone: community bot](15-community-bot.md).
