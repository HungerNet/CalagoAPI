# 07 · Your first extension

This builds on [06](06-using-extensions.md): you have used an extension.

## What you will build

A `monitoring` extension that adds `server.getMemoryPercent()` and a
`server.memoryPercent` property to every server, and a test for it.

## Step 1: declare a method

```python
from calagoapi import Server
from calagoapi.extensions import method


@method(Server)
def getMemoryPercent(self) -> float:
    '''RAM usage in percent of the limit, or None without a limit.'''
    limit = self.getRAMLimit()
    return round(self.getRAM() / limit * 100, 1) if limit else None
```

`@method(Server)` does **not** change `Server`. It labels the function: "I want to become
`Server.getMemoryPercent`". Importing this module is harmless. `self` is the server.

## Step 2: declare a property

```python
from calagoapi.extensions import propertyExtension


@propertyExtension(Server)
def memoryPercent(self) -> float:
    return getMemoryPercent(self)       # call siblings as functions (works in namespace mode)
```

## Step 3: declare the extension

```python
from calagoapi.extensions import Extension, ExtensionMetadata


class MonitoringExtension(Extension):
    extension_id = 'monitoring'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
```

With `members = None` (the default), every decorated member in the module belongs to
this extension.

## Complete program

`monitoring.py`:

```python
from calagoapi import Server
from calagoapi.extensions import Extension, ExtensionMetadata, method, propertyExtension


@method(Server)
def getMemoryPercent(self) -> float:
    '''RAM usage in percent of the limit, or None without a limit.'''
    limit = self.getRAMLimit()
    return round(self.getRAM() / limit * 100, 1) if limit else None


@propertyExtension(Server)
def memoryPercent(self) -> float:
    return getMemoryPercent(self)


class MonitoringExtension(Extension):
    extension_id = 'monitoring'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
```

`report.py`:

```python
from calagoapi import Panel
from calagoapi.extensions import enable, register

from monitoring import MonitoringExtension

register(MonitoringExtension)       # a script: no entry point needed (tutorial 10 packages it)
enable('monitoring')

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    for server in panel.servers.getServers():
        print(f'{server.name}: {server.getMemoryPercent()} % of its memory')
```

## Testing it without a panel

Decorated functions stay plain functions, and servers can be built from local data:

```python
from calagoapi import Panel, Server
from calagoapi.extensions import ExtensionRegistry

from monitoring import MonitoringExtension, getMemoryPercent


def test_memory_percent(monkeypatch):
    registry = ExtensionRegistry()                 # isolated from the global registry
    registry.register(MonitoringExtension)
    registry.enable('monitoring')
    server = Server(Panel('https://panel.example.com', 'key'), 'abc', data={'uuid': 'abc'})
    monkeypatch.setattr(server, 'resources', lambda: {'memory_bytes': 512 * 1024 ** 2,
                                                      'memory_limit_bytes': 2048 * 1024 ** 2})
    assert server.getMemoryPercent() == 25.0 == getMemoryPercent(server)
    assert server.memoryPercent == 25.0
```

## How it works

- `enable()` collects the members, checks every name against `Server`, its subclasses,
  their instance attributes (`self.files`, ...) and other extensions, and only then sets
  `Server.getMemoryPercent`. A clash raises `ExtensionConflictError` before anything
  is installed.
- Because the member lives on `Server`, every subclass inherits it, including game
  servers like `calagoapi_minecraft.MinecraftServer`.
- `registry.ownerOf(Server, 'getMemoryPercent')` returns `'monitoring'`: the registry
  records who installed every attribute.
- On `AsyncPanel`, `await server.getMemoryPercent()` works with no extra code.

Runnable versions: [examples/extensions/01–03](../../../examples/extensions/README.md).

## Next

[08 · Services and namespaces](08-services-and-namespaces.md): features with their own state.
