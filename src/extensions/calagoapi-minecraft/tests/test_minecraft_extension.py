'''enable('minecraft'), panel.minecraft, configuration, installBridge() and AsyncPanel.'''
import asyncio

import pytest

from calagoapi import AsyncPanel, Panel, Server
from calagoapi.aio import AsyncWrapper
from calagoapi.extensions import ConfigurationError
from contract import BASE, UUID
from hungerbridge import HungerBridgeNotFound, ReleaseAsset

from calagoapi_minecraft import (
    AsyncMinecraftServer,
    MinecraftError,
    MinecraftExtension,
    MinecraftManager,
    MinecraftServer,
    VersionChangerAdmin,
    settings,
)
from calagoapi_minecraft import bridge as bridge_module
from minecraft_testing import SECRET, TOKEN, bridgeRequests


def test_enable_adds_panel_minecraft(mc, panel, bridge):
    mc.enable('minecraft', config={'bridge_token': TOKEN, 'bridge_url': bridge})
    assert mc.ownerOf(Panel, 'minecraft') == 'minecraft'
    assert isinstance(panel.minecraft, MinecraftManager) and panel.minecraft is panel.minecraft
    assert isinstance(panel.minecraft.versionChanger, VersionChangerAdmin)

    server = panel.minecraft.getServer(UUID, address='play.example.com')
    assert type(server) is MinecraftServer and server.getAddress() == 'play.example.com:25565'
    assert server.getPlayerCount() == 2              # token and URL from the config
    assert server.getBridgeUrl() == bridge

    servers = panel.minecraft.getServers()
    assert servers and all(type(s) is MinecraftServer for s in servers)
    converted = panel.minecraft.fromServer(panel.servers.getServer(UUID), bridge_token=TOKEN)
    assert type(converted) is MinecraftServer and converted.data == panel.servers.getServer(UUID).data


def test_settings_without_enable(panel):
    assert settings()['bridge_port'] == 1913 and settings()['bridge_token'] is None
    with pytest.raises(TypeError):
        settings()['bridge_port'] = 1    # read-only


def test_config_reaches_servers(mc, panel):
    mc.enable('minecraft', config={'bridge_port': 2000, 'stream_reconnect': False, 'bridge_timeout': (1, 2)})
    server = MinecraftServer(panel, UUID, address='play.example.com', bridge_token=TOKEN)
    assert server.getBridgeUrl() == 'http://play.example.com:2000'
    assert server.bridge.transport.timeout == (1, 2) and server.bridge.transport.max_retries == 2


@pytest.mark.parametrize('config, message', [
    ({'bridge_token': 'no-colon'}, 'tokenId:secret'),
    ({'bridge_token': 'bot:not-hex'}, 'hex'),
    ({'bridge_port': 70000}, 'bridge_port'),
    ({'bridge_port': True}, 'bridge_port'),
    ({'bridge_url': 'ftp://x'}, 'bridge_url'),
    ({'auto_backup': 'yes'}, 'auto_backup'),
    ({'backup_timeout': 0}, 'backup_timeout'),
    ({'bridge_max_retries': -1}, 'bridge_max_retries'),
    ({'bridge_tokn': TOKEN}, 'bridge_tokn'),
])
def test_invalid_config(mc, config, message):
    with pytest.raises(ConfigurationError, match=message):
        mc.enable('minecraft', config=config)


def test_token_is_masked(mc):
    mc.enable('minecraft', config={'bridge_token': TOKEN})
    assert SECRET not in mc.describe() and "'bridge_token': '***'" in mc.describe()
    with pytest.raises(ConfigurationError) as error:
        mc.enable('minecraft', config={'bridge_token': f'other:{SECRET}'})
    assert SECRET not in str(error.value)


def test_metadata():
    assert MinecraftExtension.extension_id == 'minecraft'
    assert MinecraftExtension.metadata.package == 'calagoapi-minecraft'


@pytest.fixture
def github(mc, bridge):
    mc.enable('minecraft', config={'github_api': bridge, 'bridge_url': bridge, 'bridge_token': TOKEN})


