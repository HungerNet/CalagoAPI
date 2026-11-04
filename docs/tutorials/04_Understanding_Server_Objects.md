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

## Build a Server-Centered Script

Start with the configured connection and retrieve one server. This is the point
where the script moves from the panel-wide manager to one server's object tree:

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])
  print(server.getName(), server.getNodeName())
```

From here, choose the manager that owns the resource you need. `server.files`
is scoped to this server; its `listFiles()` method returns `File` resource
objects that retain the parent server context:

```python
  for file in server.files.listFiles('/'):
    print(file.getName(), file.isDirectory())
```

## Complete Script

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])
  print('server:', server.getName(), server.getUUID())
  for file in server.files.listFiles('/'):
    print(file.getName(), 'directory' if file.isDirectory() else 'file')
```

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
Related Examples: Code examples are embedded in this walkthrough.