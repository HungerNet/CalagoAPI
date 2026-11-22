'''MinecraftServer: the HungerBridge channel, the panel channel, and how they are kept apart.'''
import json
import threading
import time

import pytest

from calagoapi import Server
from calagoapi.extensions import ConfigurationError
from contract import UUID
from daemon import FakeDaemon
from hungerbridge import BridgeClient, Credentials, HungerBridgeAuthError

from calagoapi_minecraft import BridgeNotConfiguredError, MinecraftError, MinecraftServer
from minecraft_testing import FakeBridge, PASSKEY, PICKUP_ID, SECRET, TOKEN, TOKEN_ID, bridgeRequests, logEvent, ready


@pytest.fixture
def server(panel, network, bridge):
    return MinecraftServer(panel, UUID, data={'uuid': UUID}, bridge_url=bridge, **TOKEN)


def test_is_a_server(server):
    assert isinstance(server, Server)


def test_address(panel):
    assert MinecraftServer(panel, UUID, address='play.example.com').getAddress() == 'play.example.com:25565'
    assert MinecraftServer(panel, UUID, address='play.example.com:25570').getAddress() == 'play.example.com:25570'


def test_send_command_returns_output_and_suppresses_the_console_by_default(server, fake):
    assert server.sendCommand('list') == 'ran: list\ndone'
    assert bridgeRequests('POST', '/server/run')[-1][2] == {'command': 'list', 'show_console': False}
    server.sendCommand('say hi', show_console=True)
    assert bridgeRequests('POST', '/server/run')[-1][2]['show_console'] is True
    assert server.sendCommands(['a', 'b']) == ['ran: a\ndone', 'ran: b\ndone']
    with pytest.raises(TypeError):
        server.sendCommand('x', silent=True)          # removed
    # nothing went to the panel's command endpoint
    assert ('POST', '/api/client/servers/{server}/command') not in fake.hit


def test_panel_channel_stays_calagoapi(server, fake):
    server.sendPanelCommand('list')
    assert ('POST', '/api/client/servers/{server}/command') in fake.hit
    assert server.getRAM() is not None and server.getCPU() is not None
    server.stop()
    assert ('POST', '/api/client/servers/{server}/power') in fake.hit
    assert not bridgeRequests('POST', '/server/stop')
    assert not fake.violations


def test_chat_and_moderation_helpers(server):
    assert server.say('hello') == 'ran: say hello\ndone'
    server.tellraw('@a', {'text': 'hé', 'color': 'gold'})
    assert bridgeRequests('POST', '/server/run')[-1][2]['command'] == 'tellraw @a {"text": "hé", "color": "gold"}'
    for call, expected in [(lambda: server.kick('Steve', 'AFK'), 'kick Steve AFK'), (lambda: server.ban('X'), 'ban X'),
                           (lambda: server.pardon('X'), 'pardon X'), (lambda: server.op('A'), 'op A'),
                           (lambda: server.deop('A'), 'deop A'), (lambda: server.whitelistAdd('S'), 'whitelist add S'),
                           (lambda: server.whitelistRemove('S'), 'whitelist remove S'), (server.saveAll, 'save-all')]:
        call()
        assert bridgeRequests('POST', '/server/run')[-1][2]['command'] == expected


def test_bridge_api_is_hungerbridgepy(server):
    # One name per concept: everything inside the game is server.bridge (HungerBridgePy).
    assert isinstance(server.bridge, BridgeClient) and server.bridge is server.bridge
    assert server.bridge.getPlayers() == ['Steve', 'Alex'] and server.bridge.getTPS('15m') == 19.7
    assert server.bridge.getServerMeta()['protocol_version'] == 2
    assert server.bridge.log('hello', level='BOT', thread='calagoapi', logger='Backups') == 'hello'
    assert bridgeRequests('POST', '/server/log')[-1][2] == {'level': 'BOT', 'message': 'hello', 'thread': 'calagoapi',
                                                          'logger': 'Backups', 'normalize': False}
    for removed in ('getTPS', 'getPlayers', 'getMemoryInfo', 'writeLog', 'getBridgeInfo', 'broadcast', 'getPerformance',
                    'findBridgeRelease', 'versions'):
        assert not hasattr(MinecraftServer, removed), removed


def test_stream_console_yields_canonical_lines(server):
    lines = list(server.streamConsole(history=2, timeout=5, reconnect=False))
    assert lines == ['[12:00:00] [Server thread/INFO]: history 0', '[12:00:01] [Server thread/INFO]: history 1',
                     '[12:00:10] [Server thread/INFO]: Steve joined the game',
                     '[12:00:11] [Server thread/WARN]: [SomePlugin] line one\nline two']
    assert bridgeRequests('GET', '/server/stream')[-1][3] == 'history=2'
    list(server.streamConsole(timeout=5, reconnect=False))
    assert bridgeRequests('GET', '/server/stream')[-1][3] == ''
    list(server.streamConsole(history=True, timeout=5, reconnect=False))
    assert bridgeRequests('GET', '/server/stream')[-1][3] == 'history=all'


def test_stream_console_stops_on_timeout(server):
    release = threading.Event()

    def quiet(handler, history):
        handler.sse(ready(0) + logEvent(1, 'only line'))
        release.wait(10)

    FakeBridge.stream_script = quiet
    start = time.monotonic()
    assert list(server.streamConsole(timeout=0.5)) == ['[12:00:01] [Server thread/INFO]: only line']
    assert time.monotonic() - start < 4
    release.set()


def test_on_console_line(server):
    lines = []
    stream = server.onConsoleLine(lines.append, history=1, reconnect=False)
    deadline = time.monotonic() + 5
    while len(lines) < 3 and time.monotonic() < deadline:
        time.sleep(0.02)
    stream.disconnect()
    assert lines == ['[12:00:00] [Server thread/INFO]: history 0', '[12:00:10] [Server thread/INFO]: Steve joined the game',
                     '[12:00:11] [Server thread/WARN]: [SomePlugin] line one\nline two']


