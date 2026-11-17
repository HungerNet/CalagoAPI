'''
Example 4: service (class) extensions.

Run it:
    python examples/extensions/04_service_extensions.py

A service is a whole class attached to an object under a name, like
`server.files` or `server.backups` in CalagoAPI itself. Use one when the
feature needs its own state (a connection, a cache, credentials) or has many
methods that belong together.

Covers:
    - @classExtension(Target, 'name')
    - the service is created once per object and cached
    - per-object state
    - reading the extension's configuration from inside the service
'''
from calagoapi import Panel, Server
from calagoapi.extensions import Extension, ExtensionMetadata, classExtension, enable, register


@classExtension(Server, 'on_call')
class OnCall:
    '''The people to contact when one server has a problem.'''

    # CalagoAPI calls ServiceClass(obj) on first access: `server` is the object
    # the service belongs to.
    def __init__(self, server):
        self.server = server
        self.people = set()
        print(f'  (OnCall created for {server.getName()})')

    def add(self, person: str) -> None:
        # Read the configuration through the Extension class.
        limit = OnCallExtension.get().config['max_people']
        if len(self.people) >= limit:
            raise ValueError(f'on-call lists are limited to {limit} people')
        self.people.add(person)

    def list(self) -> list:
        return sorted(self.people)


class OnCallExtension(Extension):
    extension_id = 'on_call'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    default_config = {'max_people': 3}


register(OnCallExtension)
enable('on_call', config={'max_people': 2})

panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
survival = Server(panel, 'a1', data={'uuid': 'a1', 'name': 'Survival'})
lobby = Server(panel, 'b2', data={'uuid': 'b2', 'name': 'Lobby'})

print('first access:')
survival.on_call.add('alice')                 # creates the service
print('second access (no new instance):')
survival.on_call.add('bob')                   # same instance, no "created" line

# Cached: the same object every time.
print(survival.on_call is survival.on_call)   # True

# Every server has its own service and its own state.
print(survival.on_call.list())                # ['alice', 'bob']
print(lobby.on_call.list())                   # []

try:
    survival.on_call.add('carol')
except ValueError as e:
    print(f'error: {e}')                      # limited to 2 people (from the config)

# Services are already a namespace, so they appear at their own name in both
# modes: enable(..., mode='namespace') does not move server.on_call.
