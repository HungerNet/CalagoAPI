# Discovery

How does `enable('version_changer')` find code in a package you never imported?
Through Python **entry points**: a standard way for installed packages to
advertise things to each other.

## The entry point

An extension package declares one entry point in the group `calagoapi`:

```toml
[project.entry-points."calagoapi"]
version_changer = "calagoapi_version_changer.extension:VersionChangerExtension"
```

| Part | Meaning |
| --- | --- |
| `"calagoapi"` | the group CalagoAPI looks in (`calagoapi.extensions.ENTRY_POINT_GROUP`) |
| `version_changer` | the entry point name: use the extension id |
| `calagoapi_version_changer.extension` | the module to import |
| `VersionChangerExtension` | the Extension class in that module |

`pip install` records this in the package metadata. Nothing is imported at install time.

## What happens in `enable('x')`

1. CalagoAPI lists the `calagoapi` entry points of every installed package. This
   only reads metadata; it is done once and cached.
2. If an extension with id or alias `x` is already known, it is used.
3. Otherwise, the entry point **named** `x` is loaded: its module is imported and
   the class is checked and registered.
4. Still not found? The id may have been renamed and survive only as an alias
   declared inside a class. CalagoAPI then loads every remaining entry point once
   and checks again.
5. Still not found: `ExtensionNotFoundError`, with suggestions:

```text
Extension 'hungerbrige' is not installed.
Did you mean: 'hungerbridge'?
Installed extensions: hungerbridge, version_changer.
```

Only the extensions you enable (and their dependencies) are imported in the
normal case. `available()` is the exception: it imports every installed extension
to read its id.

## Without an entry point: `register()`

Scripts, notebooks, tests and examples can skip packaging:

```python
from calagoapi.extensions import Extension, enable, register


@register
class MyExtension(Extension):
    extension_id = 'mine'


enable('mine')
```

`register()` runs the same validation and uniqueness checks as entry points.
Registering the same class twice is harmless.

## Installing at runtime

Entry points are listed once per process. If you `pip install` an extension while
the program runs, rescan:

```python
from calagoapi.extensions import registry
registry.discover()
```

## Uniqueness

Ids and aliases form one global namespace. These are errors
(`ExtensionConflictError`), reported when the second extension is loaded:

- two extension classes with the same id;
- an alias equal to another extension's id or alias;
- two installed distributions publishing the same entry point name with different
  targets (usually an old fork and the original side by side; uninstall one).

## Broken packages

If an entry point cannot be imported (missing dependency, syntax error) or does
not point to an `Extension` subclass, enabling it raises `ExtensionLoadError`
with the entry point, the distribution and the original error:

```text
ExtensionLoadError: Could not load entry point 'hungerbridge'
(calagoapi_hungerbridge.extension:HungerBridgeExtension) from calagoapi-hungerbridge:
ModuleNotFoundError: No module named 'calagoapi_version_changer'
```

A broken package never stops other extensions from loading.

## Inspecting

```python
from calagoapi.extensions import registry

registry.discover()                       # entry point names (re-scan, no imports)
registry.available()                      # extension ids (imports all)
registry.get_class('version_changer')     # the Extension class
```

From a shell, the standard library can list entry points too:

```bash
python -c "from importlib.metadata import entry_points; print(entry_points(group='calagoapi'))"
```

## Common mistakes

- **The entry point group is misspelled** (`calagoAPI`, `calagoapi.extensions`):
  the extension is never found. The group is exactly `calagoapi`.
- **Editing pyproject.toml without reinstalling**: entry points live in the
  installed metadata. Run `pip install -e .` again.
- **Pointing the entry point at the module** instead of the class:
  `ExtensionLoadError: ... must point to a calagoapi.extensions.Extension subclass`.
