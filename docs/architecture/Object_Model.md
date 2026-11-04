# Object Model

This page describes the public object ownership model for contributors. New
users should begin with the [tutorial track](../tutorials/00_Introduction.md).

## Hierarchy

```text
Panel
├── servers: ServerManager
│   └── GenericServer / MinecraftServer
│       ├── files: FileManager
│       ├── backups: BackupManager
│       ├── databases: DatabaseManager
│       ├── schedules: ScheduleManager
│       ├── users: SubuserManager
│       ├── network: NetworkManager
│       ├── tunnel: TunnelManager
│       └── console: Console
├── account: Account
├── auth: Auth
├── admin: Admin
└── api: API
```

`Panel` is the connection and lifetime boundary. It creates the HTTP client,
the API modules, and top-level managers. A server manager creates server
objects; a server owns its feature managers. Resource objects such as `File`,
`Backup`, `Database`, and `Schedule` keep their parent server so actions can
reach the correct API namespace.

## Models and managers

Models keep the raw response in `.data`, expose stable getters and actions, and
retain the original payload through `get()`, item access, and `toDict()`. A
manager scopes retrieval and creation to its parent object. API methods return
plain data; manager methods wrap it into the public object type.

Methods that accept identifiers generally accept the corresponding object too;
`idOf()` centralizes that conversion. List methods return `Page` objects and,
unless `page=` is supplied, retrieve all pages.

## Extension points

SDK extensions attach methods, properties, and service objects to classes.
They patch classes rather than individual instances, so existing and future
objects share the same enabled API. For ownership and conflict rules see
[Extensions architecture](Extensions_Architecture.md).

## Related internals

- [API layer](Api_Layer.md)
- [Async architecture](Async_Architecture.md)
- [Architecture overview and tests](Architecture.md)