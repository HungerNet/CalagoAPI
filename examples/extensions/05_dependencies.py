'''
Example 5: dependencies.

Run it:
    python examples/extensions/05_dependencies.py

Covers:
    - `dependencies = [...]`: enabling one extension enables what it needs first
    - optional dependencies
    - who enabled what (enabled_by)
    - clear errors for missing and circular dependencies
    - several extensions in one file need explicit `members` lists
'''
from calagoapi import Panel, MinecraftServer
from calagoapi.extensions import (
    CircularDependencyError,
    Dependency,
    DependencyError,
    Extension,
    ExtensionMetadata,
    enable,
    get_extension,
    method,
    register,
)


# --- a "library" extension other extensions build on -------------------------
@method(MinecraftServer)
def onlineCount(self) -> int:
    '''Pretend player count (a real extension would ask the server).'''
    return len(self.data.get('players', []))


class PlayersExtension(Extension):
    extension_id = 'players'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    # This file defines several extensions. Without an explicit list, each one would
    # collect every decorated member in the module, and the second to be enabled
    # would fail because a member can belong to only one extension.
    members = [onlineCount]


# --- an extension that needs it ----------------------------------------------
@method(MinecraftServer)
def isBusy(self) -> bool:
    # onlineCount comes from the `players` dependency; it is guaranteed to be
    # enabled before this extension, so calling it is safe.
    return onlineCount(self) >= get_extension('busy_check').config['threshold']


class BusyCheckExtension(Extension):
    extension_id = 'busy_check'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    dependencies = [
        'players',                                   # required
        Dependency('metrics', optional=True),        # used if installed, skipped if not
    ]
    default_config = {'threshold': 2}
    members = [isBusy]


register(PlayersExtension)
register(BusyCheckExtension)

# Only busy_check is enabled explicitly; players is enabled automatically first.
enable('busy_check')
print('players enabled by:', get_extension('players').enabled_by)       # busy_check
print('busy_check enabled by:', get_extension('busy_check').enabled_by)  # None (you did)

panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
server = MinecraftServer(panel, 'a1', data={'uuid': 'a1', 'name': 'Survival', 'players': ['Steve', 'Alex']})
print(server.onlineCount(), server.isBusy())     # 2 True


# --- missing dependency -------------------------------------------------------
class NeedsMissingExtension(Extension):
    extension_id = 'needs_missing'
    dependencies = ['not_installed_anywhere']
    members = []


register(NeedsMissingExtension)
try:
    enable('needs_missing')
except DependencyError as e:
    print('DependencyError:', e)


# --- circular dependencies ----------------------------------------------------
class ChickenExtension(Extension):
    extension_id = 'chicken'
    dependencies = ['egg']
    members = []


class EggExtension(Extension):
    extension_id = 'egg'
    dependencies = ['chicken']
    members = []


register(ChickenExtension)
register(EggExtension)
try:
    enable('chicken')
except CircularDependencyError as e:
    print('CircularDependencyError:', e)           # chicken -> egg -> chicken
    print('cycle:', e.cycle)


# Common mistake: enabling a dependency yourself AFTER something already pulled it
# in with its defaults, but with a different config. That raises ConfigurationError.
# Enable the dependency with your config FIRST, then the extension that needs it.
