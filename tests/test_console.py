'''Live console tests against a local fake daemon.'''
import asyncio
import time

import pytest

from calagoapi import AsyncPanel, Console, ConsoleError, InvalidActionError, WaitTimeoutError
from contract import BASE, UUID
from daemon import FakeDaemon


@pytest.fixture
def daemon():
    daemon = FakeDaemon()
    yield daemon
    daemon.stop()


def pointAt(panel, daemon, tokens=None):
    '''Makes the panel hand out credentials for the fake daemon'''
    issued = iter(tokens or [f'token-{i}' for i in range(1, 100)])
    panel.api.servers.websocket = lambda server_id: {'token': next(issued), 'url': daemon.url}


@pytest.fixture
def server(panel, daemon):
    pointAt(panel, daemon)
    return panel.servers.getServer(UUID)


def waitUntil(check, timeout=5):
    deadline = time.monotonic() + timeout
    while not check():
        if time.monotonic() > deadline:
            raise AssertionError('condition not met in time')
        time.sleep(0.02)


def test_stream_history_and_commands(server):
    with server.console as console:
        assert console.isConnected()
        assert 'control.console' in console.getPermissions()
        console.sendCommand('list')
        assert console.waitFor('> list', timeout=5) == '> list'

    lines = []
    for line in server.streamConsole(history=True, timeout=2):
        lines.append(line)
        if len(lines) == 2:
            break
    assert lines == ['line 1', 'line 2']


def test_token_is_renewed(server, daemon):
    with server.console as console:
        console.sendCommand('ping')
        console.waitFor('> ping', timeout=5)
    # the daemon sent "token expiring" after the first auth
    assert daemon.tokens == ['token-1', 'token-2']


def test_callbacks_in_background(server):
    lines, states, stats = [], [], []
    console = server.onConsoleLine(lines.append)
    console.onStatus(states.append)
    console.onStats(stats.append)

    console.sendCommand('say hi')
    console.requestStats()
    console.setState('restart')
    waitUntil(lambda: '> say hi' in lines and stats and 'starting' in states)
    assert stats[0]['cpu_absolute'] == 12.5

    console.stop()
    assert not console.isConnected() and not console.running


def test_reconnects_after_disconnect(server, daemon):
    console = server.console
    lines = []
    console.onConsoleLine(lines.append)
    console.listen()
    dropped = console.socket
    dropped.close()  # simulate the daemon dropping the connection
    waitUntil(lambda: console.socket is not None and console.socket is not dropped, timeout=10)
    console.sendCommand('back')
    waitUntil(lambda: '> back' in lines)
    console.stop()


def test_bad_token_raises(panel, daemon):
    pointAt(panel, daemon, tokens=['bad-token'])
    server = panel.servers.getServer(UUID)
    with pytest.raises(ConsoleError):
        server.console.connect(timeout=3)


def test_unreachable_daemon_raises(panel):
    panel.api.servers.websocket = lambda server_id: {'token': 't', 'url': 'ws://127.0.0.1:9/ws'}
    with pytest.raises(ConsoleError):
        Console(panel.servers.getServer(UUID)).connect(timeout=2)


def test_wait_for_times_out(server):
    with server.console as console:
        with pytest.raises(WaitTimeoutError):
            console.waitFor('never printed', timeout=0.5)


def test_invalid_power_action(server):
    with server.console as console:
        with pytest.raises(InvalidActionError):
            console.setState('explode')


def test_panel_close_closes_consoles(server):
    server.console.connect()
    server.panel.close()
    assert not server.console.isConnected()


def test_async_console(fake, daemon):
    async def main():
        async with AsyncPanel(url=BASE, api_key='c7sp_test') as panel:
            pointAt(panel.target, daemon)
            server = await panel.servers.getServer(UUID)

            async with server.console as console:
                await console.sendCommand('list')
                assert await console.waitFor('> list', timeout=5) == '> list'

            lines = []
            async for line in server.streamConsole(history=True, timeout=2):
                lines.append(line)
                if len(lines) == 2:
                    break
            assert lines == ['line 1', 'line 2']

            received = []

            async def collect(line):
                received.append(line)

            console = await server.onConsoleLine(collect)
            await console.sendCommand('async')
            for _ in range(250):
                if '> async' in received:
                    break
                await asyncio.sleep(0.02)
            assert '> async' in received
        # leaving the block closed the console
        assert not console.isConnected()

    fake.reset()
    asyncio.run(main())
