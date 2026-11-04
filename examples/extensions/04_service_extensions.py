'''
Example 4: service (class) extensions.

Run it:
    python examples/extensions/04_service_extensions.py

A service is a whole class attached to an object under a name, like
`server.files` or `server.backups` in CalagoAPI itself. Use one when the
feature needs its own state (a connection, a cache, credentials) or has many
methods that belong together.

Covers:
    - @class_extension(Target, 'name')
    - the service is created once per object and cached
    - per-object state
    - reading the extension's configuration from inside the service
'''
from calagoapi import Panel, MinecraftServer
from calagoapi.extensions import Extension, ExtensionMetadata, class_extension, enable, register


@class_extension(MinecraftServer, 'whitelist_cache')
class WhitelistCache:
    '''Keeps a local copy of the whitelist for one server.'''

    # CalagoAPI calls ServiceClass(obj) on first access: `server` is the object
    # the service belongs to.
    def __init__(self, server):
        self.server = server
        self.players = set()
        print(f'  (WhitelistCache created for {server.getName()})')

    def add(self, player: str) -> None:
        # Read the configuration through the Extension class.
        limit = WhitelistExtension.get().config['max_players']
        if len(self.players) >= limit:
            raise ValueError(f'whitelist cache is limited to {limit} players')
        self.players.add(player)
        # A real service would also call the panel, e.g. self.server.whitelistAdd(player)

    def list(self) -> list:
        return sorted(self.players)


class WhitelistExtension(Extension):
    extension_id = 'whitelist_cache'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    default_config = {'max_players': 3}


register(WhitelistExtension)
enable('whitelist_cache', config={'max_players': 2})

panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
survival = MinecraftServer(panel, 'a1', data={'uuid': 'a1', 'name': 'Survival'})
creative = MinecraftServer(panel, 'b2', data={'uuid': 'b2', 'name': 'Creative'})

print('first access:')
survival.whitelist_cache.add('Steve')           # creates the service
print('second access (no new instance):')
survival.whitelist_cache.add('Alex')            # same instance, no "created" line

# Cached: the same object every time.
print(survival.whitelist_cache is survival.whitelist_cache)    # True

# Every server has its own service and its own state.
print(survival.whitelist_cache.list())          # ['Alex', 'Steve']
print(creative.whitelist_cache.list())          # []

try:
    survival.whitelist_cache.add('Herobrine')
except ValueError as e:
    print('error:', e)                          # limited to 2 players (from the config)

# Services are already a namespace, so they appear at their own name in both
# modes: enable(..., mode='namespace') does not move server.whitelist_cache.
