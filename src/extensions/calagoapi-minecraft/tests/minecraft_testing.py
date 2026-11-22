'''
Test doubles for calagoapi-minecraft: a local fake HungerBridge (HTTP/1.1, protocol v2)
that checks every request's HMAC signature with a canonicalizer written independently of
HungerBridgePy, answers the endpoints, streams SSE v2, redeems pickups, and serves a fake
Modrinth API for installBridge().
'''
import hashlib
import hmac
import json
import time
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

TOKEN_ID = 'bot'
SECRET = '9f' * 32
TOKEN = {'bridge_token_id': TOKEN_ID, 'bridge_token_secret': SECRET}
PICKUP_ID = '0b5b6f2e-6e0c-4f0a-9d63-1c1d2e3f4a5b'
PASSKEY = 'ab' * 16
EPOCH = 'c0ffee00'

MODRINTH_PROJECT = {'slug': 'hungerbridge', 'loaders': ['fabric', 'folia', 'paper', 'purpur', 'quilt'],
                    'game_versions': ['1.21.11', '26.1.2', '26.2', '26.3']}


def modrinthVersion(vid, number, loaders, games, date):
    filename = f'HungerBridge-{loaders[0]}-{games[0]}-{number}.jar'
    return {'id': vid, 'version_number': number, 'version_type': 'alpha', 'status': 'listed', 'loaders': loaders,
            'game_versions': games, 'date_published': date,
            'files': [{'filename': filename, 'url': f'https://cdn.modrinth.com/data/{vid}/{filename}', 'primary': True,
                       'size': 1000, 'hashes': {'sha512': 'aa' * 64}}]}


MODRINTH_VERSIONS = [
    modrinthVersion('p5', '5-alpha.1', ['paper', 'purpur', 'folia'], ['1.21.11'], '2026-12-01T00:00:00Z'),
    modrinthVersion('f5', '5-alpha.1', ['fabric'], ['26.1.2'], '2026-12-01T00:00:00Z'),
    modrinthVersion('p3', '3.0-alpha', ['paper', 'purpur', 'folia'], ['1.21.11', '26.2'], '2026-06-20T00:00:00Z'),
]

ROUTES = {
    ('GET', '/ping'): {'ok': True, 'server_time': 1700000000000},
    ('GET', '/auth/check'): {'ok': True, 'token_id': TOKEN_ID, 'policy_id': 'admin', 'permissions': ['*'], 'expiry': 0},
    ('GET', '/server/meta'): {'ok': True, 'platform': 'paper', 'minecraft_version': '1.21.11', 'bridge_version': '5-alpha.1',
                              'port': 1913, 'protocol_version': 2},
    ('GET', '/players/list'): {'ok': True, 'count': 2, 'max': 20, 'players': ['Steve', 'Alex']},
    ('GET', '/world/tps'): {'ok': True, 'tps': 20.0, 'tps_1m': 19.9, 'tps_5m': 19.8, 'tps_15m': 19.7},
    ('GET', '/world/mspt'): {'ok': True, 'mspt': 12.5},
    ('GET', '/system/memory'): {'ok': True, 'heap_used_bytes': 512 * 1024 ** 2, 'heap_committed_bytes': 1024 * 1024 ** 2,
                                'heap_max_bytes': 2048 * 1024 ** 2, 'process_used_bytes': 1536 * 1024 ** 2,
                                'process_virtual_bytes': 4096 * 1024 ** 2},
    ('GET', '/system/cpu'): {'ok': True, 'cpu_load': 0.25, 'processors': 8},
    ('GET', '/system/threads'): {'ok': True, 'current': 40, 'peak': 50, 'daemon': 30},
    ('POST', '/server/stop'): {'ok': True, 'stopped': True},
}


def canonical(value):
    '''HungerBridge's TokenManager.canonicalizeJson, written independently of HungerBridgePy'''
    if isinstance(value, dict):
        return '{' + ','.join(f'{canonical(k)}:{canonical(v)}' for k, v in sorted(value.items())) + '}'
    if isinstance(value, list):
        return '[' + ','.join(canonical(v) for v in value) + ']'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, str):
        out = '"'
        for c in value:
            escapes = {'"': '\\"', '\\': '\\\\', '\b': '\\b', '\f': '\\f', '\n': '\\n', '\r': '\\r', '\t': '\\t'}
            out += escapes.get(c, f'\\u{ord(c):04x}' if ord(c) < 0x20 or ord(c) > 0x7f else c)
        return out + '"'
    return json.dumps(value)


