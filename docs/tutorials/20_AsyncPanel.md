# AsyncPanel

## What You Will Learn

- Use CalagoAPI from an asyncio application
- Await manager and model methods
- Run independent requests concurrently

## Prerequisites

[19 Minecraft Servers](19_Minecraft_Servers.md). Basic familiarity with
`async` and `await` in Python is helpful.

## Estimated Time

20 minutes

## Concepts Introduced

- Coroutine
- `AsyncPanel`
- `async with`
- `asyncio.gather()`

## Concept Explanation

`AsyncPanel` exposes the same object model as `Panel`. Methods are awaited;
plain attributes such as `.name` are read normally. Most synchronous requests
run in worker threads so they do not block the event loop. The live console has
a native asyncio implementation.

## API Explanation

Create `AsyncPanel` with the same connection arguments. `async with` closes
connections at exit. Returned server and resource objects are async wrappers,
so getters and actions require `await`. Use `asyncio.gather()` when independent
requests can run concurrently.

## Guided Example

```python
import asyncio
from calagoapi import AsyncPanel

async def main():
    async with AsyncPanel(url=PANEL_URL, api_key=API_KEY) as panel:
        servers = await panel.servers.getServers()
        states = await asyncio.gather(*(s.getStatus() for s in servers))
        for server, state in zip(servers, states):
            print(server.name, state)

asyncio.run(main())
```

## Exercise

Using `AsyncPanel`, get the servers and fetch their status values concurrently.
Print each server name and status.

Hint: `server.name` is an attribute; `server.getName()` is an awaitable method.

## Answer

```python
import asyncio
import os
from calagoapi import AsyncPanel

async def main():
    async with AsyncPanel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
        servers = await panel.servers.getServers()
        statuses = await asyncio.gather(*(server.getStatus() for server in servers))
        for server, status in zip(servers, statuses):
            print(server.name, status)

asyncio.run(main())
```

## Common Mistakes

- Forgetting `await` on a method, including getters.
- Adding `await` to ordinary attributes such as `.name` or `.data`.
- Using synchronous `Panel` calls directly inside an event-loop callback.
- Assuming every network activity, including console streaming, uses a worker
  thread; the console is native async.

## What You Learned

- `AsyncPanel` keeps the same managers, servers, and resource relationships.
- Methods are awaitable; attributes are not.
- Independent calls can run concurrently with `asyncio.gather()`.

## Continue Learning

Next: [21 Extensions](21_Extensions.md)

## Navigation

Previous: [19 Minecraft Servers](19_Minecraft_Servers.md)
Next: [21 Extensions](21_Extensions.md)
Reference Docs: [Async](../reference/async.md)
Related Examples: [async answer](../../examples/tutorials/20_asyncpanel/answer.py)