# CalagoAPI documentation

1. [Getting started](getting-started.md): install, API keys, connecting, the object model
2. [Servers](servers.md): status, resources, power, console commands, settings, startup, groups
3. [Live console](console.md): stream output, wait for lines, callbacks
4. [Minecraft servers](minecraft.md): console helpers, server.properties, version changer
5. [Files](files.md): browse, read, write, upload, download, archives, search
6. [Backups](backups.md): create, restore, download, lock, backup groups
7. [Databases](databases.md): hosted databases, database instances, the database explorer
8. [Schedules](schedules.md): triggers, conditions, actions and variables
9. [Network, subusers and tunnels](network.md)
10. [Account and authentication](account.md): profile, API keys, SSH keys, 2FA, public endpoints
11. [Administration](admin.md): users, servers, nodes, eggs, settings and everything else
12. [Async](async.md): AsyncPanel and the async console
13. [Errors, retries, pagination and utilities](errors-and-utilities.md)
14. [Migrating from HungerLib](migrating-from-hungerlib.md)
15. [Architecture](architecture.md): for contributors, including the test suite

Every class and method also has a docstring, so `help()` works in a Python shell:

```python
help(panel.servers)
help(server.files.uploadFile)
```
