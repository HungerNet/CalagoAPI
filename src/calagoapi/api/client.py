import time
from urllib.parse import quote

import requests

from calagoapi.utils.model import Page
from calagoapi.utils.exceptions import (
    CalagoAPIError,
    BadRequestError,
    AuthenticationError,
    PermissionDeniedError,
    NotFoundError,
    ConflictError,
    RateLimitError,
    ServerError,
    PanelConnectionError,
)


RETRY_STATUSES = (502, 503, 504)

ERRORS = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    429: RateLimitError,
}


def segment(value):
    '''Encodes a free-text value (file name, identifier, ...) for use as one URL path segment'''
    return quote(str(value), safe='')


def clean(values):
    '''Drops None values so optional parameters are never sent'''
    if values is None:
        return None
    return {k: v for k, v in values.items() if v is not None}


class Client:
    '''
    Internal HTTP client for Calagopus.

    Every request made by CalagoAPI goes through this class. It handles
    authentication, JSON encoding, error handling, retries and pagination.
    You normally never need it directly, use `Panel` instead.

    Retries: rate limited requests (429) are retried after the panel's
    Retry-After delay. GET requests are also retried on connection errors
    and on 502, 503 and 504. Other requests are never retried, so a power
    action or backup is never sent twice.
    '''
    def __init__(self, url: str, api_key: str, timeout: int = 10, verify: bool = True, user_agent: str = None,
                 max_retries: int = 3, max_retry_wait: int = 60):
        self.url = url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.max_retry_wait = max_retry_wait

        self.session = requests.Session()
        self.session.verify = verify
        self.session.headers.update(self.headers)
        if user_agent:
            self.session.headers['User-Agent'] = user_agent

    @property
    def headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Accept': 'application/json',
        }

    # http core
    def request(self, method, path, params=None, json=None, data=None, headers=None, raw=False, timeout=None, stream=False):
        # optional body fields left as None are omitted, the panel then keeps its default
        if isinstance(json, dict):
            json = clean(json)

        attempt = 0
        while True:
            try:
                r = self.session.request(
                    method,
                    f'{self.url}{path}',
                    params=clean(params),
                    json=json,
                    data=data,
                    headers=headers,
                    timeout=timeout or self.timeout,
                    stream=stream,
                )
            except requests.RequestException as e:
                if method == 'GET' and attempt < self.max_retries:
                    attempt += 1
                    time.sleep(self.retryDelay(attempt))
                    continue
                raise PanelConnectionError(f'Could not reach {self.url}: {e}') from e

            retryable = r.status_code == 429 or (method == 'GET' and r.status_code in RETRY_STATUSES)
            if retryable and attempt < self.max_retries:
                attempt += 1
                time.sleep(self.retryDelay(attempt, r.headers.get('Retry-After')))
                continue
            break

        if r.status_code >= 400:
            self.raiseError(r)
        if raw:
            return r
        return self.parse(r)

    def retryDelay(self, attempt, retry_after=None):
        '''Seconds to wait before a retry: the panel's Retry-After, or 0.5s, 1s, 2s, ...'''
        try:
            delay = float(retry_after)
        except (TypeError, ValueError):
            delay = 0.5 * 2 ** (attempt - 1)
        return min(max(delay, 0), self.max_retry_wait)

    def close(self):
        '''Closes the pooled HTTP connections.'''
        self.session.close()

    def get(self, path, params=None, **kwargs):
        return self.request('GET', path, params=params, **kwargs)
    def post(self, path, json=None, params=None, **kwargs):
        return self.request('POST', path, params=params, json=json, **kwargs)
    def put(self, path, json=None, params=None, **kwargs):
        return self.request('PUT', path, params=params, json=json, **kwargs)
    def patch(self, path, json=None, params=None, **kwargs):
        return self.request('PATCH', path, params=params, json=json, **kwargs)
    def delete(self, path, json=None, params=None, **kwargs):
        return self.request('DELETE', path, params=params, json=json, **kwargs)

    # plain-text bodies (file writes, database imports)
    def postText(self, path, content, params=None, content_type='text/plain'):
        if isinstance(content, str):
            content = content.encode('utf-8')
        return self.request('POST', path, params=params, data=content, headers={'Content-Type': content_type})

    # responses
    @staticmethod
    def parse(r):
        if not r.content:
            return None
        if 'json' in r.headers.get('Content-Type', ''):
            return r.json()
        return r.text

    @staticmethod
    def raiseError(r):
        errors = []
        try:
            body = r.json()
            if isinstance(body, dict):
                errors = body.get('errors') or []
        except ValueError:
            pass

        message = '; '.join(str(e) for e in errors) or r.text.strip() or r.reason
        message = f'{r.status_code} {r.request.method} {r.request.path_url}: {message}'

        if r.status_code == 429:
            retry_after = r.headers.get('Retry-After')
            raise RateLimitError(message, r.status_code, errors, r, float(retry_after) if retry_after else None)
        if r.status_code >= 500:
            raise ServerError(message, r.status_code, errors, r)
        raise ERRORS.get(r.status_code, CalagoAPIError)(message, r.status_code, errors, r)

    # pagination
    def list(self, path, key, params=None, page=None, per_page=None) -> Page:
        '''
        Fetches a paginated listing.

        When `page` is given only that page is returned, otherwise every page is
        fetched and combined into one Page.
        '''
        params = dict(params or {})

        if page is not None:
            params.update(page=page, per_page=per_page or 50)
            result = self.get(path, params=params)[key]
            return Page(result['data'], result['total'], result['page'], result['per_page'])

        items = []
        current = 1
        while True:
            params.update(page=current, per_page=per_page or 100)
            result = self.get(path, params=params)[key]
            items.extend(result['data'])
            if not result['data'] or len(items) >= result['total']:
                return Page(items, result['total'], 1, len(items))
            current += 1
