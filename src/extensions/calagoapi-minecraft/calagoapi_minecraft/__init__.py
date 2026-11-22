'''
calagoapi-minecraft: Minecraft servers for CalagoAPI.

`MinecraftServer` is a `calagoapi.Server` with Minecraft features. Commands with
output, console streaming and everything else inside the game go through HungerBridge
(the plugin/mod) using HungerBridgePy (`server.bridge`); power, resources and files stay
on the panel.

    from calagoapi import Panel
    from calagoapi.extensions import enable

    enable('minecraft', config={'bridge_token_id': 'bot', 'bridge_token_secret': '9f2c...'})
    panel = Panel(url='https://panel.example.com', api_key='...')

    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')
    print(server.sendCommand('list'))
    print(server.bridge.getTPS('1m'))
    for line in server.streamConsole(history=10, timeout=30):
        print(line)

MinecraftServer also works without enable():
MinecraftServer(panel, 'abc123', bridge_token_id=..., bridge_token_secret=...).
'''
from importlib.metadata import version as _pkg_version, PackageNotFoundError

try:
    __version__ = _pkg_version('calagoapi-minecraft')
except PackageNotFoundError:
    __version__ = '0.0.0'

from .exceptions import BridgeNotConfiguredError, MinecraftError  # noqa: E402
from .config import DEFAULT_CONFIG, settings  # noqa: E402
from .server import DEFAULT_PORT, MinecraftServer  # noqa: E402
from .manager import MinecraftManager  # noqa: E402
from .extension import MinecraftExtension  # noqa: E402
from .aio import AsyncMinecraftServer  # noqa: E402  (also registers the async wrappers)

__all__ = [
    '__version__',
    'MinecraftServer',
    'MinecraftManager',
    'MinecraftExtension',
    'AsyncMinecraftServer',
    'MinecraftError',
    'BridgeNotConfiguredError',
    'DEFAULT_CONFIG',
    'DEFAULT_PORT',
    'settings',
]
