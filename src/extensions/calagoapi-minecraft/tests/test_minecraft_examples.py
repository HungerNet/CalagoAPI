'''
Runs examples/minecraft/ (the code the Minecraft tutorials use) against the fake panel,
the fake HungerBridge and the fake Modrinth, and checks each script is safe to run
unconfigured.
'''
import asyncio
import glob
import importlib.util
import os
import subprocess
import sys

import pytest

from calagoapi import AsyncPanel
from contract import BASE, UUID

from minecraft_testing import TOKEN, FakeBridge, logEvent, ready

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
EXAMPLES = os.path.join(ROOT, 'examples', 'minecraft')
SCRIPTS = sorted(glob.glob(os.path.join(EXAMPLES, '[0-9]*.py')))


def load(name):
    sys.path.insert(0, EXAMPLES)
    try:
        spec = importlib.util.spec_from_file_location(f'minecraft_example_{name[:2]}', os.path.join(EXAMPLES, name))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(EXAMPLES)


@pytest.fixture
def enabled(mc, bridge):
    mc.enable('minecraft', config={'stream_reconnect': False})
    return {'bridge_url': bridge, **TOKEN}


def test_connect(enabled, panel):
    info = load('01_connect.py').main(panel, UUID, **enabled)
    assert info['platform'] == 'paper' and info['protocol_version'] == 2


def test_commands_and_console(enabled, panel):
    output, joined = load('02_commands_and_console.py').main(panel, UUID, seconds=5, **enabled)
    assert output == 'ran: list\ndone'
    assert joined == ['[12:00:10] [Server thread/INFO]: Steve joined the game']


def test_monitoring(enabled, panel):
    assert load('03_monitoring.py').main(panel, UUID, **enabled) == []


def test_async_welcome_bot(enabled, fake):
    module = load('04_async_welcome_bot.py')

    async def run():
        async with AsyncPanel(url=BASE, api_key='c7sp_test') as panel:
            return await module.main(panel, UUID, seconds=2, **enabled)

    greeted, samples = asyncio.run(run())
    assert greeted == ['Steve'] and samples == [20.0]


def test_install_bridge(enabled, panel, bridge, monkeypatch):
    monkeypatch.setattr('hungerbridge.releases.MODRINTH_API', f'{bridge}/modrinth')
    release = load('05_install_bridge.py').main(panel, UUID, '1.21.11', 'paper', **enabled)
    assert release.version_number == '5-alpha.1' and release.directory == '/plugins'


def test_bot_logging(enabled, panel):
    def ownLines(handler, history):
        handler.sse(logEvent(1, 'starting nightly maintenance', thread='HungerBridge', logger='NightlyBot')
                    + logEvent(2, 'unrelated')
                    + logEvent(3, 'world saved', level='BACKUP', thread='Backups', logger='NightlyBot')
                    + logEvent(4, 'maintenance in 5 minutes', thread='HungerBridge', logger='NightlyBot')
                    + ready(4, 4))

    FakeBridge.stream_script = ownLines
    relayed, lines = load('06_bot_logging.py').main(panel, UUID, seconds=2, **enabled)
    assert relayed == 'System chat: maintenance in 5 minutes'   # the fake bridge does not normalize
    assert lines[1] == '[12:00:03] [Backups/BACKUP]: [NightlyBot] world saved'


@pytest.mark.parametrize('path', SCRIPTS, ids=os.path.basename)
def test_scripts_run_unconfigured(path):
    env = {k: v for k, v in os.environ.items() if k != 'CALAGOPUS_URL'}
    env['PYTHONPATH'] = os.pathsep.join([os.path.join(ROOT, 'src'), os.path.dirname(os.path.dirname(__file__)),
                                         env.get('PYTHONPATH', '')])
    result = subprocess.run([sys.executable, path], capture_output=True, text=True, env=env, timeout=60)
    assert result.returncode == 0, result.stderr
    assert 'CALAGOPUS_URL' in result.stdout
