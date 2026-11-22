'''
AsyncPanel support: registers how calagoapi-minecraft objects are wrapped.

    async with AsyncPanel(url=..., api_key=...) as panel:
        server = await panel.minecraft.getServer('abc123')
        print(await server.getTPS())
        async for line in server.streamConsole(history=10):
            print(line)

HungerBridgePy is a blocking client, so bridge calls and streams run in worker
threads (one per active stream), like every other AsyncPanel call.
'''
import asyncio
import inspect

from hungerbridge import BridgeClient, Stream

from calagoapi.aio import AsyncServer, AsyncWrapper, iterateInThread, registerAsyncType, wrap

from calagoapi_minecraft.server import MinecraftServer
from calagoapi_minecraft.versions import VersionChangerAdmin, VersionManager


class AsyncMinecraftServer(AsyncServer):
    '''
    The async version of MinecraftServer. Every method is awaitable;
    streamConsole() is an async generator over HungerBridge's log stream.
    '''
    async def streamConsole(self, history: int = 0, timeout: float = None, *, reconnect: bool = None,
                            sanitize: bool = True):
        '''
        Yields HungerBridge console lines (see MinecraftServer.streamConsole()).

        Example:
            async for line in server.streamConsole(history=20):
                print(line)
        '''
        lines = await asyncio.to_thread(self.target.streamConsole, history, timeout, reconnect=reconnect,
                                        sanitize=sanitize)
        async for line in iterateInThread(lines):
            yield line

    async def onConsoleLine(self, callback, history: int = 0, *, reconnect: bool = None, sanitize: bool = True):
        '''
        Calls `callback(line)` for every console line; the callback may be a coroutine
        function, it then runs on this event loop. Returns the stream (`await stream.disconnect()`).
        '''
        loop = asyncio.get_running_loop()

        def deliver(line):
            result = callback(line)
            if inspect.isawaitable(result):
                asyncio.run_coroutine_threadsafe(result, loop)

        stream = await asyncio.to_thread(self.target.onConsoleLine, deliver, history, reconnect=reconnect,
                                         sanitize=sanitize)
        return wrap(stream)


registerAsyncType(MinecraftServer, AsyncMinecraftServer)
registerAsyncType(VersionManager, AsyncWrapper)
registerAsyncType(VersionChangerAdmin, AsyncWrapper)
registerAsyncType(BridgeClient, AsyncWrapper)
registerAsyncType(Stream, AsyncWrapper)
