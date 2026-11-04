'''
Example 6: direct mode.

Run it:
    python examples/extensions/06_direct_mode.py

In direct mode (the default) methods and properties appear directly on the
object: `server.installBuild(...)`, `server.installedBuild`. It feels like
CalagoAPI always had them.

The trade-off: the names share the object's namespace with CalagoAPI and every
other extension, so a name that is already taken is an ExtensionConflictError.
'''
from calagoapi import Panel, MinecraftServer
from calagoapi.extensions import (
    Extension,
    ExtensionConflictError,
    ExtensionMetadata,
    enable,
    method,
    property_extension,
    register,
)


@method(MinecraftServer)
def installBuild(self, build: str) -> str:
    # A stand-in for the real calagoapi-version-changer extension. (Its names,
    # installVersion / installedVersion, are reserved for it: CalagoAPI still has a
    # deprecated built-in installVersion that only version_changer may take over.)
    self.data['build'] = build
    return f'installing {build} on {self.getName()}'


@property_extension(MinecraftServer)
def installedBuild(self) -> str:
    return self.data.get('build', 'unknown')


class FakeVersionsExtension(Extension):
    # Note: the real extension is called "version_changer"; a different id keeps
    # this example independent of whether calagoapi-version-changer is installed.
    extension_id = 'fake_versions'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    default_mode = 'direct'          # the default, written out for clarity
    members = [installBuild, installedBuild]


register(FakeVersionsExtension)
enable('fake_versions')

panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
server = MinecraftServer(panel, 'abc123', data={'uuid': 'abc123', 'name': 'Survival'})

print(server.installBuild('paper-1.21.11-120'))     # directly on the server
print(server.installedBuild)                         # paper-1.21.11-120


# Direct mode never replaces anything. A second extension that also wants
# `installBuild` on MinecraftServer is rejected, with both owners named:
@method(MinecraftServer, name='installBuild')
def otherInstall(self, build):
    return 'other'


class OtherExtension(Extension):
    extension_id = 'other_versions'
    members = [otherInstall]


register(OtherExtension)
try:
    enable('other_versions')
except ExtensionConflictError as e:
    print('ExtensionConflictError:', e)
    print('  extension:', e.extension, '| owner:', e.owner, '| target:', e.target.__name__, '| member:', e.member)

# The same is true for CalagoAPI's own members (say, kick, files, console, ...).
# Users who hit a conflict can often enable the extension in namespace mode
# instead (see 07_namespace_mode.py).
