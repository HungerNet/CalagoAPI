# PLAN: first-class extension system for CalagoAPI

Status: implemented in this change. This file records the design and the reasons
behind it. It is a working document, not an approval gate.

## 1. What exists today (inspection summary)

- `src/calagoapi/` is a sync SDK (`Panel`) plus `AsyncPanel`, which wraps every sync
  object in `AsyncWrapper` and runs each method in a worker thread. A method added to
  a sync class therefore becomes awaitable automatically (`await server.foo()`).
- `MinecraftServer` (`servers/minecraft.py`) contains the Calagopus **Minecraft Version
  Changer** helpers (`getInstalledVersion`, `getVersionTypes`, `getVersions`,
  `getBuilds`, `installVersion`) backed by `panel.api.versions` (`api/versions.py`).
- `panel.admin.extensions` (`ExtensionManager`) manages *panel-side* Calagopus extensions
  and also carries four Version Changer admin helpers (`getVersionChangerSettings`, ...).
- The **Subdomain Manager** panel extension is wrapped in core (`server.network`
  subdomains, `panel.admin.subdomain_domains`, `Subdomain`, `SubdomainDomain`).
- **HungerBridge** (sibling repo `../hungerbridge`) is a Paper/Fabric mod exposing an
  HMAC-signed HTTP API on port 1913. `PROJECT_NOTES.md` records it as "not ported".
- Packaging: one `pyproject.toml`, version from `version.yaml`, one GitHub workflow
  (`release.yml`) that builds and publishes on every push to `main` when `run: true`.
  There is no CI test job.
- Tests: 38 offline tests (`pytest`), including contract tests that fake the panel
  from `openapi.json` by patching `requests.Session.request` for the whole session.
- Style: single quotes, camelCase methods, snake_case attributes, light typing.

## 2. Goals

1. A process-global extension system in `calagoapi.extensions` that lets separately
   installed packages add **methods**, **properties** and **services** to existing
   CalagoAPI classes, discovered through Python entry points.
2. Extensions feel native: `enable('version_changer')` then `server.installVersion(...)`,
   on objects that already exist and on future objects, sync and async.
3. One authoritative registry that tracks discovery, metadata, aliases, enabled state,
   configuration, dependencies and **who owns every installed member**.
4. Fail loudly: conflicts, bad configuration, missing extensions and dependency
   problems raise specific exceptions with actionable messages. Nothing is silently
   overridden or reconfigured.
5. First-party extensions (`calagoapi-version-changer`, `calagoapi-hungerbridge`) are
   independent PyPI packages built only on the public extension API.
6. Existing user code keeps working.

## 3. Non-goals

- `disable()` / unloading extensions (out of scope; the registry keeps an internal,
  private rollback used only for failed enables and tests).
- Version-aware dependency constraints (the `Dependency` object is the place to add
  them later).
- Per-instance (per-server) enablement. Enablement is process-global by design.
- Sandboxing extension code. Extensions are trusted Python code.
- Moving the Subdomain Manager wrappers out of core in this change (see §11).

## 4. Public API

Everything is importable from `calagoapi.extensions`:

```python
from calagoapi.extensions import (
    # enabling and inspecting
    enable, register, get_extension, is_enabled, available, enabled_extensions, registry,
    # defining
    Extension, ExtensionMetadata, Alias, Dependency,
    method, property_extension, class_extension,
    # errors
    ExtensionError, ExtensionNotFoundError, ExtensionLoadError, ExtensionDefinitionError,
    ExtensionConflictError, DependencyError, CircularDependencyError, ConfigurationError,
    ExtensionNotEnabledError, ExtensionDeprecationWarning,
)
```

