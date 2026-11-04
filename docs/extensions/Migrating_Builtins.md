# Migrating built-in features

The extension system is the canonical way to extend CalagoAPI. Some features that
were built into CalagoAPI fit better as extensions, typically because they depend
on something optional (a Calagopus panel extension, a mod). This page explains
how they are moved without breaking users, and records what was moved.

It is written for **contributors**. If you are a user looking at a deprecation
warning, the short version is:

```bash
pip install calagoapi-version-changer
```

```python
from calagoapi.extensions import enable
enable('version_changer')     # once, at startup; your other code stays the same
```

## What was evaluated

| Feature | Where it was | Decision |
| --- | --- | --- |
| Minecraft Version Changer (`getInstalledVersion`, `getVersionTypes`, `getVersions`, `getBuilds`, `installVersion`) | `MinecraftServer` | **Moved** to `calagoapi-version-changer`. Built-ins deprecated. |
| Version Changer admin helpers (`getVersionChangerSettings`, ...) | `panel.admin.extensions` | **Moved** with it. Built-ins deprecated. |
| `panel.api.versions` (`VersionsAPI`) | `calagoapi.api` | Kept, deprecated; the extension has its own `VersionChangerAPI`. Removed together with the built-ins. |
| HungerBridge | not in CalagoAPI | **New** extension `calagoapi-hungerbridge`. |
| Subdomain Manager (`server.network` subdomains, `panel.admin.subdomain_domains`) | `NetworkManager`, `Admin`, `Subdomain`, `SubdomainDomain` | **Kept for now.** Woven through several managers, models and the contract tests; the next candidate (`calagoapi-subdomains`). |
| Panel extension management (`panel.admin.extensions`) | `Admin` | Core: it manages the panel, every admin needs it. |
| Minecraft console helpers, `server.properties`, EULA | `MinecraftServer` | Core: plain Minecraft functionality, no optional dependency. |

## The migration pattern

Moving a feature has to satisfy two requirements that pull in opposite
directions: **existing code keeps working**, and **the extension owns the names
afterwards** (with conflicts still detected for everyone else). The
`@migrated_to` decorator does both.

### 1. Write the extension

Re-implement the feature with the public extension API in its own package under
`src/extensions/`, with the **same method names and signatures**. Do not import
the built-in implementation; the built-in will be deleted later.

```python
@method(MinecraftServer)
def installVersion(self, build, truncate_directory=False, accept_eula=True):
    ...
```

### 2. Mark the built-ins

In core, keep the old methods and mark them:

```python
from calagoapi.extensions.compat import migrated_to


class MinecraftServer(GenericServer):
    @migrated_to('version_changer', 'calagoapi-version-changer')
    def installVersion(self, build, truncate_directory=False, accept_eula=True):
        '''Deprecated, use the calagoapi-version-changer extension. Installs a server build.'''
        ...   # unchanged implementation
```

`@migrated_to(extension_id, package)`:

- keeps the method working;
- emits an `ExtensionDeprecationWarning` on each call, pointing at the caller,
  with the `pip install` and `enable()` instructions;
- marks the method as **handed over** to that extension id (and its aliases).

### 3. What happens at runtime

| Situation | `server.installVersion(...)` |
| --- | --- |
| Extension not installed | built-in, with a deprecation warning |
| Installed, not enabled | built-in, with a deprecation warning |
| `enable('version_changer')` (direct mode) | the extension's method; the built-in is replaced on the class |
| `enable('version_changer', mode='namespace')` | built-in (warning) on `server.installVersion`, extension at `server.version_changer.installVersion` |
| Another extension adds `installVersion` | `ExtensionConflictError`, owner `calagoapi` (or `version_changer` once enabled) |

The registry records the replaced built-in in `Registration.replaced`:

```python
r = registry.registrations(owner='version_changer')[0]
r.name, r.replaced     # ('getInstalledVersion', <function MinecraftServer.getInstalledVersion>)
```

### 4. Tests

- Keep the core tests that call the built-ins (they prove compatibility).
- The extension's tests check that enabling replaces each built-in
  (`Registration.replaced`), that no deprecation warning is raised afterwards,
  and that every endpoint still matches `openapi.json`.

### 5. Remove the built-ins (next major version)

1. Delete the `@migrated_to` methods and any core helpers only they used.
2. Mention the removal in the release notes, with the `pip install` line.
3. The extension does not change: it no longer replaces anything, it simply adds.

## Checklist

- [ ] Same names and signatures in the extension
- [ ] Extension does not import the built-in implementation
- [ ] `@migrated_to('<id>', '<package>')` on every moved built-in
- [ ] Docstrings of the built-ins say "Deprecated, use the <package> extension"
- [ ] Extension tests cover the handover and the endpoints
- [ ] Docs: [First-party extensions](06_First_Party_Extensions.md), the feature's guide, the changelog
- [ ] `FIRST_PARTY` in `calagoapi/extensions/discovery.py` lists the package

## Why not just delete the built-ins?

Every script calling `server.installVersion()` would break on upgrade with an
`AttributeError` that says nothing about the new package. The deprecation period
turns that into a warning that explains the fix, at almost no cost: one
decorator per method.

## Why not keep both, side by side?

Because "never silently override functionality" is a core rule of the extension
system. Without the handover marker, enabling the extension would be a conflict
with CalagoAPI itself; with a silent override, any extension could replace any
built-in. `@migrated_to` is an explicit, per-method, per-extension permission.
