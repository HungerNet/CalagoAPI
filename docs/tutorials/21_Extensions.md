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

## Build a Version Inspection Script

Install the optional package separately from core CalagoAPI. The panel-side
Minecraft Version Changer must also be installed. Enable the SDK extension once
near application startup, before using its methods:

```python
from calagoapi.extensions import enable

enable('version_changer')
```

Then use the familiar Minecraft server manager and read the installed version.
This script is intentionally read-only; version installation is a separate,
state-changing operation with its own backup and restart considerations:

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
	server = panel.servers.getMinecraftServer(os.environ['SERVER_ID'])
	print(server.getInstalledVersion())
	print('up to date:', server.isUpToDate())
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
Related Examples: Code examples are embedded in this walkthrough.