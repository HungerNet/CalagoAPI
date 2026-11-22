'''
Helpers that connect a MinecraftServer to its HungerBridge: client creation and the
console pickup line.

The HungerBridge protocol itself (signing, endpoints, streaming, releases) lives in
HungerBridgePy (`hungerbridge`); nothing here talks HTTP to the bridge directly.
'''
import re

from hungerbridge import BridgeClient, Credentials

from calagoapi_minecraft.config import settings


# The "Pickup URL" line printed by "hb token create" / "hb token rotate"
PICKUP_PATTERN = re.compile(r'(/pickup/[0-9A-Za-z-]+\?passkey=[0-9a-fA-F]+)')
ANSI_PATTERN = re.compile(r'\x1b\[[0-9;?]*[ -/]*[@-~]')


def newClient(url: str, credentials: Credentials, **options) -> BridgeClient:
    '''Creates a HungerBridgePy client with the configured timeout and retries; options win.'''
    config = settings()
    kwargs = {'max_retries': config['bridge_max_retries']}
    if config['bridge_timeout'] is not None:
        kwargs['timeout'] = config['bridge_timeout']
    kwargs.update(options)
    return BridgeClient(url, token_id=credentials.token_id, token_secret=credentials.token_secret, **kwargs)


def findPickup(line: str):
    '''Returns "/pickup/<id>?passkey=<hex>" from a console line, or None.'''
    match = PICKUP_PATTERN.search(ANSI_PATTERN.sub('', line or ''))
    return match.group(1) if match else None
