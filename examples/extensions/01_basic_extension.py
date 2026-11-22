'''
Example 1: the smallest useful extension.

Run it:
    python examples/extensions/01_basic_extension.py

No panel is needed: the server object below is built from local data, and the
extension only reads that data.

What you will see:
    - an Extension class with an id and metadata
    - a method added to Server with @method
    - register() + enable() to switch it on
    - the method appearing on a server object that already existed
'''
from calagoapi import Panel, Server
from calagoapi.extensions import Extension, ExtensionMetadata, enable, method, register


# 1. Declare what the extension adds.
#
# @method(Server) does NOT change Server yet. It only records "this function wants
# to become Server.describe". Nothing happens until the extension is enabled, so
# importing this file is always harmless.
@method(Server)
def describe(self) -> str:
    '''Returns a one-line summary of the server.'''
    # `self` is the server, exactly like in a normal method.
    memory = self.getLimits().get('memory', '?')
    return f'{self.getName()} ({memory} MB)'


# 2. Declare the extension itself.
#
# CalagoAPI creates the instance for you when the extension is enabled; you never
# call DescribeExtension() yourself.
class DescribeExtension(Extension):
    extension_id = 'describe'          # what users pass to enable()
    metadata = ExtensionMetadata(
        author='you',
        version='1.0.0',
        schema=1,                      # metadata format version, always 1 today
    )
    # members = None (the default) means: collect every @method / @propertyExtension /
    # @classExtension found in this module. `describe` above is picked up automatically.


# 3. Make the extension known.
#
# A published package does this with an entry point in pyproject.toml, so users
# never import it. In a single script, register() is the shortcut.
register(DescribeExtension)


# A server object, created BEFORE the extension is enabled. (Offline: we pass the
# data ourselves instead of fetching it from a panel.)
panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
server = Server(panel, 'abc123', data={'uuid': 'abc123', 'name': 'Survival', 'limits': {'memory': 4096}})

print(f'before enable: {hasattr(server, "describe")}')     # False

# 4. Switch it on. Classes are patched, so the existing object gains the method too.
enable('describe')

print(f'after enable:  {hasattr(server, "describe")}')     # True
print(server.describe())                                   # Survival (4096 MB)

# Calling enable() again is safe: nothing happens the second time.
enable('describe')

# Objects created later have it as well, including Server subclasses that game
# extensions provide.
lobby = Server(panel, 'def456', data={'uuid': 'def456', 'name': 'Lobby', 'limits': {'memory': 2048}})
print(lobby.describe())                                    # Lobby (2048 MB)
