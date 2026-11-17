# 05 · Going async

This builds on [01–04](../README.md#track-1-the-core-sdk): the sync API.

## What you will build

A concurrent status checker that asks every server for its state at the same time, then
follows one server's console without blocking anything else. This is the shape of a
Discord bot or a web dashboard.

## Step 1: the same API, with await

```python
import asyncio
from calagoapi import AsyncPanel


async def main():
    async with AsyncPanel(url='https://panel.example.com', api_key='c7sp_...') as panel:
        server = await panel.servers.getServer('abc123')
        print(await server.getStatus())

asyncio.run(main())
```

The rule: **every method keeps its name and arguments; add `await`.** Getters are
methods too (`await server.getName()`); plain attributes are not (`server.name`).

## Step 2: many calls at once

```python
servers = await panel.servers.getServers()
statuses = await asyncio.gather(*(server.getStatus() for server in servers))
for server, status in zip(servers, statuses):
    print(f'{server.name}: {status}')
```

## Step 3: the async console

```python
async for line in server.streamConsole(timeout=30):
    print(line)
```

## Complete program

```python
import asyncio

from calagoapi import AsyncPanel


async def follow(server, seconds):
    async for line in server.streamConsole(history=False, timeout=seconds):
        print(f'[{server.name}] {line}')


async def report(panel):
    servers = await panel.servers.getServers()
    statuses = await asyncio.gather(*(server.getStatus() for server in servers))
    online = [server for server, status in zip(servers, statuses) if status == 'running']
    print(f'{len(online)} of {len(servers)} servers running')
    return online


async def main():
    async with AsyncPanel(url='https://panel.example.com', api_key='c7sp_...') as panel:
        online = await report(panel)
        if online:
            # follow the first server's console while reporting again in parallel
            await asyncio.gather(follow(online[0], seconds=20), report(panel))

asyncio.run(main())
```

## How it works

- `AsyncPanel` wraps the regular objects. Each method call runs the sync method in a
  worker thread (`asyncio.to_thread`), so the event loop never blocks and independent
  calls run concurrently. New sync methods are therefore async automatically, including
  methods added by extensions (track 2).
- Generator methods become async generators, pulled item by item in a worker thread.
- The daemon console is the exception: `AsyncConsole` is a native asyncio websocket,
  so following many consoles does not hold one thread per server.
- Extension packages tell the async layer about their own types with
  `calagoapi.aio.registerAsyncType()`. That is how `await panel.minecraft.getServer()`
  returns an async `MinecraftServer` whose console follows HungerBridge ([15](../minecraft/15-community-bot.md)).
- `obj.target` is always the wrapped sync object.

## Next

Track 2: [06 · Using extensions](../extensions/06-using-extensions.md).
