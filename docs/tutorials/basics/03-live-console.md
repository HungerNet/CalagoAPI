# 03 · Live console

This builds on [02](02-server-control.md): you can start servers and send commands.

## What you will build

Two small tools:

1. a **startup watcher** that starts a server and returns the moment a "ready" line
   appears in its console;
2. an **error relay** that runs in the background and forwards every error line.

## Step 1: stream lines

```python
for line in server.streamConsole(timeout=30):
    print(line)
```

`streamConsole()` opens a websocket to the node daemon (Wings) and yields every line
the server prints. `history=True` (the default) first replays the lines the daemon
still has. `timeout` ends the loop after that many seconds of silence; without it, the
loop runs forever.

## Step 2: wait for a specific line

```python
with server.console as console:
    console.sendCommand('status')
    line = console.waitFor('players online', timeout=30)
    print(f'answer: {line}')
```

`server.console` is a `Console`: the same websocket with more control (`waitFor()`,
`sendCommand()`, power actions, daemon events). Use it in a `with` block so the
connection closes.

## Step 3: callbacks in the background

```python
server.console.onConsoleLine(lambda line: print(f'console: {line}'))
server.console.onStatus(lambda state: print(f'state is now {state}'))
server.console.listen()          # background thread, reconnects automatically
...
server.console.stop()
```

## Complete program

```python
from calagoapi import Panel, WaitTimeoutError

READY = 'Server started'          # whatever your game prints when it is ready

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.servers.getServer('abc123')

    # 1. startup watcher
    with server.console as console:
        server.start()
        try:
            console.waitFor(READY, timeout=600)
            print(f'{server.name} is ready')
        except WaitTimeoutError:
            print(f'{server.name} printed no "{READY}" within 10 minutes')

    # 2. error relay, until Ctrl+C
    def relay(line):
        if 'ERROR' in line or 'Exception' in line:
            print(f'[{server.name}] {line}')       # post to a chat channel instead

    server.onConsoleLine(relay)
    try:
        input('relaying errors, press Enter to stop\n')
    finally:
        server.console.stop()
```

## How it works

```
your code ── REST ──► panel ── issues websocket URL + token ──┐
    │                                                          ▼
    └──────────── websocket (auth, send command, ...) ──► node daemon ──► server process
```

- The console is the one part of CalagoAPI that does not go through the panel's REST
  API. CalagoAPI asks the panel for credentials (`server.getWebsocket()`), then talks to
  the daemon directly, so lines arrive the moment they are printed. Expiring tokens
  are renewed automatically.
- `streamConsole()` gives you **lines**; `console.events()` gives you every daemon event
  (`status`, `stats`, `backup completed`, ...) as `ConsoleEvent` objects.
- Game extensions may stream from somewhere better: `calagoapi-minecraft`'s
  `streamConsole()` uses HungerBridge's log stream ([12](../minecraft/12-commands-and-console.md)).
  `server.console` keeps working there too.

## Next

[04 · Files and backups](04-files-and-backups.md): change configuration safely.
