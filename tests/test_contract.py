'''
Contract tests against openapi.json.

When Calagopus changes its API, regenerate openapi.json and run:

    pytest

- test_every_method_matches_the_spec fails if any SDK call hits an endpoint,
  query parameter or body field the spec does not have.
- test_every_endpoint_is_wrapped fails if the spec has endpoints CalagoAPI
  does not call yet, listing them so they can be added to src/calagoapi/api/.
'''
from exercise import exerciseAll
from scenarios import SCENARIOS


# endpoints intentionally not called by the SDK
NOT_WRAPPED = {
    # undocumented extension "about" endpoints
    ('GET', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/2038'),
    ('GET', '/api/admin/extensions/dev.0x7d8.subdomainmanager/2038'),
    # a browser redirect, the SDK only builds the URL (Auth.getOAuthLoginUrl)
    ('GET', '/api/auth/oauth/redirect/{oauth_provider}'),
}


def test_every_method_matches_the_spec(panel, fake):
    calls_ok, errors = exerciseAll(panel, fake)
    assert calls_ok > 1000
    assert not errors, '\n'.join(errors)
    assert not fake.violations, '\n'.join(sorted(set(fake.violations)))


def test_every_endpoint_is_wrapped(panel, fake):
    exerciseAll(panel, fake)
    for scenario in SCENARIOS:
        scenario(panel)

    spec = {(method, template) for _, method, _, template, _ in fake.endpoints}
    missing = sorted(spec - fake.hit - NOT_WRAPPED)
    assert not missing, 'Endpoints not wrapped by CalagoAPI:\n' + '\n'.join(f'{m} {p}' for m, p in missing)


def test_not_wrapped_list_is_current(fake):
    spec = {(method, template) for _, method, _, template, _ in fake.endpoints}
    stale = NOT_WRAPPED - spec
    assert not stale, f'Remove these from NOT_WRAPPED, they left the spec: {sorted(stale)}'
