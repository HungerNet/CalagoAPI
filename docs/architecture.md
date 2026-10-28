# Architecture

This page is for contributors.

## Layers

```
calagoapi/
├── panel.py          Panel: entry point, wires everything together
├── api/              the only code that knows URLs and HTTP
│   ├── client.py     Client: auth headers, JSON, errors, pagination
│   ├── servers.py    ServersAPI       /api/client/servers/...
│   ├── files.py      FilesAPI
│   ├── backups.py    BackupsAPI
│   ├── databases.py  DatabasesAPI     incl. explorer and instances
│   ├── schedules.py  SchedulesAPI
│   ├── network.py    NetworkAPI       allocations, subdomains, tunnel, firewall
│   ├── users.py      UsersAPI         subusers
│   ├── attachments.py AttachmentsAPI  server mounts and devices
│   ├── versions.py   VersionsAPI      Minecraft version changer
│   ├── account.py    AccountAPI       /api/client/account/...
│   ├── auth.py       AuthAPI          /api/auth/...
│   ├── public.py     PublicAPI        /api/settings, /api/languages, ...
│   └── admin.py      AdminAPI         /api/admin/... (ResourceAPI for CRUD collections)
├── servers/          GenericServer, MinecraftServer, ServerManager, AdminServer
├── files/            File, FileManager
├── backups/          Backup, BackupGroup, BackupManager
├── databases/        Database, DatabaseInstance, InstanceDatabase, InstanceUser, DatabaseExplorer
├── schedules/        Schedule, ScheduleStep, ScheduleManager, builders
├── users/            Subuser, SubuserManager, User, UserManager, Activity
├── network/          Allocation, Subdomain, NetworkManager
├── tunnels/          TunnelManager
├── console/          Console, ConsoleEvent: live console over the daemon websocket
├── aio/              AsyncPanel, AsyncServer, AsyncWrapper, AsyncConsole
├── nodes/            Node, NodeManager
├── account/          Account, Auth, ApiKey, SshKey, ...
├── admin/            Admin namespace, admin resources and managers
└── utils/            Model, Page, AdminResource, exceptions, convert, wait helpers
```

Rules:

1. **Only `api/` builds URLs.** High-level classes call `panel.api.<module>`.
2. API modules take and return plain Python data (dicts, lists, `Page`s of dicts).
   They unwrap the response envelope (`{'server': {...}}` becomes `{...}`).
3. High-level classes wrap that data in objects with getters, state checks
   and actions. Objects keep the raw data in `.data`.
4. Methods are camelCase, variables and attributes are snake_case, strings use
   single quotes.

## Console and async

- The live console is the one place that does not go through `api/`: it talks
  to the node daemon, not the panel. It gets its URL and token from
  `api.servers.websocket()`. The protocol is the Calagopus Wings one: JSON
  text frames `{"event": ..., "args": [...]}`, starting with `auth`.
- `aio/` does not duplicate the API. `AsyncWrapper` turns every method of any
  object into a coroutine that runs the sync method in a worker thread and
  wraps what it returns. New sync methods are therefore async automatically.
  Only the console has a native asyncio implementation (`AsyncConsole`),
  because streaming must not hold a thread per server.

## The generated client

`api_generated/` (an OpenAPI generated client) and `openapi.json` are the
reference for endpoints, parameters and models. CalagoAPI does **not** import
the generated client: it was used to write `api/`, and to verify it.

When Calagopus adds endpoints:

1. Regenerate `api_generated/` (or read `openapi.json`).
2. Add a method to the matching module in `api/`.
3. Expose it from the high-level class with a docstring and example.
4. Document it in `docs/`.

## Tests

```bash
pip install -e .[dev]
pytest
```

The suite in `tests/` runs offline against `openapi.json`:

- `contract.py` is a fake panel. It answers every request with a sample
  generated from the spec and records requests that do not match it
  (unknown endpoint, undeclared query parameter, or a JSON body that fails
  the request schema, checked recursively).
- `test_contract.py` calls every public method reachable from `Panel`
  (`exercise.py`) and fails on any mismatch. It also fails when the spec
  contains endpoints CalagoAPI never calls, so a new Calagopus release shows
  exactly what to add. Intentional gaps go in `NOT_WRAPPED`.
- `test_scenarios.py` runs realistic workflows (`scenarios.py`) with assertions.
- `test_console.py` runs the sync and async console against `daemon.py`, a
  local fake daemon speaking the Wings websocket protocol (auth, token
  renewal, logs, commands, stats, reconnects).
- `test_resilience.py` covers retries, `with` blocks and `AsyncPanel`.
- `test_units.py` covers helpers.

After a Calagopus update: replace `openapi.json`, run `pytest`, then fix
whatever it lists.

## Conventions worth knowing

- Optional arguments left as `None` are not sent, so the panel keeps its current value or default.
- List methods fetch every page unless `page=` is passed.
- Anywhere an id is expected, an object works too (`idOf()` in `utils/model.py`).
- Free-text path segments (file names, identifiers) are URL-encoded with `segment()`.
