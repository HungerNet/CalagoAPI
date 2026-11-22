'''
The `minecraft` CalagoAPI extension.

    from calagoapi.extensions import enable

    enable('minecraft', config={'bridge_token': 'bot:9f2c...'})
    server = panel.minecraft.getServer('abc123')

enable() adds `panel.minecraft` (MinecraftManager) and sets process-wide defaults for
every MinecraftServer (see calagoapi_minecraft.config.DEFAULT_CONFIG).
'''
from calagoapi.extensions import Extension, ExtensionMetadata

from calagoapi_minecraft import __version__
from calagoapi_minecraft.config import DEFAULT_CONFIG, validate
from calagoapi_minecraft.manager import MinecraftManager


class MinecraftExtension(Extension):
    '''
    Minecraft for CalagoAPI: MinecraftServer, the Version Changer and HungerBridge
    (through HungerBridgePy).

    Config (all optional):
        bridge_url: HungerBridge URL for every server. None uses each server's address
            with bridge_port.
        bridge_port: HungerBridge port, default 1913.
        bridge_token: "tokenId:secret" for every server (per server: connectBridge()).
        bridge_timeout: Seconds or (connect, read); None uses HungerBridgePy's (5, 30).
        bridge_max_retries: Retries after HTTP 429, default 2.
        stream_reconnect: Default reconnect for streamConsole()/onConsoleLine(), default True.
        auto_backup: Back up before server.versions.install(), default False.
        backup_name, backup_timeout: That backup's name and how long to wait for it.
        release: HungerBridge release used by installBridge(), default 'latest'.
        repository, github_api: Where HungerBridge releases are published.
    '''
    extension_id = 'minecraft'
    metadata = ExtensionMetadata(
        author='iFamished',
        version=__version__,
        schema=1,
        description='Minecraft servers for CalagoAPI: HungerBridge, Version Changer, server.properties',
        package='calagoapi-minecraft',
        homepage='https://github.com/HungerNet/CalagoAPI/tree/main/src/extensions/calagoapi-minecraft',
    )
    default_mode = 'direct'
    default_config = DEFAULT_CONFIG
    secret_config = ('bridge_token',)
    members = [MinecraftManager]

    def validateConfig(self, config):
        return validate(config)