def logEvent(seq, message, level='INFO', thread='Server thread', logger='net.minecraft.server.MinecraftServer'):
    line = f'[12:00:{seq:02d}] [{thread}/{level}]: ' + ('' if logger.startswith('net.minecraft.') else f'[{logger}] ') + message
    data = {'seq': seq, 'time': 1700000000000 + seq, 'level': level, 'thread': thread, 'logger': logger,
            'message': message, 'line': line}
    return f'id: {EPOCH}.{seq}\nevent: log\ndata: {json.dumps(data)}\n\n'


def ready(seq, replayed=0):
    return f'event: ready\ndata: {json.dumps({"epoch": EPOCH, "seq": seq, "replayed": replayed, "gap": False})}\n\n'


class FakeBridge(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    requests = []
    stream_script = None   # callable(handler, history) writing SSE; see sse()

    def log_message(self, *args):
        pass

    def reply(self, status, payload, protocol='2'):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        if protocol:
            self.send_header('X-HungerBridge-Protocol', protocol)
        self.end_headers()
        self.wfile.write(body)

    def sse(self, text):
        data = text.encode()
        self.wfile.write(b'%x\r\n%s\r\n' % (len(data), data))
        self.wfile.flush()

    def handle_request(self, method):
        path, _, query = self.path.partition('?')
        length = int(self.headers.get('Content-Length') or 0)
        raw = self.rfile.read(length).decode() if length else ''
        body = json.loads(raw) if raw else None
        FakeBridge.requests.append((method, path, body, query))

        # fake Modrinth API (no protocol header, like the real one)
        if path == '/modrinth/project/hungerbridge':
            return self.reply(200, MODRINTH_PROJECT, protocol=None)
        if path == '/modrinth/project/hungerbridge/version':
            params = parse_qs(query)
            loaders, games = set(json.loads(params['loaders'][0])), set(json.loads(params['game_versions'][0]))
            return self.reply(200, [v for v in MODRINTH_VERSIONS if loaders & set(v['loaders']) and games & set(v['game_versions'])],
                              protocol=None)
        if path == f'/pickup/{PICKUP_ID}':
            if query != f'passkey={PASSKEY}':
                return self.reply(401, {'ok': False, 'error': 'unauthorized'})
            return self.reply(200, {'ok': True, 'token_id': 'calagoapi', 'token_secret': SECRET})

        # HMAC check as in TokenManager.verifyHmacDetailed: the body sent must be the canonical text
        if body is not None and raw != canonical(body):
            return self.reply(400, {'ok': False, 'error': 'bad_request', 'message': 'body is not canonical'})
        message = '\n'.join([method, path, self.headers.get('X-Auth-Timestamp', ''), self.headers.get('X-Auth-Nonce', ''), raw])
        expected = hmac.new(bytes.fromhex(SECRET), message.encode(), hashlib.sha256).hexdigest()
        if self.headers.get('X-Auth-Id') not in (TOKEN_ID, 'calagoapi') or self.headers.get('X-Auth-Signature') != expected:
            return self.reply(401, {'ok': False, 'error': 'unauthorized', 'reason': 'invalid_credentials'})

        if (method, path) == ('GET', '/server/stream'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream; charset=UTF-8')
            self.send_header('Transfer-Encoding', 'chunked')
            self.send_header('X-HungerBridge-Protocol', '2')
            self.end_headers()
            value = parse_qs(query).get('history', ['0'])[0]
            history = 99 if value == 'all' else int(value)
            (FakeBridge.stream_script or defaultStream)(self, history)
            self.wfile.write(b'0\r\n\r\n')
            self.wfile.flush()
            return None
        if (method, path) == ('POST', '/server/run'):
            return self.reply(200, {'ok': True, 'output': [f'ran: {body["command"]}', 'done']})
        if (method, path) == ('POST', '/server/log'):
            return self.reply(200, {'ok': True, 'message': body['message']})
        if (method, path) in ROUTES:
            return self.reply(200, ROUTES[(method, path)])
        return self.reply(404, {'ok': False, 'error': 'not_found', 'message': f'No route {path}'})

    def do_GET(self):
        self.handle_request('GET')

    def do_POST(self):
        self.handle_request('POST')


def defaultStream(handler, history):
    events = ''.join(logEvent(i, f'history {i}') for i in range(min(history, 3)))
    handler.sse(events + ready(max(min(history, 3) - 1, 0), min(history, 3)))
    handler.sse(logEvent(10, 'Steve joined the game'))
    handler.sse(logEvent(11, 'line one\nline two', level='WARN', logger='SomePlugin'))
    time.sleep(0.2)


def bridgeRequests(method=None, path=None):
    return [r for r in FakeBridge.requests if (method is None or r[0] == method) and (path is None or r[1] == path)]
