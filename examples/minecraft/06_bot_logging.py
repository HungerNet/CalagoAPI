'''
Minecraft example 6: write structured log lines from a bot and read them back.

    CALAGOPUS_URL=... CALAGOPUS_API_KEY=... MC_SERVER=... HB_URL=... HB_TOKEN_ID=... HB_TOKEN_SECRET=... \
        python examples/minecraft/06_bot_logging.py

server.bridge.log() writes to the server log with your own level, thread and logger:

    [10:53:54] [Backups/BACKUP]: [NightlyBot] world saved

normalize=True lets HungerBridge reduce a chat-style message to plain text first.
server.bridge.streamLogs() yields the same lines as structured events (level, thread,
logger, message), so a bot can filter on its own logger instead of parsing text.
'''
from calagoapi import Panel
from calagoapi.extensions import enable

import _env

LOGGER = 'NightlyBot'


def main(panel, server_id, seconds=10, **connection):
    server = panel.minecraft.getServer(server_id, **connection)
    bridge = server.bridge

    bridge.log('starting nightly maintenance', logger=LOGGER)
    bridge.log('world saved', level='BACKUP', thread='Backups', logger=LOGGER)
    relayed = bridge.log('System chat: maintenance in 5 minutes', normalize=True, logger=LOGGER)
    print(f'relayed as: {relayed!r}')

    # read our own lines back as events (history covers the three lines above)
    mine = []
    for event in bridge.streamLogs(history=50, timeout=seconds):
        if event.logger == LOGGER:
            print(f'{event.level:<7} {event.thread:<14} {event.message}')
            mine.append(event)
        if len(mine) == 3:
            break
    return relayed, [event.line for event in mine]


if __name__ == '__main__':
    config = _env.settings()
    if config:
        enable('minecraft')
        with Panel(url=config['url'], api_key=config['api_key']) as panel:
            main(panel, config['server_id'], **config['connection'])
