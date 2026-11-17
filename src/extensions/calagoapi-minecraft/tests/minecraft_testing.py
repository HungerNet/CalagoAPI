'''
Test doubles for calagoapi-minecraft: a local fake HungerBridge (HTTP/1.1) that checks
every request's HMAC signature with a canonicalizer written independently of
HungerBridgePy, answers the protocol v1 endpoints, streams SSE, redeems pickups and
serves a fake GitHub releases API.
'''
import hashlib
import hmac
import json
import time
from http.server import BaseHTTPRequestHandler

TOKEN_ID = 'bot'
SECRET = '9f' * 32
TOKEN = f'{TOKEN_ID}:{SECRET}'
PICKUP_ID = '0b5b6f2e-6e0c-4f0a-9d63-1c1d2e3f4a5b'
PASSKEY = 'ab' * 16

RELEASE = {
    'tag_name': 'v4-alpha.94',
    'assets': [
        {'name': f'HungerBridge-{loader}-{mc}-4-alpha.94.jar', 'browser_download_url': f'https://github.example/{loader}-{mc}.jar'}
        for loader in ('paper', 'fabric') for mc in ('1.21.11', '26.1.2', '26.2')
    ] + [{'name': 'HungerBridge-paper-26.2-4-alpha.94-sources.jar', 'browser_download_url': 'x'}],
}

ROUTES = {
    ('GET', '/ping'): {'ok': True, 'server_time': 1700000000000},
    ('GET', '/auth/check'): {'ok': True, 'tokenId': TOKEN_ID, 'policyId': 'admin', 'permissions': ['*'], 'expiry': 0},
    ('GET', '/server/meta'): {'ok': True, 'platform': 'paper', 'minecraft_version': '1.21.11', 'bridge_version': '4-alpha.94',
                              'port': 1913, 'protocol_version': 1},
    ('GET', '/players/list'): {'ok': True, 'count': 2, 'max': 20, 'players': ['Steve', 'Alex']},
    ('GET', '/world/tps'): {'ok': True, 'tps': 20.0, 'tps_1m': 19.9, 'tps_5m': 19.8, 'tps_15m': 19.7},
    ('GET', '/world/mspt'): {'ok': True, 'mspt': 12.5},
    ('GET', '/world/time'): {'ok': True, 'time': 6000, 'full_time': 30000, 'day': 1, 'server_time': 1700000000},
    ('GET', '/world/weather'): {'ok': True, 'weather': 'rain'},
    ('GET', '/world/chunks'): {'ok': True, 'total': 30, 'world': 10, 'world_nether': 10, 'world_the_end': 10},
    ('GET', '/world/entities'): {'ok': True, 'total': 3, 'world': 1, 'world_nether': 1, 'world_the_end': 1},
    ('GET', '/system/uptime'): {'ok': True, 'uptime_ms': 3_900_000},
    ('GET', '/system/cpu'): {'ok': True, 'cpu_load': 0.25, 'processors': 8},
    ('GET', '/system/memory'): {'ok': True, 'heap_used_bytes': 512 * 1024 ** 2, 'heap_committed_bytes': 1024 * 1024 ** 2,
                                'heap_max_bytes': 2048 * 1024 ** 2, 'process_used_bytes': 1536 * 1024 ** 2,
                                'process_virtual_bytes': 4096 * 1024 ** 2},
    ('GET', '/system/gc'): {'ok': True, 'gc_type': 'G1', 'gc_count': 7, 'gc_time_ms': 70, 'last_gc_pause_ms': 9, 'avg_gc_pause_ms': 10},
    ('GET', '/system/threads'): {'ok': True, 'current': 40, 'peak': 50, 'daemon': 30},
    ('GET', '/system/network'): {'ok': True, 'bytes_in_per_sec': 1, 'bytes_out_per_sec': 2, 'total_bytes_in': 3, 'total_bytes_out': 4},
    ('POST', '/server/log'): {'ok': True},
    ('POST', '/server/stop'): {'ok': True, 'stopped': True, 'force': False},
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


class FakeBridge(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    requests = []
    stream_script = None   # callable(handler, history) writing SSE; see sse()

    def log_message(self, *args):
        pass

    def reply(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('X-HungerBridge-Protocol', '1')
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

        if path == '/repos/HungerNet/HungerBridge/releases/latest':
            return self.reply(200, RELEASE)
        if path.startswith('/repos/'):
            return self.reply(404, {'message': 'Not Found'})
        if path == f'/pickup/{PICKUP_ID}':
            if query != f'passkey={PASSKEY}':
                return self.reply(401, {'ok': False, 'error': 'unauthorized'})
            return self.reply(200, {'ok': True, 'token_id': 'calagoapi', 'token_secret': SECRET})

        # HMAC check as in TokenManager.verifyHmacDetailed: the body sent must be the canonical text
        if body is not None and raw != canonical(body):
            return self.reply(400, {'ok': False, 'error': 'bad_request', 'message': 'body is not canonical'})
        message = '\n'.join([method, path, self.headers.get('X-Auth-Timestamp', ''), self.headers.get('X-Auth-Nonce', ''),
                             raw])
        expected = hmac.new(bytes.fromhex(SECRET), message.encode(), hashlib.sha256).hexdigest()
        if self.headers.get('X-Auth-Id') not in (TOKEN_ID, 'calagoapi') or self.headers.get('X-Auth-Signature') != expected:
            return self.reply(401, {'ok': False, 'error': 'unauthorized', 'reason': 'invalid_credentials'})

        if (method, path) == ('GET', '/server/stream'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream; charset=UTF-8')
            self.send_header('Transfer-Encoding', 'chunked')
            self.send_header('X-HungerBridge-Protocol', '1')
            self.end_headers()
            history = int(query.split('history=')[1]) if 'history=' in query else 0
            (FakeBridge.stream_script or defaultStream)(self, history)
            self.wfile.write(b'0\r\n\r\n')
            self.wfile.flush()
            return None
        if (method, path) == ('POST', '/server/run'):
            response = {'ok': True}
            if not body.get('silent'):
                response['output'] = [f'ran: {body["command"]}', 'done']
            return self.reply(200, response)
        if (method, path) in ROUTES:
            return self.reply(200, ROUTES[(method, path)])
        return self.reply(404, {'ok': False, 'error': 'not_found', 'message': f'No route {path}'})

    def do_GET(self):
        self.handle_request('GET')

    def do_POST(self):
        self.handle_request('POST')


def defaultStream(handler, history):
    for i in range(history):
        handler.sse(f'data:[12:00:0{i} INFO]: history {i}\n\n')
    handler.sse(':history-end\n\n')
    handler.sse('data:\x1b[33m[12:00:10 INFO]: Steve joined the game\x1b[0m\n\n')
    handler.sse('data:[12:00:11 WARN]: line one\\nline two\n\n')
    time.sleep(0.2)




def bridgeRequests(method=None, path=None):
    return [r for r in FakeBridge.requests if (method is None or r[0] == method) and (path is None or r[1] == path)]