| Function | Purpose |
| --- | --- |
| `enable(extension_id, mode=None, config=None)` | Enable an extension (and its dependencies). Returns the `Extension` instance. Idempotent. |
| `register(extension_class)` | Make an extension known without an entry point (scripts, tests, examples). Usable as a class decorator. |
| `get_extension(extension_id)` | The enabled `Extension` instance (gives access to `.config`, `.mode`, `.metadata`). |
| `is_enabled(extension_id)` | `True` if enabled (ids and aliases accepted). |
| `available()` | Sorted ids of every installed or registered extension. |
| `enabled_extensions()` | Enabled `Extension` instances, in enable order. |
| `registry` | The process-global `ExtensionRegistry` (introspection: `registrations()`, `owner_of()`, `describe()`). |

Defining an extension:

```python
from calagoapi import MinecraftServer
from calagoapi.extensions import Extension, ExtensionMetadata, method, property_extension, class_extension

@method(MinecraftServer)
def installVersion(self, build): ...

@property_extension(MinecraftServer)
def installedVersion(self): ...

@class_extension(MinecraftServer, 'hungerbridge')
class HungerBridge:
    def __init__(self, server): ...

class VersionChangerExtension(Extension):
    extension_id = 'version_changer'
    metadata = ExtensionMetadata(author='iFamished', version='1.0.0', schema=1)
    aliases = []                 # strings or Alias('old_id', deprecated=True)
    dependencies = []            # strings or Dependency('other_id')
    default_mode = 'direct'      # or 'namespace'
    namespace = None             # namespace attribute name, defaults to extension_id
    default_config = {'auto_backup': False}
    secret_config = ()           # config keys masked as *** in describe() and errors
    members = None               # None = collect decorated members from this module

    def validate_config(self, config): return config   # optional
    def on_enable(self): ...                            # optional
```

Naming: the extension API uses the snake_case names given in the specification
(`enable`, `on_enable`, `extension_id`, ...). Members that extensions add to CalagoAPI
classes should keep CalagoAPI's camelCase method style (`installVersion`).

## 5. Discovery

- Entry point group: **`calagoapi`**. Name = extension id, value = the Extension class:

  ```toml
  [project.entry-points."calagoapi"]
  version_changer = "calagoapi_version_changer.extension:VersionChangerExtension"
  ```

- Discovery is lazy: entry points are listed (cheap, no imports) the first time the
  registry needs them. `enable(name)` loads only the entry point whose name matches.
  If no entry point name matches, every not-yet-loaded entry point is loaded once so
  renamed ids and aliases declared inside classes are still found.
- Loading an entry point imports the module, checks the object is an `Extension`
  subclass and registers it. Import failures become `ExtensionLoadError` naming the
  entry point and distribution.
- During the full scan, a broken or conflicting package is recorded and skipped, so it
  never blocks other extensions. Asking for it by name re-raises its original error;
  "not found" messages list recorded failures as notes.
- Two distributions publishing the same entry point name with different targets raise
  `ExtensionConflictError` when that name is used.
- `register(cls)` adds classes directly (same validation, same uniqueness rules).
- Python 3.9 `entry_points()` (dict API) and 3.10+ (`select`) are both supported.

## 6. Registry design

`ExtensionRegistry` (`calagoapi/extensions/registry.py`), one global instance:

| State | Type | Notes |
| --- | --- | --- |
| `_entry_points` | name -> EntryPoint | listed once, lazily |
| `_classes` | extension_id -> Extension subclass | discovered or registered |
| `_aliases` | alias -> `(extension_id, Alias)` | global uniqueness with ids |
| `_enabled` | extension_id -> Extension instance | ordered (enable order) |
| `_registrations` | `(target class, attribute name)` -> `Registration` | every installed member |
| `_claimed` | member spec -> extension_id | a decorated member belongs to one extension |

All mutating operations take one `threading.RLock` (AsyncPanel runs code in threads).

## 7. Ownership model

Every attribute an extension installs on a class is recorded as a `Registration`:

```python
Registration(owner='version_changer', target=MinecraftServer, name='installVersion',
             kind='method',            # 'method' | 'property' | 'service' | 'namespace'
             member=<MemberSpec>,      # what the extension declared (None for namespaces)
             namespace=None,           # namespace name for members placed in a namespace
             replaced=<legacy shim>)   # built-in this replaced through a migration handover
```