def test_bridge_errors_are_hungerbridge_errors(panel, network, bridge):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID}, bridge_url=bridge, bridge_token_id=TOKEN_ID,
                             bridge_token_secret='00' * 32)
    with pytest.raises(HungerBridgeAuthError) as error:
        server.sendCommand('list')
    assert error.value.reason == 'invalid_credentials'
    with pytest.raises(HungerBridgeAuthError):
        list(server.streamConsole(timeout=5))
    assert not server.isBridgeReachable()
    assert not server.waitForBridge(timeout=0.1, interval=0.05)


def test_not_configured_and_invalid_credentials(panel, network):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID})
    assert not server.hasBridge() and not server.isBridgeReachable()
    with pytest.raises(BridgeNotConfiguredError, match='createBridgeToken'):
        server.sendCommand('list')
    with pytest.raises(BridgeNotConfiguredError):
        server.streamConsole()           # fails on the call, not on the first line
    with pytest.raises(ConfigurationError, match='both'):
        MinecraftServer(panel, UUID, bridge_token_id='bot')
    with pytest.raises(ConfigurationError, match='64 hex'):
        MinecraftServer(panel, UUID, bridge_token_id='bot', bridge_token_secret='not-hex')
    with pytest.raises(TypeError):
        MinecraftServer(panel, UUID, bridge_token=f'bot:{SECRET}')     # the combined form is gone


def test_connect_and_set_bridge(panel, network, bridge):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID}, address='play.example.com')
    assert server.getBridgeUrl() == 'http://play.example.com:1913'
    client = server.connectBridge(f'{bridge}/', token_id=TOKEN_ID, token_secret=SECRET)
    assert server.getBridgeUrl() == bridge and client.base == bridge
    assert server.hasBridge() and server.isBridgeReachable() and server.waitForBridge(timeout=1)
    other = server.connectBridge(timeout=(1, 2))
    assert other is not client and other.transport.timeout == (1, 2)
    with pytest.raises(ConfigurationError, match='both'):
        server.connectBridge(token_id='only-id')
    custom = BridgeClient(bridge, token_id=TOKEN_ID, token_secret=SECRET)
    assert server.setBridge(custom).bridge is custom
    server.closeBridge()
    assert server.bridge is not custom


def test_redeem_pickup(panel, network, bridge):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID}, bridge_url=bridge)
    client = server.redeemBridgePickup(f'/pickup/{PICKUP_ID}?passkey={PASSKEY}')
    assert client.credentials.token_id == 'calagoapi' and server.bridge.getPlayerCount() == 2


class PickupDaemon(FakeDaemon):
    '''Answers "hb token create" like HungerBridge 5's console command'''
    def handle(self, ws):
        for raw in ws:
            message = json.loads(raw)
            self.received.append(message)
            event, args = message['event'], message.get('args') or []
            if event == 'auth':
                self.send(ws, 'auth success', 'control.console')
            elif event == 'send command':
                self.send(ws, 'console output', f'> {args[0]}')
                if args[0].startswith('hb token create'):
                    self.send(ws, 'console output', '\x1b[36;1mHungerBridge\x1b[0m » Token created')
                    self.send(ws, 'console output', '  ✔ calagoapi uses policy admin')
                    self.send(ws, 'console output', f'  • Pickup URL  \x1b[96m/pickup/{PICKUP_ID}?passkey={PASSKEY}\x1b[0m')


def test_create_bridge_token_through_the_console(panel, network, bridge):
    daemon = PickupDaemon()
    try:
        panel.api.servers.websocket = lambda server_id: {'token': 'ws-token', 'url': daemon.url}
        server = MinecraftServer(panel, UUID, data={'uuid': UUID})
        token = server.createBridgeToken('calagoapi', 'admin', expiry=3600, url=bridge)
        assert token == Credentials(token_id='calagoapi', token_secret=SECRET)
        assert {'event': 'send command', 'args': ['hb token create calagoapi admin 3600']} in daemon.received
        assert server.bridge.getPlayers() == ['Steve', 'Alex']
    finally:
        daemon.stop()


def test_create_bridge_token_times_out(panel, network):
    daemon = FakeDaemon(expire_first_token=False)   # echoes commands, never prints a pickup
    try:
        panel.api.servers.websocket = lambda server_id: {'token': 'ws-token', 'url': daemon.url}
        server = MinecraftServer(panel, UUID, data={'uuid': UUID}, bridge_url='http://127.0.0.1:9')
        with pytest.raises(MinecraftError, match='No HungerBridge pickup URL'):
            server.createBridgeToken(timeout=0.5)
    finally:
        daemon.stop()


def test_properties_and_eula(server, monkeypatch):
    files = {'/server.properties': '# comment\nmotd=Old\nmax-players=20\n'}
    monkeypatch.setattr(server.files, 'readFile', lambda path: files[path])
    monkeypatch.setattr(server.files, 'writeFile', lambda path, content: files.__setitem__(path, content))
    assert server.getProperties() == {'motd': 'Old', 'max-players': '20'}
    server.setProperties({'motd': 'New', 'pvp': False})
    assert files['/server.properties'] == '# comment\nmotd=New\nmax-players=20\npvp=false\n'
    assert server.getMOTD() == 'New' and server.getProperty('missing', 'x') == 'x'
    server.setMOTD('Hi')
    assert server.getProperty('motd') == 'Hi'
    files['/eula.txt'] = 'eula=false\n'
    assert not server.isEulaAccepted()
    server.acceptEula()
    assert server.isEulaAccepted()
