import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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
