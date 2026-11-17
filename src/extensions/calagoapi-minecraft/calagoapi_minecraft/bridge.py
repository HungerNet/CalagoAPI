'''
Helpers that connect a MinecraftServer to its HungerBridge: client creation, console
pickup parsing and loader/version detection for installBridge().

The HungerBridge protocol itself (signing, endpoints, streaming, release names) lives
in HungerBridgePy (`hungerbridge`); nothing here talks HTTP to the bridge directly.
'''
import re

from hungerbridge import BridgeClient
from hungerbridge.releases import loader_for

from calagoapi.utils.exceptions import CalagoAPIError

from calagoapi_minecraft.config import settings


# "Token created. Retrieve it at: /pickup/<uuid>?passkey=<hex>" (also printed by "hb token rotate")
PICKUP_PATTERN = re.compile(r'(/pickup/[0-9A-Za-z-]+\?passkey=[0-9a-fA-F]+)')
ANSI_PATTERN = re.compile(r'\x1b\[[0-9;]*[A-Za-z]')

# startup variables eggs commonly use for the Minecraft version
VERSION_VARIABLES = ('MINECRAFT_VERSION', 'MC_VERSION', 'VERSION')


def newClient(url: str, token: str, **options) -> BridgeClient:
    '''Creates a HungerBridgePy client with the configured timeout and retries; options win.'''
    config = settings()
    kwargs = {'max_retries': config['bridge_max_retries']}
    if config['bridge_timeout'] is not None:
        kwargs['timeout'] = config['bridge_timeout']
    kwargs.update(options)
    return BridgeClient(url, token, **kwargs)


def closeClient(client) -> None:
    session = getattr(getattr(client, 'transport', None), 'session', None)
    if session is not None:
        session.close()


def findPickup(line: str):
    '''Returns "/pickup/<id>?passkey=<hex>" from a console line, or None.'''
    match = PICKUP_PATTERN.search(ANSI_PATTERN.sub('', line or ''))
    return match.group(1) if match else None


def detectPlatform(server, loader=None, minecraft_version=None):
    '''
    Returns (loader, minecraft_version) for installBridge(). Unknown values stay None.

    Sources, first match wins: the arguments, the Version Changer's installed build, a
    reachable bridge (/server/meta), then the egg name and startup variables.
    '''
    def fill(found_loader, found_version):
        nonlocal loader, minecraft_version
        loader = loader or loader_for(found_loader)
        minecraft_version = minecraft_version or found_version

    if loader is not None:
        # server types such as 'PAPER' or 'PURPUR' -> 'paper'; unknown values are left for
        # find_release() to reject with a clear message
        loader = loader_for(loader) or loader

    if loader is None or minecraft_version is None:
        try:
            build = server.versions.getInstalledBuild() or {}
            fill(build.get('type'), build.get('version_id'))
        except CalagoAPIError:
            pass  # Version Changer not installed on the panel
    if (loader is None or minecraft_version is None) and server.hasBridge():
        try:
            meta = server.bridge.getServerMeta()
            fill(meta.get('platform'), meta.get('minecraft_version'))
        except Exception:
            pass  # bridge not running (yet)
    if loader is None or minecraft_version is None:
        egg = (server.getEggName() or '').lower()
        fill(next((word for word in re.split(r'[^a-z]+', egg) if loader_for(word)), None), None)
        if minecraft_version is None:
            for variable in server.getStartupVariables():
                value = str(variable.get('value') or '')
                if variable.get('env_variable') in VERSION_VARIABLES and re.fullmatch(r'\d+\.\d+(\.\d+)?', value):
                    minecraft_version = value
                    break
    return loader, minecraft_version
