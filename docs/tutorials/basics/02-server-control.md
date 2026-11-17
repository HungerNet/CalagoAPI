# 02 · Server control

This builds on [01](01-first-script.md): you can connect and get `Server` objects.

## What you will build

A safe-restart script: it warns the server, restarts it, waits until it is running
again and reports how long that took. If the server does not come back, it says so
instead of hanging.

## Step 1: get one server

```python
server = panel.servers.getServer('abc123')          # UUID or short id
# or by name: panel.servers.getServerByName('Survival')  (None if there is none)
```

## Step 2: power actions

```python
server.start()
server.stop()          # graceful stop (the panel's power action)
server.restart()
server.kill()          # immediate
server.powerAction('restart')   # same as restart(); unknown actions raise InvalidActionError
```

Power actions return as soon as the panel accepted them. The server then goes
through `starting` / `stopping` before it reaches `running` / `offline`.

## Step 3: wait for a state

```python
if server.waitForOnline(timeout=180):
    print('back online')
else:
    print('still not running after 3 minutes')
```

`waitForOnline()`, `waitForOffline()` and `waitForState(state)` poll `getStatus()`
every `interval` seconds and return `False` on timeout. They never raise for a slow server.

## Complete program

```python
import time

from calagoapi import Panel

SERVER = 'abc123'

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.servers.getServer(SERVER)

    if not server.isOnline():
        print(f'{server.name} is {server.getStatus()}, starting it instead')
        server.start()
    else:
        server.sendCommand('broadcast Restarting in 10 seconds')   # any console command of your game
        time.sleep(10)
        server.restart()

    started = time.monotonic()
    if server.waitForOnline(timeout=300, interval=3):
        print(f'{server.name} is running again after {time.monotonic() - started:.0f}s, '
              f'using {server.getRAM()} MiB of {server.getRAMLimit()} MiB')
    else:
        print(f'{server.name} did not come back within 5 minutes (state: {server.getStatus()})')
```

## How it works

- `sendCommand()` on a plain `Server` sends the text to the server's console through
  the panel and returns `None`. What the game prints shows up in the console
  ([03](03-live-console.md)). Game extensions can override `sendCommand()`:
  `calagoapi-minecraft` returns the command's output instead ([12](../minecraft/12-commands-and-console.md)).
- `isOnline()`, `isOffline()`, `isStarting()`, `isStopping()` all call `getStatus()`, which
  is always fresh. `isInstalled()`, `isSuspended()` and `isTransferring()` read the
  server details instead.
- The panel retries rate-limited requests and safe reads automatically
  (`Panel(max_retries=3)`). Power actions are **never** retried, so a restart is never
  sent twice.

## Next

[03 · Live console](03-live-console.md): read what the server prints, as it prints it.
