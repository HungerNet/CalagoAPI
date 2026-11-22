'''
Configuration of calagoapi-minecraft.

`enable('minecraft', config={...})` sets process-wide defaults. Without enable(),
MinecraftServer uses DEFAULT_CONFIG. Per-server values (constructor arguments,
connectBridge()) always win.
'''
from types import MappingProxyType

from calagoapi.extensions import ConfigurationError, ExtensionNotEnabledError
from hungerbridge import Credentials


DEFAULT_CONFIG = {
    'bridge_url': None,            # None: the server's address with bridge_port
    'bridge_port': 1913,
    'bridge_token_id': None,       # token for every server; per server: connectBridge()
    'bridge_token_secret': None,   # its 64 hex character secret (masked in diagnostics)
    'bridge_timeout': None,        # seconds or (connect, read); None: HungerBridgePy's default (5, 30)
    'bridge_max_retries': 2,       # retries after HTTP 429, inside HungerBridgePy
    'stream_reconnect': True,      # default for streamConsole() and onConsoleLine()
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


def credentials(token_id, token_secret, where: str = 'bridge_token_id/bridge_token_secret'):
    '''
    Returns hungerbridge.Credentials for the pair, or None when both are None.

    Raises:
        ConfigurationError: only one of them is given, or HungerBridgePy rejects them
            (empty id, secret that is not 64 hex characters). The secret is never echoed.
    '''
    if token_id is None and token_secret is None:
        return None
    if token_id is None or token_secret is None:
        raise ConfigurationError(f'minecraft: {where}: give both the token id and the token secret')
    try:
        return Credentials(token_id=token_id, token_secret=token_secret)
    except ValueError as error:
        raise ConfigurationError(f'minecraft: {where}: {error}') from None


def validate(config: dict) -> dict:
    credentials(config['bridge_token_id'], config['bridge_token_secret'])
    port = config['bridge_port']
    if isinstance(port, bool) or not isinstance(port, int) or not 0 < port < 65536:
        raise ConfigurationError(f'minecraft: bridge_port must be 1-65535, got {port!r}')
    if config['bridge_url'] is not None and not str(config['bridge_url']).startswith(('http://', 'https://')):
        raise ConfigurationError(f'minecraft: bridge_url must start with http:// or https://, got {config["bridge_url"]!r}')
    if not isinstance(config['stream_reconnect'], bool):
        raise ConfigurationError('minecraft: stream_reconnect must be True or False')
    retries = config['bridge_max_retries']
    if isinstance(retries, bool) or not isinstance(retries, int) or retries < 0:
        raise ConfigurationError('minecraft: bridge_max_retries must be 0 or more')
    return config
