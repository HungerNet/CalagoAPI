# Using Version Changer

The Minecraft Version Changer is an optional Calagopus panel extension with a
matching CalagoAPI package. It belongs after the core server workflows because
installing a build changes a server's runtime.

## Install and enable

Install the SDK extension and ensure the panel-side Minecraft Version Changer
is installed by an administrator:

```bash
pip install calagoapi-version-changer
```

```python
import os
from calagoapi import Panel
from calagoapi.extensions import enable

enable('version_changer')
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getMinecraftServer(os.environ['SERVER_ID'])
    builds = server.getBuilds('PAPER', '1.21.1', page=1, per_page=5)
    print('installed:', server.getInstalledVersion())
    for build in builds:
        print(build)
```

## Build selection and install

Use `getVersionTypes()` to discover available server types, then
`getVersions(type)` and `getBuilds(type, version)` to choose a build. Pass a
build object to `installVersion()`. `truncate_directory=True` requests a clean
install and may delete server files; the default keeps them. Consider making a
backup first and waiting for it to complete.

The extension also provides `isUpToDate()` and `updateVersion()`. To install a
build, pass the selected build object to `installVersion()`. Treat that call as
a separate deployment step: review the build, create and verify a backup, and
understand that `truncate_directory=True` may remove server files. Admin
settings are available through `panel.admin.extensions` with an admin API key.

## Common Mistakes

- Installing only the Python package: the panel-side extension is also needed.
- Calling `installVersion()` without checking the selected build and file impact.
- Treating it as a core feature: enable the SDK extension once at process start.

## What You Learned

- Version lookup is separate from build installation.
- `enable()` exposes optional SDK methods on Minecraft server objects.
- Installation is a state-changing operation that deserves a backup and review.

## Navigation

Previous: [19 Minecraft servers](../tutorials/19_Minecraft_Servers.md)
Next: [21 Extensions](../tutorials/21_Extensions.md)
Reference Docs: [Minecraft servers](../reference/minecraft.md)
Related Examples: [first-party extension example](../../examples/extensions/10_first_party_extensions.py)