'''
Fixtures for calagoapi-minecraft (test doubles in minecraft_testing.py):

- `bridge`: URL of a fake HungerBridge on localhost;
- `network`: panel requests go to the contract-checked fake panel, everything else
  (the fake bridge) to the real network on localhost;
- `mc`: a fresh extension registry with the minecraft extension registered.
'''
import threading
from http.server import ThreadingHTTPServer

import pytest
import requests

from contract import BASE
from minecraft_testing import FakeBridge

# captured at collection time, before the fake panel patches requests
ORIGINAL_REQUEST = requests.Session.request


@pytest.fixture(scope='module')
def bridge():
    server = ThreadingHTTPServer(('127.0.0.1', 0), FakeBridge)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f'http://127.0.0.1:{server.server_address[1]}'
    server.shutdown()
    server.server_close()


@pytest.fixture
def network(fake, monkeypatch):
    '''Panel requests go to the fake panel, everything else to the real network (localhost)'''
    def request(session, method, url, params=None, json=None, **kwargs):
        if url.startswith(BASE):
            return fake.handle(method, url, params, json)
        return ORIGINAL_REQUEST(session, method, url, params=params, json=json, **kwargs)

    monkeypatch.setattr(requests.Session, 'request', request)
    FakeBridge.requests.clear()
    FakeBridge.stream_script = None


@pytest.fixture
def mc(extensions, network):
    '''A fresh registry with the minecraft extension registered (not enabled)'''
    from calagoapi_minecraft import MinecraftExtension
    extensions.register(MinecraftExtension)
    return extensions
