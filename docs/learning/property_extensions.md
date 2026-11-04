# Property extensions

A property extension adds an attribute that is computed when it is read:

```python
from calagoapi import MinecraftServer
from calagoapi.extensions import property_extension


@property_extension(MinecraftServer)
def installedVersion(self):
    '''The installed build, or None.'''
    installed = getInstalledVersion(self)
    return installed.get('build') if installed else None
```

```python
print(server.installedVersion)                   # direct mode, no parentheses
print(server.version_changer.installedVersion)   # namespace mode
```

Runnable example: [03_property_extensions.py](../../examples/extensions/03_property_extensions.py).

## Options

```python
property_extension(target, name=None)
```

| Argument | Meaning |
| --- | --- |
| `target` | A class, or a list/tuple of classes |
| `name` | Attribute name; defaults to the getter's name |

## Read-only by default

Decorating a function creates a read-only property. Assigning to it raises
`AttributeError`, like any Python property without a setter.

## Properties with a setter

Build a normal `property` and decorate that:

```python
def _getNote(self):
    return self.data.get('note', '')


def _setNote(self, value):
    self.data['note'] = value


note = property_extension(MinecraftServer, name='note')(property(_getNote, _setNote))
```

```python
server.note = 'maintenance on Friday'
server.note                         # 'maintenance on Friday'
server.my_namespace.note = '...'    # also works in namespace mode
```

## When to use a property

Use a property for **cheap** values: things computed from data the object already
has, or cached values.

Use a **method** when reading the value makes a request. A property runs its code
on every read, which surprises people:

```python
if server.installedVersion and server.installedVersion['name'] != wanted:   # two requests
```

And in async code, reading a property cannot be awaited, so its request blocks the
event loop. A good pattern is to offer both, like the version changer does:

```python
server.getInstalledVersion()     # method: explicit, awaitable on AsyncPanel
server.installedVersion          # property: convenient in scripts and the REPL
```

## Common mistakes

- Expecting a cached value: properties are recomputed on every read. Cache
  inside a [service](class_extensions.md) if you need to.
- Using a property name that is an instance attribute (`data`, `name`, `panel`):
  `ExtensionConflictError`, because the instance attribute would hide it.
- Raising `AttributeError` inside the getter: Python then reports the property as
  missing (`hasattr()` returns False). Raise a CalagoAPI exception instead.