def test_install_bridge_detects_loader_and_version(github, panel, fake, monkeypatch):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID})
    monkeypatch.setattr(type(server.versions), 'getInstalledBuild',
                        lambda self: {'type': 'FABRIC', 'version_id': '26.1.2'})
    listed = []
    monkeypatch.setattr(server.files, 'listFiles', lambda directory: listed.append(directory) or [])

    asset = server.installBridge()
    assert asset == ReleaseAsset('HungerBridge-fabric-26.1.2-4-alpha.94.jar', 'https://github.example/fabric-26.1.2.jar',
                                 'fabric', '26.1.2', 'v4-alpha.94')
    assert listed == ['/mods']
    assert ('POST', '/api/client/servers/{server}/files/pull') in fake.hit
    assert not fake.violations

    assert server.installBridge('latest', 'PURPUR').name == 'HungerBridge-paper-26.2-4-alpha.94.jar'
    assert bridge_module.detectPlatform(server, 'PAPER', '1.21.11') == ('paper', '1.21.11')
    with pytest.raises(ValueError, match='loader'):
        server.installBridge('1.21.11', 'forge')
    assert server.findBridgeRelease('1.21.11', 'paper').url == 'https://github.example/paper-1.21.11.jar'
    with pytest.raises(HungerBridgeNotFound, match='Available: 1.21.11, 26.1.2, 26.2'):
        server.installBridge('1.20.4')
    with pytest.raises(HungerBridgeNotFound, match='not found'):
        server.installBridge(release='v0')


def test_install_bridge_replaces_old_jars(github, panel, monkeypatch):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID})

    class F:
        def __init__(self, name):
            self.name = name

        def getName(self):
            return self.name

    monkeypatch.setattr(server.files, 'listFiles', lambda d: [F('26.2-paper-4-alpha.93.jar'), F('LuckPerms.jar'),
                                                               F('HungerBridge-paper-1.21.11-4-alpha.94.jar')])
    deleted = []
    monkeypatch.setattr(server.files, 'deleteFiles', lambda root, files: deleted.append((root, files)))
    server.installBridge('1.21.11', 'paper')
    assert deleted == [('/plugins', ['26.2-paper-4-alpha.93.jar'])]


def test_install_bridge_detection_fallbacks(github, panel, monkeypatch):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID})
    monkeypatch.setattr(type(server.versions), 'getInstalledBuild', lambda self: None)
    # a running bridge reports platform and version
    assert bridge_module.detectPlatform(server) == ('paper', '1.21.11')

    offline = MinecraftServer(panel, UUID, data={'uuid': UUID})
    monkeypatch.setattr(offline, 'hasBridge', lambda: False)
    monkeypatch.setattr(offline, 'getEggName', lambda: 'Purpur (Minecraft)')
    monkeypatch.setattr(offline, 'getStartupVariables',
                        lambda: [{'env_variable': 'MINECRAFT_VERSION', 'value': '26.2'}])
    assert bridge_module.detectPlatform(offline) == ('paper', '26.2')

    monkeypatch.setattr(offline, 'getEggName', lambda: 'Vanilla')
    monkeypatch.setattr(offline, 'getStartupVariables', lambda: [])
    with pytest.raises(MinecraftError, match='Pass them'):
        offline.installBridge()


def test_async(mc, fake, network, bridge):
    mc.enable('minecraft', config={'bridge_token': TOKEN, 'bridge_url': bridge})

    async def main():
        async with AsyncPanel(url=BASE, api_key='c7sp_test') as panel:
            server = await panel.minecraft.getServer(UUID)
            assert isinstance(server, AsyncMinecraftServer) and isinstance(server.target, MinecraftServer)
            assert isinstance(server.versions, AsyncWrapper) and isinstance(server.bridge, AsyncWrapper)
            assert await server.sendCommand('list') == 'ran: list\ndone'
            assert await server.getTPS('1m') == 19.9
            assert await server.getRAM() is not None
            players, tps = await asyncio.gather(server.getPlayers(), server.getMSPT())
            assert players == ['Steve', 'Alex'] and tps == 12.5
            assert await server.bridge.getPlayerStats() == {'count': 2, 'max': 20, 'players': ['Steve', 'Alex']}
            lines = [line async for line in server.streamConsole(history=1, timeout=5, reconnect=False)]
            assert lines[0] == '[12:00:00 INFO]: history 0' and len(lines) == 3
            bridge_lines = [line async for line in server.bridge.streamLogs(timeout=5)]
            assert len(bridge_lines) == 2

            seen = []

            async def collect(line):
                seen.append(line)

            stream = await server.onConsoleLine(collect, reconnect=False)
            for _ in range(250):
                if len(seen) == 2:
                    break
                await asyncio.sleep(0.02)
            await stream.disconnect()
            assert seen == ['[12:00:10 INFO]: Steve joined the game', '[12:00:11 WARN]: line one\nline two']

            plain = await panel.servers.getServer(UUID)
            assert not isinstance(plain, AsyncMinecraftServer) and isinstance(plain.target, Server)

    asyncio.run(main())
    assert bridgeRequests('GET', '/server/stream')
