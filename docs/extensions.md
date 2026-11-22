# Extensions

Extensions add features to CalagoAPI from separately installed packages. Once an
extension is enabled, its methods, properties and services appear on CalagoAPI objects
as if they had always been there. This page is the reference. To learn it step by
step, follow [tutorials 06–10](tutorials/README.md#track-2-extending-calagoapi).

```python
from calagoapi.extensions import enable

enable('minecraft', config={'bridge_token_id': 'bot', 'bridge_token_secret': '9f2c...'})   # pip install calagoapi-minecraft
server = panel.minecraft.getServer('abc123')                  # added by the extension
```

> **SDK extensions vs panel extensions.** `calagoapi.extensions` is about Python
> packages that extend this SDK. `panel.admin.extensions` manages Calagopus *panel*
> extensions installed on your panel. An SDK extension may wrap a panel extension
> (none of the first-party ones currently does).

## Contents

1. [Using extensions](#using-extensions)
2. [Modes](#modes)
3. [Configuration](#configuration)
4. [Async](#async)
5. [Introspection](#introspection)
6. [Defining an extension](#defining-an-extension)
7. [Members: methods, properties, services](#members)
8. [Dependencies and aliases](#dependencies-and-aliases)
9. [Packaging and discovery](#packaging-and-discovery)
10. [Conflicts and ownership](#conflicts-and-ownership)
11. [Moving a built-in feature into an extension](#moving-a-built-in-feature-into-an-extension)
12. [Game extensions](#game-extensions)
13. [Errors](#errors)
14. [API reference](#api-reference)

## Using extensions

Extensions are separate packages. Installing `calagoapi` never installs them.

```bash
pip install calagoapi calagoapi-minecraft
```

Enable an extension by its **id**. There is no need to import its package:

```python
from calagoapi.extensions import enable

enable('minecraft')
```

`enable()` is **process-wide**. Call it once, early. It patches CalagoAPI's
*classes*, so objects that already exist gain the members immediately and objects
created later have them automatically. Calling it again without arguments is a no-op,
so libraries can call it safely. Calling it again with a **different** config or mode
raises `ConfigurationError`. There is no `disable()`; restart the process instead.

## Modes

| Mode | Members appear as | Use when |
| --- | --- | --- |
| `direct` | `server.getMemoryPercent()` | names are specific enough to live next to CalagoAPI's |
| `namespace` | `server.monitoring.getMemoryPercent()` | names are short or generic, or two extensions clash |

```python
enable('monitoring', mode='namespace')        # overrides the extension's default_mode
```

Services ignore the mode: a service already is a namespace, so `server.notes` is in
the same place in both modes.

## Configuration

User values override the extension's `default_config`; unknown keys are rejected so
typos fail immediately. The effective config is read-only.

```python
from calagoapi.extensions import enable, getExtension

enable('minecraft', config={'bridge_port': 2000})
getExtension('minecraft').config['bridge_port']     # 2000
enable('minecraft', config={'bridge_prot': 1})      # ConfigurationError: Unknown config key(s) ... bridge_prot
```

Keys listed in `secret_config` (tokens, passwords) are shown as `***` in
`registry.describe()` and in error messages.

## Async

`AsyncPanel` needs no extra step. Extension methods become awaitable, services are
wrapped and cached, `async def` members are awaited on the event loop, and generator
members become async generators. Properties run when read, so in async code prefer a
method. Extension packages that return their own types register them with
`calagoapi.aio.registerAsyncType()` (see [Async](async.md#generators-and-extension-types)).

## Introspection

```python
from calagoapi.extensions import available, enabledExtensions, isEnabled, registry

available()                              # ['minecraft', 'monitoring']  (installed or registered)
isEnabled('minecraft')                   # True
enabledExtensions()                      # [<Extension 'minecraft' mode='direct'>, ...]
registry.ownerOf(Panel, 'minecraft')     # 'minecraft'
registry.registrations(owner='minecraft')
print(registry.describe())               # versions, modes, configs (secrets masked), every member
```

## Defining an extension

```python
from calagoapi import Server
from calagoapi.extensions import ConfigurationError, Extension, ExtensionMetadata, method


@method(Server)
def getMemoryPercent(self) -> float:
    '''RAM usage in percent of the limit, or None without a limit.'''
    limit = self.getRAMLimit()
    return round(self.getRAM() / limit * 100, 1) if limit else None


class MonitoringExtension(Extension):
    extension_id = 'monitoring'                  # what users pass to enable()
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    default_mode = 'direct'                      # or 'namespace'
    namespace = None                             # namespace attribute, defaults to extension_id
    default_config = {'warn_percent': 90}
    secret_config = ()                           # config keys masked in diagnostics
    allow_unknown_config = False
    aliases = []                                 # other ids: strings or Alias(...)
    dependencies = []                            # ids or Dependency(...)
    members = None                               # None: every decorated member in this module

    def validateConfig(self, config):            # optional: check / normalize, before installing
        if not 0 < config['warn_percent'] <= 100:
            raise ConfigurationError('monitoring: warn_percent must be 1-100')
        return config

    def onEnable(self):                          # optional: runs once after installing; raising undoes it
        ...
```

Inside members, read the config with `MonitoringExtension.get().config`.

## Members

| Decorator | Installed as | Example |
| --- | --- | --- |
| `@method(Target, name=None)` | a method | `server.getMemoryPercent()` |
| `@propertyExtension(Target, name=None)` | a read-only property (or pass a `property` for setters) | `server.memoryPercent` |
| `@classExtension(Target, name)` | a service: `ServiceClass(obj)`, created on first access and cached | `server.notes.add('...')` |

- Decorators only label the object: importing a module never changes CalagoAPI.
- `Target` may be a list of classes. Members on a base class (e.g. `Server`) are
  inherited by subclasses (e.g. a game extension's `MinecraftServer`).
- Inside members, call sibling members as functions (`getMemoryPercent(self)`), not
  as `self.getMemoryPercent()`: in namespace mode the latter does not exist.
- `def` members work on `Panel` and become awaitable on `AsyncPanel`. `async def`
  members are awaited directly on `AsyncPanel`.

## Dependencies and aliases

```python
class AlertsExtension(Extension):
    extension_id = 'alerts'
    dependencies = ['monitoring', Dependency('metrics', optional=True)]
    aliases = ['server_alerts', Alias('old_alerts', deprecated=True, message='Renamed in 2.0.')]
```

- Dependencies are enabled first, with their defaults, and remember `enabled_by`. To
  configure one, enable it yourself **before** the extension that needs it.
- Missing dependencies raise `DependencyError` (with a `pip install` hint for
  first-party ids); cycles raise `CircularDependencyError` with the path; optional
  dependencies that are not installed are skipped.
- Ids and aliases share one global namespace. A deprecated alias emits an
  `ExtensionDeprecationWarning` pointing at the caller.

## Packaging and discovery

A package publishes one entry point in the group **`calagoapi`**. Its name is the
extension id, and its value is the Extension class:

```toml
[project]
name = "calagoapi-monitoring"                 # convention: calagoapi-<name>
dependencies = ["calagoapi>=2.0.dev1"]

[project.entry-points."calagoapi"]
monitoring = "calagoapi_monitoring.extension:MonitoringExtension"
```

`enable('x')` lists entry points once (metadata only), loads the one named `x`, and
falls back to loading every entry point once so aliases are found. Scripts, notebooks
and tests can skip packaging with `register(ExtensionClass)`. After installing a
package at runtime, call `registry.discover()`. A complete template is in
[examples/extensions/packaged_extension/](../examples/extensions/packaged_extension/).

## Conflicts and ownership

Before anything is installed, every planned name is checked against CalagoAPI's own
members (including instance attributes such as `server.files`, and names defined on
subclasses), other extensions on the same class, its bases and subclasses, and the
async wrappers. Any clash raises `ExtensionConflictError`, which names both owners;
nothing is installed partially and nothing is silently overridden. Every installed
attribute is recorded as a `Registration` (`owner`, `target`, `name`, `kind`).

## Moving a built-in feature into an extension

`@migratedTo(extension_id, package)` marks a built-in method that moved to an
extension. The built-in keeps working with an `ExtensionDeprecationWarning`, and only
that extension may replace it when enabled. Remove the built-in in the next major
version. CalagoAPI 2.0 removed all its 1.x shims; the mechanism stays for future
moves (the Subdomain Manager is the next candidate).

## Game extensions

Game support follows one pattern, used by `calagoapi-minecraft`:

1. A `Server` subclass with the game's features (`class MinecraftServer(Server)`),
   overriding methods such as `sendCommand()` or `streamConsole()` where the game
   offers something better. Keep the base signature callable (add keyword-only options).
2. A service on `Panel` (`@classExtension(Panel, 'minecraft')`) that builds those
   servers with `panel.servers.getServer(server_id, server_class=MinecraftServer)`.
3. `calagoapi.aio.registerAsyncType()` for the subclass and any other returned types.
4. Game-specific clients (like HungerBridgePy) are dependencies of the extension package, never of `calagoapi`.

## Errors

All derive from `ExtensionError`, a `CalagoAPIError`.

| Error | When |
| --- | --- |
| `ExtensionNotFoundError` (+`LookupError`) | not installed; lists close matches, `pip install` hints, and replacements for 1.x ids |
| `ExtensionLoadError` | an entry point fails to import or is not an Extension subclass |
| `ExtensionDefinitionError` (+`TypeError`) | invalid Extension class or member |
| `ExtensionConflictError` | duplicate ids/aliases or member names |
| `DependencyError`, `CircularDependencyError` | missing or circular dependencies |
| `ConfigurationError` (+`ValueError`) | bad config, unknown keys, re-enable with a different config/mode |
| `ExtensionNotEnabledError` | `getExtension()` / `Extension.get()` before `enable()` |
| `ExtensionDeprecationWarning` | deprecated alias or migrated built-in used |

## API reference

| Function | Purpose |
| --- | --- |
| `enable(extension_id, mode=None, config=None)` | enable an extension and its dependencies; returns the `Extension` |
| `register(extension_class)` | make a class known without an entry point (also a decorator) |
| `getExtension(extension_id)` | the enabled instance (`.config`, `.mode`, `.metadata`, `.enabled_by`) |
| `isEnabled(extension_id)` | ids and aliases |
| `available()` | ids of every installed or registered extension |
| `enabledExtensions()` | enabled instances, in enable order |
| `registry` | `ExtensionRegistry`: `ownerOf()`, `registrations()`, `describe()`, `getClass()`, `discover()` |
| `method`, `propertyExtension`, `classExtension` | member decorators |
| `migratedTo(extension_id, package)` | hand a built-in over to an extension |
| `Extension`, `ExtensionMetadata`, `Alias`, `Dependency` | definitions |

The design (registry, ownership model, alternatives considered) is recorded in
[design/extension-system.md](design/extension-system.md).
