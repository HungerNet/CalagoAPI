# Live console

`server.console` connects straight to the node daemon over a websocket, so
console output arrives the moment it is printed. Expiring tokens are renewed
automatically.

For one-off commands you don't need it: `server.sendCommand()` and
`server.getLogs()` work over plain HTTP. Use the console when you want to
**react** to output.

## Stream lines

```python
for line in server.streamConsole():
    print(line)
```

`streamConsole(history=True, timeout=None)` starts with the recent lines the
daemon still has, then yields new lines forever. Pass `timeout=` (seconds) to
stop when the console goes quiet.

## Send a command and wait for the answer

```python
with server.console as console:
    console.sendCommand('save-all')
    console.waitFor('Saved the game', timeout=30)
```

`waitFor()` returns the matching line, or raises `WaitTimeoutError`.

## Callbacks in the background

```python
server.onConsoleLine(print)                       # starts listening in a background thread

server.console.onStatus(lambda state: print('now', state))
server.console.onStats(lambda usage: print(usage['cpu_absolute']))
server.console.on('backup completed', lambda event: print('backup done', event.getArgs()))
server.console.on('*', lambda event: print(event))   # every event

...
server.console.stop()
```

`listen()` reconnects with backoff (1s, 2s, 4s, ... 30s) if the connection
drops. Exceptions raised by your callbacks are logged (logger
`calagoapi.console`) and do not stop the listener.

To block instead of using a thread:

```python
server.console.onConsoleLine(handle)
server.console.listen(background=False)   # runs until stop() is called from a callback
```

## Example: chat relay

```python
def relay(line):
    if '<' in line and '>' in line:   # "<Steve> hello"
        post_to_discord(line)

server.onConsoleLine(relay)
```

## Example: wait for a player

```python
with server.console as console:
    line = console.waitFor('Steve joined the game', timeout=600)
    console.sendCommand('title Steve title {"text":"Welcome back!"}')
```

## Reference

| Method | Description |
| --- | --- |
| `connect(timeout=10)`, `close()`, `isConnected()` | connection, also `with server.console as console:` |
| `sendCommand(command)` | run a console command |
| `setState(action)` | `start`, `restart`, `stop` or `kill` |
| `requestLogs()`, `requestStats()`, `requestStatus()` | ask the daemon to send logs, stats or status now |
| `lines(history=True, timeout=None)` | generator of console lines |
| `events(timeout=None)` | generator of every `ConsoleEvent` |
| `waitFor(text, timeout=60)` | block until a line contains `text` |
| `on(event, callback)`, `onConsoleLine`, `onStatus`, `onStats` | register callbacks |
| `listen(background=True, history=False, reconnect=True)`, `stop()` | run callbacks |
| `getPermissions()` | console permissions granted by the daemon |

`ConsoleEvent` has `getEvent()`, `getArgs()`, `getArg(index=0, default=None)`
and `getData()` (JSON-decoded argument, used for `stats`).

Events you can listen for include `console output`, `status`, `stats`,
`install output`, `install started`, `install completed`, `daemon message`,
`backup started`, `backup completed`, `backup restore completed`,
`schedule started`, `schedule completed`, `transfer status` and
`image pull progress`.

## Errors

- `ConsoleError`: the daemon can't be reached, the token was refused, or you
  sent something while disconnected.
- `WaitTimeoutError`: `waitFor()` timed out.
- `InvalidActionError`: unknown power action in `setState()`.

`Panel.close()` (or leaving `with Panel(...)`) closes every open console.

## Async

See [Async](async.md#live-console).
