'''
calagoapi-hungerbridge: talk to the HungerBridge mod/plugin from CalagoAPI.

You do not need to import this package. Install it and enable it by id:

    from calagoapi.extensions import enable
    enable('hungerbridge', config={'token': 'bot:9f2c...'})
    server.hungerbridge.players()

HungerBridgeClient and HungerBridgeError can be imported for standalone use.
'''
from importlib.metadata import version as _pkg_version, PackageNotFoundError

try:
    __version__ = _pkg_version('calagoapi-hungerbridge')
except PackageNotFoundError:
    __version__ = '0.0.0'

from .client import HungerBridgeClient, HungerBridgeError  # noqa: E402

__all__ = ['HungerBridgeClient', 'HungerBridgeError', '__version__']
