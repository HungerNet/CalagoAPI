# CalagoAPI documentation

## Tutorials

Start here if you are new: [tutorials/](tutorials/README.md), 15 tutorials in three tracks.

| Track | Tutorials |
| --- | --- |
| 1. The core SDK (any game) | [01 First script](tutorials/basics/01-first-script.md) · [02 Server control](tutorials/basics/02-server-control.md) · [03 Live console](tutorials/basics/03-live-console.md) · [04 Files and backups](tutorials/basics/04-files-and-backups.md) · [05 Going async](tutorials/basics/05-going-async.md) |
| 2. Extending CalagoAPI | [06 Using extensions](tutorials/extensions/06-using-extensions.md) · [07 Your first extension](tutorials/extensions/07-your-first-extension.md) · [08 Services and namespaces](tutorials/extensions/08-services-and-namespaces.md) · [09 Configuration and dependencies](tutorials/extensions/09-configuration-and-dependencies.md) · [10 Packaging and publishing](tutorials/extensions/10-packaging-and-publishing.md) |
| 3. Minecraft (calagoapi-minecraft) | [11 Setup](tutorials/minecraft/11-minecraft-setup.md) · [12 Commands and console](tutorials/minecraft/12-commands-and-console.md) · [13 Monitoring](tutorials/minecraft/13-monitoring.md) · [14 Installing HungerBridge](tutorials/minecraft/14-installing-hungerbridge.md) · [15 Community bot](tutorials/minecraft/15-community-bot.md) · [16 Logging from your bot](tutorials/minecraft/16-logging-from-your-bot.md) |

## Reference guides (core SDK)

1. [Getting started](getting-started.md): install, API keys, connecting, the object model
2. [Servers](servers.md): status, resources, power, console commands, settings, startup, groups
3. [Live console](console.md): stream output, wait for lines, callbacks
4. [Files](files.md): browse, read, write, upload, download, archives, search
5. [Backups](backups.md): create, restore, download, lock, backup groups
6. [Databases](databases.md): hosted databases, database instances, the database explorer
7. [Schedules](schedules.md): triggers, conditions, actions and variables
8. [Network, subusers and tunnels](network.md)
9. [Account and authentication](account.md): profile, API keys, SSH keys, 2FA, public endpoints
10. [Administration](admin.md): users, servers, nodes, eggs, settings and everything else
11. [Async](async.md): AsyncPanel, the async console, async extension types
12. [Errors, retries, pagination and utilities](errors-and-utilities.md)
13. [Extensions](extensions.md): using and writing SDK extensions

## Extension packages

- [calagoapi-minecraft](../src/extensions/calagoapi-minecraft/README.md): `MinecraftServer`,
  HungerBridge (via HungerBridgePy), bridge installs from Modrinth

## Migration and design

- [Migrating calagoapi-minecraft 1.x to 2.0](migrating-minecraft-2.0.md)

- [Migrating to 2.0](migrating-to-2.0.md): every rename and move of the 2.0 rewrite
- [Migrating from HungerLib](migrating-from-hungerlib.md)
- [Architecture](architecture.md): for contributors, including the test suite
- [Design: the extension system](design/extension-system.md); the 2.0 rewrite: [PLAN.md](../PLAN.md)

Runnable examples: [examples/](../examples/README.md).

Every class and method also has a docstring, so `help()` works in a Python shell:

```python
help(panel.servers)
help(server.files.uploadFile)
```
