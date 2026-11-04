import asyncio
import hashlib
import hmac
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest
import requests

from calagoapi import AsyncPanel, MinecraftServer
from calagoapi.extensions import ConfigurationError

from calagoapi_hungerbridge import HungerBridgeError
from calagoapi_hungerbridge.client import canonicalJson, sign
from calagoapi_hungerbridge import extension as extension_module
from calagoapi_hungerbridge.extension import HungerBridge, HungerBridgeExtension
from calagoapi_version_changer.extension import VersionChangerExtension
from contract import BASE, UUID

# captured at collection time, before any fake panel patches requests
ORIGINAL_REQUEST = requests.Session.request

TOKEN_ID = 'bot'
SECRET = '9f' * 32
TOKEN = f'{TOKEN_ID}:{SECRET}'

RELEASE = {
    'tag_name': 'v4-alpha.34',
    'assets': [
        {'name': f'HungerBridge-hb-{loader}-{mc}+4-alpha.34.jar',
         'browser_download_url': f'https://github.example/{loader}-{mc}.jar'}
        for loader in ('paper', 'fabric') for mc in ('1.21.11', '26.1.2', '26.2')
    ] + [{'name': 'HungerBridge-hb-paper-1.21.11+4-alpha.34-sources.jar', 'browser_download_url': 'x'}],
}


def canonical(value):
    '''Java TokenManager.canonicalizeJson, written independently of the client'''
    if isinstance(value, dict):
        return '{' + ','.join(f'{canonical(k)}:{canonical(v)}' for k, v in sorted(value.items())) + '}'
    if isinstance(value, list):
        return '[' + ','.join(canonical(v) for v in value) + ']'
    if isinstance(value, str):
        out = '"'
        for c in value:
            out += {'"': '\\"', '\\': '\\\\', '\b': '\\b', '\f': '\\f', '\n': '\\n', '\r': '\\r', '\t': '\\t'}.get(
                c, f'\\u{ord(c):04x}' if ord(c) < 0x20 or ord(c) > 0x7f else c)
        return out + '"'
    return json.dumps(value)


