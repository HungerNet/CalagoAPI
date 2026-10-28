import asyncio
import inspect
import time

from websockets.asyncio.client import connect
from websockets.exceptions import ConnectionClosed, WebSocketException

from calagoapi.console.console import (
    ConsoleEvent,
    socketUrl,
    sslContext,
    encode,
    decode,
    logger,
    POWER_ACTIONS,
    TOKEN_EVENTS,
    ERROR_EVENTS,
)
from calagoapi.utils.exceptions import CalagoAPIError, ConsoleError, InvalidActionError, WaitTimeoutError


class AsyncConsole:
    '''
    The live console of a server for asyncio code, available as `server.console`
    on servers from AsyncPanel.

    Same methods as Console, but awaitable. Callbacks may be plain functions
    or coroutines.

    Example:
        async with server.console as console:
            await console.sendCommand('list')
            async for line in console.lines():
                print(line)

        server.console.onConsoleLine(print)
        await server.console.listen()
        ...
        await server.console.stop()

    Args:
        server: The (regular) GenericServer whose console to open.
    '''
    def __init__(self, server):
        self.server = server
        self.socket = None
        self.permissions = []
        self.handlers = {}
        self.running = False
        self.task = None

    def __repr__(self):
        state = 'connected' if self.isConnected() else 'closed'
        return f'<AsyncConsole {self.server.name!r} {state}>'

    async def __aenter__(self):
        return await self.connect()

    async def __aexit__(self, *exc):
        await self.stop()

    # connection
    async def connect(self, timeout: int = 10) -> 'AsyncConsole':
        '''
        Opens the websocket and authenticates. Does nothing if already connected.

        Raises:
            ConsoleError: The daemon could not be reached or refused the token.
        '''
        if self.socket:
            return self
        credentials = await asyncio.to_thread(self.server.getWebsocket)
        url = socketUrl(credentials['url'])
        try:
            self.socket = await connect(
                url,
                origin=self.server.panel.url,
                ssl=sslContext(url, self.server.panel.client.session.verify),
                open_timeout=timeout,
                user_agent_header='CalagoAPI',
            )
        except (OSError, WebSocketException, asyncio.TimeoutError) as e:
            raise ConsoleError(f'Could not connect to the console of {self.server.name}: {e}') from e
        self.server.panel.consoles.add(self)

        await self._send('auth', credentials['token'])
        deadline = time.monotonic() + timeout
        while True:
            event = await self._receive(max(deadline - time.monotonic(), 0.01))
            if event is None:
                await self.close()
                raise ConsoleError(f'The console of {self.server.name} did not confirm authentication')
            if event.getEvent() == 'auth success':
                self.permissions = event.getArgs()
                return self
            if event.getEvent() in ERROR_EVENTS:
                await self.close()
                raise ConsoleError(f'Console authentication failed: {event.getArg()}')

    async def close(self) -> None:
        '''Closes the websocket. Use stop() to also end a running listen().'''
        socket, self.socket = self.socket, None
        self.server.panel.consoles.discard(self)
        if socket:
            await socket.close()

    def isConnected(self) -> bool:
        '''Returns True while the websocket is open.'''
        return self.socket is not None

    def getPermissions(self) -> list:
        '''Returns the console permissions the daemon granted.'''
        return self.permissions

    # sending
    async def _send(self, event, *args):
        if not self.socket:
            raise ConsoleError('The console is not connected, call connect() first')
        try:
            await self.socket.send(encode(event, *args))
        except ConnectionClosed as e:
            self.socket = None
            raise ConsoleError(f'The console connection was closed: {e}') from e

    async def sendCommand(self, command: str) -> None:
        '''Sends a console command over the websocket.'''
        await self._send('send command', command)

    async def setState(self, action: str) -> None:
        '''Sends a power action: start, restart, stop or kill.'''
        if action not in POWER_ACTIONS:
            raise InvalidActionError(f'Invalid power action "{action}", expected one of: {", ".join(POWER_ACTIONS)}')
        await self._send('set state', action)

    async def requestLogs(self) -> None:
        '''Asks the daemon to resend recent console lines.'''
        await self._send('send logs')

    async def requestStats(self) -> None:
        '''Asks the daemon for resource usage now.'''
        await self._send('send stats')

    async def requestStatus(self) -> None:
        '''Asks the daemon for the power state now.'''
        await self._send('send status')

    # receiving
    async def _receive(self, timeout=None):
        if not self.socket:
            return None
        try:
            raw = await asyncio.wait_for(self.socket.recv(), timeout)
        except asyncio.TimeoutError:
            return None
        except ConnectionClosed:
            await self.close()
            return None
        return decode(raw) or ConsoleEvent('unknown')

    async def _renewToken(self):
        credentials = await asyncio.to_thread(self.server.getWebsocket)
        await self._send('auth', credentials['token'])

    async def events(self, timeout: float = None):
        '''
        Yields every event from the daemon until the connection closes.

        Args:
            timeout: Stop when no event arrives for this many seconds. None waits forever.
        '''
        while self.socket:
            event = await self._receive(timeout)
            if event is None:
                return
            if event.getEvent() in TOKEN_EVENTS:
                await self._renewToken()
                continue
            yield event

    async def lines(self, history: bool = True, timeout: float = None):
        '''
        Yields console lines as they are printed.

        Example:
            async for line in console.lines(history=False):
                print(line)
        '''
        await self.connect()
        if history:
            await self.requestLogs()
        async for event in self.events(timeout):
            if event.getEvent() == 'console output':
                yield event.getArg(0, '')

    async def waitFor(self, text: str, timeout: float = 60) -> str:
        '''
        Waits until a console line contains `text` and returns that line.

        Raises:
            WaitTimeoutError: No matching line within `timeout` seconds.
        '''
        await self.connect()
        deadline = time.monotonic() + timeout
        while True:
            remaining = deadline - time.monotonic()
            event = await self._receive(remaining) if remaining > 0 else None
            if event is None:
                raise WaitTimeoutError(f'No console line containing {text!r} within {timeout}s')
            if event.getEvent() in TOKEN_EVENTS:
                await self._renewToken()
            elif event.getEvent() == 'console output' and text in event.getArg(0, ''):
                return event.getArg()

    # callbacks
    def on(self, event: str, callback) -> 'AsyncConsole':
        '''Calls `callback(ConsoleEvent)` for an event while listen() runs. Use '*' for every event.'''
        self.handlers.setdefault(event, []).append(callback)
        return self

    def onConsoleLine(self, callback) -> 'AsyncConsole':
        '''Calls `callback(line)` for every console line.'''
        return self.on('console output', lambda event: callback(event.getArg(0, '')))

    def onStatus(self, callback) -> 'AsyncConsole':
        '''Calls `callback(state)` when the power state changes.'''
        return self.on('status', lambda event: callback(event.getArg()))

    def onStats(self, callback) -> 'AsyncConsole':
        '''Calls `callback(resources)` with a resource usage dict.'''
        return self.on('stats', lambda event: callback(event.getData()))

    async def _dispatch(self, event):
        for callback in self.handlers.get(event.getEvent(), []) + self.handlers.get('*', []):
            try:
                result = callback(event)
                if inspect.isawaitable(result):
                    await result
            except Exception:
                logger.exception('console callback for %r failed', event.getEvent())

    async def listen(self, background: bool = True, history: bool = False, reconnect: bool = True) -> 'AsyncConsole':
        '''
        Delivers events to the registered callbacks.

        Args:
            background: Run as an asyncio task and return immediately. False waits until stop().
            history: Replay recent console lines first.
            reconnect: Reconnect automatically (with backoff) if the connection drops.
        '''
        if self.running:
            return self
        await self.connect()
        self.running = True
        if background:
            self.task = asyncio.create_task(self._loop(history, reconnect))
        else:
            await self._loop(history, reconnect)
        return self

    async def _loop(self, history, reconnect):
        delay = 1
        while self.running:
            try:
                await self.connect()
                delay = 1
                if history:
                    await self.requestLogs()
                    history = False
                async for event in self.events():
                    await self._dispatch(event)
            except CalagoAPIError as e:
                logger.warning('console of %s disconnected: %s', self.server.name, e)
            if not self.running or not reconnect:
                break
            await asyncio.sleep(delay)
            delay = min(delay * 2, 30)
        self.running = False

    async def stop(self) -> None:
        '''Stops listen() and closes the connection.'''
        self.running = False
        await self.close()
        task, self.task = self.task, None
        if task and task is not asyncio.current_task():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
