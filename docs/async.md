# Async

`AsyncPanel` is the asyncio version of `Panel`, for Discord bots, web apps
and anything else built on an event loop.

```python
import asyncio
from calagoapi import AsyncPanel

async def main():
    async with AsyncPanel(url='https://panel.example.com', api_key='...') as panel:
        server = await panel.servers.getServer('abc123')
        await server.restart()

        if await server.isOnline():
            print(await server.getStatus())

asyncio.run(main())
```

## The rule

**Everything is the same API, add `await` to method calls.**

- Every method keeps its name, arguments and docstring, so all other guides apply.
- Getters are methods too: `await server.getName()`.
- Plain attributes are read directly: `server.name`, `backup.data`, `server.server_id`.
- Returned objects (`Backup`, `File`, `Node`, ...) and lists of them are async as well.
- You can pass returned objects back as arguments: `await server.backups.deleteBackup(backup)`.

## Concurrency

Calls run in worker threads on top of the regular client, so they never
block the event loop and independent calls run at the same time:

```python
servers = await panel.servers.getServers()
statuses = await asyncio.gather(*(server.getStatus() for server in servers))

for server, status in zip(servers, statuses):
    print(server.name, status)
```

Python's default thread pool runs up to `min(32, CPU count + 4)` calls at once.

## Live console

On async servers `server.console` is an `AsyncConsole`, a native asyncio
websocket client with the same methods as the [sync console](console.md):

```python
async for line in server.streamConsole():
    print(line)

async with server.console as console:
    await console.sendCommand('save-all')
    await console.waitFor('Saved the game')
```

Callbacks can be plain functions or coroutines and run in a background task:

```python
async def relay(line):
    await channel.send(line)

await server.onConsoleLine(relay)
...
await server.console.stop()
```

## Example: Discord bot command

```python
panel = AsyncPanel(url=PANEL_URL, api_key=API_KEY)

@bot.command()
async def restart(ctx, name: str):
    server = await panel.servers.getServerByName(name)
    if server is None:
        return await ctx.send('No such server')
    await server.restart()
    await ctx.send(f'Restarting {server.name}...')
```

## Errors

Exceptions are the same as in the sync API (`NotFoundError`,
`PermissionDeniedError`, ...). Retries on rate limits work the same way.

## Closing

Use `async with AsyncPanel(...)` or call `await panel.close()` to close open
consoles and HTTP connections.

## Accessing the regular objects

Every async object has `.target`, the regular object it wraps:

```python
sync_panel = panel.target
```