- The registry is the source of truth: `registry.owner_of(MinecraftServer, 'installVersion')`,
  `registry.registrations(owner='version_changer')`, `registry.describe()`.
- Members placed inside a namespace are recorded too (`kind='method', namespace='hb'`),
  so tooling can list everything an extension provides.
- Decorated members are claimed by exactly one extension. Claiming a member that
  another extension already owns raises `ExtensionDefinitionError`.
- Installed descriptors (services, namespaces) carry `owner` for debugging, but the
  registry, not the class attribute, is authoritative.

## 8. Member kinds and modes

| Kind | Decorator | Installed as | Direct mode | Namespace mode |
| --- | --- | --- | --- | --- |
| method | `@method(Target, name=None)` | the function | `obj.name(...)` | `obj.<ns>.name(...)` |
| property | `@property_extension(Target, name=None)` | `property(fget)` | `obj.name` | `obj.<ns>.name` |
| service | `@class_extension(Target, name)` | cached descriptor | `obj.name` | `obj.name` |

- Decorators have **no side effects**. They attach a `MemberSpec` list to the object
  and return it unchanged, so decorated functions stay normal, testable Python.
  Decorators can be stacked to target several classes; `Target` may be a tuple/list.
- An extension's members are `Extension.members` if set, else every decorated object
  found in the module that defines the Extension class (so members can be defined in
  other modules and imported).
- **Services are namespaces already**, so mode does not move them: `server.hungerbridge`
  is the same in both modes. Mode changes where methods and properties go. This keeps
  `server.hungerbridge.players()` from turning into `server.hungerbridge.hungerbridge`.
- Namespace name: `Extension.namespace`, default `extension_id`. The namespace object is
  created once per instance and cached; method lookups bind to the *original object*
  (`self` is still the server). Namespaces resolve members through the instance's MRO,
  so a member registered on `GenericServer` is visible in `minecraft_server.<ns>`.
- Services: the descriptor creates `ServiceClass(obj)` on first access and stores it in
  `obj.__dict__`, so `server.hungerbridge is server.hungerbridge` and later lookups do
  not touch the descriptor at all. Creation is locked so two threads cannot build two
  instances. Namespaces use the same caching.
- Patch classes, never instances. Existing objects see new class attributes
  immediately; future objects inherit them.

### Async

- `AsyncWrapper` awaits coroutine-function members directly instead of running them in
  a thread, so both `def` and `async def` extension methods work with `AsyncPanel`.
  Sync `def` members are recommended: they work on `Panel` and become awaitable on
  `AsyncPanel` automatically.
- `wrap()` wraps extension services and namespaces in a cached `AsyncWrapper`, so
  `await server.hungerbridge.players()` works and `server.hungerbridge is
  server.hungerbridge` holds on async servers too.
- Properties are evaluated when read, also on async servers (documented: prefer the
  method form, e.g. `await server.getInstalledVersion()`, inside an event loop).

## 9. Dependency handling

- `dependencies` accepts ids/aliases or `Dependency(id, optional=False)` objects.
  Strings are normalized to `Dependency`. Future constraints (`version=...`) slot in here.
