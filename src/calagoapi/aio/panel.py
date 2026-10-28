import asyncio
import functools
import inspect

from calagoapi.panel import Panel
from calagoapi.console import Console
from calagoapi.servers.generic import GenericServer
from calagoapi.utils.model import Page
from calagoapi.aio.console import AsyncConsole


def wrap(value):
    '''Wraps CalagoAPI objects returned by a call so their methods are awaitable too'''
    if isinstance(value, Page):
        return value.map(wrap)
    if isinstance(value, list):
        return [wrap(v) for v in value]
    if isinstance(value, GenericServer):
        return AsyncServer(value)
    if isinstance(value, Console):
        return AsyncConsole(value.server)
    if type(value).__module__.startswith('calagoapi.') and not isinstance(value, BaseException):
        return AsyncWrapper(value)
    return value


def unwrap(value):
    '''Turns wrapped objects passed as arguments back into the regular objects'''
    if isinstance(value, AsyncWrapper):
        return value.target
    if isinstance(value, list):
        return [unwrap(v) for v in value]
    if isinstance(value, tuple):
        return tuple(unwrap(v) for v in value)
    if isinstance(value, dict):
        return {unwrap(k): unwrap(v) for k, v in value.items()}
    return value


class AsyncWrapper:
    '''
    The async version of any CalagoAPI object.

    Every method of the wrapped object becomes a coroutine with the same name,
    arguments and docstring. Calls run in a worker thread, so many can run at
    once with asyncio.gather(). Plain attributes (like `server.name`) are read
    directly. Objects returned by a method are wrapped as well.

    Example:
        backups = await server.backups.getBackups()
        await backups[0].lock()
        print(await backups[0].getName())    # getters are awaitable too
        print(backups[0].data['name'])       # plain attributes are not
    '''
    def __init__(self, target):
        object.__setattr__(self, 'target', target)

    def __getattr__(self, name):
        value = getattr(self.target, name)
        if not inspect.ismethod(value):
            return wrap(value)

        @functools.wraps(value)
        async def method(*args, **kwargs):
            args = [unwrap(a) for a in args]
            kwargs = {k: unwrap(v) for k, v in kwargs.items()}
            return wrap(await asyncio.to_thread(value, *args, **kwargs))

        return method

    def __setattr__(self, name, value):
        setattr(self.target, name, value)

    def __getitem__(self, key):
        return self.target[key]

    def __contains__(self, key):
        return key in self.target

    def __eq__(self, other):
        return self.target == unwrap(other)

    def __hash__(self):
        return hash(self.target)

    def __repr__(self):
        return f'<async {self.target!r}>'

    def __str__(self):
        return str(self.target)

    def __dir__(self):
        return sorted(set(dir(self.target)) | set(super().__dir__()))


class AsyncServer(AsyncWrapper):
    '''
    The async version of GenericServer / MinecraftServer.

    Every server method is awaitable, and `server.console` is an AsyncConsole.

    Example:
        server = await panel.servers.getServer('abc123')
        await server.restart()
        async for line in server.streamConsole():
            print(line)
    '''
    def __init__(self, server):
        super().__init__(server)
        object.__setattr__(self, 'console', AsyncConsole(server))

    async def streamConsole(self, history: bool = True, timeout: float = None):
        '''
        Yields console lines live, as they are printed.

        Example:
            async for line in server.streamConsole(history=False):
                print(line)
        '''
        async with AsyncConsole(self.target) as console:
            async for line in console.lines(history, timeout):
                yield line

    async def onConsoleLine(self, callback, history: bool = False) -> AsyncConsole:
        '''
        Calls `callback(line)` for every console line in a background task.
        The callback may be a plain function or a coroutine.

        Example:
            await server.onConsoleLine(print)
        '''
        self.console.onConsoleLine(callback)
        return await self.console.listen(history=history)


class AsyncPanel(AsyncWrapper):
    '''
    The async version of Panel, for asyncio applications such as Discord bots.

    Takes the same arguments as Panel. Every method of every object is
    awaitable and keeps its name, so the documentation of the regular API
    applies unchanged, just add `await`.

    Requests run in worker threads on top of the regular client, so slow
    calls never block the event loop and independent calls run concurrently.
    The live console uses a native asyncio websocket.

    Example:
        import asyncio
        from calagoapi import AsyncPanel

        async def main():
            async with AsyncPanel(url='https://panel.example.com', api_key='...') as panel:
                servers = await panel.servers.getServers()
                statuses = await asyncio.gather(*(server.getStatus() for server in servers))
                for server, status in zip(servers, statuses):
                    print(server.name, status)

        asyncio.run(main())
    '''
    def __init__(self, url: str, api_key: str, name: str = None, timeout: int = 10, verify: bool = True,
                 max_retries: int = 3):
        super().__init__(Panel(url, api_key, name, timeout, verify, max_retries))

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        await self.close()

    async def close(self) -> None:
        '''Closes open consoles and the pooled HTTP connections.'''
        for console in list(self.target.consoles):
            if inspect.iscoroutinefunction(console.close):
                await console.close()
        await asyncio.to_thread(self.target.close)
