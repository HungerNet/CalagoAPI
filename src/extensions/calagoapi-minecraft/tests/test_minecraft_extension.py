'''enable('minecraft'), panel.minecraft, configuration, installBridge() and AsyncPanel.'''
import asyncio

import pytest

from calagoapi import AsyncPanel, Panel, Server
from calagoapi.aio import AsyncWrapper
from calagoapi.extensions import ConfigurationError
from contract import BASE, UUID
from hungerbridge import BridgeRelease, HungerBridgeNotFound

from calagoapi_minecraft import AsyncMinecraftServer, MinecraftExtension, MinecraftManager, MinecraftServer, settings
from minecraft_testing import SECRET, TOKEN, TOKEN_ID, bridgeRequests


def test_enable_adds_panel_minecraft(mc, panel, bridge):
    mc.enable('minecraft', config={**TOKEN, 'bridge_url': bridge})
    assert mc.ownerOf(Panel, 'minecraft') == 'minecraft'
    assert isinstance(panel.minecraft, MinecraftManager) and panel.minecraft is panel.minecraft
    assert not hasattr(panel.minecraft, 'versionChanger')

    server = panel.minecraft.getServer(UUID, address='play.example.com')
    assert type(server) is MinecraftServer and server.getAddress() == 'play.example.com:25565'
    assert server.bridge.getPlayerCount() == 2              # token and URL from the config
    assert server.getBridgeUrl() == bridge

    servers = panel.minecraft.getServers()
    assert servers and all(type(s) is MinecraftServer for s in servers)
    converted = panel.minecraft.fromServer(panel.servers.getServer(UUID), bridge_token_id=TOKEN_ID, bridge_token_secret=SECRET)
    assert type(converted) is MinecraftServer and converted.data == panel.servers.getServer(UUID).data


def test_settings_without_enable(panel):
    assert settings()['bridge_port'] == 1913 and settings()['bridge_token_id'] is None
    assert 'bridge_token' not in settings() and 'auto_backup' not in settings() and 'github_api' not in settings()
    with pytest.raises(TypeError):
        settings()['bridge_port'] = 1    # read-only


def test_config_reaches_servers(mc, panel):
    mc.enable('minecraft', config={'bridge_port': 2000, 'stream_reconnect': False, 'bridge_timeout': (1, 2)})
    server = MinecraftServer(panel, UUID, address='play.example.com', **TOKEN)
    assert server.getBridgeUrl() == 'http://play.example.com:2000'
    assert server.bridge.transport.timeout == (1, 2) and server.bridge.transport.max_retries == 2


@pytest.mark.parametrize('config, message', [
    ({'bridge_token_id': 'bot'}, 'both'),
    ({'bridge_token_secret': SECRET}, 'both'),
    ({'bridge_token_id': 'bot', 'bridge_token_secret': 'not-hex'}, '64 hex'),
    ({'bridge_token': f'bot:{SECRET}'}, 'bridge_token'),     # the combined form is an unknown key now
    ({'bridge_port': 70000}, 'bridge_port'),
    ({'bridge_port': True}, 'bridge_port'),
    ({'bridge_url': 'ftp://x'}, 'bridge_url'),
    ({'stream_reconnect': 'yes'}, 'stream_reconnect'),
    ({'bridge_max_retries': -1}, 'bridge_max_retries'),
    ({'auto_backup': True}, 'auto_backup'),                   # Version Changer config is gone
])
def test_invalid_config(mc, config, message):
    with pytest.raises(ConfigurationError, match=message):
        mc.enable('minecraft', config=config)


def test_secret_is_masked(mc):
    mc.enable('minecraft', config=TOKEN)
    assert SECRET not in mc.describe() and "'bridge_token_secret': '***'" in mc.describe()
    with pytest.raises(ConfigurationError) as error:
        mc.enable('minecraft', config={'bridge_token_id': 'x', 'bridge_token_secret': SECRET[:-2]})
    assert SECRET[:-2] not in str(error.value)


def test_metadata():
    assert MinecraftExtension.extension_id == 'minecraft'
    assert MinecraftExtension.metadata.package == 'calagoapi-minecraft'


@pytest.fixture
def modrinth(bridge, monkeypatch):
    monkeypatch.setattr('hungerbridge.releases.MODRINTH_API', f'{bridge}/modrinth')


