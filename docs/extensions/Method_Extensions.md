# Method extensions

A method extension adds a method to a CalagoAPI class.

```python
from calagoapi import MinecraftServer
from calagoapi.extensions import method


@method(MinecraftServer)
def installVersion(self, build, truncate_directory=False):
    '''Installs a server build.'''
    ...
```

After `enable()`:

```python
server.installVersion(build)                         # direct mode
server.version_changer.installVersion(build)         # namespace mode
await server.installVersion(build)                   # on AsyncPanel objects
```

Runnable example: [02_method_extensions.py](../../examples/extensions/02_method_extensions.py).

## Writing the function

Write it exactly like a method inside the class: the first parameter is `self`,
the object the method is called on.

```python
@method(MinecraftServer)
def memoryGB(self) -> float:
    '''Returns the memory limit in GB.'''
    return self.getLimits().get('memory', 0) / 1024
```

Everything the object offers is available: `self.panel`, `self.server_id`,
`self.files`, `self.sendCommand(...)`, and so on. For HTTP calls, use the panel's
client so authentication, retries and errors behave like the rest of CalagoAPI:

```python
@method(MinecraftServer)
def getInstalledVersion(self):
    return self.panel.client.get(f'/api/client/servers/{self.server_id}/minecraft/versions/installed')['build']
```

## Options

```python
method(target, name=None)
```

| Argument | Meaning |
| --- | --- |
| `target` | A class, or a list/tuple of classes |
| `name` | Attribute name; defaults to the function's name |

```python
# a different public name than the function name
@method(MinecraftServer, name='isBig')
def _isBig(self):
    ...

# several classes at once
@method([GenericServer, AdminServer])
def label(self):
    ...

# stacking also works
@method(GenericServer)
@method(Panel)
def hello(self):
    ...
```

A method added to a base class (`GenericServer`) is inherited by its subclasses
(`MinecraftServer`). An extension may specialise its own method on a subclass by
targeting both classes with the same name; it may not override another
extension's or CalagoAPI's method.

## Sync or async?

Write plain `def` methods. They work with `Panel`, and `AsyncPanel` runs them in
a worker thread automatically, so `await server.myMethod()` works too. This is
how all of CalagoAPI works.

`async def` methods are supported: on `AsyncPanel` objects they are awaited on
the event loop directly. On a regular `Panel`, calling one returns a coroutine
you would have to run yourself, so only use `async def` if your extension is
meant for async code only, and say so in its README.

## Calling other members of your extension

Call them as functions:

```python
@method(MinecraftServer)
def isUpToDate(self):
    installed = getInstalledVersion(self)       # good
    # installed = self.getInstalledVersion()    # breaks in namespace mode
    ...
```

In namespace mode, `getInstalledVersion` lives at `server.version_changer`, not
on the server, so `self.getInstalledVersion()` would reach the wrong thing (or
nothing). Calling the function directly works in both modes.

## Names and conflicts

Extensions never replace existing members. `enable()` raises
`ExtensionConflictError` when the name:

- is already defined by the class, one of its base classes or a subclass
  (`say`, `kick`, `getStatus`, ...);
- is set as an instance attribute in CalagoAPI's code (`files`, `console`, `name`, ...);
- is already provided by another enabled extension on a related class;
- is used by the async wrappers (`target`, `console`, `streamConsole`, ...).

The error names everything you need:

```text
ExtensionConflictError: Extension 'other' cannot add method 'installVersion' to MinecraftServer:
it is already provided by extension 'version_changer' (method on MinecraftServer).
```

```python
e.extension   # 'other'            the extension being enabled
e.owner       # 'version_changer'  who already has the name ('calagoapi' for built-ins)
e.target      # MinecraftServer
e.member      # 'installVersion'
```

The check happens before anything is changed, so a conflict never leaves an
extension half-installed.

## Common mistakes

- `@method` without `(Target)`: raises `ExtensionDefinitionError`.
- Dunder names (`__len__`, `__init__`): not allowed.
- `@staticmethod` / `@classmethod`: not supported; write a normal function.
- Expecting the decorator to change the class right away: nothing happens until
  `enable()`.

## Best practices

- camelCase names, like the rest of CalagoAPI (`installVersion`, not `install_version`).
- A docstring with an `Example:` section; it shows up in `help(server.installVersion)`.
- Accept objects or ids for parameters that take an id, like CalagoAPI does
  (`calagoapi.utils.model.idOf`).
- Return CalagoAPI objects, dicts or `None`; raise CalagoAPI exceptions.
