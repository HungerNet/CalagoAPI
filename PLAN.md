# PLAN: CalagoAPI 2.0, a game-agnostic core and the `calagoapi-minecraft` extension

Status: **implemented**. This file is the design record for the 2.0 rewrite. It was written
before implementation and updated where implementation forced a decision (marked
*Implementation note*). The earlier extension-system design (CalagoAPI 1.0-dev.2) now lives
in [docs/design/extension-system.md](docs/design/extension-system.md).

Contents:

1. [Executive summary](#1-executive-summary)
2. [Current state analysis](#2-current-state-analysis)
3. [Goals](#3-goals)
4. [Non-goals](#4-non-goals)
5. [Architecture changes](#5-architecture-changes)
6. [Repository responsibilities](#6-repository-responsibilities)
7. [Dependency architecture](#7-dependency-architecture)
8. [Package structure changes](#8-package-structure-changes)
9. [Extension redesign](#9-extension-redesign)
10. [Public API changes](#10-public-api-changes)
11. [Method inventory](#11-method-inventory)
12. [Naming review](#12-naming-review)
13. [Documentation rewrite plan](#13-documentation-rewrite-plan)
14. [Tutorial rewrite plan](#14-tutorial-rewrite-plan)
15. [HungerBridgePy changes](#15-hungerbridgepy-changes)
16. [HungerBridge changes](#16-hungerbridge-changes)
17. [Mandatory changes](#17-mandatory-changes)
18. [Recommended improvements](#18-recommended-improvements)
19. [Implementation phases](#19-implementation-phases)
20. [Risk assessment](#20-risk-assessment)
21. [Proposed final API](#21-proposed-final-api)
22. [Decision log](#22-decision-log)
23. [Implementation notes and verification](#23-implementation-notes-and-verification)

---

## 1. Executive summary

CalagoAPI is a Python SDK for the Calagopus game-server panel. Its 1.0 dev builds shipped
`GenericServer` and a `MinecraftServer` subclass in the core package. A first-party
`calagoapi-hungerbridge` extension talked to the HungerBridge Minecraft mod through its own
hand-written HMAC client, and a `calagoapi-version-changer` extension added Minecraft Version
Changer methods to `MinecraftServer`.

The 2.0 rewrite:

- renames `GenericServer` to **`Server`**, a fully game-agnostic class. The core package
  no longer contains, documents or depends on anything Minecraft-specific;
- moves **all** Minecraft functionality into one extension package, **`calagoapi-minecraft`**
  (import `calagoapi_minecraft`, extension id `minecraft`). It defines
  `class MinecraftServer(Server)` and merges the old `calagoapi-hungerbridge` and
  `calagoapi-version-changer` packages;
- makes **HungerBridgePy** (`pip install hungerbridge`) the only HungerBridge client.
  `MinecraftServer.sendCommand()` and `streamConsole()` keep their names but are rebuilt on
  HungerBridgePy's `runCommand()` and SSE log stream. The duplicate HMAC client is deleted;
- adds missing pieces where they belong instead of working around them:
  - in HungerBridgePy: an iterator log-stream API, typed stream errors, release discovery,
    and token `expiry`;
  - in HungerBridge: self-describing release jar names;
- keeps `getRAM()`, `getCPU()` and `stop()` as CalagoAPI (panel) implementations. The JVM-level
  data HungerBridge offers becomes new APIs: `getMemoryInfo()`, `getProcessorInfo()`,
  `getThreadInfo()`, `getGarbageCollectorInfo()`, `getProcessInfo()` and `getNetworkInfo()`;
- replaces the extension-centric "learning" pages with a three-track tutorial path
  (basics → extensions → Minecraft) and rewrites the reference docs so they match the code.

This is a major-version break (core `2.0-dev.1`). Migration guidance is in
[docs/migrating-to-2.0.md](docs/migrating-to-2.0.md), but it did not limit the design.

```
BEFORE                                         AFTER
──────                                         ─────
calagoapi                                      calagoapi                 (game-agnostic)
├── GenericServer                              ├── Server
├── MinecraftServer(GenericServer)             ├── ServerManager, AdminServer, ...
│   └── deprecated version-changer shims       ├── aio  (+ async type registry)
├── api.versions (deprecated)                  └── extensions (camelCase API)
├── admin.extensions.getVersionChanger*()
└── extensions                                 calagoapi_minecraft        (extension "minecraft")
                                               ├── MinecraftServer(Server)
calagoapi_version_changer  ──┐                 │   ├── bridge  → hungerbridge.BridgeClient
calagoapi_hungerbridge ──────┤  merged  ─────► │   ├── versions → VersionManager
  └── own HMAC client  ✗     │                 │   └── sendCommand/streamConsole via HungerBridgePy
                             ┘                 ├── MinecraftManager  (panel.minecraft)
                                               └── VersionChangerAdmin (panel.minecraft.versionChanger)
```

---

## 2. Current state analysis

### 2.1 Workspace

| Project | Location | State at start |
| --- | --- | --- |
| CalagoAPI | `CalagoAPI/` (git, `main`, large uncommitted extension-system change) | 121 tests pass, 1 skipped (Python 3.12) |
| calagoapi-hungerbridge | `CalagoAPI/src/extensions/calagoapi-hungerbridge/` | first-party extension, untracked |
| calagoapi-version-changer | `CalagoAPI/src/extensions/calagoapi-version-changer/` | first-party extension, untracked |
| HungerBridgePy | `HungerBridgePy/` (dist `hungerbridge`, import `hungerbridge`) | 65 tests pass, 1 live test skipped |
| HungerBridge | `HungerBridge-1/` (remote `HungerNet/HungerBridge`) | Java 21/25, Paper/Folia/Fabric, protocol v1 |

`hungerbridge/` (lower case, remote `hungernet/hungerbridge`) is an older checkout of the same
plugin. It is not one of the session's working directories and is **not modified**;
`HungerBridge-1` is the current one (`ENDPOINTS.md`, protocol v1, CHANGELOG 2026-11).

There is no `tutorials/` directory and no page contains "Prerequisites" or "Estimated time"
sections. The tutorial material is `docs/learning/` (10 extension guides) and
`examples/extensions/` (10 scripts plus a packaged example).

### 2.2 CalagoAPI core

- `servers/generic.py` `GenericServer(Model)`: about 120 public methods covering details,
  resources, power, console, settings, startup, mounts and devices, plus HungerLib-compatible
  shortcuts to the managers. It is game-agnostic in code, but its docstrings use Minecraft
  examples (`say Hello`, `MINECRAFT_VERSION`, `SERVER_JARFILE`, `joined the game`, port 25565).
- `servers/minecraft.py` `MinecraftServer(GenericServer)`:
  - console helpers built on `sendCommand`, which sends the command through the panel REST API
    and returns nothing;
  - `server.properties` and EULA helpers;
  - five deprecated `@migrated_to` version-changer shims backed by `api/versions.py`.
- `ServerManager.getMinecraftServer()` is in core. `ExtensionManager` (admin) carries four
  deprecated Version Changer admin shims.
- `aio/panel.py`: `wrap()` wraps `GenericServer` as `AsyncServer`, plus any object whose
  module starts with `calagoapi.`. Objects from extension packages (`calagoapi_*`) are **not**
  wrapped, so their methods stay blocking under `AsyncPanel` (bug). `AsyncServer.streamConsole`
  always uses the daemon websocket, so a subclass that streams differently is silently
  bypassed under async (bug once `MinecraftServer` overrides it).
- `calagoapi/__init__.py` defines `utils`, `servers` and `schedules` `SimpleNamespace`
  objects that **shadow the real subpackages** of the same names
  (`calagoapi.servers is not sys.modules['calagoapi.servers']`). `servers` even contains `Panel`.
- Extension system (`calagoapi.extensions`): solid design (class patching, ownership,
  conflicts, dependencies, async support). Its public functions and hooks are snake_case
  (`get_extension`, `is_enabled`, `on_enable`, `validate_config`, `property_extension`), while
  the rest of the SDK's methods are camelCase.

### 2.3 calagoapi-hungerbridge (to become calagoapi-minecraft)

- Re-implements HungerBridge's HMAC signing and canonical JSON (`client.py`) instead of using
  HungerBridgePy, so the protocol is maintained in two places.
- Calls endpoints that **do not exist** in HungerBridge protocol v1: `/server/status`,
  `/server/info` and `/system/disk` (ENDPOINTS.md: "Removed / never registered").
- Unwraps a `data` envelope that HungerBridge never sends.
- `install()` parses release jar names as `<loader>-<mc>` (`...-paper-1.21.11+4-alpha.34.jar`).
  HungerBridge's Gradle builds name jars after the project directory, `<mc>-<loader>-<version>.jar`
  (`26.2-paper-4-alpha.93.jar`), so `install()` cannot find real releases.
- Requires `calagoapi-version-changer` only to detect the installed server type.
- The service uses noun-style methods (`players()`, `tps()`, `run()`), unlike the SDK's
  `getX()` convention, and has no console streaming. HungerBridge's SSE stream is unused.

### 2.4 HungerBridgePy

- Well-structured: `client` (`BridgeClient`), `transport` (signing, retries, typed errors),
  `auth`, `canonical`, `stream` (SSE `Stream` with reconnect and history de-duplication),
  `exceptions`, `units`, `protocol`. It has golden vectors shared with the Java tests.
- Gaps found while designing the integration:
  1. `Stream` is callback/buffer only. There is no iterator form, which `streamConsole()` needs,
     and one `client.stream` per client means two consumers cannot stream independently.
  2. Stream failures are raw `requests.HTTPError`s, not the package's typed errors. With
     `reconnect=True` a revoked token is retried forever.
  3. `getTokenInfo()` drops the `expiry` field HungerBridge returns.
  4. There is no release discovery: knowledge of how HungerBridge jars are named lives in
     CalagoAPI.
  5. There is no constant for the server's SSE history cap (200).

### 2.5 HungerBridge (Java)

- Protocol v1 is documented in `ENDPOINTS.md` and matches HungerBridgePy.
- Release jars are named `<mc>-<loader>-<version>.jar` (Gradle project directory name). That is
  ambiguous next to other jars and not self-describing once downloaded into `plugins/`.
- Its docs show HungerBridgePy usage only through `client.stream.connect(...)`.

### 2.6 Discrepancies (HungerBridgePy is authoritative)

| # | Discrepancy | Resolution |
| --- | --- | --- |
| 1 | CalagoAPI extension has its own HMAC/canonical-JSON client | Delete it; use `hungerbridge.BridgeClient` |
| 2 | Extension calls `/server/status`, `/server/info`, `/system/disk` (not in protocol v1) | Remove those methods; `getBridgeInfo()` uses `/server/meta` |
| 3 | Extension expects a `data` envelope | Gone with the client |
| 4 | Jar naming `<loader>-<mc>` assumed vs `<mc>-<loader>` built | HungerBridge names jars `HungerBridge-<loader>-<mc>-<version>.jar`; HungerBridgePy's finder accepts both orders |
| 5 | HungerBridge returns `expiry` from `/auth/check`, HungerBridgePy drops it | HungerBridgePy returns it |
| 6 | Server stream errors are typed in Java (401 `reason`, 429 `Retry-After`) but untyped in the Python stream | HungerBridgePy maps them to `HungerBridgeError` subclasses |

---

## 3. Goals

1. `Server` is game-agnostic in code, docstrings and docs. Core installs and imports without
   any Minecraft or HungerBridge package.
2. `calagoapi_minecraft.MinecraftServer(Server)` owns every Minecraft feature.
3. Dependency direction: `calagoapi-minecraft → calagoapi`, `calagoapi-minecraft → hungerbridge`,
   and nothing points back.
4. HungerBridgePy is the single HungerBridge client. Missing capabilities are added there, or in
   HungerBridge, not shimmed in CalagoAPI.
5. `sendCommand()` / `streamConsole()` keep their names and adopt HungerBridgePy semantics on
   `MinecraftServer`. `getRAM()`, `getCPU()` and `stop()` stay CalagoAPI's panel implementations.
   Bridge metrics are new, additive APIs.
6. Sync and async (`AsyncPanel`) behave the same for extension types.
7. Consistent camelCase methods / snake_case attributes across core, extension API and the
   Minecraft extension.
8. Documentation, tutorials, examples and tests match the implementation and run offline.

## 4. Non-goals

- Keeping 1.x import paths or deprecated shims working (`GenericServer`,
  `calagoapi.MinecraftServer`, `server.hungerbridge`, version-changer methods on the server).
- Changing HungerBridge's wire protocol (stays v1) or its Java runtime behaviour.
- A native-asyncio HungerBridge client. The async layer runs HungerBridgePy in threads, like the
  rest of CalagoAPI. HungerBridge's own design doc already proposes an async client for later.
- Moving the Subdomain Manager wrappers out of core (unchanged, still the next candidate).
- Testing against a live panel or a live HungerBridge server (the environment has neither).
- Modifying the older `hungerbridge/` checkout.

---

## 5. Architecture changes

### 5.1 Layering

```
┌──────────────────────────────────────────────────────────────────────────┐
│ user code (scripts, bots, dashboards)                                    │
├───────────────────────────────┬──────────────────────────────────────────┤
│ calagoapi_minecraft           │  (any other game extension, same shape)  │
│  MinecraftServer(Server)      │                                          │
│  MinecraftManager, VersionMgr │                                          │
├───────────────┬───────────────┴──────────────────────────────────────────┤
│ hungerbridge  │ calagoapi  (Panel, Server, managers, console, aio,       │
│ (HungerBridge │             extensions, api/ = only HTTP layer)          │
│  HTTP client) │                                                          │
├───────────────┼──────────────────────────────────────────────────────────┤
│ HungerBridge  │ Calagopus panel + Wings daemon                           │
│ (in the game) │                                                          │
└───────────────┴──────────────────────────────────────────────────────────┘
```

### 5.2 Two transports on a Minecraft server

A `MinecraftServer` has two independent channels, and each method uses exactly one:

| Channel | Implemented by | Used for |
| --- | --- | --- |
| Panel / daemon | CalagoAPI (`api/`, `Console`) | power (`start`/`stop`/...), resources (`getRAM`, `getCPU`, ...), files, backups, `server.properties`, version changer, `sendPanelCommand()`, `server.console` |
| HungerBridge | HungerBridgePy (`server.bridge`) | `sendCommand()` (with captured output), `streamConsole()`, players, TPS/MSPT, world and JVM metrics, `writeLog()` |

There is **no silent fallback** from bridge to panel. A fallback would make return types
depend on runtime state: `sendCommand` returns output through the bridge, but nothing through
the panel. Calling a bridge method without a configured token raises `BridgeNotConfiguredError`,
and its message names the fix. `sendPanelCommand()` and `server.console` remain as explicit
panel-side alternatives. They are needed anyway to create the first bridge token, because
`/hb token create` only runs on the server console. `createBridgeToken()` automates that.

### 5.3 Class hierarchy

```
calagoapi.utils.model.Model
└── calagoapi.Server                           (servers/server.py, was GenericServer)
    └── calagoapi_minecraft.MinecraftServer    (calagoapi-minecraft)

calagoapi.aio.AsyncWrapper
├── calagoapi.aio.AsyncServer                  (wraps Server; native asyncio console)
│   └── calagoapi_minecraft.aio.AsyncMinecraftServer   (bridge stream in a worker thread)
└── calagoapi.aio.AsyncPanel

calagoapi.utils.exceptions.CalagoAPIError
└── calagoapi_minecraft.MinecraftError
    └── calagoapi_minecraft.BridgeNotConfiguredError

hungerbridge.HungerBridgeError                 (raised unchanged from bridge calls)
```

### 5.4 Async type registry (core)

`calagoapi.aio.registerAsyncType(cls, wrapper=AsyncWrapper)` tells `wrap()` how to wrap
instances of a class, resolved through the MRO (most specific first). This replaces the
`__module__.startswith('calagoapi.')` heuristic for anything outside core, and it lets
`MinecraftServer` get `AsyncMinecraftServer` instead of the daemon-console `AsyncServer`.
Core registers its own types the same way. `AsyncWrapper` also gains generic support for
**generator methods**: they become async generators that pull items in a worker thread.
`calagoapi.aio.iterateInThread(iterable)` is the public helper for that.

### 5.5 Configuration model

`MinecraftServer` works without `enable('minecraft')`: its defaults come from
`calagoapi_minecraft.settings()`. That returns the enabled extension's frozen config when
enabled, and `MinecraftExtension.default_config` otherwise. `enable('minecraft', config=...)`
sets process-wide defaults (bridge token, port, release, auto backup) and installs
`panel.minecraft`. Per-server values (`bridge_url`, `bridge_token`, `address`) are constructor
or `connectBridge()` arguments and always win.

---

## 6. Repository responsibilities

| Repository | Owns | Must not own |
| --- | --- | --- |
| **CalagoAPI** (`calagoapi`) | Calagopus panel and daemon API, `Server`, managers, live daemon console, `AsyncPanel`, the extension system, game-agnostic docs and tutorials (tracks 1–2) | Anything about a specific game; any HungerBridge code |
| **calagoapi-minecraft** (in `CalagoAPI/src/extensions/`) | `MinecraftServer`, `panel.minecraft`, Version Changer panel-extension wrappers, `server.properties`/EULA, mapping CalagoAPI concepts onto HungerBridgePy, installing the bridge through the panel, Minecraft tutorials (track 3) | HTTP signing, wire format, SSE parsing, release naming (HungerBridgePy) |
| **HungerBridgePy** (`hungerbridge`) | Python source of truth for HungerBridge: protocol, signing, typed errors, endpoints, SSE stream (callback and iterator), pickup redemption, **release discovery** | Panel concepts (servers, allocations, files) |
| **HungerBridge** | Server-side implementation: endpoints, auth, policies, SSE, **release artifact names**, `ENDPOINTS.md` | Client-side conveniences |

Coordination requirements:

1. Release order for users: `hungerbridge >= 1.0.dev2` (new APIs) → `calagoapi >= 2.0.dev1` →
   `calagoapi-minecraft`. Publishing order does not matter (pip resolves at install time), but
   `calagoapi-minecraft` cannot be *installed* before both are on PyPI.
2. The jar name format is a contract between HungerBridge (produces) and HungerBridgePy
   (parses). HungerBridgePy accepts both the new and the old format so existing releases keep
   working.
3. CalagoAPI CI installs HungerBridgePy from its GitHub repository until `hungerbridge` is on PyPI.
4. Protocol changes stay governed by HungerBridge's `protocol-vectors.json` shared with
   HungerBridgePy (unchanged by this work).

---

## 7. Dependency architecture

```
            ┌─────────────────────────┐
            │   calagoapi-minecraft   │
            │  (calagoapi_minecraft)  │
            └───────┬───────────┬─────┘
          depends on│           │depends on
                    ▼           ▼
        ┌───────────────┐   ┌──────────────────┐
        │   calagoapi   │   │  hungerbridge    │  (HungerBridgePy, source of truth)
        │  (core, Server)│  │                  │
        └───────┬───────┘   └────────┬─────────┘
                │ HTTP / websocket   │ HTTP + SSE (HMAC, protocol v1)
                ▼                    ▼
        ┌───────────────┐   ┌──────────────────┐
        │ Calagopus     │   │ HungerBridge     │  (plugin/mod inside the game server)
        │ panel + Wings │   │                  │
        └───────────────┘   └──────────────────┘

  calagoapi        ─╳─▶ hungerbridge      (forbidden)
  calagoapi        ─╳─▶ HungerBridge      (forbidden)
  hungerbridge     ─╳─▶ calagoapi         (forbidden)
```

Validation, enforced by tests:

- `tests/test_architecture.py` (core): no module under `src/calagoapi` imports
  `hungerbridge` or `calagoapi_minecraft`, and core source contains no Minecraft-specific
  identifiers (`MinecraftServer`, `minecraft`, `HungerBridge`). `pyproject.toml` runtime
  dependencies are exactly `requests` and `websockets`. `import calagoapi` with `hungerbridge`
  blocked in `sys.modules` still works.
- `calagoapi-minecraft`'s `pyproject.toml` depends on `calagoapi>=2.0.dev1`,
  `hungerbridge>=1.0.dev2`, `requests`.
- HungerBridgePy depends only on `requests`.

---

## 8. Package structure changes

### Before

```
CalagoAPI/
├── PLAN.md                        extension-system design
├── docs/                          15 guides incl. minecraft.md
│   └── learning/                  10 extension guides
├── examples/extensions/           10 examples (MinecraftServer targets) + packaged example
├── src/
│   ├── calagoapi/
│   │   ├── api/versions.py        deprecated VersionsAPI
│   │   ├── servers/generic.py     GenericServer
│   │   ├── servers/minecraft.py   MinecraftServer
│   │   └── ...
│   └── extensions/
│       ├── calagoapi-hungerbridge/     client.py (own HMAC), extension.py
│       └── calagoapi-version-changer/  api.py, extension.py
└── tests/
```

### After

```
CalagoAPI/
├── PLAN.md                        this document
├── docs/
│   ├── README.md                  index: reference guides + tutorials
│   ├── getting-started.md  servers.md  console.md  files.md  backups.md  databases.md
│   ├── schedules.md  network.md  account.md  admin.md  async.md
│   ├── extensions.md              reference for calagoapi.extensions (was learning/*)
│   ├── errors-and-utilities.md  architecture.md
│   ├── migrating-from-hungerlib.md  migrating-to-2.0.md (new)
│   ├── design/extension-system.md     previous PLAN (design record)
│   └── tutorials/
│       ├── README.md              learning path
│       ├── basics/                01–05
│       ├── extensions/            06–10
│       └── minecraft/             11–15  (requires calagoapi-minecraft)
├── examples/
│   ├── README.md
│   ├── extensions/                01–09 (Server targets) + packaged_extension/
│   └── minecraft/                 01–04 (offline, fake panel + fake bridge)
├── src/
│   ├── calagoapi/                 game-agnostic
│   │   ├── servers/server.py      Server  (servers/generic.py and minecraft.py removed)
│   │   └── api/                   versions.py removed
│   └── extensions/
│       ├── conftest.py
│       └── calagoapi-minecraft/
│           ├── pyproject.toml  version.yaml  README.md
│           ├── calagoapi_minecraft/
│           │   ├── __init__.py    public API
│           │   ├── server.py      MinecraftServer
│           │   ├── bridge.py      bridge connection helpers (URL, token, pickup, install)
│           │   ├── versions.py    VersionManager, VersionChangerAPI, VersionChangerAdmin
│           │   ├── properties.py  server.properties parsing/writing
│           │   ├── manager.py     MinecraftManager (panel.minecraft)
│           │   ├── extension.py   MinecraftExtension
│           │   ├── config.py      DEFAULT_CONFIG, validation, settings()
│           │   ├── aio.py         AsyncMinecraftServer + async type registration
│           │   └── exceptions.py  MinecraftError, BridgeNotConfiguredError
│           └── tests/
└── tests/                         + test_architecture.py
```

Removed: `src/extensions/calagoapi-hungerbridge/`, `src/extensions/calagoapi-version-changer/`,
`src/calagoapi/servers/generic.py`, `src/calagoapi/servers/minecraft.py`,
`src/calagoapi/api/versions.py`, `docs/minecraft.md`, `docs/learning/`,
`examples/extensions/10_first_party_extensions.py`.

---

## 9. Extension redesign

### 9.1 Options considered for where `MinecraftServer` lives

| Option | Description | Verdict |
| --- | --- | --- |
| A. Extension members on `Server` | `enable('minecraft')` patches `say()`, `getTPS()`, ... onto every `Server` | Rejected: every server (Valheim, Rust, ...) would show Minecraft methods. It contradicts "`class MinecraftServer(Server)`" and makes `sendCommand` overrides impossible without patching a built-in. |
| B. Plain subclass package, no extension | `from calagoapi_minecraft import MinecraftServer` only | Rejected: no panel-level entry point, and process-wide config would need its own mechanism. It ignores the SDK's integration system. |
| **C. Subclass + extension service** | `MinecraftServer(Server)` is a normal class. `enable('minecraft')` adds the `panel.minecraft` service (`MinecraftManager`) and process-wide config | **Chosen**: real type for overrides and `isinstance`; the extension system provides discovery, config, secrets masking and async wrapping |

### 9.2 Merging `calagoapi-version-changer`

The Version Changer is a Calagopus panel extension that only makes sense on Minecraft servers.
Keeping it as a separate package would need a dependency on `calagoapi-minecraft` for its
target class. `installBridge()` wants its server-type detection, and users would install two
packages for one game. It becomes `server.versions` (a `VersionManager`, shaped like
`server.backups`) and `panel.minecraft.versionChanger` (admin settings). Endpoints that fail
because the panel extension is not installed raise the normal `NotFoundError`.
`server.versions.isAvailable()` checks without raising.

### 9.3 The `minecraft` extension

```python
class MinecraftExtension(Extension):
    extension_id = 'minecraft'
    default_mode = 'direct'
    secret_config = ('bridge_token',)
    default_config = {
        'bridge_url': None,           # None = derive from the server address + bridge_port
        'bridge_port': 1913,
        'bridge_token': None,         # 'tokenId:secret'
        'bridge_timeout': None,       # None = HungerBridgePy default (5, 30)
        'bridge_max_retries': 2,      # 429 retries inside HungerBridgePy
        'stream_reconnect': True,     # default for streamConsole()/onConsoleLine()
        'auto_backup': False,         # backup before server.versions.install()
        'backup_name': 'Before version change',
        'backup_timeout': 3600,
        'release': 'latest',          # HungerBridge release for installBridge()
        'repository': 'HungerNet/HungerBridge',
        'github_api': 'https://api.github.com',
    }
```

Members: one service, `@classExtension(Panel, 'minecraft') class MinecraftManager`. Old
extension ids `hungerbridge` and `version_changer` are not aliased, because their APIs changed
completely. `ExtensionNotFoundError` instead names the replacement
("'hungerbridge' was replaced by 'minecraft' (pip install calagoapi-minecraft)").

### 9.4 Extension-system API naming (applies to every extension)

The public functions, decorators and hooks move to camelCase, matching the SDK rule
"methods are camelCase, attributes are snake_case":

| 1.x | 2.0 |
| --- | --- |
| `get_extension()` | `getExtension()` |
| `is_enabled()` | `isEnabled()` |
| `enabled_extensions()` | `enabledExtensions()` |
| `@property_extension` | `@propertyExtension` |
| `@class_extension` | `@classExtension` |
| `@migrated_to` | `@migratedTo` (helper formerly named `migratedTo` → `migrationTarget`) |
| `Extension.on_enable()` | `Extension.onEnable()` |
| `Extension.validate_config()` | `Extension.validateConfig()` |
| `registry.owner_of()` / `get_class()` / `is_enabled()` | `ownerOf()` / `getClass()` / `isEnabled()` |

Unchanged: `enable`, `register`, `available`, `method`, `registry.registrations()`,
`describe()`, and the snake_case class attributes (`extension_id`, `default_config`,
`default_mode`, `secret_config`, `allow_unknown_config`, `enabled_by`).
`FIRST_PARTY = {'minecraft': 'calagoapi-minecraft'}` plus `REPLACED` hints for the old ids.

---

## 10. Public API changes

### 10.1 Core, before → after

```python
# 1.x                                            # 2.0
from calagoapi import GenericServer              from calagoapi import Server
from calagoapi import MinecraftServer            from calagoapi_minecraft import MinecraftServer
panel.servers.getMinecraftServer('abc')          panel.minecraft.getServer('abc')   # after enable('minecraft')
calagoapi.servers.Generic / .Minecraft           (removed, import the classes)
calagoapi.utils.formatBytes (namespace)          calagoapi.utils.formatBytes (real subpackage, same name)
panel.api.versions                               (removed, calagoapi_minecraft.VersionChangerAPI)
panel.admin.extensions.getVersionChanger*()      panel.minecraft.versionChanger.get*()
from calagoapi.extensions import get_extension   from calagoapi.extensions import getExtension
```

### 10.2 Minecraft, before → after

```python
# 1.x (calagoapi + calagoapi-hungerbridge + calagoapi-version-changer)
enable('hungerbridge', config={'token': 'bot:9f2c...'})
server = panel.servers.getMinecraftServer('abc', server_domain='play.example.com')
server.sendCommand('list')                 # panel REST, returns None
server.hungerbridge.run('list')            # bridge, returns ['line', ...]
server.hungerbridge.players()
server.hungerbridge.tps()                  # dict
server.hungerbridge.memory()
for line in server.streamConsole(): ...    # daemon websocket
server.getBuilds('PAPER', '1.21.11')
server.installVersion(build)
server.hungerbridge.install()

# 2.0 (calagoapi + calagoapi-minecraft)
enable('minecraft', config={'bridge_token': 'bot:9f2c...'})
server = panel.minecraft.getServer('abc', address='play.example.com')
server.sendCommand('list')                 # HungerBridge, returns captured output text
server.sendPanelCommand('list')            # panel REST, returns None
server.getPlayers()
server.getTPS('1m')                        # float, like HungerBridgePy
server.getMemoryInfo()                     # JVM heap/non-heap/process (new, additive)
server.getRAM()                            # unchanged: container RAM from the panel
for line in server.streamConsole(history=50): ...   # HungerBridge SSE (HungerBridgePy)
server.versions.getBuilds('PAPER', '1.21.11')
server.versions.install(build)
server.installBridge()
```

### 10.3 `sendCommand()` redesign

| | `Server.sendCommand` (core) | `MinecraftServer.sendCommand` |
| --- | --- | --- |
| Signature | `sendCommand(command)` | `sendCommand(command, *, silent=False, showConsole=False)` |
| Transport | panel `POST /servers/{id}/command` | HungerBridgePy `BridgeClient.runCommand()` → `POST /server/run` |
| Returns | `None` | captured output joined with `\n`, or `None` when `silent=True` (HungerBridgePy `normalize=True` semantics) |
| Errors | `CalagoAPIError` subclasses | `hungerbridge.HungerBridgeError` subclasses; `BridgeNotConfiguredError` |
| Runs as | daemon stdin | server console on the main thread / Folia global region, waits up to 5 s |

The extra arguments are keyword-only and the return type widens `None` to `str | None`, so
any code written against `Server.sendCommand(command)` keeps working on a `MinecraftServer`
(Liskov-compatible). `sendCommands(commands, **options)` returns the list of outputs.

### 10.4 `streamConsole()` redesign

| | `Server.streamConsole` (core) | `MinecraftServer.streamConsole` |
| --- | --- | --- |
| Signature | `streamConsole(history=True, timeout=None)` | `streamConsole(history=0, timeout=None, *, reconnect=None, sanitize=True)` |
| Transport | Wings websocket (`Console`) | HungerBridgePy `BridgeClient.streamLogs()` → `GET /server/stream` (SSE) |
| `history` | bool: replay what the daemon still has | int: replay the last N lines (≤ 200, `True` means 200); the bridge marks the end with `:history-end` |
| Lines | raw daemon output | `[HH:mm:ss LEVEL]: message`, ANSI stripped and `\n` unescaped when `sanitize=True` |
| Reconnect | none (iterator ends) | `reconnect=None` uses the `stream_reconnect` config (default `True`); replays only missed lines |
| Ends | connection closed or `timeout` s of silence | permanent error (raised), stream closed without reconnect, or `timeout` s of silence |

`bool` is a subclass of `int`, so `streamConsole(history=True)` works on both. Under
`AsyncPanel`, `async for line in server.streamConsole()` works on both: native asyncio for
`Server`, a worker thread for `MinecraftServer`. `onConsoleLine(callback, history=0)` follows
the same split and returns a `hungerbridge.Stream` (stop with `.disconnect()`).

### 10.5 Methods that stay CalagoAPI's

`getRAM()`, `getRAMLimit()`, `getCPU()`, `getCPULimit()`, `getDisk()`, `getUptime()`,
`getStatus()`, `start()`, `stop()`, `restart()` and `kill()` are inherited from `Server`
unchanged. They describe the container as the panel and daemon see it. `stop()` is the panel
power action, never HungerBridge's `/server/stop`. That endpoint stays reachable as
`server.bridge.stopServer()` for people who want it explicitly.

### 10.6 New bridge-backed information APIs (additive)

| Method | HungerBridgePy | Returns |
| --- | --- | --- |
| `getMemoryInfo(unit='mib')` | `getMemoryStats(unit)` | heap/non-heap/JVM/process memory + `used`, `total`, `free`, `max` |
| `getProcessInfo(unit='mib')` | `getProcessMemory(unit)` + `getUptime()` | `process_used`, `process_virtual`, `uptime_ms` |
| `getProcessorInfo()` | `getCPUStats()` | `load` (0–1, JVM process), `processors` |
| `getThreadInfo()` | `getThreadStats()` | `current`, `peak`, `daemon` |
| `getGarbageCollectorInfo()` | `getGCStats()` | `gc_type`, `gc_count`, `gc_time_ms`, `last_gc_pause_ms`, `avg_gc_pause_ms` |
| `getNetworkInfo()` | `getNetworkStats()` | `bytes_in_per_sec`, `bytes_out_per_sec`, `total_bytes_in`, `total_bytes_out` |
| `getJVMUptime(formatted=False)` | `getUptime()` | ms, or `'3h 12m'` |
| `getPerformance()` | TPS + MSPT + players | one dict for dashboards |

HungerBridge has no hardware endpoint (only `processors`), so there is no `getHardwareInfo()`.
That would be a HungerBridge protocol addition and is listed in §18 as future work.

---

## 11. Method inventory

Classification: **Keep** (same name and behaviour), **Replace** (same name, new behaviour or
signature), **Rename**, **Move**, **Remove**, **New**. Areas the rewrite does not touch (files,
backups, databases, schedules, network, users, tunnels, nodes, account, admin resources: about
1,100 methods) are **Keep** and are listed per class in §11.9 rather than per method.

### 11.1 `GenericServer` → `calagoapi.Server`

| Current method | Current location | Classification | Future location | Notes |
| --- | --- | --- | --- | --- |
| class `GenericServer` | `calagoapi.servers.generic` | Rename + Move | `calagoapi.Server` (`servers/server.py`) | game-agnostic docstrings |
| `__init__(panel, server_id, name, data)` | GenericServer | Keep | Server | |
| `__repr__`, `__str__`, `__eq__`, `__hash__` | GenericServer | Keep | Server | `__eq__` checks `Server` |
| `api` (property) | GenericServer | Keep | Server | |
| `details`, `refreshDetails`, `get` | GenericServer | Keep | Server | |
| `getUUID`, `getShortId`, `getName`, `getDescription` | GenericServer | Keep | Server | |
| `getNodeName`, `getNodeId`, `getLocationName`, `getNodeResources` | GenericServer | Keep | Server | |
| `getEgg`, `getEggName`, `getLimits`, `getFeatureLimits` | GenericServer | Keep | Server | |
| `getDockerImage`, `getDockerImages`, `getStartupCommand`, `getTimezone` | GenericServer | Keep | Server | |
| `getAutoKill`, `getAutoStartBehavior`, `getSftpHost`, `getSftpPort` | GenericServer | Keep | Server | |
| `getPermissions`, `hasPermission`, `getPrimaryAllocation`, `getAddress` | GenericServer | Keep | Server | `getAddress` doc: generic host:port |
| `getInstallStatus` | GenericServer | Keep | Server | |
| `refresh`, `resources`, `getResources` | GenericServer | Keep | Server | |
| `getRAM`, `getRAMLimit` | GenericServer | **Keep (CalagoAPI-owned)** | Server | not replaced by bridge data |
| `getCPU`, `getCPULimit` | GenericServer | **Keep (CalagoAPI-owned)** | Server | not replaced by bridge data |
| `getDisk`, `getDiskLimit`, `getNetworkIn`, `getNetworkOut`, `getUptime` | GenericServer | Keep | Server | |
| `getStatus`, `getPowerState` | GenericServer | Keep | Server | `getPowerState` = HungerLib alias |
| `isOnline`, `isOffline`, `isRunning`, `isStopped`, `isStarting`, `isStopping` | GenericServer | Keep | Server | |
| `isInstalled`, `isInstalling`, `isInstallFailed`, `isRestoringBackup` | GenericServer | Keep | Server | |
| `isSuspended`, `isTransferring`, `isOwner`, `isNodeInMaintenance` | GenericServer | Keep | Server | |
| `waitForState`, `waitForOnline`, `waitForOffline` | GenericServer | Keep | Server | |
| `powerAction`, `start`, `restart`, `kill` | GenericServer | Keep | Server | |
| `stop` | GenericServer | **Keep (CalagoAPI-owned)** | Server | panel power action |
| `sendCommand(command)` | GenericServer | Keep | Server | panel REST; overridden by MinecraftServer |
| `sendCommands(commands)` | GenericServer | Keep | Server | |
| `getLogs`, `getWebsocket` | GenericServer | Keep | Server | |
| `streamConsole(history, timeout)` | GenericServer | Keep | Server | daemon websocket; overridden by MinecraftServer |
| `onConsoleLine(callback, history)` | GenericServer | Keep | Server | overridden by MinecraftServer |
| `getActivity`, `getAnnouncements` | GenericServer | Keep | Server | |
| `rename`, `setName`, `setDescription`, `setTimezone`, `setAutoKill`, `setAutoStart` | GenericServer | Keep | Server | return type `Server` |
| `reinstall`, `cancelInstall`, `unlockInstall` | GenericServer | Keep | Server | |
| `getStartupVariables`, `getStartupVariable`, `updateStartupVariable(s)`, `setStartupCommand`, `setDockerImage` | GenericServer | Keep | Server | generic examples |
| `getMounts`, `attachMount`, `detachMount`, `getDevices`, `attachDevice`, `detachDevice` | GenericServer | Keep | Server | |
| file shortcuts (`listFiles` … `decompress`, 12) | GenericServer | Keep | Server | HungerLib compatibility |
| backup shortcuts (`listBackups` … `downloadBackup`, 7) | GenericServer | Keep | Server | |
| database shortcuts (5), schedule shortcuts (9), `getSubusers`, `getAllocations` | GenericServer | Keep | Server | |

### 11.2 `MinecraftServer` (core) → `calagoapi_minecraft.MinecraftServer`

| Current method | Current location | Classification | Future location | Notes |
| --- | --- | --- | --- | --- |
| class `MinecraftServer(GenericServer)` | `calagoapi.servers.minecraft` | Move | `calagoapi_minecraft.MinecraftServer(Server)` | |
| `__init__(..., server_domain, server_port, data)` | MinecraftServer | Replace | `__init__(panel, server_id=None, name=None, data=None, *, address=None, bridge_url=None, bridge_token=None)` | keyword-only extras |
| `server_domain`, `server_port` attributes | MinecraftServer | Rename | `address` | `'host'` or `'host:port'`, port defaults to 25565 |
| `getAddress()` | MinecraftServer | Keep | MinecraftServer | uses `address` |
| `say(message)` | MinecraftServer | Keep | MinecraftServer | via bridge `sendCommand` |
| `broadcast(message)` | MinecraftServer (alias of `say`) | Replace | `broadcast(message, prefix=None)` | HungerBridgePy `broadcast()` (tellraw) |
| `tellraw`, `kick`, `ban`, `pardon`, `op`, `deop`, `whitelistAdd`, `whitelistRemove`, `saveAll` | MinecraftServer | Keep | MinecraftServer | via bridge `sendCommand`, return output |
| `getProperties`, `getProperty`, `setProperty`, `setProperties`, `getMOTD`, `setMOTD` | MinecraftServer | Keep | MinecraftServer | parsing moved to `properties.py` |
| `acceptEula`, `isEulaAccepted` | MinecraftServer | Keep | MinecraftServer | |
| `getInstalledVersion()` | MinecraftServer (deprecated shim) | Move + Rename | `server.versions.getInstalled()` | |
| `getVersionTypes()` | shim | Move + Rename | `server.versions.getTypes()` | |
| `getVersions(type, ...)` | shim | Move | `server.versions.getVersions(type, ...)` | |
| `getBuilds(type, version, ...)` | shim | Move | `server.versions.getBuilds(type, version, ...)` | |
| `installVersion(build, ...)` | shim | Move + Rename | `server.versions.install(build, ..., backup=None)` | `backup=None` uses `auto_backup` |

### 11.3 `ServerManager`, `AdminServer`, `ServerGroup`, `ExtensionManager`, package namespaces

| Current method | Current location | Classification | Future location | Notes |
| --- | --- | --- | --- | --- |
| `getServer`, `getServers`, `listServers`, `getServerByName` | `ServerManager` | Keep | ServerManager | return `Server` |
| `getMinecraftServer(...)` | `ServerManager` | Move | `panel.minecraft.getServer(...)` | extension service |
| `getEggs`, `getCommandSnippets`, group methods | `ServerManager` | Keep | ServerManager | |
| `ServerGroup.getServers` | `ServerGroup` | Keep | ServerGroup | returns `Server` |
| `AdminServer.asServer()` | `AdminServer` | Keep | AdminServer | returns `Server` |
| `VERSION_CHANGER` constant | `ExtensionManager` | Move | `calagoapi_minecraft.versions.PANEL_EXTENSION` | |
| `getVersionChangerSettings()` | `ExtensionManager` (shim) | Move + Rename | `panel.minecraft.versionChanger.getSettings()` | |
| `updateVersionChangerSettings(**settings)` | `ExtensionManager` (shim) | Move + Rename | `panel.minecraft.versionChanger.updateSettings(**settings)` | |
| `getVersionChangerStatistics()` | `ExtensionManager` (shim) | Move + Rename | `panel.minecraft.versionChanger.getStatistics()` | |
| `getVersionChangerDefaultOrder()` | `ExtensionManager` (shim) | Move + Rename | `panel.minecraft.versionChanger.getDefaultOrder()` | |
| other `ExtensionManager` methods | `ExtensionManager` | Keep | ExtensionManager | panel-side extensions |
| `panel.api.versions` (`VersionsAPI`) | `calagoapi.api.versions` | Move | `calagoapi_minecraft.VersionChangerAPI` | |
| `calagoapi.servers` namespace (`Panel`, `Generic`, `Minecraft`) | `calagoapi/__init__` | Remove | import classes | shadowed the `calagoapi.servers` package |
| `calagoapi.utils` namespace | `calagoapi/__init__` | Remove | the real `calagoapi.utils` package | same names already exported there |
| `calagoapi.schedules` namespace | `calagoapi/__init__` | Remove | the real `calagoapi.schedules` package | exports `triggers`, `conditions`, `actions`, `variable`, `backups` |

### 11.4 Async layer

| Current method | Current location | Classification | Future location | Notes |
| --- | --- | --- | --- | --- |
| `wrap(value)` | `calagoapi.aio.panel` | Replace | same | registry lookup through the MRO, then the old rules |
| — | — | New | `calagoapi.aio.registerAsyncType(cls, wrapper=AsyncWrapper)` | extensions register their types |
| — | — | New | `calagoapi.aio.iterateInThread(iterable)` | async generator over a blocking iterator |
| `AsyncWrapper.__getattr__` | `calagoapi.aio.panel` | Replace | same | generator methods become async generators |
| `AsyncServer.streamConsole`, `onConsoleLine` | `calagoapi.aio.panel` | Keep | AsyncServer | native asyncio, only for daemon console |
| — | — | New | `calagoapi_minecraft.aio.AsyncMinecraftServer` | bridge stream through `iterateInThread` |

### 11.5 Extension system (`calagoapi.extensions`)

| Current method | Current location | Classification | Future location | Notes |
| --- | --- | --- | --- | --- |
| `enable`, `register`, `available` | `calagoapi.extensions` | Keep | same | |
| `get_extension` | `calagoapi.extensions` | Rename | `getExtension` | camelCase rule |
| `is_enabled` | `calagoapi.extensions` | Rename | `isEnabled` | |
| `enabled_extensions` | `calagoapi.extensions` | Rename | `enabledExtensions` | |
| `property_extension`, `class_extension` | `calagoapi.extensions` | Rename | `propertyExtension`, `classExtension` | |
| `migrated_to` | `calagoapi.extensions` | Rename | `migratedTo` | no core user left, kept for future moves |
| `compat.migratedTo` (helper) | `calagoapi.extensions.compat` | Rename | `migrationTarget` | frees the name |
| `Extension.on_enable`, `validate_config` | `Extension` | Rename | `onEnable`, `validateConfig` | |
| `ExtensionRegistry.get_class`, `is_enabled`, `owner_of` | registry | Rename | `getClass`, `isEnabled`, `ownerOf` | |
| `ExtensionRegistry.get`, `enable`, `register`, `registrations`, `describe`, `enabled`, `available` | registry | Keep | same | |
| `FIRST_PARTY` | `discovery` | Replace | `{'minecraft': 'calagoapi-minecraft'}` + `REPLACED` | |

### 11.6 `calagoapi-hungerbridge` service → `MinecraftServer` / HungerBridgePy

| Current method | Current location | Classification | Future location | Notes |
| --- | --- | --- | --- | --- |
| `HungerBridgeClient`, `sign`, `canonicalJson`, `parseToken` | `calagoapi_hungerbridge.client` | Remove | `hungerbridge.BridgeClient`, `hungerbridge.auth` | single source of truth |
| `HungerBridgeError(CalagoAPIError)` | `calagoapi_hungerbridge` | Remove | `hungerbridge.HungerBridgeError` | raised unchanged |
| `server.hungerbridge` (service) | `MinecraftServer` | Replace | `server.bridge` (a `BridgeClient`) | full HungerBridgePy API |
| `connect(url, token)` | service | Rename | `connectBridge(url=None, token=None, **options)` | returns `BridgeClient` |
| — | — | New | `setBridge(client)`, `closeBridge()`, `hasBridge()` | |
| `getUrl()` | service | Rename | `getBridgeUrl()` | |
| `client` (property) | service | Rename | `bridge` (property) | |
| `close()` | service | Rename | `closeBridge()` | |
| `ping()` | service | Remove | `server.bridge.getServerTime()` / `getPing()` | |
| `isReachable()` | service | Rename | `isBridgeReachable()` | |
| `authCheck()` | service | Rename | `getBridgeTokenInfo()` | includes `expiry` |
| `status()` | service | Remove | — | `/server/status` is not in protocol v1 |
| `info()` | service | Remove | `getBridgeInfo()` | `/server/info` is not in protocol v1 |
| `meta()` | service | Rename | `getBridgeInfo()` | `/server/meta` |
| `players()` | service | Rename | `getPlayers()` | |
| `playerCount()` | service | Rename | `getPlayerCount()` | |
| — | — | New | `getMaxPlayers()` | |
| `run(command, silent, show_console)` | service | Replace | `sendCommand(command, *, silent, showConsole)` | HungerBridgePy names |
| `log(message, level, thread)` | service | Rename | `writeLog(message, level='info', thread=None)` | |
| `stop()` | service | Remove | `server.bridge.stopServer()` | `stop()` stays CalagoAPI's |
| `tps()` | service | Replace | `getTPS(mode='current')` | float per mode, like HungerBridgePy |
| `mspt()` | service | Rename | `getMSPT()` | |
| `chunks()`, `entities()` | service | Rename | `getLoadedChunks()`, `getLoadedEntities()` | |
| `time()`, `weather()` | service | Rename | `getWorldTime()`, `getWeather()` | + `getWorldTimeInfo()` |
| `uptime()` | service | Rename | `getJVMUptime(formatted=False)` | `getUptime()` stays the panel's |
| `cpu()` | service | Rename | `getProcessorInfo()` | additive to `getCPU()` |
| `memory()` | service | Rename | `getMemoryInfo(unit='mib')` | additive to `getRAM()` |
| `gc()` | service | Rename | `getGarbageCollectorInfo()` | |
| `threads()` | service | Rename | `getThreadInfo()` | |
| `network()` | service | Rename | `getNetworkInfo()` | |
| `disk()` | service | Remove | `getDisk()` (panel) | `/system/disk` is not in protocol v1 |
| `findRelease(mc_version, loader, release)` | service | Move | `hungerbridge.releases.find_release()`; `server.findBridgeRelease()` | naming contract owned by HungerBridge(Py) |
| `install(mc_version, loader, release)` | service | Rename | `installBridge(minecraft_version=None, loader=None, release=None)` | detection: Version Changer → bridge meta → egg name |
| `HungerBridgeExtension` (id `hungerbridge`) | extension | Replace | `MinecraftExtension` (id `minecraft`) | |

### 11.7 `calagoapi-version-changer` → `calagoapi_minecraft.versions`

| Current method | Current location | Classification | Future location | Notes |
| --- | --- | --- | --- | --- |
| `getInstalledVersion()` | `@method(MinecraftServer)` | Rename | `server.versions.getInstalled()` | |
| `installedVersion` (property) | `@propertyExtension` | Replace | `server.versions.getInstalledBuild()` | method: async-friendly, explicit request |
| `isUpToDate()` | `@method` | Move | `server.versions.isUpToDate()` | |
| `getVersionTypes()` | `@method` | Rename | `server.versions.getTypes()` | |
| `getVersions(...)`, `getBuilds(...)` | `@method` | Move | `server.versions.getVersions(...)`, `getBuilds(...)` | |
| — | — | New | `server.versions.getLatestBuild(type, version)` | |
| `installVersion(build, truncate_directory, accept_eula)` | `@method` | Rename | `server.versions.install(build, truncate_directory=False, accept_eula=True, backup=None)` | |
| `updateVersion(truncate_directory)` | `@method` | Rename | `server.versions.update(...)` | |
| — | — | New | `server.versions.isAvailable()` | panel extension installed? |
| `getVersionChangerSettings` … `DefaultOrder` (4) | `@method(ExtensionManager)` | Move + Rename | `panel.minecraft.versionChanger.getSettings()` … `getDefaultOrder()` | |
| `VersionChangerAPI` | `calagoapi_version_changer.api` | Move | `calagoapi_minecraft.versions.VersionChangerAPI` | |
| `VersionChangerExtension` | extension | Remove | merged into `MinecraftExtension` | |

### 11.8 New `calagoapi_minecraft` API (not mapped from an old method)

| Method | Class | Notes |
| --- | --- | --- |
| `sendPanelCommand(command)` | MinecraftServer | `Server.sendCommand` through the panel |
| `streamConsole(...)`, `onConsoleLine(...)`, `sendCommands(...)` | MinecraftServer | Replace (see §10.3/10.4) |
| `createBridgeToken(token_id='calagoapi', policy='admin', expiry=None, timeout=30)` | MinecraftServer | console `hb token create` → pickup → `connectBridge` |
| `redeemBridgePickup(pickup_url)` | MinecraftServer | |
| `waitForBridge(timeout=120, interval=2)` | MinecraftServer | after start/install |
| `getPlatform()`, `getMinecraftVersion()` | MinecraftServer | `/server/meta` |
| `getPerformance()` | MinecraftServer | TPS (4 windows), MSPT, players |
| `getMemoryInfo`, `getProcessInfo`, `getProcessorInfo`, `getThreadInfo`, `getGarbageCollectorInfo`, `getNetworkInfo` | MinecraftServer | §10.6 |
| `getServer(server_id, name=None, **options)`, `fromServer(server, **options)` | MinecraftManager (`panel.minecraft`) | |
| `versionChanger` | MinecraftManager | `VersionChangerAdmin` |
| `settings()` | module | effective config |

### 11.9 Unchanged classes (Keep)

`Panel`, `Console`, `ConsoleEvent`, `AsyncConsole`, `File`, `FileManager`, `Backup`,
`BackupGroup`, `BackupManager`, `Database*`, `DatabaseExplorer`, `Schedule`, `ScheduleStep`,
`ScheduleManager` + builders, `Subuser`, `SubuserManager`, `User`, `UserManager`, `Activity`,
`Allocation`, `Subdomain`, `NetworkManager`, `TunnelManager`, `Node`, `NodeManager`,
`Account`, `Auth`, all account models, `Admin` and every admin resource/manager, `Page`,
`Model`, every exception and `utils` function. Only docstring examples change (generic
commands instead of `say`/`save-all`), plus the extension-API renames inside their docs.

### 11.10 HungerBridgePy

| Current method | Current location | Classification | Future location | Notes |
| --- | --- | --- | --- | --- |
| all endpoint getters, `runCommand`, `broadcast`, `log`, `stopServer`, pickup | `BridgeClient` | Keep | same | |
| `getTokenInfo()` | `BridgeClient` | Replace | same | adds `expiry` |
| — | — | New | `BridgeClient.openStream(history_handler=None, new_log_handler=None)` | independent `Stream` per consumer |
| — | — | New | `BridgeClient.streamLogs(history=None, *, timeout=None, reconnect=False, sanitize=False)` | iterator |
| — | — | New | `BridgeClient.getTPSStats()`, `getPlayerStats()` | one request each (used by `getPerformance()`) |
| `Stream._stream_once` errors | `Stream` | Replace | same | typed `HungerBridgeError`s |
| `Stream._run` reconnect loop | `Stream` | Replace | same | no reconnect after auth/forbidden/not-found |
| — | — | New | `Stream(close_handler=...)` | called when the worker ends |
| — | — | New | `hungerbridge.releases`: `find_release()`, `list_release_assets()`, `parse_asset_name()`, `loader_for()`, `ReleaseAsset`, `LOADERS` | |
| — | — | New | `protocol.MAX_HISTORY = 200` | |

---

## 12. Naming review

| Area | Finding | Decision |
| --- | --- | --- |
| Class | `GenericServer`: "generic" implies a special case | **Rename** to `Server` |
| Package | `calagoapi-hungerbridge` named after the transport, not the domain | **Rename** to `calagoapi-minecraft` / `calagoapi_minecraft` / id `minecraft` |
| Package | `calagoapi-version-changer`: a second package for the same game | **Merge** into `calagoapi-minecraft` |
| Module | `servers/generic.py` | **Rename** to `servers/server.py` |
| Methods | hungerbridge service used nouns (`players()`, `tps()`, `memory()`) | **Rename** to `getPlayers()`, `getTPS()`, `getMemoryInfo()` |
| Methods | `getVersionTypes`/`installVersion` on the server mixed two concerns | **Move** to `server.versions.getTypes()` / `install()`, like `server.backups` |
| Methods | `getVersionChangerSettings` etc. on the generic `ExtensionManager` | **Move** to `panel.minecraft.versionChanger.getSettings()` |
| Methods | `broadcast()` was an alias of `say()` | **Replace** with HungerBridgePy's real `broadcast(message, prefix)` |
| Methods | bridge "uptime" vs container uptime | `getJVMUptime()` (bridge), `getUptime()` (panel) |
| Methods | bridge CPU/memory vs panel CPU/RAM | `getProcessorInfo()`/`getMemoryInfo()` (bridge, dicts), `getCPU()`/`getRAM()` (panel, numbers) |
| Methods | extension API snake_case functions/hooks | **Rename** to camelCase (§9.4) |
| Methods | `getPowerState`, `isRunning`, `isStopped`, `listBackups`/`getBackups` duplicates | **Keep**: documented HungerLib-compatible aliases |
| Parameters | `server_domain` + `server_port` | **Rename** to `address` |
| Parameters | `mc_version` | **Rename** to `minecraft_version` (snake_case words, no abbreviations) |
| Parameters | `showConsole` (camelCase parameter) | **Keep**: it is HungerBridgePy's parameter name, which is the source of truth for the redesigned method |
| Namespaces | `calagoapi.servers/utils/schedules` SimpleNamespaces shadowing subpackages | **Remove** |
| Terminology | "GenericServer", "Minecraft helpers" in core docs | "server"; Minecraft only in the extension |
| Terminology | "bridge" / "HungerBridge" / "HungerBridgePy" used loosely | **HungerBridge** = the plugin/mod, **HungerBridgePy** = the Python client (`hungerbridge` package), **bridge** = a server's HungerBridge connection (`server.bridge`) |
| Terminology | "extension" means two things | "**SDK extension**" (`calagoapi.extensions`) vs "**panel extension**" (Calagopus, `panel.admin.extensions`), stated in both docs |
| Errors | `HungerBridgeError` existed in two packages | only `hungerbridge.HungerBridgeError`; CalagoAPI side adds `MinecraftError` |

No wholesale snake_case migration: camelCase methods, snake_case attributes/parameters and
single-quoted strings stay the CalagoAPI style. HungerBridgePy keeps its own (double-quoted,
module functions snake_case, methods camelCase) style.

---

## 13. Documentation rewrite plan

Standards for every page and docstring example:

- 4-space Python indentation; runnable top-level imports; `from calagoapi import ...` shown
  once per page.
- f-strings for any formatting (`print(f'{server.name}: {server.getStatus()}')`) instead of
  `print(a, b)` concatenation lists, `%` or `.format()`. The codebase has no `%`/`.format()`
  uses in docs; the main targets are multi-argument `print(...)` calls and string building
  in examples, which become f-strings.
- Current names only (`Server`, `getExtension`, `panel.minecraft`, `server.versions`).
- Game-agnostic examples in core docs (`'status'`, `'help'`, `GAME_PORT`, `7777`). Minecraft
  examples only in the Minecraft extension's README and tutorial track.
- Reference pages are tables plus short examples; tutorials explain.

| Page | Action |
| --- | --- |
| `README.md` | rewrite: core quick start with `Server`, extension overview, link to `calagoapi-minecraft` |
| `docs/README.md` | rewrite: reference index + tutorial path |
| `docs/getting-started.md`, `servers.md`, `console.md`, `async.md` | update: `Server`, generic examples, f-strings, async type registry |
| `docs/files.md`, `backups.md`, `databases.md`, `schedules.md`, `network.md`, `account.md`, `admin.md`, `errors-and-utilities.md` | update: names, f-strings, game-agnostic examples |
| `docs/minecraft.md` | remove from core; content moves to `calagoapi-minecraft/README.md` + tutorials track 3 |
| `docs/learning/*.md` (10) | replace by `docs/extensions.md` (reference) + tutorials track 2 |
| `docs/architecture.md` | rewrite layers, ownership, dependency rule, async registry, tests |
| `docs/migrating-from-hungerlib.md` | update to `Server` and point Minecraft users to the extension |
| `docs/migrating-to-2.0.md` | new: every rename/move from §11 as a table |
| `docs/design/extension-system.md` | previous PLAN, with a 2.0 naming note at the top |
| `src/extensions/calagoapi-minecraft/README.md` | new: complete reference for the extension |
| `PROJECT_NOTES.md`, `version.yaml` | update status, decisions, changelog |
| HungerBridgePy `README.md`, `CHANGELOG.md` | document `streamLogs`, `openStream`, releases, typed stream errors |
| HungerBridge `ENDPOINTS.md`, `README.md`, `BUILDING.md`, `CHANGELOG.md` | new jar names, iterator streaming example, CalagoAPI integration pointer |

## 14. Tutorial rewrite plan

The old guides were organized by extension-system feature (method, property, class, ...),
always using `MinecraftServer` as the target, with no path through the core SDK. The new
hierarchy is a progression with three tracks. Each tutorial has: what you will build,
the steps with explanations, a complete program, "how it works" (the architecture behind
it) and "next". There are no Prerequisites or Estimated Time sections. Each tutorial says in
its first sentence what it builds on.

```
docs/tutorials/
├── README.md                       learning path + how the tracks connect
├── basics/                         Track 1: the core SDK (any game)
│   ├── 01-first-script.md          connect, list servers, read status (sync)
│   ├── 02-server-control.md        power, wait for state, resources, safe restart
│   ├── 03-live-console.md          streamConsole, waitFor, callbacks, daemon events
│   ├── 04-files-and-backups.md     config edits, backup-before-change workflow
│   └── 05-going-async.md           AsyncPanel, gather, async console, a small bot loop
├── extensions/                     Track 2: extending CalagoAPI
│   ├── 06-using-extensions.md      install, enable, config, modes, introspection
│   ├── 07-your-first-extension.md  @method + @propertyExtension on Server, testing it
│   ├── 08-services-and-namespaces.md  @classExtension, namespace mode, async behaviour
│   ├── 09-configuration-and-dependencies.md  default_config, validateConfig, onEnable, Dependency, aliases
│   └── 10-packaging-and-publishing.md  entry points, discovery, migratedTo, conflicts, tests
└── minecraft/                      Track 3: calagoapi-minecraft (+ HungerBridge)
    ├── 11-minecraft-setup.md       install, enable, the two transports, first bridge token
    ├── 12-commands-and-console.md  sendCommand output, streamConsole, onConsoleLine, panel fallback
    ├── 13-monitoring.md            getRAM vs getMemoryInfo, TPS/MSPT, a health check
    ├── 14-versions-and-installs.md server.versions, auto backup, installBridge, waitForBridge
    └── 15-community-bot.md         capstone: async bot combining every track
```

Missing topics that are now covered: the core SDK as a learning path (01–05), async (05), the
two-transport model (11), monitoring semantics (13), safe upgrades (14), and an end-to-end
capstone (15). Every tutorial's code is mirrored by an offline example or test, so it keeps running.

---

## 15. HungerBridgePy changes

1. `stream.py`:
   - `Stream(..., close_handler=None)`: `close_handler(error)` is called when the worker thread ends.
   - Non-2xx stream responses raise `Transport._error_for(response)` (401 →
     `HungerBridgeAuthError` with `reason`, 403 → `HungerBridgeForbidden`, 404 →
     `HungerBridgeNotFound`, 429 → `HungerBridgeRateLimit(retry_after=...)`). Connection
     failures become `HungerBridgeConnectionError`. `last_error` holds the typed error.
   - Reconnect stops on permanent errors (401, 403, 404).
2. `client.py`:
   - `openStream(history_handler=None, new_log_handler=None) -> Stream`: an independent
     stream with fresh signing per connection.
   - `streamLogs(history=None, *, timeout=None, reconnect=False, sanitize=False) -> Iterator[str]`:
     blocking iterator; ends after `timeout` seconds without a line, when the server ends the
     stream, or with the typed error; closing the generator disconnects.
   - `getTokenInfo()` also returns `expiry`.
3. `releases.py` (new): `ReleaseAsset(name, url, loader, minecraft_version, release)`,
   `parse_asset_name(name)` (accepts `HungerBridge-<loader>-<mc>-<v>.jar` and
   `<mc>-<loader>-<v>.jar`; skips `-sources`/`-dev`/`-javadoc`), `list_release_assets(...)`,
   `find_release(minecraft_version, loader, release='latest', repository=..., api_url=..., timeout=..., session=None)`
   (`'latest'` picks the newest Minecraft version), `loader_for(server_type)` (`PAPER`/`PURPUR`/
   `FOLIA`/... → `paper`, `FABRIC`/`QUILT` → `fabric`).
4. `protocol.py`: `MAX_HISTORY = 200`.
5. `__init__.py` exports; `version.yaml` `1.0-dev.2`; README and CHANGELOG.
6. Tests: iterator streaming (history, live, timeout, close, typed errors, no reconnect on 401),
   release parsing (both formats, latest selection, errors), token `expiry`.

## 16. HungerBridge changes

1. `build.gradle`: per-target projects (`<mc>-<loader>`) set
   `base.archivesName = "HungerBridge-<loader>-<mc>"`, so release assets are
   `HungerBridge-paper-26.2-<version>.jar`: self-describing in `plugins/`, and parseable by
   HungerBridgePy.
2. `ENDPOINTS.md`: SSE section shows both `client.streamLogs(...)` (iterator) and
   `client.stream.connect(...)` (callbacks); stream error semantics; `/auth/check` `expiry`
   mapped in the Python column.
3. `README.md` / `BUILDING.md`: jar names; "Using HungerBridge from CalagoAPI" pointer to
   `calagoapi-minecraft`.
4. `CHANGELOG.md`: unreleased entry for the jar rename.

No Java runtime changes are needed: every capability `calagoapi-minecraft` uses already exists
in protocol v1.

## 17. Mandatory changes

Taken directly from the specification:

1. `GenericServer` → `Server`; `Server` free of Minecraft code, docs and dependencies.
2. Remove `MinecraftServer` from core; define `class MinecraftServer(Server)` in the extension.
3. Rename and redesign `calagoapi-hungerbridge` → `calagoapi-minecraft`.
4. Dependency rule: CalagoAPI depends on neither HungerBridge nor HungerBridgePy;
   `calagoapi-minecraft` depends on CalagoAPI and HungerBridgePy.
5. HungerBridgePy is the authority; fix discrepancies upstream (§2.6, §15, §16).
6. `sendCommand()` / `streamConsole()` keep names, adopt HungerBridgePy behaviour.
7. `getRAM()`, `getCPU()`, `stop()` remain CalagoAPI-owned; bridge data as new APIs.
8. Full method inventory (§11) driving the rewrite.
9. Naming review keeping camelCase (§12).
10. Documentation rewrite with f-strings, 4-space indentation, current imports and names (§13).
11. Tutorial redesign without Prerequisites/Estimated Time sections (§14).
12. Repository responsibilities and coordination (§6).
13. Update code, docs, tutorials, examples, tests, imports, layouts and references.

## 18. Recommended improvements

Found during analysis. All except the future-work items are implemented:

| # | Improvement | Why |
| --- | --- | --- |
| R1 | Merge `calagoapi-version-changer` into `calagoapi-minecraft` (`server.versions`) | one package per game; no cross-extension coupling |
| R2 | Remove 1.x deprecated shims, `api/versions.py`, version-changer admin shims | major version; dead code in core |
| R3 | Remove `servers`/`utils`/`schedules` SimpleNamespaces | they shadow real subpackages |
| R4 | Async type registry + generator support in `AsyncWrapper` | extension types were not async; subclass streams were bypassed |
| R5 | camelCase extension API | one naming rule for all methods |
| R6 | `sendPanelCommand()` + `createBridgeToken()` | explicit second transport; zero-touch bridge onboarding |
| R7 | `waitForBridge()`, `getPerformance()`, `getProcessInfo()` | monitoring and install workflows |
| R8 | Architecture test enforcing the dependency rule | keeps the boundary from eroding |
| R9 | HungerBridgePy typed stream errors, no reconnect on permanent errors | a revoked token no longer reconnects forever |
| R10 | Self-describing HungerBridge jar names | fixes `installBridge()` and makes `plugins/` readable |
| R11 | `ExtensionNotFoundError` hints for replaced ids | clear migration error |
| R12 | Genericize core docstring examples | `Server` docs must not be Minecraft docs |
| F1 *(future)* | HungerBridge `/system/hardware` endpoint → `getHardwareInfo()` | needs a protocol addition |
| F2 *(future)* | native asyncio HungerBridgePy client (HungerBridge design doc 02 §4) | removes worker threads for streams |
| F3 *(future)* | Move Subdomain Manager wrappers to `calagoapi-subdomains` | same pattern as this rewrite |

## 19. Implementation phases

| Phase | Work | Exit criteria |
| --- | --- | --- |
| 0 | Inspect, baseline tests, write this plan | plan committed to `PLAN.md` |
| 1 | HungerBridgePy: stream iterator, typed errors, releases, token expiry, docs | HungerBridgePy tests green |
| 2 | HungerBridge: jar names, docs | build script change reviewed (not buildable offline) |
| 3 | Core: `Server`, removals, namespaces, aio registry, extension API camelCase, generic docstrings, architecture test | core tests green |
| 4 | `calagoapi-minecraft`: package, `MinecraftServer`, bridge, versions, manager, extension, async; delete old packages | extension tests green against fake panel + fake bridge |
| 5 | Docs, tutorials, examples, README files, migration guide | example tests green, docs reference only existing names |
| 6 | CI workflows, version files, PROJECT_NOTES, final full run | all suites green |

## 20. Risk assessment

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| `hungerbridge` not yet on PyPI blocks installing `calagoapi-minecraft` | High | High | CI installs it from GitHub; release notes state the order; `hungerbridge` dist name already fixed in HungerBridgePy |
| Gradle `archivesName` change untested (no network/JDK run here) | Medium | Medium | minimal change in the root `subprojects` block; HungerBridgePy still parses the old names |
| Bridge default URL (server address + 1913) wrong when HungerBridge binds 127.0.0.1 | High | Low | documented; `bridge_url` config / `connectBridge(url)`; `createBridgeToken()` takes `url` |
| `createBridgeToken()` depends on the console line format `Retrieve it at: /pickup/<id>?passkey=<hex>` | Medium | Low | regex on `/pickup/<id>?passkey=<hex>` only; clear `MinecraftError` on timeout |
| Users relying on 1.x names | Certain | Medium | major version; `docs/migrating-to-2.0.md`; `ExtensionNotFoundError` hints |
| Behaviour change: `MinecraftServer.sendCommand` needs HungerBridge | Certain | Medium | explicit `BridgeNotConfiguredError` with fix; `sendPanelCommand()` |
| Thread-based async streams use one thread per stream | Low | Low | documented; native async client is future work F2 |
| Live panel/bridge never exercised | High | Medium | contract-faked panel + HMAC-verifying fake bridge in tests; live checks listed in PROJECT_NOTES |

## 21. Proposed final API

```python
# ── core: any game ───────────────────────────────────────────────────────────
from calagoapi import Panel, AsyncPanel, Server

with Panel(url='https://panel.example.com', api_key='...') as panel:
    server: Server = panel.servers.getServer('abc123')
    server.start()
    server.waitForOnline(timeout=120)
    print(f'{server.name}: {server.getRAM()} MiB, {server.getCPU()} % CPU')
    server.sendCommand('status')                       # panel REST
    for line in server.streamConsole(timeout=30):      # daemon websocket
        print(line)
    server.stop()                                      # panel power action

# ── extension system ─────────────────────────────────────────────────────────
from calagoapi.extensions import Extension, enable, getExtension, method, propertyExtension, classExtension

# ── Minecraft: pip install calagoapi-minecraft ───────────────────────────────
from calagoapi_minecraft import MinecraftServer, MinecraftError, BridgeNotConfiguredError

enable('minecraft', config={'bridge_token': 'bot:9f2c...', 'auto_backup': True})
server: MinecraftServer = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

server.sendCommand('list')                     # -> 'There are 2 of a max of 20 players online: ...'
server.sendCommand('save-all', silent=True)    # -> None
server.say('Restarting soon')
server.broadcast('Event starts now', prefix='[Event] ')
for line in server.streamConsole(history=50, timeout=60):
    print(line)

server.getPlayers(), server.getPlayerCount(), server.getMaxPlayers()
server.getTPS('1m'), server.getMSPT(), server.getPerformance()
server.getRAM(), server.getCPU()                       # panel (container)
server.getMemoryInfo(), server.getProcessorInfo()      # bridge (JVM)
server.getThreadInfo(), server.getGarbageCollectorInfo(), server.getProcessInfo(), server.getNetworkInfo()
server.getWorldTime(), server.getWeather(), server.getLoadedChunks(), server.getLoadedEntities()
server.getPlatform(), server.getMinecraftVersion(), server.getBridgeInfo()

server.getProperties(), server.setProperty('max-players', 50), server.acceptEula()

build = server.versions.getLatestBuild('PAPER', '1.21.11')
server.versions.install(build)                 # backup first (auto_backup)
server.installBridge()                         # right jar into plugins/ or mods/
server.restart()
server.waitForBridge(timeout=180)

server.bridge                                  # hungerbridge.BridgeClient: full HungerBridgePy API
panel.minecraft.versionChanger.getSettings()   # admin

# async: identical names
async with AsyncPanel(url=..., api_key=...) as panel:
    server = await panel.minecraft.getServer('abc123')
    print(await server.getTPS())
    async for line in server.streamConsole(history=10):
        print(line)
```

## 22. Decision log

| # | Decision | Alternatives | Reason |
| --- | --- | --- | --- |
| D1 | `MinecraftServer` subclass + `panel.minecraft` service | patch `Server`; subclass only | §9.1 |
| D2 | merge version changer | separate package | §9.2 |
| D3 | no bridge→panel fallback | automatic fallback; config switch | stable return types, explicit errors; `sendPanelCommand()` covers the panel route |
| D4 | `server.bridge` *is* a `hungerbridge.BridgeClient` | wrapper class | no workaround layer; HungerBridgePy is the API |
| D5 | thread-based async for bridge streams | native asyncio SSE in CalagoAPI | would duplicate HungerBridgePy's SSE parser (protocol in two places again) |
| D6 | release discovery in HungerBridgePy | keep in extension | naming is a HungerBridge/HungerBridgePy contract |
| D7 | camelCase extension API | keep snake_case | one rule for methods SDK-wide; unreleased API, major version |
| D8 | no aliases for `hungerbridge`/`version_changer` ids | deprecated aliases | APIs differ completely; an alias would enable something that does not provide the old members. A not-found hint is clearer |
| D9 | `history` int on `MinecraftServer`, bool on `Server` | unify to int | the Wings protocol cannot replay "last N"; `bool` ⊂ `int` keeps calls compatible |
| D10 | Core version `2.0-dev.1`, `calagoapi-minecraft` `1.0-dev.1`, HungerBridgePy `1.0-dev.2` | — | breaking core; new package; additive client release |
| D11 | `ServerManager.getServer(server_class=..., **options)` in core | a Minecraft-specific manager method | a game-agnostic hook every game extension can use; `panel.minecraft.getServer()` is a thin wrapper |

## 23. Implementation notes and verification

Decisions made or refined during implementation:

- **`server_class=` on `getServer()` / `getServers()`** (D11) replaced `getMinecraftServer()`
  in core. **`panel.admin.extensions.call(extension, path, method, json)`** is a generic
  hook for SDK extensions that wrap a panel extension's admin API.
- **HungerBridgePy got two more getters**, `getTPSStats()` and `getPlayerStats()`, so
  `getPerformance()` needs 3 requests instead of 6, and does not reach into HungerBridgePy's
  transport (that would have been a workaround layer).
- **HungerBridgePy bug found and fixed:** on Windows, `Stream.disconnect()` always blocked
  for its whole timeout, because `shutdown()` does not wake a `recv()` blocked in another
  thread and `close()` is deferred while `http.client` holds a `makefile()` reference. The
  socket handle is now closed at the C level. This was found because `streamLogs()` must
  disconnect promptly when a caller `break`s out of the loop.
- `MinecraftServer.streamConsole()` is a plain method returning HungerBridgePy's iterator,
  not a generator function. It therefore fails **on the call** when no token is configured,
  instead of at the first line. `AsyncMinecraftServer` wraps it with `iterateInThread()`.
- `installBridge(loader='PAPER')` normalizes server types to loaders, and `replace=True`
  deletes older HungerBridge jars (both naming schemes) in the target directory first, so an
  upgrade never leaves two bridge jars loaded.
- The configuration moved to its own `config.py`, so `server.py`, `versions.py` and
  `bridge.py` can read `settings()` without importing the Extension class (no import cycle).
- The only core file allowed to mention Minecraft is `extensions/discovery.py` (the
  first-party package table and the `REPLACED` hints for 1.x ids).
  `tests/test_architecture.py` enforces it.
- Removed artifacts (the old extension packages, `docs/learning/`, the old first-party
  example) were untracked, so not recoverable from git. They were **moved** to
  `../_removed-in-calagoapi-2.0/` instead of deleted.
- No "Prerequisites" or "Estimated time" sections existed anywhere, so there was nothing to
  remove. The new tutorials follow a fixed structure without them: what you build, steps,
  complete program, how it works, next.

Verified (2026-11-07):

| Check | Result |
| --- | --- |
| CalagoAPI `pytest` (core, extension system, architecture, async types, `calagoapi-minecraft`, all examples), Python 3.12 | 158 passed |
| Same on Python 3.9 | 158 passed |
| HungerBridgePy `pytest`, Python 3.12 and 3.9 | 94 passed, 1 skipped (live) each |
| Wheels for `calagoapi`, `calagoapi-minecraft`, `hungerbridge` build; core wheel contains only `calagoapi/` | yes |
| Clean venv: `available() == ['minecraft']` through the entry point, package not imported before `enable()`, token masked in `describe()` | yes |
| Tutorial 07–09 code extracted from the Markdown and run | passes |
| Relative links in all Markdown of the three repositories; `server.<method>(` calls in docs exist | no broken links; no unknown methods (`admin.md` calls are on `AdminServer`) |

Not verified:

- The HungerBridge Gradle change (`archivesName`): no JDK in this environment. HungerBridgePy
  still parses the old names, so `installBridge()` works with existing releases either way.
- Nothing ran against a live Calagopus panel or a live HungerBridge. Panel calls are checked
  against `openapi.json`. Bridge calls are checked against a fake that verifies HMAC
  signatures independently, and HungerBridgePy has its own live suite for real servers.
- GitHub workflows have not run (CI installs HungerBridgePy from
  `git+https://github.com/HungerNet/HungerBridgePy`, which must be readable by the workflow).