def test_install_bridge_is_explicit_and_uses_modrinth(modrinth, panel, network, fake, monkeypatch):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID})
    listed = []
    monkeypatch.setattr(server.files, 'listFiles', lambda directory: listed.append(directory) or [])

    release = server.installBridge(minecraft_version='1.21.11', loader='purpur')
    assert isinstance(release, BridgeRelease)
    assert (release.version_number, release.loader, release.directory) == ('5-alpha.1', 'purpur', '/plugins')
    assert release.url == 'https://cdn.modrinth.com/data/p5/HungerBridge-paper-1.21.11-5-alpha.1.jar'
    assert listed == ['/plugins']
    assert ('POST', '/api/client/servers/{server}/files/pull') in fake.hit
    assert not fake.violations
    assert server.installBridge('26.1.2', 'fabric').directory == '/mods'

    with pytest.raises(TypeError):
        server.installBridge()                                   # nothing is detected any more
    with pytest.raises(ValueError, match='required'):
        server.installBridge(minecraft_version=None, loader='paper')
    with pytest.raises(ValueError, match='Loaders on Modrinth'):
        server.installBridge('1.21.11', 'forge')
    with pytest.raises(ValueError, match='Versions on Modrinth'):
        server.installBridge('1.20.4', 'paper')
    with pytest.raises(HungerBridgeNotFound, match='HungerBridge 5.x'):
        server.installBridge('26.2', 'paper')                    # only a protocol-v1 release exists
    with pytest.raises(HungerBridgeNotFound, match='version 9-alpha.1'):
        server.installBridge('1.21.11', 'paper', version='9-alpha.1')


def test_install_bridge_replaces_old_jars(modrinth, panel, network, monkeypatch):
    server = MinecraftServer(panel, UUID, data={'uuid': UUID})

    class F:
        def __init__(self, name):
            self.name = name

        def getName(self):
            return self.name

    monkeypatch.setattr(server.files, 'listFiles', lambda d: [F('HungerBridge-paper-3.0-alpha1+1.21.11.jar'), F('LuckPerms.jar'),
                                                               F('HungerBridge-paper-1.21.11-5-alpha.1.jar')])
    deleted = []
    monkeypatch.setattr(server.files, 'deleteFiles', lambda root, files: deleted.append((root, files)))
    server.installBridge('1.21.11', 'paper')
    assert deleted == [('/plugins', ['HungerBridge-paper-3.0-alpha1+1.21.11.jar'])]


def test_async(mc, fake, network, bridge):
    mc.enable('minecraft', config={**TOKEN, 'bridge_url': bridge})

    async def main():
        async with AsyncPanel(url=BASE, api_key='c7sp_test') as panel:
            server = await panel.minecraft.getServer(UUID)
            assert isinstance(server, AsyncMinecraftServer) and isinstance(server.target, MinecraftServer)
            assert isinstance(server.bridge, AsyncWrapper)
            assert await server.sendCommand('list') == 'ran: list\ndone'
            assert await server.bridge.getTPS('1m') == 19.9
            assert await server.getRAM() is not None
            players, mspt = await asyncio.gather(server.bridge.getPlayers(), server.bridge.getMSPT())
            assert players == ['Steve', 'Alex'] and mspt == 12.5
            lines = [line async for line in server.streamConsole(history=1, timeout=5, reconnect=False)]
            assert lines[0] == '[12:00:00] [Server thread/INFO]: history 0' and len(lines) == 3
            events = [event async for event in server.bridge.streamLogs(timeout=5, reconnect=False)]
            assert [e.message for e in events] == ['Steve joined the game', 'line one\nline two']

            seen = []

            async def collect(line):
                seen.append(line)

            stream = await server.onConsoleLine(collect, reconnect=False)
            for _ in range(250):
                if len(seen) == 2:
                    break
                await asyncio.sleep(0.02)
            await stream.disconnect()
            assert seen == ['[12:00:10] [Server thread/INFO]: Steve joined the game',
                            '[12:00:11] [Server thread/WARN]: [SomePlugin] line one\nline two']

            plain = await panel.servers.getServer(UUID)
            assert not isinstance(plain, AsyncMinecraftServer) and isinstance(plain.target, Server)

    asyncio.run(main())
    assert bridgeRequests('GET', '/server/stream')
