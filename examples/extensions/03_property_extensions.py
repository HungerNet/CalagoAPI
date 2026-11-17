'''
Example 3: property extensions.

Run it:
    python examples/extensions/03_property_extensions.py

Covers:
    - read-only properties with @propertyExtension
    - a property with a setter (pass a property object)
    - properties are computed on every read
'''
from calagoapi import Panel, Server
from calagoapi.extensions import Extension, ExtensionMetadata, enable, propertyExtension, register


# A read-only property: decorate a getter function.
@propertyExtension(Server)
def memoryMB(self) -> int:
    '''The memory limit in MB.'''
    return self.getLimits().get('memory', 0)


# A property with a setter: build a normal `property` and decorate that.
def _getNote(self):
    return self.data.get('note', '')


def _setNote(self, value):
    self.data['note'] = value


note = propertyExtension(Server, name='note')(property(_getNote, _setNote, doc='A local note.'))


class PropertiesExtension(Extension):
    extension_id = 'properties_demo'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)


register(PropertiesExtension)
enable('properties_demo')

panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
server = Server(panel, 'abc123', data={'uuid': 'abc123', 'name': 'Survival', 'limits': {'memory': 4096}})

print(server.memoryMB)                 # 4096 (no parentheses, it is a property)

server.data['limits']['memory'] = 6144
print(server.memoryMB)                 # 6144: recomputed on every read

server.note = 'upgrade on Friday'
print(f'note: {server.note}')

# Common mistake: properties that make HTTP requests run on every read, and in
# async code they block the event loop. Prefer a method for anything slow, and
# keep properties for cheap, local values (or expose both: a getX() method plus
# a cheap property).
