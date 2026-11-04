# Understanding Server Objects

## What You Will Learn

- What a server object represents
- How managers hang from the server
- Why resource objects belong to a particular server

## Prerequisites

[03 Finding Servers](03_Finding_Servers.md).

## Estimated Time

15 minutes

## Concepts Introduced

- `GenericServer`
- Child managers
- Resource objects
- Cached details and raw data

## Concept Explanation

A `GenericServer` represents one server on the panel, not the server process
itself. It combines server-wide actions and state with managers for resources.
For example, `server.files` is the file manager for that server, while
`server.backups` manages its backups. A returned `File` or `Backup` stays
associated with the same server.

## API Explanation

`getServer()` fetches server details and wraps them in `GenericServer`. Getters
such as `getName()` read details; `.data` and `toDict()` expose the underlying
panel data. Child managers include `files`, `backups`, `databases`, `schedules`,
`users`, `network`, `tunnel`, and `console`.

## Guided Example

```python
server = panel.servers.getServer(server_id)
print(server.getName(), server.getNodeName())
print(server.files)       # manager scoped to this server
print(server.backups)
print(server.get('uuid')) # raw detail field
```

## Exercise

Retrieve a server and print its name, UUID, file manager type, and backup
manager type. Explain why `server.files` is not a panel-wide file manager.

Hint: `type(value).__name__` prints the class name.

## Answer

```python
server = panel.servers.getServer(server_id)
print(server.getName(), server.getUUID())
print(type(server.files).__name__)
print(type(server.backups).__name__)
```

Each manager stores its parent server, so operations are automatically scoped
to that server.

## Common Mistakes

- Confusing `GenericServer` with the manager that finds it. The manager is
  `panel.servers`; the result is one server object.
- Treating a file or backup as global. It belongs to one server's manager.
- Depending on undocumented raw fields when a public getter exists.

## What You Learned

- Server objects are the center of the per-server API.
- Resource managers are scoped beneath their server.
- Models provide getters and preserve raw response data.

## Continue Learning

Next: [05 Reading Status and Resources](05_Reading_Status_And_Resources.md)

## Navigation

Previous: [03 Finding Servers](03_Finding_Servers.md)
Next: [05 Reading Status and Resources](05_Reading_Status_And_Resources.md)
Reference Docs: [Servers](../reference/servers.md), [Object model](../architecture/Object_Model.md)
Related Examples: [server object answer](../../examples/tutorials/04_understanding_servers/answer.py)