class FakeBridge(BaseHTTPRequestHandler):
    requests = []

    def log_message(self, *args):
        pass

    def reply(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def handle_request(self, method):
        path = self.path.split('?')[0]
        length = int(self.headers.get('Content-Length') or 0)
        raw = self.rfile.read(length).decode() if length else ''
        body = json.loads(raw) if raw else None
        FakeBridge.requests.append((method, path, body))

        if path == '/repos/hungernet/hungerbridge/releases/latest':
            return self.reply(200, RELEASE)
        if path.startswith('/repos/'):
            return self.reply(404, {'message': 'Not Found'})

        # HMAC check, as in HungerBridge's TokenManager.verifyHmacDetailed
        message = '\n'.join([method, path, self.headers.get('X-Auth-Timestamp', ''), self.headers.get('X-Auth-Nonce', ''),
                             canonical(body) if body is not None else ''])
        expected = hmac.new(bytes.fromhex(SECRET), message.encode(), hashlib.sha256).hexdigest()
        if self.headers.get('X-Auth-Id') != TOKEN_ID or self.headers.get('X-Auth-Signature') != expected:
            return self.reply(401, {'ok': False, 'error': 'unauthorized', 'message': 'Authentication required'})

        routes = {
            ('GET', '/players/list'): {'ok': True, 'count': 2, 'players': ['Steve', 'Alex']},
            ('GET', '/world/tps'): {'ok': True, 'tps': 20.0, 'tps_1m': 19.9, 'tps_5m': 19.8, 'tps_15m': 19.7},
            ('GET', '/world/mspt'): {'ok': True, 'mspt': 12.5},
            ('GET', '/ping'): {'ok': True, 'server_time': 1700000000000},
            ('GET', '/system/memory'): {'ok': True, 'data': {'heap_used_bytes': 1024}},
            ('GET', '/server/status'): {'ok': True, 'online': True},
            ('POST', '/server/log'): {'ok': True},
            ('POST', '/server/stop'): {'ok': True, 'stopped': True, 'force': False},
        }
        if (method, path) == ('POST', '/server/run'):
            output = [] if body.get('silent') else [f'ran: {body["command"]}']
            return self.reply(200, {'ok': True, 'output': output})
        if (method, path) in routes:
            return self.reply(200, routes[(method, path)])
        return self.reply(404, {'ok': False, 'error': 'not_found', 'message': f'No route {path}'})

    def do_GET(self):
        self.handle_request('GET')

    def do_POST(self):
        self.handle_request('POST')


@pytest.fixture(scope='module')
def bridge():
    server = ThreadingHTTPServer(('127.0.0.1', 0), FakeBridge)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f'http://127.0.0.1:{server.server_address[1]}'
    server.shutdown()


@pytest.fixture
def network(fake, monkeypatch):
    '''Panel requests go to the fake panel, everything else to the real network (localhost)'''
    def request(session, method, url, params=None, json=None, **kwargs):
        if url.startswith(BASE):
            return fake.handle(method, url, params, json)
        return ORIGINAL_REQUEST(session, method, url, params=params, json=json, **kwargs)

    monkeypatch.setattr(requests.Session, 'request', request)
    FakeBridge.requests.clear()


@pytest.fixture
def hb(extensions, bridge, network):
    extensions.register(VersionChangerExtension)
    extensions.register(HungerBridgeExtension)
    return extensions


def test_signature_matches_hungerbridge():
    body = {'command': 'say héllo "x"', 'silent': False, 'show_console': True, 'n': 1}
    assert canonicalJson(body) == canonical(body)
    message = 'POST\n/server/run\n1700000000\nabc\n' + canonical(body)
    expected = hmac.new(bytes.fromhex(SECRET), message.encode(), hashlib.sha256).hexdigest()
    assert sign(SECRET, 'post', '/server/run/', '1700000000', 'abc', canonicalJson(body)) == expected


def test_enable_pulls_in_version_changer(hb, panel, bridge):
    hb.enable('hungerbridge', config={'url': bridge, 'token': TOKEN})
    assert hb.get('version_changer').enabled_by == 'hungerbridge'

    server = panel.servers.getMinecraftServer(UUID)
    assert isinstance(server.hungerbridge, HungerBridge)
    assert server.hungerbridge is server.hungerbridge
    assert hb.owner_of(MinecraftServer, 'hungerbridge') == 'hungerbridge'

    assert server.hungerbridge.players() == ['Steve', 'Alex']
    assert server.hungerbridge.playerCount() == 2
    assert server.hungerbridge.tps()['tps'] == 20.0
    assert server.hungerbridge.mspt() == 12.5
    assert server.hungerbridge.ping() == 1700000000000
    assert server.hungerbridge.memory() == {'heap_used_bytes': 1024}
    assert server.hungerbridge.status() == {'online': True}
    assert server.hungerbridge.isReachable()
    assert server.hungerbridge.run('say hi') == ['ran: say hi']
    assert server.hungerbridge.run('say hi', silent=True) == []
    server.hungerbridge.log('hello', level='BRIDGE', thread='bot')
    assert server.hungerbridge.stop()['stopped'] is True
    assert ('POST', '/server/log', {'message': 'hello', 'level': 'BRIDGE', 'thread': 'bot'}) in FakeBridge.requests


def test_existing_server_gains_service(hb, panel, bridge):
    server = panel.servers.getMinecraftServer(UUID)
    assert not hasattr(server, 'hungerbridge')
    hb.enable('hungerbridge', config={'url': bridge, 'token': TOKEN})
    assert server.hungerbridge.players() == ['Steve', 'Alex']


def test_errors(hb, panel, bridge):
    hb.enable('hungerbridge', config={'url': bridge, 'token': f'{TOKEN_ID}:{"00" * 32}'})
    server = panel.servers.getMinecraftServer(UUID)
    with pytest.raises(HungerBridgeError) as error:
        server.hungerbridge.players()
    assert error.value.status_code == 401 and error.value.error == 'unauthorized'
    assert not server.hungerbridge.isReachable()

    # per-server credentials override the config
    server.hungerbridge.connect(token=TOKEN)
    assert server.hungerbridge.players() == ['Steve', 'Alex']
    with pytest.raises(HungerBridgeError, match='No route'):
        server.hungerbridge.client.get('/nope')

    server.hungerbridge.connect('http://127.0.0.1:9')
    with pytest.raises(HungerBridgeError, match='Could not reach'):
        server.hungerbridge.players()


def test_url_defaults_to_server_address(hb, panel):
    hb.enable('hungerbridge', config={'port': 2000})
    server = panel.servers.getMinecraftServer(UUID, server_domain='play.example.com')
    assert server.hungerbridge.getUrl() == 'http://play.example.com:2000'
    server.hungerbridge.connect('http://10.0.0.5:1913/')
    assert server.hungerbridge.getUrl() == 'http://10.0.0.5:1913'


def test_reenable_with_other_config_fails(hb):
    hb.enable('hungerbridge', config={'mc_version': '1.20.4'})
    hb.enable('hungerbridge', config={'mc_version': '1.20.4'})
    with pytest.raises(ConfigurationError, match='already enabled with a different configuration'):
        hb.enable('hungerbridge', config={'mc_version': '1.21.1'})


@pytest.mark.parametrize('config, message', [
    ({'token': 'no-colon'}, 'tokenId:secret'),
    ({'token': 'bot:not-hex'}, 'hexadecimal'),
    ({'port': 70000}, 'port'),
    ({'mc_version': 1.21}, 'mc_version'),
])
def test_invalid_config(hb, config, message):
    with pytest.raises(ConfigurationError, match=message):
        hb.enable('hungerbridge', config=config)


def test_install_detects_loader_and_version(hb, panel, fake, bridge, monkeypatch):
    hb.enable('hungerbridge', config={'github_api': bridge})
    server = panel.servers.getMinecraftServer(UUID)
    # pretend the Version Changer reports a Fabric 26.1.2 server
    monkeypatch.setattr(extension_module, 'getInstalledVersion',
                        lambda server: {'build': {'type': 'FABRIC', 'version_id': '26.1.2'}, 'latest': None})

    asset = server.hungerbridge.install()
    assert asset == {'name': 'HungerBridge-hb-fabric-26.1.2+4-alpha.34.jar', 'url': 'https://github.example/fabric-26.1.2.jar',
                     'mc_version': '26.1.2', 'loader': 'fabric', 'release': 'v4-alpha.34'}
    assert ('POST', '/api/client/servers/{server}/files/pull') in fake.hit
    assert not fake.violations

    assert server.hungerbridge.install(mc_version='latest', loader='paper')['name'] == 'HungerBridge-hb-paper-26.2+4-alpha.34.jar'
    assert server.hungerbridge.findRelease('1.21.11', 'paper')['url'] == 'https://github.example/paper-1.21.11.jar'

    with pytest.raises(HungerBridgeError, match='no fabric build for Minecraft 1.21.1. Available: 1.21.11, 26.1.2, 26.2'):
        server.hungerbridge.install(mc_version='1.21.1')
    with pytest.raises(HungerBridgeError, match='not found'):
        server.hungerbridge.install(release='v0')

    monkeypatch.setattr(extension_module, 'getInstalledVersion', lambda server: {'build': {'type': 'VANILLA'}})
    with pytest.raises(HungerBridgeError, match='loader="paper"'):
        server.hungerbridge.install()


def test_async(hb, fake, bridge):
    hb.enable('hungerbridge', config={'url': bridge, 'token': TOKEN})

    async def main():
        async with AsyncPanel(url=BASE, api_key='c7sp_test') as panel:
            server = await panel.servers.getMinecraftServer(UUID)
            assert server.hungerbridge is server.hungerbridge
            assert await server.hungerbridge.players() == ['Steve', 'Alex']
            assert await server.hungerbridge.run('list') == ['ran: list']

    asyncio.run(main())


def test_token_is_masked_in_diagnostics(hb):
    hb.enable('hungerbridge', config={'token': TOKEN})
    assert SECRET not in hb.describe() and "'token': '***'" in hb.describe()
    with pytest.raises(ConfigurationError) as error:
        hb.enable('hungerbridge', config={'token': f'other:{SECRET}'})
    assert SECRET not in str(error.value)
