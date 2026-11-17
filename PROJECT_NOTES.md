# CalagoAPI: project notes

Outcomes, decisions and open items from building CalagoAPI (October 2026), updated for the
2.0 rewrite (November 2026, design in `PLAN.md`).

## Status at a glance

| Item | State |
| --- | --- |
| SDK (sync) | Done: `src/calagoapi/`, 65 modules |
| Live console (websocket) | Done: sync and async |
| Async API (`AsyncPanel`) | Done |
| Retries / `with` blocks | Done |
| Docs | Done: README + 15 guides in `docs/`, docstrings on all 1,250 public classes and methods |
| 2.0 rewrite | Done (November 2026): game-agnostic `Server`, `calagoapi-minecraft`, camelCase extension API; design in `PLAN.md` |
| Extension system | Done: `calagoapi.extensions`, reference `docs/extensions.md`, design record `docs/design/extension-system.md` |
| First-party extensions | `calagoapi-minecraft` in `src/extensions/` (replaces `calagoapi-version-changer` and `calagoapi-hungerbridge`) |
| Tutorials | 15 tutorials in three tracks, `docs/tutorials/`; examples in `examples/extensions/` and `examples/minecraft/` |
| Offline test suite | Done: core + extension system + `calagoapi-minecraft` + examples, `pytest` (see `PLAN.md` for the last run) |
| Licence metadata | Fixed: GPL-3.0, matches `LICENSE` |
| Tested against a real panel | **Not yet** |
| Git | **Not committed**, index was already in an odd state (see below) |
| Release safety | **`version.yaml` has `run: true`** (now `1.0-dev.2`), and so do both extension `version.yaml` files, so a push to `main` publishes all three packages to PyPI once tests pass |

## Goal and constraints

- Build a Calagopus-native Python SDK, not a Pterodactyl wrapper and not a re-export of the generated client.
- Match HungerLib's style: single-quoted strings, camelCase methods, snake_case variables and attributes, light typing, simple code.
- HungerLib was used as reference only and was never modified.
- `api_generated/` and `openapi.json` were used as the source of endpoint and model information. The generated client is **not imported** anywhere.

## Architecture

```
src/calagoapi/
├── panel.py      Panel: entry point (servers, account, admin, auth, api)
├── api/          the only code that builds URLs (Client + one module per area)
├── servers/      Server, ServerManager, ServerGroup, AdminServer   (MinecraftServer: calagoapi-minecraft)
├── console/      Console, ConsoleEvent: live console over the daemon websocket
├── aio/          AsyncPanel, AsyncServer, AsyncWrapper, AsyncConsole
├── files/  backups/  databases/  schedules/  users/  network/  tunnels/  nodes/  account/  admin/
└── utils/        Model, Page, AdminResource, exceptions, convert, wait helpers
```

Key conventions:

- High-level objects call `panel.api.<module>`. API modules return plain data and unwrap response envelopes.
- Objects keep the raw panel data in `.data` (`get()`, `obj['key']`, `toDict()`).
- Any method that takes an id also takes the object (`idOf()`).
- Optional arguments left as `None` are not sent.
- List methods fetch every page unless `page=` is given, and return a `Page` (a list with pagination info).
- Free-text URL segments are encoded with `segment()`.

## Decisions made

| Decision | Choice | Reason |
| --- | --- | --- |
| Package location | `src/calagoapi/` (old HungerLib copies in `src/` removed) | needed for `from calagoapi import Panel` |
| `Panel` signature | `Panel(url, api_key, name=None, timeout=10, verify=True, max_retries=3)` | `name` made optional |
| Return values | objects, dicts or `None`; errors raise typed exceptions | instead of HungerLib's raw responses / `(status, text)` |
| `getStatus()` | power state (`running`, `offline`, ...), same as HungerLib | `getInstallStatus()` covers install state |
| Game support | core is game-agnostic; `MinecraftServer(Server)` lives in `calagoapi-minecraft` (2.0) | enforced by `tests/test_architecture.py` |
| HungerBridge | used only through HungerBridgePy (`server.bridge`), never re-implemented | HungerBridgePy is the source of truth for the protocol |
| `sendCommand()` / `streamConsole()` on Minecraft | through HungerBridge (output, SSE log stream); no silent fallback to the panel | `sendPanelCommand()` / `server.console` for the panel route |
| `getRAM()`, `getCPU()`, `stop()` | stay the panel's; JVM data is additive (`getMemoryInfo()`, ...) | matches what the panel shows and works without the plugin |
| Version changer | `server.versions` in `calagoapi-minecraft` (2.0); 1.x shims removed | one package per game |
| Extension system | class patching, entry point group `calagoapi`, explicit `enable()` | see `PLAN.md` for the full design and alternatives |
| Licence | **GPL-3.0** (chosen by the user) | the `LICENSE` file is the legal text |
| Async design | wrapper running the sync client in worker threads; native asyncio only for the console | one source of truth; new methods are async automatically |
| Retries | 429 on any method; connection errors and 502/503/504 on GET only | writes (power actions, backups) are never sent twice |

