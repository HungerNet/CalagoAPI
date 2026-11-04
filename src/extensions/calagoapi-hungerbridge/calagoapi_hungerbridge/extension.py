'''
HungerBridge as a CalagoAPI extension: `server.hungerbridge` talks to the
HungerBridge mod/plugin running inside a Minecraft server.

    from calagoapi.extensions import enable

    enable('hungerbridge', config={'token': 'bot:9f2c...'})
    print(server.hungerbridge.players())
    print(server.hungerbridge.tps())
'''
import re
import threading

import requests

from calagoapi import MinecraftServer
from calagoapi.extensions import ConfigurationError, Extension, ExtensionMetadata, class_extension

from calagoapi_version_changer.extension import getInstalledVersion

from calagoapi_hungerbridge import __version__
from calagoapi_hungerbridge.client import HungerBridgeClient, HungerBridgeError, parseToken


# Version Changer server types -> HungerBridge loader
LOADERS = {
    'PAPER': 'paper', 'PURPUR': 'paper', 'FOLIA': 'paper', 'PUFFERFISH': 'paper', 'LEAVES': 'paper',
    'SPIGOT': 'paper', 'FABRIC': 'fabric', 'QUILT': 'fabric',
}

# where each loader looks for the jar
DIRECTORIES = {'paper': '/plugins', 'fabric': '/mods'}


def _versionKey(version):
    return tuple(int(part) if part.isdigit() else 0 for part in re.split(r'[.\-]', version))


