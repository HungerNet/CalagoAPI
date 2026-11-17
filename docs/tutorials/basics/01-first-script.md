# 01 · First script

This is the starting point: you need a Calagopus panel, an API key and Python 3.9+.

## What you will build

A script that prints one line per server: name, power state, memory and uptime.

```text
Survival             running   1843.2 MiB   3h 12m
Lobby                offline        0 MiB   -
```

## Step 1: install and connect

```bash
pip install calagoapi
```

Create an API key in the panel under **Account → API Keys** with the server
permissions you need (`control.*` is enough for this tutorial).

```python
from calagoapi import Panel

panel = Panel(url='https://panel.example.com', api_key='c7sp_...')
print(f'panel reachable: {panel.ping()}, key valid: {panel.validateAPI()}')
```

`Panel` is the only object you create yourself. Everything else is reached from it.

## Step 2: list servers

```python
for server in panel.servers.getServers():
    print(server.getName())
```

`panel.servers` is a **manager**. Managers group the operations of one area and
return **objects**: here a `Page` (a list with pagination info) of `Server` objects.
List methods fetch every page unless you pass `page=`.

## Step 3: ask each server for its state

```python
for server in panel.servers.getServers():
    status = server.getStatus()                 # always fresh
    memory = server.getRAM()                    # MiB, from the cached resources
    uptime = server.getUptime(formatted=True) if status == 'running' else '-'
    print(f'{server.getName():20} {status:9} {memory:8} MiB   {uptime}')
```

## Complete program

```python
from calagoapi import Panel

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    for server in panel.servers.getServers():
        status = server.getStatus()
        memory = server.getRAM() or 0
        uptime = server.getUptime(formatted=True) if status == 'running' else '-'
        print(f'{server.getName():20} {status:9} {memory:8} MiB   {uptime}')
```

The `with` block closes the pooled HTTP connections at the end.

## How it works

```
Panel ──► panel.servers (ServerManager) ──► Server ──► server.files, server.backups, ...
  │
  └──► panel.api (one module per API area, the only code that builds URLs)
```

- **Objects keep the raw panel data** in `.data`, with getters on top:
  `server.getName()` is `server.data['name']`. `server['name']` and `server.toDict()`
  work too.
- **Details are cached** (`refreshDetails()` reloads them). **Resources** (RAM, CPU,
  disk) have their own cache: `getStatus()` refreshes it, so `getRAM()` right after it
  costs no extra request.
- **Errors are exceptions**, not return codes. A missing server raises `NotFoundError`,
  and every error is a `CalagoAPIError`.
- **`Server` is game-agnostic.** Game extensions subclass it. Track 3 covers Minecraft.

## Next

[02 · Server control](02-server-control.md): start, stop and restart servers safely.
