'''Retries, context managers and the async wrapper.'''
import asyncio

import pytest
import requests

import calagoapi.api.client as client_module
from calagoapi import Panel, AsyncPanel, RateLimitError, ServerError, PanelConnectionError, Backup, Page
from contract import BASE, UUID, FakeResponse


class Scripted:
    '''Answers requests with a scripted list of status codes, then 200'''
    def __init__(self, statuses, retry_after=None):
        self.statuses = list(statuses)
        self.retry_after = retry_after
        self.calls = 0

    def __call__(self, session, method, url, **kwargs):
        self.calls += 1
        if self.statuses:
            status = self.statuses.pop(0)
            if status == 'down':
                raise requests.ConnectionError('connection refused')
            response = FakeResponse(status, {'errors': ['nope']}, method=method, path=url)
            if self.retry_after:
                response.headers['Retry-After'] = self.retry_after
            return response
        return FakeResponse(200, {'user': {'uuid': UUID, 'username': 'steve'}}, method=method, path=url)


@pytest.fixture
def sleeps(monkeypatch):
    waited = []
    monkeypatch.setattr(client_module.time, 'sleep', waited.append)
    return waited


def scripted(monkeypatch, statuses, retry_after=None):
    script = Scripted(statuses, retry_after)
    monkeypatch.setattr(requests.Session, 'request', lambda session, method, url, **kwargs: script(session, method, url, **kwargs))
    return script


def test_rate_limit_is_retried_with_retry_after(monkeypatch, sleeps):
    script = scripted(monkeypatch, [429, 429], retry_after='2')
    panel = Panel(BASE, 'key')
    assert panel.api.account.get()['username'] == 'steve'
    assert script.calls == 3 and sleeps == [2.0, 2.0]


def test_rate_limit_gives_up(monkeypatch, sleeps):
    scripted(monkeypatch, [429] * 10)
    with pytest.raises(RateLimitError):
        Panel(BASE, 'key', max_retries=2).api.account.get()
    assert sleeps == [0.5, 1.0]


def test_retry_after_is_capped(monkeypatch, sleeps):
    scripted(monkeypatch, [429], retry_after='3600')
    Panel(BASE, 'key').api.account.get()
    assert sleeps == [60]


def test_get_retries_server_errors_and_connection_errors(monkeypatch, sleeps):
    script = scripted(monkeypatch, [503, 'down', 502])
    Panel(BASE, 'key').api.account.get()
    assert script.calls == 4 and sleeps == [0.5, 1.0, 2.0]


def test_writes_are_not_retried_on_server_errors(monkeypatch, sleeps):
    script = scripted(monkeypatch, [503])
    with pytest.raises(ServerError):
        Panel(BASE, 'key').api.servers.power(UUID, 'restart')
    assert script.calls == 1 and sleeps == []


def test_writes_are_not_retried_on_connection_errors(monkeypatch, sleeps):
    script = scripted(monkeypatch, ['down'])
    with pytest.raises(PanelConnectionError):
        Panel(BASE, 'key').api.servers.power(UUID, 'restart')
    assert script.calls == 1


def test_retries_can_be_disabled(monkeypatch, sleeps):
    script = scripted(monkeypatch, [429])
    with pytest.raises(RateLimitError):
        Panel(BASE, 'key', max_retries=0).api.account.get()
    assert script.calls == 1


def test_panel_context_manager(panel):
    with Panel(BASE, 'key') as p:
        assert p.account.getUsername() == 'sample'


def test_async_panel(fake):
    async def main():
        async with AsyncPanel(url=BASE, api_key='key') as panel:
            servers = await panel.servers.getServers()
            assert isinstance(servers, Page) and servers.getTotal() == 1

            statuses = await asyncio.gather(*(s.getStatus() for s in servers))
            assert statuses == ['offline']

            server = await panel.servers.getServer(UUID)
            assert server.name == 'sample'                 # attributes are plain
            assert await server.getName() == 'sample'      # methods are awaitable

            backup = await server.createBackup('nightly')
            assert isinstance(backup.target, Backup)
            await backup.lock()
            # wrapped objects can be passed back in as arguments
            await server.backups.deleteBackup(backup)
            await server.files.listFiles('/')

            db = await server.databases.createDatabase('stats')
            await db.explorer.insertRow('players', {'name': 'Steve'})
            instance = await server.databases.createInstance({'uuid': UUID}, 'db')
            database = await instance.createDatabase('x')
            await instance.createUser('app', databases={database: 'read_write'})

    fake.reset()
    asyncio.run(main())
    assert not fake.violations, fake.violations
