'''
Minecraft example 4: an asyncio bot that welcomes players and reports TPS.

    CALAGOPUS_URL=... CALAGOPUS_API_KEY=... MC_SERVER=... HB_URL=... HB_TOKEN=... \
        python examples/minecraft/04_async_welcome_bot.py

The same API as the sync examples, with await. Two tasks run concurrently:
one follows the console and greets every player who joins, the other prints TPS
every few seconds. Stops after `seconds`.
'''
import asyncio
import re

from calagoapi import AsyncPanel
from calagoapi.extensions import enable

import _env

JOIN = re.compile(r'\]: (\w+) joined the game')


async def welcome(server, seconds):
    greeted = []
    async for line in server.streamConsole(timeout=seconds):
        match = JOIN.search(line)
        if match:
            player = match.group(1)
            await server.broadcast(f'Welcome, {player}!', prefix='[Bot] ')
            greeted.append(player)
    return greeted


async def watchTps(server, seconds, interval=2):
    samples = []
    for _ in range(max(1, int(seconds // interval))):
        samples.append(await server.getTPS())
        print(f'TPS {samples[-1]}')
        await asyncio.sleep(interval)
    return samples


async def main(panel, server_id, bridge_url=None, bridge_token=None, seconds=10):
    server = await panel.minecraft.getServer(server_id, bridge_url=bridge_url, bridge_token=bridge_token)
    print(f'watching {server.name} for {seconds}s')
    greeted, samples = await asyncio.gather(welcome(server, seconds), watchTps(server, seconds))
    print(f'greeted: {", ".join(greeted) or "nobody"}')
    return greeted, samples


async def run(config):
    async with AsyncPanel(url=config['url'], api_key=config['api_key']) as panel:
        await main(panel, config['server_id'], config['bridge_url'], config['bridge_token'], seconds=60)


if __name__ == '__main__':
    config = _env.settings()
    if config:
        enable('minecraft')
        asyncio.run(run(config))
