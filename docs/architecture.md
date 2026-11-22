# Architecture

This page is for contributors. The reasoning behind the 2.0 layout is in
[PLAN.md](../PLAN.md); the extension system's design in [design/extension-system.md](design/extension-system.md).

## Repositories and packages

```
┌──────────────────────────── CalagoAPI repository ─────────────────────────────┐
│ src/calagoapi/                    calagoapi           core, game-agnostic      │
│ src/extensions/calagoapi-minecraft/  calagoapi-minecraft  MinecraftServer, ... │
└────────────────────────────────────────────────────────────────────────────────┘
HungerBridgePy repository           hungerbridge        HungerBridge Python client (source of truth)
HungerBridge repository             (jar)               the plugin/mod inside Minecraft servers
```

| Owner | Owns | Must not contain |
| --- | --- | --- |
| `calagoapi` | Calagopus panel/daemon API, `Server`, managers, daemon console, `AsyncPanel`, extension system | game-specific code or docs; imports of `hungerbridge` or game extensions |
| `calagoapi-minecraft` | `MinecraftServer`, `panel.minecraft`, `server.properties`, bridge install/token bootstrap | HungerBridge protocol details (signing, streaming, release resolution) |
| HungerBridgePy | HungerBridge protocol, typed errors, streams, pickups, release discovery | panel concepts |
| HungerBridge | endpoints, auth, policies, SSE, release artifact names | client conveniences |

Dependencies point one way: `calagoapi-minecraft → calagoapi`, `calagoapi-minecraft → hungerbridge`.
`tests/test_architecture.py` enforces that core imports no game package, mentions no
game, and depends only on `requests` and `websockets`.

## Core layers

```
calagoapi/
├── panel.py          Panel: entry point, wires everything together
├── api/              the only code that knows URLs and HTTP
│   ├── client.py     Client: auth headers, JSON, errors, pagination, retries
│   ├── servers.py    ServersAPI       /api/client/servers/...
│   ├── files.py  backups.py  databases.py  schedules.py  network.py  users.py  attachments.py
│   ├── account.py    AccountAPI       /api/client/account/...
│   ├── auth.py       AuthAPI          /api/auth/...
│   ├── public.py     PublicAPI        /api/settings, /api/languages, ...
│   └── admin.py      AdminAPI         /api/admin/... (ResourceAPI for CRUD collections)
├── servers/          Server, ServerManager, ServerGroup, AdminServer
├── files/  backups/  databases/  schedules/  users/  network/  tunnels/  nodes/  account/  admin/
├── console/          Console, ConsoleEvent: live console over the daemon websocket
├── aio/              AsyncPanel, AsyncServer, AsyncWrapper, AsyncConsole, registerAsyncType
├── extensions/       extension system: registry, decorators, discovery, exceptions
└── utils/            Model, Page, AdminResource, exceptions, convert, wait helpers
```

Rules:

1. **Only `api/` builds URLs.** High-level classes call `panel.api.<module>`.
2. API modules take and return plain Python data and unwrap response envelopes.
3. High-level classes wrap that data in objects with getters, state checks and actions;
   objects keep the raw data in `.data`.
4. Methods are camelCase, variables, attributes and parameters snake_case, strings use
   single quotes, formatting uses f-strings (logging keeps lazy `%s` arguments).
5. `Server` is game-agnostic. Game behaviour goes into `Server` subclasses in extension
   packages; `ServerManager.getServer(server_class=...)` builds them.

## Console and async

- The live console is the one part that does not go through `api/`: it talks to the node
  daemon with credentials from `api.servers.websocket()` (Wings protocol: JSON text frames
  `{"event": ..., "args": [...]}`, starting with `auth`).
- `aio/` does not duplicate the API. `AsyncWrapper` turns every method into a coroutine
  running in a worker thread and wraps what it returns. Generator methods become async
  generators (`iterateInThread`). Only the daemon console has a native asyncio
  implementation (`AsyncConsole`).
- `wrap()` picks a wrapper through the **async type registry**
  (`registerAsyncType(cls, wrapper)`, resolved through the MRO). Core registers
  `Server → AsyncServer`; extension packages register their own types
  (`MinecraftServer → AsyncMinecraftServer`, `BridgeClient`, ...). Unregistered objects
  from `calagoapi.*` modules get a plain `AsyncWrapper`.

## Extension system

