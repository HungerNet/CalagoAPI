# 08 · Services and namespaces

This builds on [07](07-your-first-extension.md): methods and properties.

## What you will build

A `notes` service: per-server state behind one attribute (`server.notes.add()`,
`server.notes.list()`), like CalagoAPI's own `server.files`. Then the `monitoring`
extension from 07, moved under a namespace.

## Step 1: a service class

```python
from calagoapi import Server
from calagoapi.extensions import classExtension


@classExtension(Server, 'notes')
class Notes:
    '''Notes about one server, kept in memory.'''

    def __init__(self, server):          # CalagoAPI calls Notes(server) on first access
        self.server = server
        self.items = []

    def add(self, text: str) -> None:
        self.items.append(text)

    def list(self) -> list:
        return list(self.items)
```

## Step 2: use it

```python
server.notes.add('restarted after a crash')
server.notes is server.notes             # True: created once per object, then cached
other_server.notes.list()                # []: every server has its own instance
```

## Step 3: namespace mode

Short method names like `list()` or `status()` collide easily. In namespace mode an
extension's methods and properties move under one attribute:

```python
enable('monitoring', mode='namespace')
server.monitoring.getMemoryPercent()
server.monitoring.memoryPercent
hasattr(server, 'getMemoryPercent')      # False
```

Inside the members, `self` is still the server. That is why 07 called
`getMemoryPercent(self)` instead of `self.getMemoryPercent()`. The second form does not
exist on the server in namespace mode.

## Complete program

```python
from calagoapi import Panel, Server
from calagoapi.extensions import Extension, ExtensionMetadata, classExtension, enable, register


@classExtension(Server, 'notes')
class Notes:
    def __init__(self, server):
        self.server = server
        self.items = []

    def add(self, text: str) -> None:
        self.items.append(f'{self.server.getStatus()}: {text}')

    def list(self) -> list:
        return list(self.items)


class NotesExtension(Extension):
    extension_id = 'notes'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    default_mode = 'namespace'           # methods/properties would go under server.notes_ns
    namespace = 'notes_ns'               # services stay at their own name in both modes


register(NotesExtension)
enable('notes')

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.servers.getServer('abc123')
    server.notes.add('checked by the tutorial')
    print(server.notes.list())
```

## How it works

- A service is installed as a descriptor on the class. On first access it builds
  `Notes(server)`, stores it in the object's `__dict__` and never runs again for that
  object. Creation is locked, so two threads cannot build two instances.
- **Services ignore the mode**: a service already is a namespace, so
  `server.notes.add()` never becomes `server.notes.notes.add()`.
- On `AsyncPanel`, services are wrapped and cached too: `await server.notes.add('x')`,
  and `server.notes is server.notes` still holds.
- Use a service when a feature has state (a connection, a cache, credentials) or many
  related methods. `calagoapi-minecraft`'s `panel.minecraft` is a service on `Panel`.

Runnable versions: [examples/extensions/04, 06, 07](../../../examples/extensions/README.md).

## Next

[09 · Configuration and dependencies](09-configuration-and-dependencies.md).
