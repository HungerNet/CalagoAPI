'''
Minecraft example 5: install (or upgrade) HungerBridge from Modrinth.

    CALAGOPUS_URL=... CALAGOPUS_API_KEY=... MC_SERVER=... MC_VERSION=1.21.11 MC_LOADER=paper \
        python examples/minecraft/05_install_bridge.py

installBridge() takes the Minecraft version and loader explicitly (nothing is guessed),
asks Modrinth for the newest HungerBridge release that matches them and that speaks this
HungerBridgePy's protocol, and pulls the jar into /plugins or /mods through the panel.
'''
import os

from calagoapi import Panel
from calagoapi.extensions import enable

import _env


def main(panel, server_id, minecraft_version, loader, restart=True, **connection):
    server = panel.minecraft.getServer(server_id, **connection)
    release = server.installBridge(minecraft_version=minecraft_version, loader=loader)
    print(f'installed {release.filename} (HungerBridge {release.version_number}, {release.version_type}) '
          f'into {release.directory}')
    print(f'sha512 {release.sha512[:16]}...  {release.url}')
    if restart:
        server.restart()
        if server.hasBridge() and server.waitForBridge(timeout=180):
            print(f'bridge is back: {server.bridge.getBridgeVersion()}')
    return release


if __name__ == '__main__':
    config = _env.settings()
    if config:
        enable('minecraft')
        with Panel(url=config['url'], api_key=config['api_key']) as panel:
            main(panel, config['server_id'], os.environ['MC_VERSION'], os.environ['MC_LOADER'], **config['connection'])
