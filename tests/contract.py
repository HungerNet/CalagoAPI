'''
A fake Calagopus panel driven by openapi.json.

It replaces requests.Session.request, answers every request with a sample
response generated from the spec, and records every request that does not
match the spec (unknown endpoint, undeclared query parameter, or a JSON body
that does not validate against the request schema).
'''
import json
import re

import requests


BASE = 'https://panel.test'
UUID = '11111111-2222-3333-4444-555555555555'
METHODS = ('get', 'post', 'put', 'patch', 'delete')


class FakeResponse:
    def __init__(self, status, body=None, text='', content_type='application/json', method='GET', path=''):
        self.status_code = status
        self.reason = 'OK' if status < 400 else 'Error'
        self.content = json.dumps(body).encode() if body is not None else text.encode()
        self.text = self.content.decode()
        self.headers = {'Content-Type': content_type}
        self.request = type('Request', (), {'method': method, 'path_url': path})()

    def json(self):
        return json.loads(self.content)

    def iter_content(self, chunk_size=1):
        yield self.content


class FakePanel:
    def __init__(self, spec_path):
        spec = json.load(open(spec_path, encoding='utf-8'))
        self.schemas = spec.get('components', {}).get('schemas', {})
        self.endpoints = []
        for path, ops in spec['paths'].items():
            if path.startswith('/api/remote'):
                continue
            regex = re.compile('^' + re.sub(r'\\\{[^}]+\\\}', '[^/]+', re.escape(path)) + '$')
            for method, op in ops.items():
                if method in METHODS:
                    self.endpoints.append((path.count('{'), method.upper(), regex, path, op))
        # prefer literal segments: /backups/groups before /backups/{backup}
        self.endpoints.sort(key=lambda e: e[0])
        self.original = None
        self.reset()

    def reset(self):
        self.calls = []
        self.violations = []
        self.hit = set()

    # patching
    def install(self):
        fake = self
        self.original = requests.Session.request

        def request(session, method, url, params=None, json=None, **kwargs):
            return fake.handle(method, url, params, json)

        requests.Session.request = request

    def uninstall(self):
        if self.original:
            requests.Session.request = self.original

    # schema helpers
    def resolve(self, schema):
        for _ in range(20):
            if not (isinstance(schema, dict) and '$ref' in schema):
                break
            # the spec contains a few dangling refs, treat them as "anything"
            schema = self.schemas.get(schema['$ref'].split('/')[-1], {})
        return schema

    def find(self, method, template):
        for _, m, _, path, op in self.endpoints:
            if m == method and path == template:
                return op
        raise KeyError(f'{method} {template} is not in the spec')

    def sample(self, schema, depth=0, name=''):
        schema = self.resolve(schema)
        if not isinstance(schema, dict) or depth > 7:
            return None
        for key in ('oneOf', 'anyOf'):
            if key in schema:
                options = [o for o in schema[key] if self.resolve(o).get('type') != 'null']
                return self.sample(options[0], depth + 1, name) if options else None
        if 'enum' in schema:
            return schema['enum'][0]
        kind = schema.get('type')
        if isinstance(kind, list):
            kind = next((k for k in kind if k != 'null'), None)
        if kind == 'object' or 'properties' in schema:
            props = schema.get('properties', {})
            if 'total' in props and 'data' in props:
                return {'total': 1, 'per_page': 50, 'page': 1, 'data': [self.sample(props['data'].get('items', {}), depth + 1)]}
            return {k: self.sample(v, depth + 1, k) for k, v in props.items()}
        if kind == 'array':
            return [self.sample(schema.get('items', {}), depth + 1, name)]
        if kind == 'string':
            fmt = schema.get('format')
            if fmt == 'uuid':
                return UUID
            if fmt == 'date-time':
                return '2026-01-01T00:00:00Z'
            if fmt == 'uri' or name.endswith('url'):
                return 'https://files.test/signed'
            return 'sample'
        return {'integer': 1, 'number': 1.5, 'boolean': True}.get(kind)

    def sampleBody(self, method, template):
        '''A valid request body for an endpoint, for methods that pass fields straight through'''
        content = self.find(method, template).get('requestBody', {}).get('content', {})
        return self.sample(content['application/json']['schema'])

    def validate(self, value, schema, where):
        schema = self.resolve(schema)
        if not isinstance(schema, dict) or not schema:
            return []
        for key in ('oneOf', 'anyOf'):
            if key in schema:
                results = [self.validate(value, o, where) for o in schema[key]]
                if any(not r for r in results):
                    return []
                return [f'{where}: matches no variant: ' + ' || '.join('; '.join(r[:2]) for r in results[:4])]
        if 'enum' in schema and value not in schema['enum']:
            return [f'{where}: {value!r} not in {schema["enum"]}']
        kind = schema.get('type')
        kinds = kind if isinstance(kind, list) else ([kind] if kind else [])
        if kinds and not any(_typeOk(value, k) for k in kinds):
            return [f'{where}: expected {kinds}, got {type(value).__name__} {value!r}'[:200]]
        errors = []
        if isinstance(value, dict) and ('properties' in schema or kind == 'object'):
            props = schema.get('properties', {})
            if props and not schema.get('additionalProperties'):
                errors += [f'{where}: unknown field {k!r}' for k in value if k not in props]
            errors += [f'{where}: missing required {k!r}' for k in schema.get('required', []) if k not in value]
            for k, v in value.items():
                if k in props:
                    errors += self.validate(v, props[k], f'{where}.{k}')
        if isinstance(value, list) and 'items' in schema:
            for i, v in enumerate(value):
                errors += self.validate(v, schema['items'], f'{where}[{i}]')
        return errors

    # request handling
    def handle(self, method, url, params, body):
        self.calls.append((method, url))
        if not url.startswith(BASE):
            # signed upload/download URLs pointing at the daemon
            return FakeResponse(200, text='filedata', content_type='application/octet-stream', method=method, path=url)

        path = url[len(BASE):]
        for _, m, regex, template, op in self.endpoints:
            if m != method or not regex.match(path):
                continue
            self.hit.add((m, template))
            declared = {p['name'] for p in op.get('parameters', []) if p.get('in') == 'query'}
            self.violations += [f'{m} {template}: undeclared query parameter {p!r}' for p in params or {} if p not in declared]

            request_content = op.get('requestBody', {}).get('content', {})
            if body is not None:
                if 'application/json' not in request_content:
                    self.violations.append(f'{m} {template}: sent JSON, endpoint takes {list(request_content) or "no body"}')
                else:
                    schema = request_content['application/json'].get('schema', {})
                    self.violations += [f'{m} {template}: {e}' for e in self.validate(body, schema, 'body')]
            elif self.resolve(request_content.get('application/json', {}).get('schema', {})).get('required'):
                self.violations.append(f'{m} {template}: missing JSON body')

            response = op.get('responses', {}).get('200', {}).get('content', {})
            if 'application/json' in response:
                return FakeResponse(200, self.sample(response['application/json'].get('schema', {})), method=m, path=path)
            if response:
                return FakeResponse(200, text='sample text', content_type=list(response)[0], method=m, path=path)
            return FakeResponse(200, method=m, path=path)

        self.violations.append(f'{method} {path}: no such endpoint')
        return FakeResponse(404, {'errors': ['not found']}, method=method, path=path)


def _typeOk(value, kind):
    return {
        'string': isinstance(value, str),
        'integer': isinstance(value, int) and not isinstance(value, bool),
        'number': isinstance(value, (int, float)) and not isinstance(value, bool),
        'boolean': isinstance(value, bool),
        'array': isinstance(value, list),
        'object': isinstance(value, dict),
        'null': value is None,
    }.get(kind, True)
