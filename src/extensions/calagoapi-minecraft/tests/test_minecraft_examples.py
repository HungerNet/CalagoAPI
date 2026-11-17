'''
Runs examples/minecraft/ (the code the Minecraft tutorials use) against the fake panel
and the fake HungerBridge, and checks each script is safe to run unconfigured.
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

from minecraft_testing import TOKEN

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
    return {'bridge_url': bridge, 'bridge_token': TOKEN}


def test_connect(enabled, panel):
    info = load('01_connect.py').main(panel, UUID, **enabled)
    assert info['platform'] == 'paper'


def test_commands_and_console(enabled, panel):
    output, joined = load('02_commands_and_console.py').main(panel, UUID, seconds=5, **enabled)
    assert output == 'ran: list\ndone'
    assert joined == ['[12:00:10 INFO]: Steve joined the game']


def test_monitoring(enabled, panel):
    warnings = load('03_monitoring.py').main(panel, UUID, **enabled)
    assert warnings == []


def test_async_welcome_bot(enabled, fake):
    module = load('04_async_welcome_bot.py')

    async def run():
        async with AsyncPanel(url=BASE, api_key='c7sp_test') as panel:
            return await module.main(panel, UUID, seconds=2, **enabled)

    greeted, samples = asyncio.run(run())
    assert greeted == ['Steve'] and samples == [20.0]


@pytest.mark.parametrize('path', SCRIPTS, ids=os.path.basename)
def test_scripts_run_unconfigured(path):
    env = {k: v for k, v in os.environ.items() if k != 'CALAGOPUS_URL'}
    env['PYTHONPATH'] = os.pathsep.join([os.path.join(ROOT, 'src'), os.path.dirname(os.path.dirname(__file__)),
                                         env.get('PYTHONPATH', '')])
    result = subprocess.run([sys.executable, path], capture_output=True, text=True, env=env, timeout=60)
    assert result.returncode == 0, result.stderr
    assert 'CALAGOPUS_URL' in result.stdout