- `enable(x)` resolves the graph depth-first with an explicit path stack:
  - missing dependency -> `DependencyError` ("'hungerbridge' requires 'version_changer',
    which is not installed. Install it with: pip install calagoapi-version-changer");
  - cycle -> `CircularDependencyError` with the path (`a -> b -> a`);
  - optional dependencies that are not installed are skipped.
- Dependencies are enabled first, with their defaults, and remember who enabled them
  (`enabled_by`) for error messages.

## 10. Configuration and re-enablement

- `config = {**default_config, **user_config}` (shallow merge), then
  `validate_config(config)` may normalize or raise `ConfigurationError`.
- Unknown keys raise `ConfigurationError` unless `allow_unknown_config = True`
  (typos fail fast; listed with the known keys).
- The effective config is frozen (`MappingProxyType`) and exposed as `extension.config`.
- Keys listed in `secret_config` (tokens, passwords) are shown as `***` in
  `registry.describe()` and in re-enable error messages.
- Re-enable rules:
  - `enable(x)` again with no `config`/`mode`: no-op, returns the existing instance.
  - Explicit `config` whose effective result equals the current one: no-op.
  - Explicit different `config` or `mode`: `ConfigurationError` naming both values,
    and, if the extension was auto-enabled as a dependency, telling the user to enable
    it explicitly first.
  - Using an alias counts as the same extension.

## 11. Conflict handling

Before anything is installed, every planned attribute is checked against:

1. **Built-in members**: an attribute defined in the target's MRO, defined on any
   subclass (it would shadow the extension there), or assigned as `self.<name>` in any
   method of those classes (instance attributes shadow class attributes; found by
   parsing the class source with `ast`, cached).
2. **Other extensions**: any registration with the same name on the same class, a base
   class or a subclass, owned by a different extension.
3. **The same extension**: the same name twice on the same class.
4. **Async wrapper names** (`target`, `console`, `streamConsole`, ...), which would make the
   member unreachable through `AsyncPanel`.
5. Invalid names: non-identifiers and dunder names (`ExtensionDefinitionError`).

`ExtensionConflictError` carries `extension`, `owner`, `target`, `member` and a message
such as:

```
Extension 'other_ext' cannot add method 'installVersion' to MinecraftServer:
it is already provided by extension 'version_changer' (method on MinecraftServer).
```

The whole extension is checked first and installed only if every member is clean, so a
conflict never leaves a half-installed extension.

**Migration handover** (the one exception to rule 1): a built-in that is moving to an
extension is decorated in core with `@migrated_to('version_changer', ...)`. Only that
extension (by id or alias) may replace it; everyone else still gets a conflict. The
replaced built-in is recorded in `Registration.replaced`.

## 12. Lifecycle design

`enable()` for one extension runs these steps under the registry lock:

1. resolve id/alias (deprecation warning for deprecated aliases);
2. resolve and enable dependencies;
3. instantiate the Extension (`__init__` takes no arguments);
4. merge and validate config, set `mode`, `namespace`;
5. collect members, claim them, plan installs, run conflict checks;
6. install members on classes;
7. call `on_enable()`;
8. mark enabled.

If step 5 fails nothing was changed. If step 6 or 7 fails, the attributes installed by
this call are removed and claims released (internal rollback), then the error is
re-raised. Dependencies enabled successfully before stay enabled.

Hooks are plain methods on `Extension` with default no-op implementations, so new hooks
(e.g. `on_service_created`, `on_panel_created`) can be added later without breaking
existing extensions. `Extension.get()` returns the enabled instance of that class.

## 13. Exceptions

All derive from `ExtensionError(CalagoAPIError)`:

| Exception | Raised when |
| --- | --- |
| `ExtensionNotFoundError` (+`LookupError`) | id/alias unknown; message lists available ids, close matches and a pip hint for first-party ids |
| `ExtensionLoadError` | an entry point fails to import or is not an Extension subclass |
| `ExtensionDefinitionError` (+`TypeError`) | invalid Extension class or member (bad id, bad mode, dunder name, ...) |
| `ExtensionConflictError` | duplicate ids/aliases, member conflicts |
| `DependencyError` | dependency missing or failing |
| `CircularDependencyError(DependencyError)` | dependency cycle |
| `ConfigurationError` (+`ValueError`) | bad config, unknown keys, re-enable with different config/mode |
| `ExtensionNotEnabledError` | `get_extension()` / `Extension.get()` before `enable()` |
| `ExtensionDeprecationWarning(DeprecationWarning)` | deprecated alias or migrated built-in used |

## 14. Migration strategy

| Feature | Decision |
| --- | --- |
| Minecraft Version Changer (`MinecraftServer` helpers + `ExtensionManager.getVersionChanger*`) | **Migrated** to `calagoapi-version-changer`. Core keeps the old methods as deprecated shims (`@migrated_to`), so existing code works unchanged; enabling the extension hands the names over. Adds `installedVersion` property and optional `auto_backup` (default `False`, so behaviour is unchanged). Core `panel.api.versions` stays as a deprecated alias for one major version. |
| HungerBridge | **New** `calagoapi-hungerbridge`: a `server.hungerbridge` service for the HungerBridge mod API (HMAC-signed), plus `install()` which uses the version changer to pick the right jar. Depends on `version_changer`. |
| Subdomain Manager (`server.network` subdomains, `admin.subdomain_domains`) | **Kept in core for now.** It is woven through `NetworkManager`, `Admin`, models and the contract tests; moving it is a larger, separate change. Documented as the next candidate. |
| `panel.admin.extensions` (panel-side extension management) | Core. It manages Calagopus panel extensions, not SDK extensions; the docs explain the difference. |
| Minecraft console helpers, `server.properties`, EULA | Core: general Minecraft functionality, not tied to a panel extension. |

## 15. Package structure

```
src/
├── calagoapi/
│   └── extensions/          the extension system (part of core)
└── extensions/
    ├── calagoapi-version-changer/
    │   ├── pyproject.toml   name = calagoapi-version-changer, entry point
    │   ├── version.yaml     run / version / description, like the core
    │   ├── README.md
    │   ├── calagoapi_version_changer/
    │   └── tests/
    └── calagoapi-hungerbridge/
        └── (same layout)
```

- Core `pyproject.toml` still packages only `calagoapi*` from `src/`, so extension
  packages are never bundled into the core wheel and never installed automatically.
- Extensions depend on `calagoapi>=1.0.dev2` (the first core release with the extension
  system; `version.yaml` is bumped to `1.0-dev.2`).

## 16. Publishing strategy

- New `.github/workflows/tests.yml`: on push and pull request, install core and every
  extension (editable) on Python 3.9 and 3.13 and run all tests.
- `release.yml` becomes a matrix over every package directory (core `.` and each
  `src/extensions/*`):
  - runs the test job first (`needs: tests`);
  - reads each package's own `version.yaml`, skips `run: false`;
  - skips a package whose tag already exists, so a push that only changes core does not
    try to republish extensions (tags: core keeps `<version>`, extensions use
    `<package>-v<version>`);
  - builds, creates a GitHub release and publishes with trusted publishing
    (`skip-existing: true` as a second guard).
- Manual step for maintainers: add each new PyPI project as a trusted publisher.

## 17. Edge cases

- `enable()` before any server exists, after servers exist, and objects created later.
- `enable()` from several threads at once (lock).
- `enable(alias)` then `enable(id)` (same extension, idempotent).
- Deprecated alias warning points at the caller (`stacklevel`).
- Two extensions declaring the same id or alias, or an alias equal to another id.
- Same entry point name from two distributions.
- Entry point that fails to import, or points to a non-Extension object.
- Extension with zero members (lifecycle-only extensions are valid).
- Member registered on a base class that a subclass shadows (built-in or extension).
- Instance attribute shadowing (`files`, `console`, `name` on servers).
- Namespace name colliding with a built-in or another extension.
- Async extension methods on sync `Panel` (returns a coroutine; documented).
- Services whose constructor raises: not cached, error propagates, next access retries.
- Config values that are unhashable (comparison uses equality, not hashing).
- Dependency enabled with defaults, later explicitly enabled with other config.
- `on_enable` raising: rollback of installed members.

## 18. Testing strategy

- `tests/test_extensions.py` (core, offline): uses a fresh `ExtensionRegistry` and
  throwaway target classes per test, covering every rule above: enable/idempotency,
  aliases and deprecation warnings, uniqueness, modes, properties, service caching,
  namespaces through the MRO, existing and future objects, conflicts (built-in,
  instance attribute, subclass, cross-extension, async names), dependencies (auto-enable,
  missing, cycles, optional), configuration (merge, unknown keys, re-enable), lifecycle
  and rollback, migration handover, thread safety, AsyncPanel integration, and real
  entry point discovery through a temporary `*.dist-info` directory on `sys.path`.
- `src/extensions/*/tests/`: each first-party extension against the core fake panel
  (version changer: every endpoint, shims, handover, async) or a local HMAC-checking
  fake HungerBridge server (signing, envelopes, errors, install()).
- Existing 38 tests keep passing (legacy shims still hit the version endpoints).
- Examples are executed by a test (`tests/test_examples.py`) so they stay runnable.

## 19. File changes

New:
- `src/calagoapi/extensions/{__init__,base,members,registry,discovery,exceptions,compat}.py`
- `src/extensions/calagoapi-version-changer/**`, `src/extensions/calagoapi-hungerbridge/**`
- `tests/test_extensions.py`, `tests/test_examples.py`
- `docs/extensions/*.md` (extension guides), `examples/extensions/*.py` (+ README)
- `.github/workflows/tests.yml`

Changed:
- `servers/minecraft.py`, `admin/admin.py`: Version Changer methods become `@migrated_to` shims
- `aio/panel.py`: await coroutine members, wrap and cache extension services/namespaces
- `api/versions.py`: marked deprecated (kept)
- `.github/workflows/release.yml`: multi-package matrix, tests gate, tag guard
- `pyproject.toml` (pytest paths), `version.yaml` (Dev 2 changelog), `README.md`,
  `docs/README.md`, `docs/reference/minecraft.md`, `docs/architecture/Architecture.md`,
  `docs/reference/migrating-from-hungerlib.md`, `PROJECT_NOTES.md`
- `.gitignore` (new): build artifacts from editable installs of the extension packages

## 20. Alternatives considered

| Alternative | Why not |
| --- | --- |
| Import-time registration (decorators register into a global registry) | Ownership would depend on import order, importing a package would change behaviour without `enable()`, and two extensions in one process could not be told apart. Side-effect-free decorators + explicit enable make ownership deterministic. |
| Patching instances / `__getattr__` hooks on `Model` | Would miss objects created before `enable()`, slow every attribute lookup, and hide conflicts. Class patching is what the spec asks for and is zero-cost after install. |
| Subclass-based plugins (`class MyServer(MinecraftServer)`) | Objects are created by managers (`panel.servers.getServer`), so users would never get the subclass. |
| Mixins injected into `__bases__` | Fragile with MRO and `__slots__`, harder to attribute ownership per member. |
| Services also moved under the namespace in namespace mode | Produces `server.hungerbridge.hungerbridge`; a service already is a namespace. |
| Silently last-wins on conflicts | Explicitly forbidden; debugging silent overrides is the main pain point of monkey patching. |
| Removing the Version Changer methods from core outright | Breaks every existing caller; deprecation shims plus handover keep compatibility at almost no cost. |
| `pluggy` / `stevedore` | Extra dependencies built for hook calling, not for adding attributes to classes; the registry we need is small. |

## 21. Implementation notes and verification

- Found while testing: members that call siblings through `self.` break in namespace
  mode (the attribute lives under `obj.<namespace>`). First-party members call sibling
  functions directly (`getInstalledVersion(self)`), and HungerBridge imports the
  version changer's function instead of going through the server. Documented as a
  best practice in the guides.
- `auto_backup` defaults to `False` (the spec's example used `True`) so that enabling
  the extension does not change what `installVersion()` did before.
- Verified: 122 tests pass on Python 3.9 and 3.14; wheels built for all three packages;
  the core wheel contains only `calagoapi`; installed wheels are discovered through
  entry points without importing them before `enable()`; every example runs.
- Not verified: the GitHub workflows have not run (YAML parsed and the package-ordering
  script executed locally); nothing has been tested against a live panel or a running
  HungerBridge.
