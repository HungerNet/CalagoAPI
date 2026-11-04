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

## Extensions

Learning guides in [learning/](learning/extensions.md):

1. [Extensions](learning/extensions.md): installing, enabling, modes, configuration
2. [Creating extensions](learning/creating_extensions.md)
3. [Method extensions](learning/method_extensions.md)
4. [Property extensions](learning/property_extensions.md)
5. [Class (service) extensions](learning/class_extensions.md)
6. [Discovery](learning/discovery.md): entry points
7. [Dependencies](learning/dependencies.md)
8. [Aliases](learning/aliases.md)
9. [First-party extensions](learning/first_party_extensions.md): `version_changer`, `hungerbridge`
10. [Migrating built-in features](learning/migrating_builtin_features.md)

Runnable examples: [examples/extensions/](../examples/extensions/README.md).

Every class and method also has a docstring, so `help()` works in a Python shell:

```python
help(panel.servers)
help(server.files.uploadFile)
```
