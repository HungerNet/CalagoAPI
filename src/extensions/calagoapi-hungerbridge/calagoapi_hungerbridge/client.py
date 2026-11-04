import hashlib
import hmac
import json
import secrets
import time
from urllib.parse import urlsplit

import requests

from calagoapi.utils.exceptions import CalagoAPIError


class HungerBridgeError(CalagoAPIError):
    '''
    HungerBridge returned an error or could not be reached.

    Attributes:
        status_code: HTTP status, or None if the bridge was unreachable.
        error: HungerBridge error code, e.g. 'unauthorized', 'forbidden'.
    '''
    def __init__(self, message, status_code=None, error=None, response=None):
        super().__init__(message, status_code, [error] if error else [], response)
        self.error = error


def canonicalJson(value) -> str:
    '''
    Serializes a request body exactly like HungerBridge's canonicalizer: sorted keys,
    no whitespace, ASCII-only string escapes. The same text is sent and signed.
    '''
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def sign(secret_hex: str, method: str, path: str, timestamp: str, nonce: str, body: str = '') -> str:
    '''
    Returns the X-Auth-Signature for a request.

    The signed message is "METHOD\\npath\\ntimestamp\\nnonce\\nbody" and the key is the
    token secret (hex) from HungerBridge's pickup URL.
    '''
    path = urlsplit(path).path or '/'
    if len(path) > 1:
        path = path.rstrip('/') or '/'
    message = f'{method.upper()}\n{path}\n{timestamp}\n{nonce}\n{body}'
    return hmac.new(bytes.fromhex(secret_hex), message.encode('utf-8'), hashlib.sha256).hexdigest()


def parseToken(token: str):
    '''Splits an "id:secret" token. Returns (token_id, secret_hex).'''
    if not isinstance(token, str) or ':' not in token:
        raise ValueError('HungerBridge tokens look like "tokenId:secret" (the secret is the hex string from the pickup URL)')
    token_id, secret = token.split(':', 1)
    try:
        bytes.fromhex(secret)
    except ValueError:
        raise ValueError('The secret part of a HungerBridge token must be hexadecimal') from None
    if not token_id or not secret:
        raise ValueError('HungerBridge tokens look like "tokenId:secret"')
    return token_id, secret


class HungerBridgeClient:
    '''
    Minimal client for the HungerBridge HTTP API (v3), with HMAC request signing.

    Usually used through `server.hungerbridge`, but works on its own too.

    Args:
        url: Bridge URL, e.g. "http://10.0.0.5:1913".
        token: "tokenId:secret" from `hb token create` and the pickup URL.
        timeout: Request timeout in seconds.
        verify: Verify TLS certificates (for bridges behind HTTPS).

    Example:
        client = HungerBridgeClient('http://10.0.0.5:1913', 'bot:9f2c...')
        print(client.request('GET', '/players/list'))
    '''
    def __init__(self, url: str, token: str = None, timeout: float = 10, verify: bool = True):
        self.url = url.rstrip('/')
        self.token = token
        self.timeout = timeout
        self.session = requests.Session()
        self.session.verify = verify
        self._credentials = parseToken(token) if token else None

    def __repr__(self):
        return f'<HungerBridgeClient {self.url!r}>'

    def close(self) -> None:
        '''Closes the pooled HTTP connections.'''
        self.session.close()

    def headers(self, method: str, path: str, body: str = '') -> dict:
        '''Returns the signed authentication headers for one request.'''
        if self._credentials is None:
            return {}
        token_id, secret = self._credentials
        timestamp = str(int(time.time()))
        nonce = secrets.token_hex(16)
        return {
            'X-Auth-Id': token_id,
            'X-Auth-Timestamp': timestamp,
            'X-Auth-Nonce': nonce,
            'X-Auth-Signature': sign(secret, method, path, timestamp, nonce, body),
        }

    def request(self, method: str, path: str, body: dict = None, params: dict = None) -> dict:
        '''
        Sends a signed request and returns the JSON response without its "ok" flag.

        Raises:
            HungerBridgeError: Unreachable bridge, HTTP error, or {"ok": false}.
        '''
        method = method.upper()
        data = canonicalJson(body) if body is not None else ''
        headers = self.headers(method, path, data)
        if body is not None:
            headers['Content-Type'] = 'application/json'
        try:
            r = self.session.request(method, f'{self.url}{path}', params=params, data=data.encode('utf-8') or None,
                                     headers=headers, timeout=self.timeout)
        except requests.RequestException as e:
            raise HungerBridgeError(f'Could not reach HungerBridge at {self.url}: {e}') from e

        try:
            payload = r.json()
        except ValueError:
            payload = None
        if not isinstance(payload, dict):
            if r.status_code >= 400:
                raise HungerBridgeError(f'HungerBridge {method} {path} failed with HTTP {r.status_code}',
                                        r.status_code, response=r)
            raise HungerBridgeError(f'HungerBridge {method} {path} returned no JSON object', r.status_code, response=r)
        if r.status_code >= 400 or payload.get('ok') is False:
            error = payload.get('error')
            message = payload.get('message') or error or f'HTTP {r.status_code}'
            raise HungerBridgeError(f'HungerBridge {method} {path} failed: {message}', r.status_code, error, r)

        # some builds wrap results as {"ok": true, "data": {...}}
        if isinstance(payload.get('data'), dict):
            return payload['data']
        return {k: v for k, v in payload.items() if k != 'ok'}

    def get(self, path: str, params: dict = None) -> dict:
        return self.request('GET', path, params=params)

    def post(self, path: str, body: dict = None) -> dict:
        return self.request('POST', path, body if body is not None else {})