@class_extension(MinecraftServer, 'hungerbridge')
class HungerBridge:
    '''
    The HungerBridge API of one Minecraft server, available as `server.hungerbridge`.

    The bridge URL defaults to the server's address with the configured port
    (1913); set `url` in the extension config, or call connect() per server.

    Example:
        enable('hungerbridge', config={'token': 'bot:9f2c...'})
        server.hungerbridge.players()          # ['Steve', 'Alex']
        server.hungerbridge.run('say hi')      # console output lines
    '''
    def __init__(self, server):
        self.server = server
        self._url = None
        self._token = None
        self._client = None
        self._lock = threading.Lock()

    def __repr__(self):
        return f'<HungerBridge of {self.server!r}>'

    # connection
    def connect(self, url: str = None, token: str = None) -> 'HungerBridge':
        '''
        Sets the bridge URL and/or token for this server only (overrides the extension config).

        Example:
            server.hungerbridge.connect('http://10.0.0.5:1913', 'bot:9f2c...')
        '''
        if token is not None:
            parseToken(token)
        with self._lock:
            if url is not None:
                self._url = url.rstrip('/')
            if token is not None:
                self._token = token
            if self._client is not None:
                self._client.close()
            self._client = None
        return self

    def getUrl(self) -> str:
        '''Returns the bridge URL used for this server.'''
        if self._url:
            return self._url
        config = HungerBridgeExtension.get().config
        if config['url']:
            return config['url'].rstrip('/')
        host = self.server.getAddress().rsplit(':', 1)[0]
        return f'http://{host}:{config["port"]}'

    @property
    def client(self) -> HungerBridgeClient:
        '''The HungerBridgeClient used for requests (created on first use).'''
        with self._lock:
            if self._client is None:
                config = HungerBridgeExtension.get().config
                self._client = HungerBridgeClient(self.getUrl(), self._token or config['token'],
                                                  timeout=config['timeout'], verify=config['verify'])
            return self._client

    def close(self) -> None:
        '''Closes the HTTP connections to the bridge.'''
        with self._lock:
            if self._client is not None:
                self._client.close()
                self._client = None

    # health
    def ping(self) -> int:
        '''Returns the bridge's server time in milliseconds.'''
        return self.client.get('/ping').get('server_time')

    def isReachable(self) -> bool:
        '''Returns True if the bridge answers.'''
        try:
            self.ping()
            return True
        except HungerBridgeError:
            return False

    def authCheck(self) -> dict:
        '''Returns the token's id, policy and permissions.'''
        return self.client.get('/auth/check')

    def status(self) -> dict:
        '''Returns the runtime status of the Minecraft server.'''
        return self.client.get('/server/status')

    def info(self) -> dict:
        '''Returns bridge metadata (version, platform, Minecraft version).'''
        return self.client.get('/server/info')

    def meta(self) -> dict:
        '''Returns server metadata.'''
        return self.client.get('/server/meta')

    # players
    def players(self) -> list:
        '''Returns the names of the online players.'''
        return self.client.get('/players/list').get('players', [])

    def playerCount(self) -> int:
        '''Returns how many players are online.'''
        return self.client.get('/players/list').get('count', 0)

    # console
    def run(self, command: str, silent: bool = False, show_console: bool = False) -> list:
        '''
        Runs a console command and returns its output lines (empty when silent).

        Example:
            server.hungerbridge.run('list')
        '''
        result = self.client.post('/server/run', {'command': command, 'silent': silent, 'show_console': show_console})
        return result.get('output') or []

    def log(self, message: str, level: str = 'INFO', thread: str = None) -> None:
        '''Writes a line to the server log (any level name, e.g. 'INFO', 'WARN', 'BRIDGE').'''
        body = {'message': message, 'level': level}
        if thread:
            body['thread'] = thread
        self.client.post('/server/log', body)

    def stop(self) -> dict:
        '''Stops the Minecraft server (the panel restarts it if configured to).'''
        return self.client.post('/server/stop', {})

    # performance
    def tps(self) -> dict:
        '''Returns ticks per second: tps, tps_1m, tps_5m, tps_15m.'''
        return self.client.get('/world/tps')

    def mspt(self) -> float:
        '''Returns milliseconds per tick.'''
        return self.client.get('/world/mspt').get('mspt')

    def chunks(self) -> dict:
        '''Returns loaded chunks per world and in total.'''
        return self.client.get('/world/chunks')

    def entities(self) -> dict:
        '''Returns entities per world and in total.'''
        return self.client.get('/world/entities')

    def time(self):
        '''Returns the world time.'''
        return self.client.get('/world/time').get('time')

    def weather(self):
        '''Returns the world weather.'''
        return self.client.get('/world/weather').get('weather')

    # system
    def uptime(self) -> int:
        '''Returns the JVM uptime in milliseconds.'''
        return self.client.get('/system/uptime').get('uptime_ms')

    def cpu(self) -> dict:
        '''Returns CPU load and processor count.'''
        return self.client.get('/system/cpu')

    def memory(self) -> dict:
        '''Returns heap, non-heap, JVM and process memory in bytes.'''
        return self.client.get('/system/memory')

    def gc(self) -> dict:
        '''Returns garbage collector statistics.'''
        return self.client.get('/system/gc')

    def threads(self) -> dict:
        '''Returns JVM thread counts.'''
        return self.client.get('/system/threads')

    def network(self) -> dict:
        '''Returns network throughput.'''
        return self.client.get('/system/network')

    def disk(self) -> dict:
        '''Returns disk usage of the server directory.'''
        return self.client.get('/system/disk')

    # installation
    def findRelease(self, mc_version: str = None, loader: str = None, release: str = None) -> dict:
        '''
        Finds the HungerBridge jar for a Minecraft version and loader on GitHub releases.

        Args:
            mc_version: e.g. '1.21.11', or 'latest' for the newest one in the release.
            loader: 'paper' or 'fabric'.
            release: Release tag, or None for the configured release ('latest' by default).

        Returns:
            dict with name, url, mc_version, loader and release.
        '''
        config = HungerBridgeExtension.get().config
        release = release or config['release']
        repository = config['repository']
        api = config['github_api'].rstrip('/')
        path = 'releases/latest' if release == 'latest' else f'releases/tags/{release}'
        try:
            r = requests.get(f'{api}/repos/{repository}/{path}', timeout=config['timeout'],
                             headers={'Accept': 'application/vnd.github+json'})
        except requests.RequestException as e:
            raise HungerBridgeError(f'Could not reach GitHub to find HungerBridge releases: {e}') from e
        if r.status_code >= 400:
            raise HungerBridgeError(f'GitHub release {release!r} of {repository} not found (HTTP {r.status_code})', r.status_code)
        data = r.json()

        jars = []
        for asset in data.get('assets', []):
            name = asset.get('name', '')
            lowered = name.lower()
            if not lowered.endswith('.jar') or 'sources' in lowered or loader not in lowered:
                continue
            # names look like "...-paper-1.21.11+4-alpha.34.jar": the version follows the loader
            found = re.search(r'(?<![\d.])(\d+\.\d+(?:\.\d+)?)(?![\d.])', lowered.split(loader, 1)[1])
            if found:
                jars.append((found.group(1), asset))
        if not jars:
            raise HungerBridgeError(f'Release {data.get("tag_name")} of {repository} has no {loader} jar')

        if mc_version == 'latest':
            mc_version, asset = max(jars, key=lambda j: _versionKey(j[0]))
        else:
            matches = [asset for version, asset in jars if version == mc_version]
            if not matches:
                supported = ', '.join(sorted({v for v, _ in jars}, key=_versionKey))
                raise HungerBridgeError(
                    f'HungerBridge {data.get("tag_name")} has no {loader} build for Minecraft {mc_version}. '
                    f'Available: {supported}')
            asset = matches[0]
        return {'name': asset['name'], 'url': asset['browser_download_url'], 'mc_version': mc_version,
                'loader': loader, 'release': data.get('tag_name')}

    def install(self, mc_version: str = None, loader: str = None, release: str = None) -> dict:
        '''
        Downloads the matching HungerBridge jar into /plugins (Paper, Purpur, ...)
        or /mods (Fabric). The loader and Minecraft version are read from the
        Version Changer unless given. Restart the server afterwards.

        Args:
            mc_version: Minecraft version; defaults to the `mc_version` config
                ('auto' = the installed version).
            loader: 'paper' or 'fabric'; detected from the installed server type.
            release: HungerBridge release tag, defaults to the `release` config.

        Returns:
            The release asset that was installed (see findRelease()).

        Example:
            server.hungerbridge.install()
            server.restart()
        '''
        config = HungerBridgeExtension.get().config
        mc_version = mc_version or config['mc_version']
        build = None
        if loader is None or mc_version == 'auto':
            # the version_changer dependency's function, called directly so it works in either of its modes
            installed = getInstalledVersion(self.server)
            build = (installed or {}).get('build') or {}
        if loader is None:
            loader = LOADERS.get(str(build.get('type', '')).upper())
            if loader is None:
                raise HungerBridgeError(
                    f'Cannot tell which HungerBridge build fits server type {build.get("type")!r}. '
                    f'Pass loader="paper" or loader="fabric".')
        if loader not in DIRECTORIES:
            raise HungerBridgeError(f'loader must be "paper" or "fabric", got {loader!r}')
        if mc_version == 'auto':
            mc_version = build.get('version_id')
            if not mc_version:
                raise HungerBridgeError('The installed Minecraft version is unknown. Pass mc_version="1.21.11".')

        asset = self.findRelease(mc_version, loader, release)
        self.server.files.pullFile(asset['url'], DIRECTORIES[loader], name=asset['name'])
        return asset