## Coverage

- Every client, admin, auth and public endpoint in `openapi.json` is wrapped, except three intentional exclusions:
  - `GET /api/admin/extensions/dev.0x7d8.minecraftversionchanger/2038` (undocumented)
  - `GET /api/admin/extensions/dev.0x7d8.subdomainmanager/2038` (undocumented)
  - `GET /api/auth/oauth/redirect/{oauth_provider}` (browser redirect; the SDK builds the URL)
- `/api/remote/*` (daemon-to-panel) is intentionally not wrapped.
- The generator skipped 29 endpoints (e.g. `files/list`, `files/write`, schedule create/update); they were implemented from `openapi.json`.

## Verification

- **Contract tests** (`tests/test_contract.py`): a fake panel built from `openapi.json` answers every request and validates method, path, query parameters and JSON bodies (recursively). Over 1,000 SDK methods are called. The suite also fails if the spec has an endpoint the SDK never calls.
- **Scenarios** (`tests/test_scenarios.py`): nine realistic workflows with assertions.
- **Console** (`tests/test_console.py`): sync and async console against a local fake daemon (auth, token renewal, logs, commands, stats, reconnects, errors).
- **Resilience** (`tests/test_resilience.py`): retries, context managers, `AsyncPanel`.
- Docs check: every method used in a doc example exists.
- Wheel builds and imports.

Run with:

```bash
pip install -e .[dev]
pytest
```

After a Calagopus update: replace `openapi.json`, run `pytest`, add whatever it lists.

## Bugs found and fixed during verification

- `duplicate()` was offered on admin objects whose endpoint does not exist.
- `refresh()` called non-existent single-item endpoints (subdomain domains, egg variables).
- `setName()`/`setDescription()` sent fields that announcements, database hosts and domains do not have.
- Free-text URL segments were not encoded.
- An import cycle between `servers/` and `admin/` (base classes moved to `utils/resource.py`).
- Schedule builders were inconsistent about `output_into` (now accepts a name or `variable()`).
- The console read the line index instead of a default value (crashed on every line).
- websockets 17 deprecated the way the sync connection was opened.

## Assumptions to confirm on a live panel

1. Auth header is `Authorization: Bearer <key>` (the spec only names the header; the generated client also uses Bearer).
2. File uploads to the daemon's signed URL use a multipart field `files` plus a `directory` query parameter (Pterodactyl Wings behaviour).
3. `ServerStatus` values (`installing`, `install_failed`, `reinstall_failed`, `restoring_backup`) are missing from the spec; conventional names were used.
4. The console protocol was taken from the Calagopus Wings source code, not tested against a running daemon.

## Spec quirks found

- Dangling `$ref`s in `openapi.json` (e.g. `ServerStatus`, `ApiEggConfiguration`).
- Some generated endpoint modules end in `_test.py`; pytest is limited to `tests/` and `src/extensions/` (`[tool.pytest.ini_options]`).

## Open items

1. **Prevent an accidental release**: set `run: false` in `version.yaml` until a live test passes.
2. **Live smoke test** against a real panel (read-only by default) to confirm the assumptions above.
3. **Git**: the CalagoAPI index had every file staged as deleted before work started. Suggested fix: `git reset`, then commit the new layout on a branch.
4. ~~**CI**: run `pytest` on every push and pull request, and make the release job depend on it.~~
   Done: `.github/workflows/tests.yml`, called by `release.yml` before publishing.
5. **PyPI trusted publishing** for `calagoapi-minecraft` (repository `HungerNet/CalagoAPI`,
   workflow `release.yml`) and for `hungerbridge` (HungerBridgePy) before their first release.
   `calagoapi-minecraft` needs `hungerbridge>=1.0.dev2` on PyPI to be installable.
6. **HungerBridge checks**: the Gradle change that names jars `HungerBridge-<loader>-<mc>-<version>.jar`
   (HungerBridge `build.gradle`) has not been built here (no JDK); build one target and check the
   name. `createBridgeToken()` assumes the console line `... Retrieve it at: /pickup/<id>?passkey=<hex>`
   (matches `CommonCommandHandler`). The default bridge URL (server address + 1913) only works when
   HungerBridge's `bind-address` is not `127.0.0.1`.
8. **Old packages**: `calagoapi-hungerbridge`, `calagoapi-version-changer`, `docs/learning/` and the old
   first-party example were moved to `../_removed-in-calagoapi-2.0/` (they were untracked, so not in git);
   delete that folder after review.
7. **Subdomain Manager** is the next candidate for an extension (`calagoapi-subdomains`).

## Dependencies

- Runtime: `requests`, `websockets>=13`
- Dev: `pytest`
- Python 3.9+

## Where things are

| What | Where |
| --- | --- |
| User docs | `README.md`, `docs/` |
| Contributor docs | `docs/architecture.md` |
| Changelog | `version.yaml` (Dev 1, Dev 2) |
| Tests | `tests/` |
| API reference material | `api_generated/`, `openapi.json` |