```
extensions/
├── __init__.py    public API: enable(), register(), getExtension(), isEnabled(), registry, ...
├── base.py        Extension, ExtensionMetadata, Alias, Dependency, class validation
├── members.py     @method, @propertyExtension, @classExtension; service and namespace descriptors
├── registry.py    ExtensionRegistry: discovery, enablement, dependencies, conflicts, ownership
├── discovery.py   "calagoapi" entry points, FIRST_PARTY package hints, REPLACED 1.x ids
├── compat.py      @migratedTo: hand a built-in method over to an extension
└── exceptions.py
```

- Decorators only label functions and classes. `enable()` patches **classes** (never
  instances) after checking every name for conflicts, and records a `Registration`
  (owner, target, name, kind) per installed attribute.
- First-party extensions are separate packages in `src/extensions/`, built only on the
  public API, each with its own `pyproject.toml`, `version.yaml`, README and tests.

## calagoapi-minecraft

```
calagoapi_minecraft/
├── server.py      MinecraftServer(Server): panel channel (inherited) + bridge channel (server.bridge)
├── bridge.py      BridgeClient creation, console pickup parsing
├── properties.py  server.properties text handling
├── manager.py     MinecraftManager: @classExtension(Panel, 'minecraft')
├── extension.py   MinecraftExtension (id 'minecraft'); config.py: defaults, validation, settings()
├── aio.py         AsyncMinecraftServer + registerAsyncType() calls
└── exceptions.py  MinecraftError, BridgeNotConfiguredError
```

- `server.bridge` is a `hungerbridge.BridgeClient`; no HungerBridge protocol code lives
  in CalagoAPI. Missing client capabilities are added to HungerBridgePy (for example
  `streamLogs()`, `findRelease()`). MinecraftServer adds no aliases for
  HungerBridgePy methods; bridge features are used as `server.bridge.<method>`.
- Overrides keep base calls working: `sendCommand(command)` and
  `streamConsole()` are valid on both `Server` and `MinecraftServer`.
- `getRAM()`, `getCPU()` and `stop()` are inherited unchanged; bridge metrics are
  HungerBridgePy's (`server.bridge.getMemoryStats()`, `getCPUStats()`, ...).

## The generated client

`api_generated/` (an OpenAPI generated client) and `openapi.json` are the reference for
endpoints, parameters and models. CalagoAPI does **not** import the generated client.

When Calagopus adds endpoints:

1. Regenerate `api_generated/` (or read `openapi.json`).
2. Add a method to the matching module in `api/` (or, for a game-specific panel
   extension, to the extension package).
3. Expose it from the high-level class with a docstring and example.
4. Document it in `docs/`.

## Tests

```bash
pip install -e .[dev]
pip install -e src/extensions/calagoapi-minecraft    # and hungerbridge (HungerBridgePy)
pytest
```

Everything runs offline:

- `contract.py` is a fake panel built from `openapi.json`. It answers every request and
  records requests that do not match the spec.
- `test_contract.py` calls every public method reachable from `Panel` (`exercise.py`) and
  fails on any mismatch, or when the spec has endpoints nobody calls. Endpoints of
  game-specific panel extensions are listed in `WRAPPED_BY_EXTENSIONS`: core must not
  call them, and the owning extension's tests must.
- `test_scenarios.py`, `test_console.py` (fake daemon), `test_resilience.py`, `test_units.py`.
- `test_extensions.py` covers the extension system; `test_aio_types.py` the async type
  registry, generators and `server_class`; `test_architecture.py` the dependency rules;
  `test_examples.py` runs `examples/extensions/`.
- `src/extensions/calagoapi-minecraft/tests/` runs against the same fake panel plus a fake
  HungerBridge (`minecraft_testing.py`). The fake HungerBridge verifies HMAC signatures
  with a canonicalizer written independently of HungerBridgePy, streams SSE, redeems
  pickups and serves a fake GitHub releases API. It also runs `examples/minecraft/`.

After a Calagopus update: replace `openapi.json`, run `pytest`, then fix whatever it lists.

## Conventions worth knowing

- Optional arguments left as `None` are not sent, so the panel keeps its value or default.
- List methods fetch every page unless `page=` is passed.
- Anywhere an id is expected, an object works too (`idOf()` in `utils/model.py`).
- Free-text path segments are URL-encoded with `segment()`.
