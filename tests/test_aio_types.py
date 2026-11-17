'''The async type registry, generator methods and ServerManager(server_class=...).'''
import asyncio

from calagoapi import AsyncPanel, Server
from calagoapi.aio import AsyncServer, AsyncWrapper, asyncTypeFor, iterateInThread, registerAsyncType, wrap
from calagoapi.aio import panel as aio_panel
from contract import BASE, UUID


class GameServer(Server):
    def __init__(self, panel, server_id=None, name=None, data=None, *, region=None):
        super().__init__(panel, server_id, name, data)
        self.region = region

    def countdown(self, start):
        for number in range(start, 0, -1):
            yield number


class AsyncGameServer(AsyncServer):
    pass


class Stats:
    def total(self):
        return 3


def test_core_server_wraps_as_async_server(panel):
    assert asyncTypeFor(Server) is AsyncServer
    assert isinstance(wrap(Server(panel, UUID)), AsyncServer)


def test_subclass_and_plain_types(panel, monkeypatch):
    monkeypatch.setattr(aio_panel, '_async_types', dict(aio_panel._async_types))
    # unregistered subclasses inherit their base class's wrapper
    assert type(wrap(GameServer(panel, UUID))) is AsyncServer
    registerAsyncType(GameServer, AsyncGameServer)
    assert type(wrap(GameServer(panel, UUID))) is AsyncGameServer
    # objects from outside calagoapi are left alone until registered
    stats = Stats()
    assert wrap(stats) is stats
    registerAsyncType(Stats)
    assert type(wrap(stats)) is AsyncWrapper
    wrapped = wrap(stats)
    assert wrap(wrapped) is wrapped


def test_generator_methods_become_async_generators(panel):
    server = AsyncServer(GameServer(panel, UUID))

    async def main():
        return [n async for n in server.countdown(3)]

    assert asyncio.run(main()) == [3, 2, 1]


def test_iterate_in_thread_closes_the_iterator():
    closed = []

    def numbers():
        try:
            yield from range(100)
        finally:
            closed.append(True)

    async def main():
        async for number in iterateInThread(numbers()):
            if number == 2:
                break

    asyncio.run(main())
    assert closed == [True]


def test_server_class_option(panel):
    server = panel.servers.getServer(UUID, server_class=GameServer, region='eu')
    assert type(server) is GameServer and server.region == 'eu'
    servers = panel.servers.getServers(server_class=GameServer, region='us')
    assert servers and all(type(s) is GameServer and s.region == 'us' for s in servers)


def test_server_class_through_async_panel(fake):
    async def main():
        async with AsyncPanel(url=BASE, api_key='key') as panel:
            server = await panel.servers.getServer(UUID, server_class=GameServer)
            assert isinstance(server, AsyncServer) and isinstance(server.target, GameServer)

    asyncio.run(main())
