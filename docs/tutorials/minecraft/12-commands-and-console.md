# 12 · Commands and console

This builds on [11](11-minecraft-setup.md): a `MinecraftServer` with a working bridge.

## What you will build

A command runner that prints what each command answered, and a join watcher that
follows the console and reacts to players joining.
Code: [examples/minecraft/02_commands_and_console.py](../../../examples/minecraft/02_commands_and_console.py).

## Step 1: commands with output

```python
print(server.sendCommand('list'))
# There are 2 of a max of 20 players online: Steve, Alex
```

On a plain `Server`, `sendCommand()` sends text through the panel and returns `None`
(tutorial 02). On a `MinecraftServer` it runs through HungerBridge and returns what the
command printed: it is HungerBridgePy's `runCommand()`.

| Call | Channel | Returns |
| --- | --- | --- |
| `server.sendCommand('list')` | HungerBridge | the output text |
| `server.sendCommand('save-all', silent=True)` | HungerBridge | `None` (output not captured) |
| `server.sendCommand('say hi', showConsole=True)` | HungerBridge | output, also echoed to the console |
| `server.sendCommands(['a', 'b'])` | HungerBridge | a list of outputs |
| `server.sendPanelCommand('list')` | panel | `None`, works without HungerBridge |

The chat and moderation helpers are built on `sendCommand()`: `say()`, `tellraw()`,
`kick()`, `ban()`, `pardon()`, `op()`, `deop()`, `whitelistAdd()`, `whitelistRemove()`,
`saveAll()`. `broadcast(message, prefix=None)` is HungerBridgePy's `tellraw @a` broadcast.

## Step 2: the console stream

```python
for line in server.streamConsole(history=20, timeout=60):
    print(line)              # '[12:00:05 INFO]: Steve joined the game'
```

| Argument | Meaning |
| --- | --- |
| `history` | replay the last N lines first (≤ 200; `True` = 200; default 0) |
| `timeout` | stop after that many seconds without a line (default: never) |
| `reconnect` | reconnect and replay only missed lines (default: the `stream_reconnect` config, `True`) |
| `sanitize` | strip colours and unescape line breaks (default `True`) |

This is HungerBridgePy's `streamLogs()` over HungerBridge's SSE endpoint. Every line is
`[HH:mm:ss LEVEL]: message`, and stack traces stay attached to their line. For callbacks
in a background thread use `onConsoleLine()`:

```python
stream = server.onConsoleLine(print, history=10)
...
stream.disconnect()
```

## Complete program

```python
from calagoapi import Panel
from calagoapi.extensions import enable

enable('minecraft', config={'bridge_token': 'calagoapi:9f2c...'})

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

    print(f'list -> {server.sendCommand("list")}')
    server.say('Hello from CalagoAPI')
    server.sendCommand('save-all', silent=True)

    joined = []
    for line in server.streamConsole(history=5, timeout=10):
        print(f'console | {line}')
        if 'joined the game' in line:
            joined.append(line)
    print(f'{len(joined)} join message(s) seen')
```

## How it works

- `MinecraftServer.sendCommand(command, *, silent=False, showConsole=False)` keeps the
  base call `sendCommand(command)` working. The extra options are keyword-only and the
  return value widens from `None` to the output, so code written for `Server` runs on a
  `MinecraftServer` unchanged.
- HungerBridge runs the command as the console on the server thread (Folia: the
  global region) and waits up to 5 s for it, so output arrives in the same call. That
  needs no RCON.
- `streamConsole()` fails **when called** if no token is configured, not at the first line.
  A revoked token or a missing permission ends the stream with `HungerBridgeAuthError` /
  `HungerBridgeForbidden` and is not retried. Network drops are retried with back-off
  when `reconnect` is on.
- When the bridge is down, the daemon console still works: `server.console` (tutorial 03)
  and `sendPanelCommand()`.

## Next

[13 · Monitoring](13-monitoring.md).
