'''
Example 7: namespace mode.

Run it:
    python examples/extensions/07_namespace_mode.py

In namespace mode, an extension's methods and properties live under one
attribute, `obj.<namespace>`:

    server.stats.players()
    server.stats.tps

Only that one attribute can clash with other names, so namespace mode is the
safe choice for extensions with short or generic method names.

Covers:
    - default_mode = 'namespace' and a custom `namespace` name
    - users overriding the mode in enable()
    - `self` inside methods is still the server
    - services are not moved by the mode
'''
from calagoapi import Panel, MinecraftServer
from calagoapi.extensions import (
    Extension,
    ExtensionMetadata,
    class_extension,
    enable,
    method,
    property_extension,
    register,
)


@method(MinecraftServer)
def players(self) -> list:
    # `self` is the server, not the namespace object.
    return self.data.get('players', [])


@method(MinecraftServer)
def status(self) -> str:
    return f'{self.getName()}: {len(players(self))} online'


@property_extension(MinecraftServer)
def tps(self) -> float:
    return self.data.get('tps', 20.0)


@class_extension(MinecraftServer, 'stats_history')
class StatsHistory:
    def __init__(self, server):
        self.samples = []


class StatsExtension(Extension):
    extension_id = 'stats'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    default_mode = 'namespace'       # members go under server.stats
    namespace = None                 # None = use the extension id ("stats")


register(StatsExtension)
enable('stats')

panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
server = MinecraftServer(panel, 'abc123', data={'uuid': 'abc123', 'name': 'Survival', 'players': ['Steve'], 'tps': 19.8})

print(server.stats.players())       # ['Steve']
print(server.stats.status())        # Survival: 1 online
print(server.stats.tps)             # 19.8
print(dir(server.stats))            # ['players', 'status', 'tps']
print(hasattr(server, 'players'))   # False: nothing was added directly
print(server.stats is server.stats) # True: the namespace object is cached

# The service is still at its own name: a service already is a namespace.
print(type(server.stats_history).__name__)   # StatsHistory


# Users choose the mode, whatever the default is:
#
#     enable('version_changer', mode='namespace')
#     server.version_changer.installVersion(build)
#
#     enable('stats', mode='direct')
#     server.players()
#
# Common mistake: inside a member, calling a sibling as self.players(). In
# namespace mode that attribute does not exist on the server. Call the function
# directly instead: players(self), as status() does above.
