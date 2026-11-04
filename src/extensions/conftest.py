'''
Shared fixtures for the first-party extension tests.

Each extension test uses a fresh ExtensionRegistry and registers the extension
class directly (so the tests also run when the packages are not pip-installed),
then removes everything it installed on the real CalagoAPI classes.
'''
import glob
import os
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.join(ROOT, 'tests'))
for package_dir in sorted(glob.glob(os.path.join(HERE, 'calagoapi-*'))):
    sys.path.insert(0, package_dir)

from contract import FakePanel, BASE  # noqa: E402


@pytest.fixture(scope='session')
def fake():
    spec_path = os.path.join(ROOT, 'openapi.json')
    if not os.path.exists(spec_path):
        pytest.skip('openapi.json not found in the repository root')
    fake = FakePanel(spec_path)
    fake.install()
    yield fake
    fake.uninstall()


@pytest.fixture
def panel(fake):
    from calagoapi import Panel
    fake.reset()
    return Panel(url=BASE, api_key='c7sp_test')


@pytest.fixture
def extensions():
    '''A fresh registry; everything enabled through it is removed after the test.'''
    from calagoapi.extensions import ExtensionRegistry
    registry = ExtensionRegistry()
    registry._entry_points = {}
    yield registry
    registry._reset_for_tests()
