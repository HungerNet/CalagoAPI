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
from calagoapi.extensions import enable

enable('version_changer')
server = panel.servers.getMinecraftServer('abc123')
builds = server.getBuilds('PAPER', '1.21.1', page=1, per_page=5)
print(server.installedVersion)
```

## Build selection and install

Use `getVersionTypes()` to discover available server types, then
`getVersions(type)` and `getBuilds(type, version)` to choose a build. Pass a
build object to `installVersion()`. `truncate_directory=True` requests a clean
install and may delete server files; the default keeps them. Consider making a
backup first and waiting for it to complete.

The extension also provides `getInstalledVersion()`, `isUpToDate()`, and
`updateVersion()`. Admin settings are available through
`panel.admin.extensions` with an admin API key.

## Exercise

Enable the extension, read the installed version, and list one page of Paper
builds for a version you select. Do not install a build in an unattended
exercise.

Hint: `getBuilds()` accepts `page` and `per_page`.

## Answer

```python
from calagoapi.extensions import enable

enable('version_changer')
server = panel.servers.getMinecraftServer(server_id)
print('installed:', server.getInstalledVersion())
for build in server.getBuilds('PAPER', '1.21.1', page=1, per_page=5):
    print(build)
```

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