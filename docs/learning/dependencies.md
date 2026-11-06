# Dependencies

An extension can build on other extensions. CalagoAPI enables them first,
automatically:

```python
class HungerBridgeExtension(Extension):
    extension_id = 'hungerbridge'
    dependencies = ['version_changer']
```

```python
enable('hungerbridge')
# 1. enables version_changer (with its default config and mode)
# 2. enables hungerbridge
```

Runnable example: [05_dependencies.py](../../examples/extensions/05_dependencies.py).

## Declaring dependencies

Strings for the simple case, `Dependency` objects for options:

```python
from calagoapi.extensions import Dependency

dependencies = [
    'version_changer',                       # required
    Dependency('metrics', optional=True),    # enabled if installed, skipped if not
]
```

Ids and aliases both work. Also list the dependency's **package** in your
`pyproject.toml`, so `pip install` brings it along:

```toml
dependencies = ["calagoapi>=1.0.dev2", "calagoapi-version-changer>=1.0.0"]
```

`dependencies` on the Extension class is about *enabling*; the pyproject
dependency is about *installing*. You usually need both.

## Who enabled what

```python
get_extension('version_changer').enabled_by   # 'hungerbridge'
get_extension('hungerbridge').enabled_by      # None: you enabled it yourself
```

`registry.describe()` shows the same information.

## Configuring a dependency

Dependencies are enabled with their defaults. To configure one, enable it
**yourself, first**:

```python
enable('version_changer', config={'auto_backup': True})
enable('hungerbridge')      # version_changer is already enabled; it is reused
```

The other order fails, because the dependency is already active with its
defaults and extensions cannot be reconfigured:

```python
enable('hungerbridge')
enable('version_changer', config={'auto_backup': True})
# ConfigurationError: ... It was enabled automatically as a dependency of 'hungerbridge';
# to choose its mode or configuration, enable 'version_changer' before 'hungerbridge'.
```

## Errors

**Missing:**

```text
DependencyError: Extension 'hungerbridge' requires 'version_changer', which is not installed.
Install it with: pip install calagoapi-version-changer
```

**Circular** (`CircularDependencyError`, a `DependencyError`):

```text
CircularDependencyError: Circular extension dependency: chicken -> egg -> chicken
```

`e.cycle` holds the list (`['chicken', 'egg', 'chicken']`).

**A dependency fails to enable** (conflict, bad config, broken package): a
`DependencyError` naming both extensions, with the original error attached as
`__cause__`.

In every case the extension you asked for is not enabled. Dependencies that were
enabled successfully before the failure stay enabled.

## Using a dependency from your code

The dependency is guaranteed to be enabled before your `on_enable()` runs and
before any of your members can be called. Import its functions and call them
directly, so your code works whatever mode the user chose for the dependency:

```python
from calagoapi_version_changer.extension import getInstalledVersion


@class_extension(MinecraftServer, 'hungerbridge')
class HungerBridge:
    def install(self):
        installed = getInstalledVersion(self.server)
        ...
```

`self.server.getInstalledVersion()` would also work in direct mode, but not if
the user enabled `version_changer` in namespace mode.

## Version constraints

Dependencies are not version-aware yet: `Dependency('x')` accepts any installed
version. Use version specifiers in `pyproject.toml` meanwhile
(`calagoapi-version-changer>=1.0.0`). The `Dependency` object is where version
constraints will be added later.

## Common mistakes

- Listing the dependency in `Extension.dependencies` but not in `pyproject.toml`:
  users get `DependencyError` after `pip install`ing your package.
- Configuring a dependency after the extension that needs it: see above.
- Optional dependencies that are not really optional: if your code imports the
  dependency's package at module level, the import fails when it is missing.
  Import it inside the function that uses it.
