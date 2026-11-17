'''MinecraftServer: the HungerBridge channel, the panel channel, and how they are kept apart.'''
import json
import threading
import time

import pytest

from calagoapi import Server
from calagoapi.extensions import ConfigurationError
from contract import UUID
from daemon import FakeDaemon
from hungerbridge import BridgeClient, HungerBridgeAuthError, MAX_HISTORY

from calagoapi_minecraft import BridgeNotConfiguredError, MinecraftError, MinecraftServer
from minecraft_testing import FakeBridge, PASSKEY, PICKUP_ID, SECRET, TOKEN, bridgeRequests


@pytest.fixture
def server(panel, network, bridge):
    return MinecraftServer(panel, UUID, data={'uuid': UUID}, bridge_url=bridge, bridge_token=TOKEN)


def test_is_a_server(server):
    assert isinstance(server, Server)
    assert server.versions.server is server


def test_address(panel):
    assert MinecraftServer(panel, UUID, address='play.example.com').getAddress() == 'play.example.com:25565'
    assert MinecraftServer(panel, UUID, address='play.example.com:25570').getAddress() == 'play.example.com:25570'


def test_send_command_returns_output_through_the_bridge(server, fake):
    assert server.sendCommand('list') == 'ran: list\ndone'
    assert server.sendCommand('save-all', silent=True) is None
    assert bridgeRequests('POST', '/server/run')[-1][2] == {'command': 'save-all', 'silent': True, 'show_console': False}
    server.sendCommand('say hi', showConsole=True)
    assert bridgeRequests('POST', '/server/run')[-1][2]['show_console'] is True
    assert server.sendCommands(['a', 'b']) == ['ran: a\ndone', 'ran: b\ndone']
    # nothing went to the panel's command endpoint
    assert ('POST', '/api/client/servers/{server}/command') not in fake.hit


def test_panel_channel_stays_calagoapi(server, fake):
    server.sendPanelCommand('list')
    assert ('POST', '/api/client/servers/{server}/command') in fake.hit
    # getRAM/getCPU/stop are the panel's, never the bridge's
    assert server.getRAM() is not None and server.getCPU() is not None
    assert ('GET', '/api/client/servers/{server}/resources') in fake.hit
    server.stop()
    assert ('POST', '/api/client/servers/{server}/power') in fake.hit
    assert not bridgeRequests('POST', '/server/stop')
    assert not fake.violations


def test_chat_helpers(server):
    assert server.say('hello') == 'ran: say hello\ndone'
    server.tellraw('@a', {'text': 'hé', 'color': 'gold'})
    assert bridgeRequests('POST', '/server/run')[-1][2]['command'] == 'tellraw @a {"text": "hé", "color": "gold"}'
    server.broadcast('event', prefix='[E] ')
    command = bridgeRequests('POST', '/server/run')[-1][2]['command']
    assert command.startswith('tellraw @a ') and json.loads(command[len('tellraw @a '):]) == {'text': '[E] event'}
    for call, expected in [(lambda: server.kick('Steve', 'AFK'), 'kick Steve AFK'), (lambda: server.ban('X'), 'ban X'),
                           (lambda: server.pardon('X'), 'pardon X'), (lambda: server.op('A'), 'op A'),
                           (lambda: server.deop('A'), 'deop A'), (lambda: server.whitelistAdd('S'), 'whitelist add S'),
                           (lambda: server.whitelistRemove('S'), 'whitelist remove S'), (server.saveAll, 'save-all')]:
        call()
        assert bridgeRequests('POST', '/server/run')[-1][2]['command'] == expected


def test_players_and_performance(server):
    assert server.getPlayers() == ['Steve', 'Alex']
    assert server.getPlayerCount() == 2 and server.getMaxPlayers() == 20
    assert server.getTPS() == 20.0 and server.getTPS('15m') == 19.7
    assert server.getMSPT() == 12.5
    assert server.getPerformance() == {'tps': {'current': 20.0, '1m': 19.9, '5m': 19.8, '15m': 19.7}, 'mspt': 12.5,
                                       'players': 2, 'max_players': 20}
    assert server.getWorldTime() == 6000 and server.getWorldTimeInfo()['day'] == 1
    assert server.getWeather() == 'rain'
    assert server.getLoadedChunks()['total'] == 30 and server.getLoadedEntities()['world'] == 1


def test_jvm_information_is_additional(server):
    memory = server.getMemoryInfo()
    assert memory['used'] == 512.0 and memory['total'] == 1024.0 and memory['max'] == 2048.0
    assert server.getMemoryInfo('gib')['max'] == 2.0
    assert server.getProcessInfo() == {'process_used': 1536.0, 'process_virtual': 4096.0, 'uptime_ms': 3_900_000}
    assert server.getProcessorInfo() == {'load': 0.25, 'processors': 8}
    assert server.getThreadInfo() == {'current': 40, 'peak': 50, 'daemon': 30}
    assert server.getGarbageCollectorInfo()['gc_type'] == 'G1'
    assert server.getNetworkInfo()['total_bytes_out'] == 4
    assert server.getJVMUptime() == 3_900_000 and server.getJVMUptime(formatted=True) == '1h 5m'


