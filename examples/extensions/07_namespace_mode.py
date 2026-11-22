'''
Example 7: namespace mode.

Run it:
    python examples/extensions/07_namespace_mode.py

In namespace mode, an extension's methods and properties live under one
attribute, `obj.<namespace>`:

    server.stats.players()
    server.stats.load

Only that one attribute can clash with other names, so namespace mode is the
safe choice for extensions with short or generic method names.

Covers:
    - default_mode = 'namespace' and a custom `namespace` name
    - users overriding the mode in enable()
    - `self` inside methods is still the server
    - services are not moved by the mode
'''
from calagoapi import Panel, Server
from calagoapi.extensions import (
    Extension,
    ExtensionMetadata,
    classExtension,
    enable,
    method,
    propertyExtension,
    register,
)


@method(Server)
def players(self) -> list:
    # `self` is the server, not the namespace object.
    return self.data.get('players', [])


@method(Server)
def status(self) -> str:
    return f'{self.getName()}: {len(players(self))} online'


@propertyExtension(Server)
def load(self) -> float:
    return self.data.get('load', 0.0)


@classExtension(Server, 'stats_history')
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
server = Server(panel, 'abc123', data={'uuid': 'abc123', 'name': 'Survival', 'players': ['alice'], 'load': 0.42})

print(server.stats.players())       # ['alice']
print(server.stats.status())        # Survival: 1 online
print(server.stats.load)            # 0.42
print(dir(server.stats))            # ['load', 'players', 'status']
print(hasattr(server, 'players'))   # False: nothing was added directly
print(server.stats is server.stats) # True: the namespace object is cached

# The service is still at its own name: a service already is a namespace.
print(type(server.stats_history).__name__)   # StatsHistory


# Users choose the mode, whatever the default is:
#
#     enable('stats', mode='direct')
#     server.players()
#
# Common mistake: inside a member, calling a sibling as self.players(). In
# namespace mode that attribute does not exist on the server. Call the function
# directly instead: players(self), as status() does above.
