'''
Minecraft example 2: commands with output and the live console.

    CALAGOPUS_URL=... CALAGOPUS_API_KEY=... MC_SERVER=... HB_URL=... HB_TOKEN=... \
        python examples/minecraft/02_commands_and_console.py

sendCommand() runs through HungerBridge and returns what the command printed.
streamConsole() follows HungerBridge's log stream. Both are HungerBridgePy calls
underneath (runCommand() and streamLogs()).
'''
from calagoapi import Panel
from calagoapi.extensions import enable

import _env


def main(panel, server_id, bridge_url=None, bridge_token=None, seconds=10):
    server = panel.minecraft.getServer(server_id, bridge_url=bridge_url, bridge_token=bridge_token)

    output = server.sendCommand('list')
    print(f'list -> {output}')

    server.say('Hello from CalagoAPI')                  # chat helpers use sendCommand too
    server.sendCommand('save-all', silent=True)         # silent: no output captured

    # the last 5 lines, then live lines until the console is quiet for `seconds`
    joined = []
    for line in server.streamConsole(history=5, timeout=seconds):
        print(f'console | {line}')
        if 'joined the game' in line:
            joined.append(line)
    print(f'{len(joined)} join message(s) seen')
    return output, joined


if __name__ == '__main__':
    config = _env.settings()
    if config:
        enable('minecraft')
        with Panel(url=config['url'], api_key=config['api_key']) as panel:
            main(panel, config['server_id'], config['bridge_url'], config['bridge_token'])
