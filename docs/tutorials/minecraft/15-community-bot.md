# 15 · Capstone: community bot

This brings together every track: async (05), extensions (06–10) and Minecraft (11–14).

## What you will build

An asyncio bot that runs next to your server for as long as you like:

- it greets every player who joins (console stream → command);
- it posts TPS every few seconds (bridge metrics);
- on demand it reports panel resources (panel channel) and can restart safely.

Code: [examples/minecraft/04_async_welcome_bot.py](../../../examples/minecraft/04_async_welcome_bot.py).
The same structure plugs into a Discord bot: call the functions from your command handlers.

## Step 1: async Minecraft servers

```python
from calagoapi import AsyncPanel
from calagoapi.extensions import enable

enable('minecraft', config={'bridge_token': 'calagoapi:9f2c...'})

async with AsyncPanel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = await panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')
    print(await server.getTPS())
    async for line in server.streamConsole(timeout=60):
        print(line)
```

Same names, with `await`. `server.streamConsole()` is an async generator over
HungerBridge's log stream; `server.bridge` is an async HungerBridgePy client.

## Step 2: tasks that run together

```python
greeted, samples = await asyncio.gather(welcome(server, 600), watchTps(server, 600))
```

## Complete program

```python
import asyncio
import re

from calagoapi import AsyncPanel
from calagoapi.extensions import enable

JOIN = re.compile(r'\]: (\w+) joined the game')

enable('minecraft', config={'bridge_token': 'calagoapi:9f2c...'})


async def welcome(server, seconds):
    greeted = []
    async for line in server.streamConsole(timeout=seconds):
        match = JOIN.search(line)
        if match:
            await server.broadcast(f'Welcome, {match.group(1)}!', prefix='[Bot] ')
            greeted.append(match.group(1))
    return greeted


async def watchTps(server, seconds, interval=10):
    samples = []
    for _ in range(max(1, int(seconds // interval))):
        samples.append(await server.getTPS())
        print(f'TPS {samples[-1]}')
        await asyncio.sleep(interval)
    return samples


async def status(server) -> str:
    await server.refresh()
    ram, players = await asyncio.gather(server.getRAM(), server.getPlayerCount())
    return f'{server.name}: {await server.getStatus()}, {ram} MiB, {players} online'


async def main():
    async with AsyncPanel(url='https://panel.example.com', api_key='c7sp_...') as panel:
        server = await panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')
        print(await status(server))
        greeted, _ = await asyncio.gather(welcome(server, 600), watchTps(server, 600))
        print(f'greeted: {", ".join(greeted) or "nobody"}')

asyncio.run(main())
```

## How it works

```
asyncio event loop
├── welcome()   async for ... server.streamConsole()   ─► worker thread ─► HungerBridgePy streamLogs() ─► SSE
├── watchTps()  await server.getTPS()                   ─► worker thread ─► HungerBridgePy getTPS()     ─► HTTP
└── status()    await server.getRAM() / getStatus()     ─► worker thread ─► CalagoAPI panel client      ─► panel
```

- `calagoapi_minecraft` registers `MinecraftServer` with
  `calagoapi.aio.registerAsyncType()`. `AsyncPanel` therefore returns an
  `AsyncMinecraftServer`, whose `streamConsole()` follows HungerBridge, instead of the generic
  `AsyncServer`, which would follow the daemon.
- HungerBridgePy is a blocking client, so each bridge call and each open stream uses a
  worker thread, exactly like the rest of `AsyncPanel`. The daemon console
  (`server.console`) stays native asyncio.
- Callbacks may be coroutines: `await server.onConsoleLine(async_handler)` runs them on
  your event loop and returns the stream (`await stream.disconnect()`).
- Errors are the same as in the sync API. Catch `hungerbridge.HungerBridgeError` for bridge
  problems and `calagoapi.CalagoAPIError` for panel problems.

## Where to go from here

- Reference: [calagoapi-minecraft README](../../../src/extensions/calagoapi-minecraft/README.md),
  [HungerBridgePy](https://github.com/HungerNet/HungerBridgePy), [HungerBridge endpoints](https://github.com/HungerNet/HungerBridge/blob/main/ENDPOINTS.md).
- Build your own game extension with the pattern from [10](../extensions/10-packaging-and-publishing.md#scaling-up-a-game-extension).