class HungerBridgeExtension(Extension):
    '''
    HungerBridge for CalagoAPI: run commands, read players, TPS, memory, ... through
    the HungerBridge mod/plugin, and install it on servers.

    Config:
        url: Bridge URL for every server, e.g. "http://10.0.0.5:1913". None (default)
            uses each server's address with `port`.
        port: Bridge port, default 1913.
        token: "tokenId:secret" used for every server (per server: connect()).
        timeout: Request timeout in seconds.
        verify: Verify TLS certificates.
        mc_version: Minecraft version used by install(): 'auto' (installed version),
            'latest', or e.g. '1.21.11'.
        release: HungerBridge release tag used by install(), default 'latest'.
        repository: GitHub repository of HungerBridge releases.
        github_api: GitHub API URL (GitHub Enterprise or a mirror).
    '''
    extension_id = 'hungerbridge'
    aliases = ['hunger_bridge']
    metadata = ExtensionMetadata(
        author='iFamished',
        version=__version__,
        schema=1,
        description='HungerBridge client for CalagoAPI',
        package='calagoapi-hungerbridge',
        homepage='https://github.com/hungernet/hungerbridge',
    )
    dependencies = ['version_changer']
    default_mode = 'namespace'
    default_config = {
        'url': None,
        'port': 1913,
        'token': None,
        'timeout': 10,
        'verify': True,
        'mc_version': 'auto',
        'release': 'latest',
        'repository': 'hungernet/hungerbridge',
        'github_api': 'https://api.github.com',
    }
    secret_config = ('token',)

    def validate_config(self, config):
        if config['token'] is not None:
            try:
                parseToken(config['token'])
            except ValueError as e:
                raise ConfigurationError(f'hungerbridge: {e}') from None
        if not isinstance(config['port'], int) or not 0 < config['port'] < 65536:
            raise ConfigurationError(f'hungerbridge: port must be 1-65535, got {config["port"]!r}')
        if not isinstance(config['mc_version'], str):
            raise ConfigurationError('hungerbridge: mc_version must be a string like "1.21.11", "auto" or "latest"')
        return config
