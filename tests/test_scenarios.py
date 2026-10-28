import pytest

from scenarios import SCENARIOS


@pytest.mark.parametrize('scenario', SCENARIOS, ids=lambda s: s.__name__)
def test_scenario(panel, fake, scenario):
    scenario(panel)
    assert not fake.violations, '\n'.join(sorted(set(fake.violations)))
