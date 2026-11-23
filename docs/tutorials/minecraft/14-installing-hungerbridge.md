# 14 · Installing HungerBridge

This builds on [11–13](../README.md#track-3-minecraft) and on the backup workflow of
[04](../basics/04-files-and-backups.md).

## What you will build

An install-and-upgrade script: back up the server, put the right HungerBridge jar into
`/plugins` or `/mods`, restart, and wait until the bridge answers again.
Code: [examples/minecraft/05_install_bridge.py](../../../examples/minecraft/05_install_bridge.py).

## Step 1: say what the server runs

```python
release = server.installBridge(minecraft_version='1.21.11', loader='paper')
```

Both arguments are required and nothing is guessed. Use the loader as Modrinth names it:

| Server software | `loader` | Jar goes to |
| --- | --- | --- |
| Paper | `paper` | `/plugins` |
| Purpur | `purpur` | `/plugins` |
| Folia | `folia` | `/plugins` |
| Fabric | `fabric` | `/mods` |

A loader or Minecraft version HungerBridge is not published for raises `ValueError` listing
what is available, so a typo fails before anything is downloaded.

## Step 2: what installBridge() does

1. HungerBridgePy's `findRelease()` asks [Modrinth](https://modrinth.com/project/hungerbridge) 
   for versions whose **metadata** lists that loader and Minecraft version. File names are never parsed.
2. Only HungerBridge 5.x releases are taken (they speak the protocol your HungerBridgePy
   speaks); the newest wins. Pin one with `version='5-alpha.1'`.
3. Other `HungerBridge*.jar` files in the target directory are deleted (`replace=False`
   keeps them), and the panel pulls the jar from Modrinth's CDN (`files.pullFile`).
4. It returns a `hungerbridge.BridgeRelease`: `version_number`, `version_type`, `filename`,
   `url`, `size`, `sha512`, `directory`, `loaders`, `game_versions`.

The new jar is loaded on the next start, so restart afterwards.

## Complete program

```python
from calagoapi import Panel
from calagoapi.extensions import enable

MINECRAFT_VERSION = '1.21.11'
LOADER = 'paper'

enable('minecraft', config={'bridge_token_id': 'calagoapi', 'bridge_token_secret': '9f2c...'})

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

    backup = server.backups.createBackup(name='Before HungerBridge update')
    backup.waitUntilComplete(timeout=3600)
    if not backup.isSuccessful():
        raise SystemExit('backup failed, nothing changed')

    release = server.installBridge(minecraft_version=MINECRAFT_VERSION, loader=LOADER)
    print(f'installed {release.filename} (HungerBridge {release.version_number})')

    server.restart()
    if server.waitForBridge(timeout=180):
        print(f'bridge is back: {server.bridge.getBridgeVersion()}')
```

## How it works

- Release resolution lives in HungerBridgePy (`hungerbridge.findRelease`), so every
  HungerBridge client agrees on which jar is right; CalagoAPI only adds the panel file
  operations.
- When the Minecraft version itself changes (a new Paper build, a new major version), change
  the server software first with the panel or your egg, then run `installBridge()` with the
  new version.
- `waitForBridge()` polls an authenticated `/ping` until it answers or the timeout passes.
  A newly installed server needs a token first: tutorial [11](11-minecraft-setup.md#step-3-a-token).
- `findRelease()` raises `HungerBridgeNotFound` when no compatible release exists for that
  loader and version, and `HungerBridgeConnectionError` when Modrinth cannot be reached.

## Next

[15 · Capstone: community bot](15-community-bot.md).
