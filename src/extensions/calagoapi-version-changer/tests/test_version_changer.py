import asyncio
import importlib.metadata
import warnings

import pytest

from calagoapi import AsyncPanel, MinecraftServer
from calagoapi.admin.admin import ExtensionManager
from calagoapi.extensions import ExtensionDeprecationWarning, ExtensionNamespace

from calagoapi_version_changer.extension import VersionChangerExtension, installVersion
from contract import BASE, UUID

VERSION_ENDPOINTS = {
    ('GET', '/api/client/servers/{server}/minecraft/versions/installed'),
    ('GET', '/api/client/servers/{server}/minecraft/versions/types'),
    ('GET', '/api/client/servers/{server}/minecraft/versions/types/{type}'),
    ('GET', '/api/client/servers/{server}/minecraft/versions/types/{type}/{version}'),
    ('POST', '/api/client/servers/{server}/minecraft/versions/install'),
}

ADMIN_ENDPOINTS = {
    ('GET', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/settings'),
    ('PUT', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/settings'),
    ('GET', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/statistics/total'),
    ('GET', '/api/admin/extensions/dev.0x7d8.minecraftversionchanger/default-order'),
}


def test_builtins_are_deprecated_until_enabled(panel, fake, extensions):
    server = panel.servers.getMinecraftServer(UUID)
    with pytest.warns(ExtensionDeprecationWarning, match='calagoapi-version-changer'):
        server.installVersion({'uuid': UUID})

    extensions.register(VersionChangerExtension)
    extensions.enable('version_changer')

    # the object created before enable() now uses the extension, without warnings
    assert MinecraftServer.installVersion is installVersion
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        server.installVersion({'uuid': UUID})
    assert extensions.owner_of(MinecraftServer, 'installVersion') == 'version_changer'
    replaced = [r for r in extensions.registrations(owner='version_changer') if r.replaced is not None]
    assert {r.name for r in replaced} == {
        'getInstalledVersion', 'getVersionTypes', 'getVersions', 'getBuilds', 'installVersion',
        'getVersionChangerSettings', 'updateVersionChangerSettings', 'getVersionChangerStatistics',
        'getVersionChangerDefaultOrder',
    }


def test_every_endpoint_matches_the_spec(panel, fake, extensions):
    extensions.register(VersionChangerExtension)
    extensions.enable('version_changer')
    server = panel.servers.getMinecraftServer(UUID)

    with warnings.catch_warnings():
        warnings.simplefilter('error', ExtensionDeprecationWarning)
        assert isinstance(server.getInstalledVersion(), dict)
        assert server.installedVersion['uuid'] == UUID
        assert server.isUpToDate() is True
        assert server.updateVersion() is False
        server.getVersionTypes()
        server.getVersions('PAPER', page=1, per_page=5)
        builds = server.getBuilds('PAPER', '1.21.11', page=1, per_page=1)
        server.installVersion(builds[0], truncate_directory=True)
        server.installVersion(UUID)

        admin = panel.admin.extensions
        admin.getVersionChangerSettings()
        admin.updateVersionChangerSettings(mcjars_url='https://mcjars.app')
        admin.getVersionChangerStatistics()
        admin.getVersionChangerDefaultOrder()

    assert not fake.violations, '\n'.join(fake.violations)
    assert VERSION_ENDPOINTS | ADMIN_ENDPOINTS <= fake.hit


def test_auto_backup(panel, fake, extensions, monkeypatch):
    from calagoapi.backups.backup import Backup
    monkeypatch.setattr(Backup, 'waitUntilComplete', lambda self, timeout=3600, interval=5: self)
    monkeypatch.setattr(Backup, 'isSuccessful', lambda self: True)

    extensions.register(VersionChangerExtension)
    extensions.enable('version_changer', config={'auto_backup': True, 'backup_name': 'pre-update'})
    server = panel.servers.getMinecraftServer(UUID)
    server.installVersion(UUID)
    assert ('POST', '/api/client/servers/{server}/backups') in fake.hit
    assert ('POST', '/api/client/servers/{server}/minecraft/versions/install') in fake.hit
    assert not fake.violations


def test_failed_backup_prevents_install(panel, fake, extensions, monkeypatch):
    from calagoapi import InvalidActionError
    from calagoapi.backups.backup import Backup
    monkeypatch.setattr(Backup, 'waitUntilComplete', lambda self, timeout=3600, interval=5: self)
    monkeypatch.setattr(Backup, 'isSuccessful', lambda self: False)

    extensions.register(VersionChangerExtension)
    extensions.enable('version_changer', config={'auto_backup': True})
    with pytest.raises(InvalidActionError, match='nothing was installed'):
        panel.servers.getMinecraftServer(UUID).installVersion(UUID)
    assert ('POST', '/api/client/servers/{server}/minecraft/versions/install') not in fake.hit


def test_namespace_mode_keeps_builtins(panel, fake, extensions):
    extensions.register(VersionChangerExtension)
    extensions.enable('version_changer', mode='namespace')
    server = panel.servers.getMinecraftServer(UUID)

    assert isinstance(server.version_changer, ExtensionNamespace)
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        server.version_changer.installVersion(UUID)
        assert server.version_changer.installedVersion['uuid'] == UUID
        panel.admin.extensions.version_changer.getVersionChangerStatistics()
    # the deprecated built-in is untouched in namespace mode
    with pytest.warns(ExtensionDeprecationWarning):
        server.installVersion(UUID)
    assert not fake.violations


def test_invalid_config(extensions):
    from calagoapi.extensions import ConfigurationError
    extensions.register(VersionChangerExtension)
    with pytest.raises(ConfigurationError, match='auto_backup'):
        extensions.enable('version_changer', config={'auto_backup': 'yes'})
    with pytest.raises(ConfigurationError, match='Unknown config'):
        extensions.enable('version_changer', config={'autobackup': True})


def test_alias(extensions):
    extensions.register(VersionChangerExtension)
    assert extensions.enable('minecraft_version_changer') is extensions.get('version_changer')


def test_async(fake, extensions):
    extensions.register(VersionChangerExtension)
    extensions.enable('version_changer')

    async def main():
        async with AsyncPanel(url=BASE, api_key='c7sp_test') as panel:
            server = await panel.servers.getMinecraftServer(UUID)
            with warnings.catch_warnings():
                warnings.simplefilter('error', ExtensionDeprecationWarning)
                await server.installVersion({'uuid': UUID})
                builds = await server.getBuilds('PAPER', '1.21.11', page=1, per_page=1)
                assert builds[0]['uuid'] == UUID
                assert (await server.getInstalledVersion())['build']['uuid'] == UUID

    fake.reset()
    asyncio.run(main())
    assert not fake.violations


def test_reset_restores_builtins(extensions):
    builtin = MinecraftServer.__dict__['installVersion']
    extensions.register(VersionChangerExtension)
    extensions.enable('version_changer')
    assert MinecraftServer.__dict__['installVersion'] is installVersion
    assert ExtensionManager.__dict__['getVersionChangerSettings'].__module__ == 'calagoapi_version_changer.extension'
    extensions._reset_for_tests()
    assert MinecraftServer.__dict__['installVersion'] is builtin
    assert 'installedVersion' not in MinecraftServer.__dict__


def test_entry_point_is_published():
    try:
        importlib.metadata.distribution('calagoapi-version-changer')
    except importlib.metadata.PackageNotFoundError:
        pytest.skip('calagoapi-version-changer is not pip-installed')
    from calagoapi.extensions import ExtensionRegistry
    registry = ExtensionRegistry()
    assert registry.get_class('version_changer') is VersionChangerExtension
