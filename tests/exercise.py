'''
Calls every public method reachable from a Panel with plausible arguments.

Objects returned by a method (Backup, Node, Egg, ...) are queued and their
methods are called too, so new methods are covered automatically.
'''
import inspect
import os
import tempfile
import traceback

from calagoapi import triggers, conditions, actions, variable, backup_selectors, DatabaseExplorer
from calagoapi.utils.model import Model, Page
from contract import UUID


# methods that block, loop or need a live object
SKIP = {'waitForState', 'waitForOnline', 'waitForOffline', 'waitUntilComplete', 'runOn', 'get', 'toDict', 'map',
        # open a websocket, covered by test_console.py
        'streamConsole', 'onConsoleLine'}

# methods that are expected to raise
EXPECTED_ERRORS = {
    ('DatabaseHost', 'setDescription'),
    ('SubdomainDomain', 'setDescription'),
}

# arguments by parameter name
VALUES = {
    'action': 'start', 'state': 'running', 'command': 'say hi', 'commands': ['say hi'], 'message': 'hi',
    'player': 'Steve', 'target': '@a', 'component': {'text': 'hi'}, 'key': 'SERVER_JARFILE', 'value': '1',
    'values': {'name': 'x'}, 'where': {'id': '1'}, 'rows': [{'id': '1'}], 'table': 'players', 'column': 'name',
    'sql': 'SELECT 1', 'query': 'hello', 'type': 'PAPER', 'version': '1.21.1', 'build': {'uuid': UUID},
    'path': '/folder/file.txt', 'file_path': '/folder/archive.zip', 'new_path': '/folder/new.txt',
    'file': '/folder/file.txt', 'directory': '/', 'root': '/', 'destination': '/folder/moved.txt',
    'link': 'a', 'mode': '755', 'files': ['a.txt'], 'content': 'text', 'dump': b'dump',
    'image': 'ghcr.io/image:latest', 'url': 'https://example.com/file', 'urls': ['https://example.com/egg.json'],
    'email': 'a@example.com', 'password': 'pw', 'new_password': 'pw2', 'code': '123456', 'token': 'tok',
    'confirmation_token': 'tok', 'username': 'steve', 'user': 'steve', 'name': 'test', 'name_first': 'A',
    'description': 'desc', 'permissions': ['control.console'], 'permission': 'read_only', 'ignored_files': [],
    'provider': 'github', 'public_key': 'ssh-ed25519 AAA', 'cron': '0 0 * * * *', 'schedule': '0 0 * * * *',
    'enabled': True, 'admin': True, 'behavior': 'always', 'timezone': 'UTC', 'seconds': 30, 'lines': 10,
    'retention': {'daily': 7}, 'public_key_credential': {}, 'backup_disk': 'local', 'backup_configs': {},
    'provider_config': {}, 'pairing_code': 'abc', 'git_repository': 'https://example.com/r.git', 'author': 'me',
    'env_variable': 'TEST', 'title': 'Hello', 'memory': 1024, 'disk': 2048, 'port': 8080, 'ip': '0.0.0.0',
    'host': 'tunnel.example.com', 'ports': [25565], 'names': ['a.png'], 'labels': {'a': 'b'}, 'settings': {},
    'config': {}, 'variables': {'SERVER_JARFILE': 'server.jar'}, 'columns': [{'name': 'id', 'type': 'INT'}],
    'locations': [UUID], 'nodes': [UUID], 'eggs': [UUID], 'servers': [UUID], 'groups': [UUID], 'backup_ids': [UUID],
    'databases': {UUID: 'read_write'},
    'rules': [{'action': 'allow', 'protocols': ['tcp'], 'sources': [], 'ports': [25565]}],
    'triggers': [triggers.cron('0 0 4 * * *'), triggers.crash(), triggers.consoleLine('joined', output_into='line')],
    'condition': conditions.all(conditions.serverState('running'), conditions.negate(conditions.fileExists('/x'))),
    'steps': [
        actions.sendCommand('say hi'), actions.sleep(1000), actions.createBackup('nightly'),
        actions.waitForState('offline'), actions.httpRequest('https://example.com', headers={'a': 'b'}),
        actions.restoreBackup(backup_selectors.latest()), actions.renameFiles('/', [('a', 'b')]),
        actions.ifCondition(conditions.uptime('greater_than', 1)), actions.otherwise(), actions.endIf(),
        actions.compressFiles('/', ['world'], 'world.tar.gz'), actions.matchRegex(variable('line'), '(.*)', ['x', None]),
    ],
    'actions': [actions.sendCommand('say hi')],
    'data': {'name': 'x', 'enabled': True, 'triggers': [], 'condition': {'type': 'none'}, 'steps': []},
}

ID_NAMES = {
    'server', 'node', 'egg', 'owner', 'location', 'group', 'mount', 'device', 'role', 'allocation', 'backup',
    'database', 'host', 'nest', 'template', 'security_key', 'ssh_key', 'api_key', 'snippet', 'oauth_link',
    'oauth_provider', 'policy', 'configuration', 'repository', 'subuser', 'database_host', 'database_instance',
    'instance', 'destination_server', 'subdomain', 'announcement', 'domain',
}


