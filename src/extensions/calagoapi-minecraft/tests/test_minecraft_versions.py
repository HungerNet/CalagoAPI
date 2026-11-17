'''server.versions and panel.minecraft.versionChanger against the contract-checked fake panel.'''
import pytest

from calagoapi.utils.exceptions import InvalidActionError, NotFoundError
from contract import UUID

from calagoapi_minecraft import MinecraftServer, VersionChangerAdmin
from calagoapi_minecraft import versions as versions_module

# every Version Changer endpoint core leaves to this package (see tests/test_contract.py)
ENDPOINTS = {
    ('GET', '/api/client/servers/{server}/minecraft/versions/installed'),
    ('GET', '/api/client/servers/{server}/minecraft/versions/types'),
    ('GET', '/api/client/servers/{server}/minecraft/versions/types/{type}'),
    ('GET', '/api/client/servers/{server}/minecraft/versions/types/{type}/{version}'),
    ('POST', '/api/client/servers/{server}/minecraft/versions/install'),
    ('GET', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/settings'),
    ('PUT', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/settings'),
    ('GET', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/statistics/total'),
    ('GET', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/default-order'),
}


@pytest.fixture
def server(panel, network):
    return MinecraftServer(panel, UUID, data={'uuid': UUID})


def test_every_endpoint_matches_the_spec(server, panel, fake):
    versions = server.versions
    versions.getInstalled()
    versions.getInstalledBuild()
    versions.isUpToDate()
    versions.getTypes()
    versions.getVersions('PAPER', search='1.21', page=1, per_page=5)
    versions.getBuilds('PAPER', '1.21.11', page=1, per_page=5)
    versions.getLatestBuild('PAPER', '1.21.11')
    versions.install({'uuid': UUID}, truncate_directory=True, accept_eula=True, backup=False)
    assert versions.isAvailable()

    admin = VersionChangerAdmin(panel)
    admin.getSettings()
    admin.updateSettings(mcjars_url='https://mcjars.app')
    admin.getStatistics()
    admin.getDefaultOrder()

    assert ENDPOINTS <= fake.hit
    assert not fake.violations, '\n'.join(fake.violations)


class FakeBackup:
    def __init__(self, ok):
        self.ok = ok

    def waitUntilComplete(self, timeout):
        self.timeout = timeout
        return self

    def isSuccessful(self):
        return self.ok


def test_install_backs_up_first(server, monkeypatch):
    installs = []
    created = []
    monkeypatch.setattr(versions_module.VersionChangerAPI, 'install',
                        lambda api, server_id, build_id, truncate, eula: installs.append(build_id))
    monkeypatch.setattr(server.backups, 'createBackup', lambda name: created.append(name) or FakeBackup(True))

    server.versions.install('build-1')                 # auto_backup defaults to False
    assert installs == ['build-1'] and created == []
    server.versions.install({'uuid': 'build-2'}, backup=True)
    assert installs == ['build-1', 'build-2'] and created == ['Before version change']

    monkeypatch.setattr(server.backups, 'createBackup', lambda name: FakeBackup(False))
    with pytest.raises(InvalidActionError, match='nothing was installed'):
        server.versions.install('build-3', backup=True)
    assert installs == ['build-1', 'build-2']


def test_auto_backup_config(mc, panel, monkeypatch):
    mc.enable('minecraft', config={'auto_backup': True, 'backup_name': 'pre-update', 'backup_timeout': 60})
    server = MinecraftServer(panel, UUID, data={'uuid': UUID})
    backups = []
    monkeypatch.setattr(versions_module.VersionChangerAPI, 'install', lambda *args: None)
    monkeypatch.setattr(server.backups, 'createBackup', lambda name: backups.append(FakeBackup(True)) or backups[-1])
    server.versions.install('build')
    assert len(backups) == 1 and backups[0].timeout == 60


def test_update(server, monkeypatch):
    installed = {'build': {'uuid': 'old'}, 'latest': {'uuid': 'new'}}
    monkeypatch.setattr(versions_module.VersionChangerAPI, 'installed', lambda api, server_id: installed)
    installs = []
    monkeypatch.setattr(versions_module.VersionChangerAPI, 'install', lambda api, sid, build, *rest: installs.append(build))
    assert server.versions.isUpToDate() is False
    assert server.versions.update() is True and installs == ['new']
    installed['build'] = {'uuid': 'new'}
    assert server.versions.isUpToDate() is True and server.versions.update() is False
    monkeypatch.setattr(versions_module.VersionChangerAPI, 'installed', lambda api, server_id: None)
    assert server.versions.isUpToDate() is None and server.versions.getInstalledBuild() is None
    with pytest.raises(InvalidActionError, match='unknown'):
        server.versions.update()


def test_not_available(server, monkeypatch):
    def missing(api, server_id):
        raise NotFoundError('no such extension', 404)

    monkeypatch.setattr(versions_module.VersionChangerAPI, 'types', missing)
    assert server.versions.isAvailable() is False
