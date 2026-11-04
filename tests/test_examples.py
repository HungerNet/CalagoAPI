'''
Runs every example in examples/extensions/ in its own process, so they stay runnable.
'''
import glob
import os
import subprocess
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLES = sorted(glob.glob(os.path.join(ROOT, 'examples', 'extensions', '[0-9]*.py')))


def run(args, env_extra=None):
    env = dict(os.environ)
    env.pop('CALAGOPUS_URL', None)  # keep the real-panel example offline
    env['PYTHONPATH'] = os.pathsep.join(filter(None, [os.path.join(ROOT, 'src'), env_extra, env.get('PYTHONPATH')]))
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, env=env, timeout=120, cwd=ROOT)


@pytest.mark.parametrize('path', EXAMPLES, ids=os.path.basename)
def test_example_runs(path):
    result = run([path])
    assert result.returncode == 0, result.stdout + result.stderr
    assert 'Traceback' not in result.stderr, result.stderr


def test_packaged_extension(tmp_path):
    package = os.path.join(ROOT, 'examples', 'extensions', 'packaged_extension')
    script = f'''
from calagoapi import Panel, GenericServer
from calagoapi.extensions import register, enable
from calagoapi_server_notes.extension import ServerNotesExtension
register(ServerNotesExtension)
enable('server_notes', config={{'path': {str(tmp_path / 'notes.json')!r}}})
server = GenericServer(Panel('https://panel.example.com', 'key'), 'abc', data={{'uuid': 'abc'}})
server.notes.add('first')
server.notes.add('second')
assert server.notes.list() == ['first', 'second'], server.notes.list()
assert server.lastNote == 'second'
print('ok')
'''
    result = run(['-c', script], env_extra=package)
    assert result.returncode == 0 and 'ok' in result.stdout, result.stdout + result.stderr
