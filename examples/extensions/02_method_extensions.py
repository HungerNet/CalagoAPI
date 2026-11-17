'''
Example 2: method extensions in detail.

Run it:
    python examples/extensions/02_method_extensions.py

Covers:
    - adding a method to a base class (subclasses inherit it)
    - adding a method to several classes at once
    - choosing the attribute name with name=
    - methods that call other members of the same extension
    - async: the same method becomes awaitable on AsyncPanel objects
'''
from calagoapi import Panel, Server
from calagoapi.extensions import Extension, ExtensionMetadata, enable, method, register


# Added to Server, so every Server subclass (for example a game extension's
# server class) gets it as well.
@method(Server)
def memoryGB(self) -> float:
    '''Returns the memory limit in GB.'''
    return round(self.getLimits().get('memory', 0) / 1024, 1)


# name= sets the attribute name when the function name should differ.
# Here the function is called `_isBig` but appears as `server.isBig()`.
@method(Server, name='isBig')
def _isBig(self, threshold_gb: float = 4) -> bool:
    '''Returns True if the server has at least `threshold_gb` GB of memory.'''
    # Call sibling members directly (memoryGB(self)), not through self.memoryGB().
    # Direct calls keep working if a user enables the extension in namespace mode,
    # where the method lives at server.<namespace>.memoryGB instead.
    return memoryGB(self) >= threshold_gb


# A list of targets adds the same method to several unrelated classes.
# (Stacking two @method decorators would work too.)
@method([Server, Panel], name='hello')
def hello(self) -> str:
    return f'hello from {type(self).__name__}'


class SizingExtension(Extension):
    extension_id = 'sizing'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)


# A subclass, the way game extensions define theirs. It inherits every member
# added to Server.
class GameServer(Server):
    pass


register(SizingExtension)
enable('sizing')

panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
big = GameServer(panel, 'a1', data={'uuid': 'a1', 'name': 'Big', 'limits': {'memory': 8192}})
small = Server(panel, 'b2', data={'uuid': 'b2', 'name': 'Small', 'limits': {'memory': 1024}})

print(f'{big.memoryGB()} GB, big: {big.isBig()}')            # 8.0 GB, big: True
print(f'{small.memoryGB()} GB, big: {small.isBig()}')        # 1.0 GB, big: False
print(small.isBig(threshold_gb=1))                           # True
print(f'{big.hello()} | {panel.hello()}')                    # hello from GameServer | hello from Panel

# Decorated functions are still plain functions, handy for unit tests:
print(memoryGB(big))                                         # 8.0


# Async: AsyncPanel wraps the same classes, so every extension method is
# awaitable there automatically, without writing an async version:
#
#     async with AsyncPanel(url=..., api_key=...) as panel:
#         server = await panel.servers.getServer('abc123')
#         print(await server.memoryGB())
