'''
Minecraft example 1: connect a Minecraft server to CalagoAPI and HungerBridge.

    pip install calagoapi calagoapi-minecraft
    CALAGOPUS_URL=... CALAGOPUS_API_KEY=... MC_SERVER=... HB_URL=... python examples/minecraft/01_connect.py

Shows the two channels of a MinecraftServer: the panel (status, resources) and
HungerBridge (bridge info, token). Without HB_TOKEN it creates a token through
the server console with createBridgeToken() and prints it so you can store it.
'''
from calagoapi import Panel
from calagoapi.extensions import enable

import _env


def main(panel, server_id, bridge_url=None, bridge_token=None):
    server = panel.minecraft.getServer(server_id, bridge_url=bridge_url, bridge_token=bridge_token)

    # the panel channel works without HungerBridge
    print(f'{server.name}: {server.getStatus()}, egg {server.getEggName()}, address {server.getAddress()}')

    # the bridge channel needs a token
    if not server.hasBridge():
        token = server.createBridgeToken(token_id='calagoapi', policy='admin')
        print(f'created bridge token {token.split(":")[0]}:<secret> - store it, e.g. as HB_TOKEN')

    info = server.getBridgeInfo()
    print(f'HungerBridge {info["bridge_version"]} on {info["platform"]} {info["minecraft_version"]} '
          f'(protocol {info["protocol_version"]}) at {server.getBridgeUrl()}')
    token = server.getBridgeTokenInfo()
    print(f'token {token["token_id"]} uses policy {token["policy_id"]}')
    return info


if __name__ == '__main__':
    config = _env.settings()
    if config:
        enable('minecraft')
        with Panel(url=config['url'], api_key=config['api_key']) as panel:
            main(panel, config['server_id'], config['bridge_url'], config['bridge_token'])
