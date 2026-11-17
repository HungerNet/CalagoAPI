# 06 · Using extensions

This builds on track 1: you know `Panel`, `Server` and the managers.

## What you will build

A script that installs and uses an extension package: notes attached to servers,
kept in a local file. The package is the example that ships with CalagoAPI,
`calagoapi-server-notes`.

## Step 1: install the package

```bash
pip install -e examples/extensions/packaged_extension     # from a CalagoAPI checkout
```

Extensions are ordinary packages. Installing `calagoapi` never installs any of them, and
installing one changes nothing until you enable it.

## Step 2: enable it

```python
from calagoapi.extensions import enable

enable('server_notes', config={'path': 'notes.json'})
```

You enable by **id**, not by importing. CalagoAPI finds the package through its entry
point. `enable()` is process-wide: call it once at startup.

## Step 3: use what it added

```python
server = panel.servers.getServer('abc123')
server.notes.add('Upgrade on Friday')        # a service: server.notes
print(server.notes.list())
print(server.lastNote)                       # a property
```

## Complete program

```python
from calagoapi import Panel
from calagoapi.extensions import enable, getExtension, isEnabled, registry

enable('server_notes', config={'path': 'notes.json'})

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    for server in panel.servers.getServers():
        if server.getStatus() == 'offline':
            server.notes.add('found offline by the nightly check')
        print(f'{server.name}: {len(server.notes.list())} note(s), last: {server.lastNote}')

print(f'enabled: {isEnabled("server_notes")}, config: {dict(getExtension("server_notes").config)}')
print(registry.describe())
```

## Things to try

```python
enable('server_notes')                                 # again, no arguments: a no-op
enable('server_notes', config={'path': 'other.json'})  # ConfigurationError: already enabled differently
enable('server_notes', config={'pth': 'x.json'})       # (fresh process) ConfigurationError: unknown key 'pth'
enable('server_note')                                  # ExtensionNotFoundError: Did you mean 'server_notes'?
```

## How it works

```
pip install ──► entry point "calagoapi": server_notes = calagoapi_server_notes.extension:ServerNotesExtension
enable('server_notes')
   ├── load the entry point named server_notes (metadata only until now)
   ├── merge config with default_config, validateConfig()
   ├── check every member name for conflicts
   └── patch the Server CLASS: Server.notes, Server.lastNote
         └── every existing and future Server (and subclass) has them
```

- Extensions patch **classes**, never single objects, so the order of `enable()` and
  `getServer()` does not matter.
- **Modes:** in `direct` mode, methods and properties sit on the object
  (`server.lastNote`). In `namespace` mode they go under one attribute named after the
  extension (`server.server_notes.lastNote`). Services such as `server.notes` stay where
  they are in both modes. Choose the mode with `enable(..., mode='namespace')`.
- Nothing is ever silently overridden. A name that is taken raises
  `ExtensionConflictError` naming both owners.
- Game support is delivered the same way: `enable('minecraft')` adds `panel.minecraft`
  (track 3).

## Next

[07 · Your first extension](07-your-first-extension.md): write one.
