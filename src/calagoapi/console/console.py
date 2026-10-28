import json
import logging
import ssl
import threading
import time

from websockets.sync.client import connect
from websockets.exceptions import ConnectionClosed, WebSocketException

from calagoapi.utils.exceptions import CalagoAPIError, ConsoleError, InvalidActionError, WaitTimeoutError


logger = logging.getLogger('calagoapi.console')

POWER_ACTIONS = ('start', 'restart', 'stop', 'kill')
TOKEN_EVENTS = ('token expiring', 'token expired')
ERROR_EVENTS = ('jwt error', 'daemon error')


class ConsoleEvent:
    '''
    One message from the server's live websocket.

    Common events: 'console output', 'status', 'stats', 'install output',
    'backup completed', 'daemon message', 'schedule completed'.

    Example:
        for event in console.events():
            if event.getEvent() == 'status':
                print('now', event.getArg())
    '''
    def __init__(self, event: str, args: list = None):
        self.event = event
        self.args = args or []

    def __repr__(self):
        return f'<ConsoleEvent {self.event!r} {self.args!r}>'[:200]

    def getEvent(self) -> str:
        '''Returns the event name, e.g. "console output".'''
        return self.event

    def getArgs(self) -> list:
        '''Returns every argument (always strings).'''
        return self.args

    def getArg(self, index: int = 0, default=None) -> str:
        '''Returns one argument, e.g. the console line or the new status.'''
        return self.args[index] if index < len(self.args) else default

    def getData(self, index: int = 0):
        '''Returns an argument decoded from JSON, e.g. the resource usage of a "stats" event.'''
        value = self.getArg(index)
        try:
            return json.loads(value)
        except (TypeError, ValueError):
            return value


# helpers shared with the async console
def socketUrl(url: str) -> str:
    if url.startswith('https://'):
        return 'wss://' + url[len('https://'):]
    if url.startswith('http://'):
        return 'ws://' + url[len('http://'):]
    return url


def sslContext(url: str, verify: bool):
    if not url.startswith('wss://') or verify:
        return None
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    return context


def encode(event: str, *args) -> str:
    return json.dumps({'event': event, 'args': [str(a) for a in args]})


def decode(raw) -> ConsoleEvent:
    if isinstance(raw, bytes):
        # binary (MessagePack) mode is never requested by CalagoAPI
        return None
    try:
        message = json.loads(raw)
    except ValueError:
        return None
    return ConsoleEvent(message.get('event'), [a for a in message.get('args') or [] if a is not None])


