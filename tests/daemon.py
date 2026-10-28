'''
A tiny fake node daemon speaking the Calagopus (Wings) websocket protocol:
JSON {"event": ..., "args": [...]} text frames.
'''
import json
import threading

from websockets.sync.server import serve


class FakeDaemon:
    def __init__(self, expire_first_token=True):
        self.received = []
        self.tokens = []
        self.expire_first_token = expire_first_token
        self.server = serve(self.handle, '127.0.0.1', 0)
        self.port = self.server.socket.getsockname()[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    @property
    def url(self):
        return f'ws://127.0.0.1:{self.port}/api/servers/test/ws'

    def stop(self):
        self.server.shutdown()

    @staticmethod
    def send(ws, event, *args):
        ws.send(json.dumps({'event': event, 'args': list(args)}))

    def handle(self, ws):
        for raw in ws:
            message = json.loads(raw)
            self.received.append(message)
            event, args = message['event'], message.get('args') or []

            if event == 'auth':
                if args[0] == 'bad-token':
                    self.send(ws, 'jwt error', 'invalid token')
                    continue
                self.tokens.append(args[0])
                self.send(ws, 'auth success', 'control.console', 'control.start')
                self.send(ws, 'status', 'running')
                if self.expire_first_token and len(self.tokens) == 1:
                    self.send(ws, 'token expiring')
            elif event == 'send logs':
                self.send(ws, 'console output', 'line 1')
                self.send(ws, 'console output', 'line 2')
            elif event == 'send command':
                self.send(ws, 'console output', f'> {args[0]}')
            elif event == 'send stats':
                self.send(ws, 'stats', json.dumps({'cpu_absolute': 12.5, 'state': 'running'}))
            elif event == 'set state':
                self.send(ws, 'status', 'stopping' if args[0] in ('stop', 'kill') else 'starting')
