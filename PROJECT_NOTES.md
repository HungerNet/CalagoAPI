# CalagoAPI: project notes

Outcomes, decisions and open items from building CalagoAPI (October 2026).

## Status at a glance

| Item | State |
| --- | --- |
| SDK (sync) | Done: `src/calagoapi/`, 65 modules |
| Live console (websocket) | Done: sync and async |
| Async API (`AsyncPanel`) | Done |
| Retries / `with` blocks | Done |
| Docs | Done: README + 15 guides in `docs/`, docstrings on all 1,250 public classes and methods |
| Offline test suite | Done: 38 tests, `pytest` |
| Licence metadata | Fixed: GPL-3.0, matches `LICENSE` |
| Tested against a real panel | **Not yet** |
| Git | **Not committed**, index was already in an odd state (see below) |
| Release safety | **`version.yaml` has `run: true`**, so a push to `main` publishes to PyPI |

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
├── servers/      GenericServer, MinecraftServer, ServerManager, ServerGroup, AdminServer
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
| HungerBridge | not ported | console streaming now comes from the Calagopus daemon |
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
- Some generated endpoint modules end in `_test.py`; pytest is limited to `tests/` (`[tool.pytest.ini_options]`).

## Open items

1. **Prevent an accidental release**: set `run: false` in `version.yaml` until a live test passes.
2. **Live smoke test** against a real panel (read-only by default) to confirm the assumptions above.
3. **Git**: the CalagoAPI index had every file staged as deleted before work started. Suggested fix: `git reset`, then commit the new layout on a branch.
4. **CI**: run `pytest` on every push and pull request, and make the release job depend on it.

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
