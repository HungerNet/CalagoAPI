# Extensions

Extensions add features to CalagoAPI without changing CalagoAPI itself. An
extension is a normal Python package. Once you install it and enable it, its
methods appear on CalagoAPI objects as if they had always been there:

```python
from calagoapi.extensions import enable

enable('version_changer')

server = panel.servers.getMinecraftServer('abc123')
server.installVersion(build)        # added by the extension
print(server.installedVersion)      # a property, also added by the extension
```

This guide is for **using** extensions. To write one, continue with
[Creating extensions](creating_extensions.md).

## Contents

1. [Installing and enabling](#installing-and-enabling)
2. [What an extension can add](#what-an-extension-can-add)
3. [Direct and namespace mode](#direct-and-namespace-mode)
4. [Configuration](#configuration)
5. [Enabling twice](#enabling-twice)
6. [Async](#async)
7. [Seeing what is enabled](#seeing-what-is-enabled)
8. [Errors](#errors)
9. [Common mistakes](#common-mistakes)
10. [All guides](#all-guides)

## Installing and enabling

Extensions are separate packages. Installing `calagoapi` never installs them:

```bash
pip install calagoapi
pip install calagoapi-version-changer
```

Enable an extension by its **id**. You do not import the package:

```python
from calagoapi.extensions import enable

enable('version_changer')     # good
# import calagoapi_version_changer   <- not needed
```

`enable()` is **process-wide**: call it once, early (for example next to where
you create your `Panel`). It affects:

- objects that **already exist**: they gain the new members immediately;
- objects created **later**: they have them automatically.

```python
server = panel.servers.getMinecraftServer('abc123')   # created first
enable('version_changer')                              # enabled afterwards
server.installVersion(build)                           # works
```

That works because extensions patch CalagoAPI's *classes* (like
`MinecraftServer`), never single objects.

## What an extension can add

| Kind | Looks like | Guide |
| --- | --- | --- |
| Method | `server.installVersion(build)` | [Method extensions](method_extensions.md) |
| Property | `server.installedVersion` | [Property extensions](property_extensions.md) |
| Service | `server.hungerbridge.players()` | [Class extensions](class_extensions.md) |

A **service** is a helper object attached to another object, like CalagoAPI's
own `server.files` or `server.backups`. Each server gets its own service, created
on first use and then reused:

```python
server.hungerbridge is server.hungerbridge   # True
```

## Direct and namespace mode

Every extension has a default **mode**, and you can choose another one when you
enable it.

**Direct** (members appear on the object):

```python
enable('version_changer')                       # its default is direct
server.installVersion(build)
```

**Namespace** (members appear under one attribute, named after the extension):

```python
enable('version_changer', mode='namespace')
server.version_changer.installVersion(build)
server.version_changer.installedVersion
```

Namespace mode is useful when two extensions want the same method name, or when
you want to see at a glance which extension a call comes from.

Services ignore the mode: a service is already a namespace, so
`server.hungerbridge` is in the same place in both modes.

## Configuration

Extensions can be configured when enabled. Your values override the
extension's defaults; keys you leave out keep their default:

```python
enable('hungerbridge', config={
    'token': 'bot:9f2c...',
    'mc_version': '1.21.11',
})
```

Unknown keys are rejected, so typos fail immediately instead of being ignored:

```python
enable('hungerbridge', config={'tokn': '...'})
# ConfigurationError: Unknown config key(s) for extension 'hungerbridge': tokn. Known keys: ...
```

The extension's README lists its keys. You can read the effective configuration
back with `get_extension()`:

```python
from calagoapi.extensions import get_extension
get_extension('hungerbridge').config['port']   # 1913
```

## Enabling twice

Calling `enable()` again is safe:

```python
enable('version_changer')
enable('version_changer')     # does nothing
```

Enabling it again with a **different** configuration or mode is an error, because
an extension cannot be reconfigured once it is active:

```python
enable('hungerbridge', config={'mc_version': '1.20.4'})
enable('hungerbridge', config={'mc_version': '1.21.1'})
# ConfigurationError: Extension 'hungerbridge' is already enabled with a different configuration.
```

`enable('x')` without `config` or `mode` never fails for an enabled extension:
it just means "make sure x is on". Libraries can call it safely.

There is no `disable()`. Restart the process to turn an extension off.

## Async

`AsyncPanel` works with extensions without any extra step. Methods become
awaitable, services too:

```python
from calagoapi import AsyncPanel
from calagoapi.extensions import enable

enable('version_changer')
enable('hungerbridge', config={'token': 'bot:9f2c...'})

async with AsyncPanel(url=..., api_key=...) as panel:
    server = await panel.servers.getMinecraftServer('abc123')
    await server.installVersion(build)
    print(await server.hungerbridge.players())
```

Properties are read without `await`, and they run their code right away. In
async code prefer the method form when an extension offers one
(`await server.getInstalledVersion()` instead of `server.installedVersion`).

## Seeing what is enabled

```python
from calagoapi.extensions import available, enabled_extensions, is_enabled, registry

available()                  # ['hungerbridge', 'version_changer']  (installed)
is_enabled('hungerbridge')   # True / False
enabled_extensions()         # [<Extension 'version_changer' mode='direct'>, ...]

registry.owner_of(MinecraftServer, 'installVersion')   # 'version_changer'
print(registry.describe())
```

`describe()` prints every enabled extension, its version, mode, configuration
(secrets masked) and every member it added:

```text
version_changer 1.0.0 by iFamished [direct, enabled by 'hungerbridge'] (entry point ...)
  config: {'auto_backup': False, ...}
  MinecraftServer.installVersion (method, from 'version_changer')
  ...
```

## Errors

All extension errors derive from `ExtensionError`, which is a `CalagoAPIError`.

| Error | When |
| --- | --- |
| `ExtensionNotFoundError` | The extension is not installed. The message suggests close matches and, for first-party extensions, the `pip install` command. |
| `DependencyError` | Something the extension needs is missing. |
| `CircularDependencyError` | Extensions depend on each other in a loop. |
| `ConfigurationError` | Bad configuration, or a different configuration/mode than before. |
| `ExtensionConflictError` | The extension wants a name that is already taken (by CalagoAPI or another extension). |
| `ExtensionLoadError` | The installed package is broken (import error). |
| `ExtensionNotEnabledError` | `get_extension()` before `enable()`. |

```python
from calagoapi.extensions import enable, ExtensionNotFoundError

try:
    enable('hungerbridge')
except ExtensionNotFoundError as e:
    print(e)
    # Extension 'hungerbridge' is not installed.
    # Install it with: pip install calagoapi-hungerbridge
```

## Common mistakes

- **Importing the extension package.** Not needed and not enough:
  importing does not enable anything. Use `enable('id')`.
- **Enabling inside a loop or per request with different configs.** Configure
  once at startup; a second, different config raises `ConfigurationError`.
- **Expecting `enable()` to affect one server only.** It is process-wide by design.
- **Mixing up panel extensions and SDK extensions.** `panel.admin.extensions`
  manages Calagopus *panel* extensions installed on your panel.
  `calagoapi.extensions` is about Python packages that extend this SDK. Some SDK
  extensions (like `version_changer`) talk to a panel extension of the same name.

## All guides

1. **Extensions** (this page)
2. [Creating extensions](creating_extensions.md)
3. [Method extensions](method_extensions.md)
4. [Property extensions](property_extensions.md)
5. [Class (service) extensions](class_extensions.md)
6. [Discovery](discovery.md): how `enable('x')` finds a package
7. [Dependencies](dependencies.md)
8. [Aliases](aliases.md): renaming extensions safely
9. [First-party extensions](first_party_extensions.md): `version_changer`, `hungerbridge`
10. [Migrating built-in features](migrating_builtin_features.md): moving CalagoAPI features into extensions

Runnable examples: [examples/extensions/](../../examples/extensions/README.md).