def overrides(fake, upload_path):
    '''Per-method arguments, callables receive the fake panel'''
    egg_import = lambda: fake.sampleBody('POST', '/api/admin/nests/{nest}/eggs/import')
    mapping = lambda: fake.sampleBody('POST', '/api/admin/oauth-providers/{oauth_provider}/mappings')
    return {
        ('AnnouncementManager', 'createAnnouncement'): {'type': 'info'},
        ('DatabaseHostManager', 'createDatabaseHost'): {'type': 'mysql', 'credentials': fake.sampleBody('POST', '/api/admin/database-hosts')['credentials']},
        ('SubdomainDomainManager', 'createDomain'): {'domain': 'example.com', 'provider': 'cloudflare'},
        ('DeviceManager', 'createDevice'): {'permissions': 'rwm'},
        ('Account', 'setAvatar'): {'image': b'png'},
        ('Schedule', 'addStep'): {'action': actions.sendCommand('say hi')},
        ('Schedule', 'orderSteps'): {'steps': [UUID]},
        ('FileManager', 'chmod'): {'files': [{'file': 'a', 'mode': '755'}]},
        ('FileManager', 'uploadFile'): {'file': upload_path},
        ('GenericServer', 'uploadFile'): {'file_data': upload_path},
        ('MinecraftServer', 'uploadFile'): {'file_data': upload_path},
        ('NetworkManager', 'addFirewallRule'): {'action': 'allow'},
        ('Egg', 'createVariable'): {'rules': ['required']},
        ('ExtensionManager', 'install'): {'file': b'zip'},
        ('AssetManager', 'upload'): {'file': b'png'},
        ('Panel', 'get'): {'path': '/api/client/account'},
        ('Panel', 'post'): {'path': '/api/client/account/logout'},
        ('Panel', 'put'): {'path': '/api/client/account/password', 'json': {'password': 'a', 'new_password': 'b'}},
        ('Panel', 'patch'): {'path': '/api/client/account', 'json': {'language': 'en'}},
        ('Panel', 'delete'): {'path': '/api/client/account/avatar'},
        # methods that pass fields straight to Calagopus get a valid body generated from the spec
        ('Nest', 'createEgg'): lambda: fake.sampleBody('POST', '/api/admin/nests/{nest}/eggs'),
        ('Nest', 'importEgg'): lambda: {'data': egg_import()},
        ('Egg', 'updateFromImport'): lambda: {'data': egg_import()},
        ('DatabaseAgentTemplateManager', 'createTemplate'): lambda: fake.sampleBody('POST', '/api/admin/database-agent-templates'),
        ('DatabaseAgentTemplate', 'updateInstances'): lambda: fake.sampleBody('POST', '/api/admin/database-agent-templates/{database_agent_template}/instances/update'),
        ('OAuthProviderManager', 'createProvider'): lambda: fake.sampleBody('POST', '/api/admin/oauth-providers'),
        ('OAuthProvider', 'createMapping'): mapping,
        ('OAuthProvider', 'updateMapping'): lambda: {'mapping_id': UUID, **mapping()},
        ('EggConfigurationManager', 'createEggConfiguration'): lambda: {
            'name': 'test', 'matcher': fake.sampleBody('POST', '/api/admin/egg-configurations')['matcher'],
        },
    }


def argFor(param):
    name = param.name
    if name in VALUES:
        return VALUES[name]
    if name.endswith('_ids'):
        return [UUID]
    if name.endswith('_id') or name in ID_NAMES:
        return UUID
    return 'sample'


def exerciseAll(panel, fake):
    '''
    Returns (calls_ok, errors). Every object reachable from `panel` gets each
    public method called once.
    '''
    upload_path = os.path.join(tempfile.mkdtemp(), 'upload.bin')
    with open(upload_path, 'wb') as f:
        f.write(b'data')
    custom = overrides(fake, upload_path)

    server = panel.servers.getServer(UUID)
    minecraft = panel.servers.getMinecraftServer(UUID)
    queue = [panel, panel.servers, panel.account, panel.auth, panel.admin, server, minecraft]
    queue += [getattr(server, attr) for attr in ('files', 'backups', 'databases', 'schedules', 'users', 'network', 'tunnel')]
    queue += [value for attr, value in vars(panel.admin).items() if attr not in ('panel', 'api')]
    queue.append(DatabaseExplorer(panel, panel.api.databases.databasePath(UUID, UUID)))
    seen = {type(server), type(minecraft)}

    calls_ok = 0
    errors = []
    for obj in queue:
        cls = obj.__class__
        for name, member in inspect.getmembers(cls, predicate=inspect.isfunction):
            if name.startswith('_') or name in SKIP:
                continue
            kwargs = {}
            for param in list(inspect.signature(member).parameters.values())[1:]:
                if param.kind in (param.VAR_KEYWORD, param.VAR_POSITIONAL) or param.default is not param.empty:
                    continue
                kwargs[param.name] = argFor(param)
            extra = custom.get((cls.__name__, name), {})
            kwargs.update(extra() if callable(extra) else extra)

            try:
                result = getattr(obj, name)(**kwargs)
                calls_ok += 1
            except Exception as e:
                if (cls.__name__, name) in EXPECTED_ERRORS:
                    calls_ok += 1
                    continue
                trace = ''.join(traceback.format_tb(e.__traceback__)[-2:])
                errors.append(f'{cls.__name__}.{name}({", ".join(kwargs)}): {type(e).__name__}: {e}\n{trace}')
                continue

            items = list(result) if isinstance(result, (list, Page)) else [result]
            for item in items[:1]:
                if isinstance(item, Model) and item.__class__ not in seen:
                    seen.add(item.__class__)
                    queue.append(item)
    return calls_ok, errors