def test_bridge_info_and_log(server):
    assert server.getPlatform() == 'paper' and server.getMinecraftVersion() == '1.21.11'
    assert server.getBridgeInfo()['protocol_version'] == 1
    assert server.getBridgeTokenInfo() == {'token_id': 'bot', 'policy_id': 'admin', 'permissions': ['*'], 'expiry': 0}
    server.writeLog('hello', level='BOT', thread='calagoapi')
    assert bridgeRequests('POST', '/server/log')[-1][2] == {'level': 'BOT', 'message': 'hello', 'thread': 'calagoapi'}
    assert isinstance(server.bridge, BridgeClient) and server.bridge is server.bridge


def test_stream_console(server):
    lines = list(server.streamConsole(history=2, timeout=5, reconnect=False))
    assert lines == ['[12:00:00 INFO]: history 0', '[12:00:01 INFO]: history 1',
                     '[12:00:10 INFO]: Steve joined the game', '[12:00:11 WARN]: line one\nline two']
    assert bridgeRequests('GET', '/server/stream')[-1][3] == 'history=2'

    raw = list(server.streamConsole(timeout=5, reconnect=False, sanitize=False))
    assert raw[0] == '\x1b[33m[12:00:10 INFO]: Steve joined the game\x1b[0m'
    assert bridgeRequests('GET', '/server/stream')[-1][3] == ''

    list(server.streamConsole(history=True, timeout=5, reconnect=False))
    assert bridgeRequests('GET', '/server/stream')[-1][3] == f'history={MAX_HISTORY}'


def test_stream_console_stops_on_timeout(server):
    release = threading.Event()

    def quiet(handler, history):
        handler.sse(':history-end\n\ndata:only line\n\n')
        release.wait(10)

    FakeBridge.stream_script = quiet
    start = time.monotonic()
    assert list(server.streamConsole(timeout=0.5)) == ['only line']
    assert time.monotonic() - start < 4
    release.set()


def test_on_console_line(server):
    lines = []
    stream = server.onConsoleLine(lines.append, history=1, reconnect=False)
    deadline = time.monotonic() + 5
    while len(lines) < 3 and time.monotonic() < deadline:
        time.sleep(0.02)
    stream.disconnect()
    assert lines == ['[12:00:00 INFO]: history 0', '[12:00:10 INFO]: Steve joined the game',
                     '[12:00:11 WARN]: line one\nline two']


def test_bridge_errors_are_hungerbridge_errors(panel, network, bridge):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID}, bridge_url=bridge, bridge_token=f'bot:{"00" * 32}')
    with pytest.raises(HungerBridgeAuthError) as error:
        server.getPlayers()
    assert error.value.reason == 'invalid_credentials'
    with pytest.raises(HungerBridgeAuthError):
        list(server.streamConsole(timeout=5))
    assert not server.isBridgeReachable()
    assert not server.waitForBridge(timeout=0.1, interval=0.05)


def test_not_configured(panel, network):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID})
    assert not server.hasBridge() and not server.isBridgeReachable()
    with pytest.raises(BridgeNotConfiguredError, match='createBridgeToken'):
        server.sendCommand('list')
    with pytest.raises(BridgeNotConfiguredError):
        server.streamConsole()           # fails on the call, not on the first line
    with pytest.raises(ConfigurationError, match='tokenId:secret'):
        MinecraftServer(panel, UUID, bridge_token=12)
    with pytest.raises(ConfigurationError, match='hex'):
        MinecraftServer(panel, UUID, bridge_token='bot:not-hex')


def test_connect_and_set_bridge(panel, network, bridge):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID}, address='play.example.com')
    assert server.getBridgeUrl() == 'http://play.example.com:1913'
    client = server.connectBridge(f'{bridge}/', TOKEN)
    assert server.getBridgeUrl() == bridge and client.base == bridge
    assert server.hasBridge() and server.isBridgeReachable() and server.waitForBridge(timeout=1)
    other = server.connectBridge(timeout=(1, 2))
    assert other is not client and other.transport.timeout == (1, 2)
    custom = BridgeClient(bridge, TOKEN)
    assert server.setBridge(custom).bridge is custom
    server.closeBridge()
    assert server.bridge is not custom


def test_redeem_pickup(panel, network, bridge):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID}, bridge_url=bridge)
    client = server.redeemBridgePickup(f'/pickup/{PICKUP_ID}?passkey={PASSKEY}')
    assert client.credentials.token_id == 'calagoapi' and server.getPlayerCount() == 2


class PickupDaemon(FakeDaemon):
    '''Answers "hb token create" like HungerBridge's console command'''
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
                    self.send(ws, 'console output', f'\x1b[32m[HungerBridge] Pickup passkey: {PASSKEY}\x1b[0m')
                    self.send(ws, 'console output',
                              f'[HungerBridge] Token created. Retrieve it at: /pickup/{PICKUP_ID}?passkey={PASSKEY}')


def test_create_bridge_token_through_the_console(panel, network, bridge):
    daemon = PickupDaemon()
    try:
        panel.api.servers.websocket = lambda server_id: {'token': 'ws-token', 'url': daemon.url}
        server = MinecraftServer(panel, UUID, data={'uuid': UUID})
        token = server.createBridgeToken('calagoapi', 'admin', expiry=3600, url=bridge)
        assert token == f'calagoapi:{SECRET}'
        assert {'event': 'send command', 'args': ['hb token create calagoapi admin 3600']} in daemon.received
        assert server.getPlayers() == ['Steve', 'Alex']
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