class Console:
    '''
    The live console of a server, available as `server.console`.

    Connects straight to the node daemon over a websocket, so console output
    arrives the moment it is printed. Expiring tokens are renewed automatically.

    Three ways to use it:

    1. Iterate lines:

        with server.console as console:
            console.sendCommand('list')
            for line in console.lines():
                print(line)

    2. Wait for something:

        with server.console as console:
            console.sendCommand('save-all')
            console.waitFor('Saved the game', timeout=30)

    3. Callbacks in a background thread:

        server.console.onConsoleLine(print)
        server.console.onStatus(lambda state: print('status:', state))
        server.console.listen()
        ...
        server.console.stop()

    Args:
        server: The server whose console to open.
    '''
    def __init__(self, server):
        self.server = server
        self.socket = None
        self.permissions = []
        self.handlers = {}
        self.running = False
        self.thread = None

    def __repr__(self):
        state = 'connected' if self.isConnected() else 'closed'
        return f'<Console {self.server.name!r} {state}>'

    def __enter__(self):
        return self.connect()

    def __exit__(self, *exc):
        self.stop()

    # connection
    def connect(self, timeout: int = 10) -> 'Console':
        '''
        Opens the websocket and authenticates. Does nothing if already connected.

        Raises:
            ConsoleError: The daemon could not be reached or refused the token.
        '''
        if self.socket:
            return self
        credentials = self.server.getWebsocket()
        url = socketUrl(credentials['url'])
        try:
            # entering the connection marks it as managed (websockets 17+ warns otherwise),
            # close() exits it
            self.socket = connect(
                url,
                origin=self.server.panel.url,
                ssl=sslContext(url, self.server.panel.client.session.verify),
                open_timeout=timeout,
                user_agent_header='CalagoAPI',
            ).__enter__()
        except (OSError, WebSocketException) as e:
            raise ConsoleError(f'Could not connect to the console of {self.server.name}: {e}') from e
        self.server.panel.consoles.add(self)

        self._send('auth', credentials['token'])
        deadline = time.monotonic() + timeout
        while True:
            event = self._receive(max(deadline - time.monotonic(), 0.01))
            if event is None:
                self.close()
                raise ConsoleError(f'The console of {self.server.name} did not confirm authentication')
            if event.getEvent() == 'auth success':
                self.permissions = event.getArgs()
                return self
            if event.getEvent() in ERROR_EVENTS:
                self.close()
                raise ConsoleError(f'Console authentication failed: {event.getArg()}')

    def close(self) -> None:
        '''Closes the websocket. Use stop() to also end a running listen().'''
        socket, self.socket = self.socket, None
        self.server.panel.consoles.discard(self)
        if socket:
            socket.close()

    def isConnected(self) -> bool:
        '''Returns True while the websocket is open.'''
        return self.socket is not None

    def getPermissions(self) -> list:
        '''Returns the console permissions the daemon granted, e.g. ["control.console", ...].'''
        return self.permissions

    # sending
    def _send(self, event, *args):
        if not self.socket:
            raise ConsoleError('The console is not connected, call connect() first')
        try:
            self.socket.send(encode(event, *args))
        except ConnectionClosed as e:
            self.socket = None
            raise ConsoleError(f'The console connection was closed: {e}') from e

    def sendCommand(self, command: str) -> None:
        '''
        Sends a console command over the websocket.

        Example:
            console.sendCommand('say Hello')
        '''
        self._send('send command', command)

    def setState(self, action: str) -> None:
        '''Sends a power action: start, restart, stop or kill.'''
        if action not in POWER_ACTIONS:
            raise InvalidActionError(f'Invalid power action "{action}", expected one of: {", ".join(POWER_ACTIONS)}')
        self._send('set state', action)

    def requestLogs(self) -> None:
        '''Asks the daemon to resend recent console lines (they arrive as "console output").'''
        self._send('send logs')

    def requestStats(self) -> None:
        '''Asks the daemon for resource usage now (arrives as a "stats" event).'''
        self._send('send stats')

    def requestStatus(self) -> None:
        '''Asks the daemon for the power state now (arrives as a "status" event).'''
        self._send('send status')

    # receiving
    def _receive(self, timeout=None):
        if not self.socket:
            return None
        try:
            return decode(self.socket.recv(timeout=timeout)) or ConsoleEvent('unknown')
        except TimeoutError:
            return None
        except ConnectionClosed:
            self.close()
            return None

    def _renewToken(self):
        self._send('auth', self.server.getWebsocket()['token'])

    def events(self, timeout: float = None):
        '''
        Yields every event from the daemon until the connection closes.

        Args:
            timeout: Stop when no event arrives for this many seconds. None waits forever.

        Example:
            for event in console.events():
                print(event.getEvent(), event.getArgs())
        '''
        while self.socket:
            event = self._receive(timeout)
            if event is None:
                return
            if event.getEvent() in TOKEN_EVENTS:
                self._renewToken()
                continue
            yield event

    def lines(self, history: bool = True, timeout: float = None):
        '''
        Yields console lines as they are printed.

        Args:
            history: Start with the recent lines the daemon still has.
            timeout: Stop when nothing arrives for this many seconds. None waits forever.

        Example:
            for line in console.lines(history=False):
                if 'joined the game' in line:
                    print(line)
        '''
        self.connect()
        if history:
            self.requestLogs()
        for event in self.events(timeout):
            if event.getEvent() == 'console output':
                yield event.getArg(0, '')

    def waitFor(self, text: str, timeout: float = 60) -> str:
        '''
        Blocks until a console line contains `text` and returns that line.

        Raises:
            WaitTimeoutError: No matching line within `timeout` seconds.

        Example:
            console.sendCommand('save-all')
            console.waitFor('Saved the game')
        '''
        self.connect()
        deadline = time.monotonic() + timeout
        while True:
            remaining = deadline - time.monotonic()
            event = self._receive(remaining) if remaining > 0 else None
            if event is None:
                raise WaitTimeoutError(f'No console line containing {text!r} within {timeout}s')
            if event.getEvent() in TOKEN_EVENTS:
                self._renewToken()
            elif event.getEvent() == 'console output' and text in event.getArg(0, ''):
                return event.getArg()

    # callbacks
    def on(self, event: str, callback) -> 'Console':
        '''
        Calls `callback(ConsoleEvent)` for an event while listen() runs. Use '*' for every event.

        Example:
            console.on('backup completed', lambda e: print('backup done', e.getArgs()))
        '''
        self.handlers.setdefault(event, []).append(callback)
        return self

    def onConsoleLine(self, callback) -> 'Console':
        '''Calls `callback(line)` for every console line.'''
        return self.on('console output', lambda event: callback(event.getArg(0, '')))

    def onStatus(self, callback) -> 'Console':
        '''Calls `callback(state)` when the power state changes ('running', 'offline', ...).'''
        return self.on('status', lambda event: callback(event.getArg()))

    def onStats(self, callback) -> 'Console':
        '''Calls `callback(resources)` with a resource usage dict, sent every few seconds while running.'''
        return self.on('stats', lambda event: callback(event.getData()))

    def _dispatch(self, event):
        for callback in self.handlers.get(event.getEvent(), []) + self.handlers.get('*', []):
            try:
                callback(event)
            except Exception:
                logger.exception('console callback for %r failed', event.getEvent())

    def listen(self, background: bool = True, history: bool = False, reconnect: bool = True) -> 'Console':
        '''
        Delivers events to the registered callbacks.

        Args:
            background: Run in a daemon thread and return immediately. False blocks until stop().
            history: Replay recent console lines first.
            reconnect: Reconnect automatically (with backoff) if the connection drops.

        Raises:
            ConsoleError: The first connection failed.
        '''
        if self.running:
            return self
        self.connect()
        self.running = True
        if background:
            self.thread = threading.Thread(target=self._loop, args=(history, reconnect), name=f'calagoapi-console-{self.server.server_id}', daemon=True)
            self.thread.start()
        else:
            self._loop(history, reconnect)
        return self

    def _loop(self, history, reconnect):
        delay = 1
        while self.running:
            try:
                self.connect()
                delay = 1
                if history:
                    self.requestLogs()
                    history = False
                for event in self.events():
                    self._dispatch(event)
            except CalagoAPIError as e:
                logger.warning('console of %s disconnected: %s', self.server.name, e)
            if not self.running or not reconnect:
                break
            time.sleep(delay)
            delay = min(delay * 2, 30)
        self.running = False

    def stop(self) -> None:
        '''Stops listen() and closes the connection.'''
        self.running = False
        self.close()
        if self.thread and self.thread is not threading.current_thread():
            self.thread.join(timeout=5)
        self.thread = None
