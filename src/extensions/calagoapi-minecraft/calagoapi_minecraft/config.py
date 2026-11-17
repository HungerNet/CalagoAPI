'''
Configuration of calagoapi-minecraft.

`enable('minecraft', config={...})` sets process-wide defaults. Without enable(),
MinecraftServer uses DEFAULT_CONFIG. Per-server values (constructor arguments,
connectBridge()) always win.
'''
from types import MappingProxyType

from calagoapi.extensions import ConfigurationError, ExtensionNotEnabledError
from hungerbridge.auth import Credentials


DEFAULT_CONFIG = {
    # HungerBridge connection
    'bridge_url': None,           # None: the server's address with bridge_port
    'bridge_port': 1913,
    'bridge_token': None,         # 'tokenId:secret'
    'bridge_timeout': None,       # seconds or (connect, read); None: HungerBridgePy's default (5, 30)
    'bridge_max_retries': 2,      # retries after HTTP 429, inside HungerBridgePy
    'stream_reconnect': True,     # default for streamConsole() and onConsoleLine()
    # Version Changer
    'auto_backup': False,         # back up before server.versions.install()
    'backup_name': 'Before version change',
    'backup_timeout': 3600,
    # installBridge()
    'release': 'latest',
    'repository': 'HungerNet/HungerBridge',
    'github_api': 'https://api.github.com',
}


def settings():
    '''
    Returns the effective configuration (read-only): the enabled extension's config,
    or DEFAULT_CONFIG when enable('minecraft') was not called.

    Example:
        from calagoapi_minecraft import settings
        print(settings()['bridge_port'])
    '''
    from calagoapi_minecraft.extension import MinecraftExtension

    try:
        return MinecraftExtension.get().config
    except ExtensionNotEnabledError:
        return MappingProxyType(dict(DEFAULT_CONFIG))


def checkToken(token, where: str = 'bridge_token'):
    '''Raises ConfigurationError unless token is None or "tokenId:secret" with a hex secret.'''
    if token is None:
        return
    credentials = Credentials.parse(token) if isinstance(token, str) else None
    if credentials is None:
        raise ConfigurationError(f'minecraft: {where} must look like "tokenId:secret", got a {type(token).__name__}')
    try:
        bytes.fromhex(credentials.secret)
    except ValueError:
        raise ConfigurationError(f'minecraft: the secret in {where} must be the 64 hex characters from the pickup') from None


def validate(config: dict) -> dict:
    checkToken(config['bridge_token'])
    port = config['bridge_port']
    if isinstance(port, bool) or not isinstance(port, int) or not 0 < port < 65536:
        raise ConfigurationError(f'minecraft: bridge_port must be 1-65535, got {port!r}')
    if config['bridge_url'] is not None and not str(config['bridge_url']).startswith(('http://', 'https://')):
        raise ConfigurationError(f'minecraft: bridge_url must start with http:// or https://, got {config["bridge_url"]!r}')
    for key in ('auto_backup', 'stream_reconnect'):
        if not isinstance(config[key], bool):
            raise ConfigurationError(f'minecraft: {key} must be True or False')
    timeout = config['backup_timeout']
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or timeout <= 0:
        raise ConfigurationError('minecraft: backup_timeout must be a positive number of seconds')
    retries = config['bridge_max_retries']
    if isinstance(retries, bool) or not isinstance(retries, int) or retries < 0:
        raise ConfigurationError('minecraft: bridge_max_retries must be 0 or more')
    return config
