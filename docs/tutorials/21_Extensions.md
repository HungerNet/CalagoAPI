# Extensions

## What You Will Learn

- Enable optional SDK extensions
- Distinguish methods, properties, and services
- Understand direct and namespace modes

## Prerequisites

[20 AsyncPanel](20_AsyncPanel.md). Core server, file, backup, and schedule
workflows should already be familiar.

## Estimated Time

25 minutes

## Concepts Introduced

- SDK extension
- `enable()`
- Method, property, and service members
- Process-wide extension activation

## Concept Explanation

An SDK extension is an installed Python package that adds features to
CalagoAPI objects. Enabling one is process-wide: existing and future instances
of a patched class gain its members. An extension is different from a
Calagopus panel extension, which is managed by `panel.admin.extensions`.

## API Explanation

`calagoapi.extensions.enable(id, mode=None, config=None)` activates a package.
Methods look like `server.installVersion(...)`, properties like
`server.installedVersion`, and services like `server.hungerbridge.players()`.
Extensions may use direct or namespace mode; services are already namespaces.

## Guided Example

```python
from calagoapi.extensions import enable

enable('version_changer')
server = panel.servers.getMinecraftServer(server_id)
print(server.getInstalledVersion())
```

## Exercise

Install and enable the version changer extension, then query the current
installed version. Do not install or update a build.

Hint: read the extension's install guide first; the panel-side extension is
also required.

## Answer

```python
from calagoapi.extensions import enable

enable('version_changer')
server = panel.servers.getMinecraftServer(server_id)
print(server.getInstalledVersion())
```

## Common Mistakes

- Importing the extension package and assuming that enables it. Call `enable()`.
- Enabling extensions inside a request loop or with different configurations.
- Confusing Python SDK extensions with extensions installed on the panel.
- Assuming an optional feature is available in core without the extension.

## What You Learned

- Extensions enrich the established Panel -> manager -> server model.
- `enable()` activates extensions once for the process.
- Extension member type and mode determine how code is accessed.

## Continue Learning

Next: [22 Admin API](22_Admin_API.md)

## Navigation

Previous: [20 AsyncPanel](20_AsyncPanel.md)
Next: [22 Admin API](22_Admin_API.md)
Reference Docs: [Extensions overview](../extensions/01_Extensions_Overview.md), [Minecraft](../reference/minecraft.md)
Related Examples: [extension answer](../../examples/tutorials/21_extensions/answer.py)