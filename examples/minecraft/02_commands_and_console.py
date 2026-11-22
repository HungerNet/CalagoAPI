'''
Minecraft example 2: commands with output and the live console.

    CALAGOPUS_URL=... CALAGOPUS_API_KEY=... MC_SERVER=... HB_URL=... HB_TOKEN_ID=... HB_TOKEN_SECRET=... \
        python examples/minecraft/02_commands_and_console.py

sendCommand() runs through HungerBridge and returns what the command printed; the
output stays off the server console unless show_console=True. streamConsole() follows
HungerBridge's log stream. Both are HungerBridgePy calls underneath (runCommand() and
streamLogs()).
'''
from calagoapi import Panel
from calagoapi.extensions import enable

import _env


def main(panel, server_id, seconds=10, **connection):
    server = panel.minecraft.getServer(server_id, **connection)

    output = server.sendCommand('list')                    # not shown on the console
    print(f'list -> {output}')

    server.say('Hello from CalagoAPI')                     # chat helpers use sendCommand too
    server.sendCommand('save-all', show_console=True)      # also visible to people watching the console

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
            main(panel, config['server_id'], **config['connection'])
