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
command answered: it is HungerBridgePy's `runCommand()`.

The output is captured directly by HungerBridge and is **not** printed on the server
console, so a bot polling `list` every minute does not flood the console. Ask for it when
people watching the console should see it:

| Call | Channel | Returns | On the server console |
| --- | --- | --- | --- |
| `server.sendCommand('list')` | HungerBridge | the output text | nothing |
| `server.sendCommand('save-all', show_console=True)` | HungerBridge | the output text | the output |
| `server.sendCommands(['a', 'b'])` | HungerBridge | a list of outputs | nothing |
| `server.sendPanelCommand('list')` | panel | `None` | the output (it is typed into the console) |

Things the game logs by itself still appear: `say hi` is a chat broadcast, so the console
shows `[Server] hi` either way.

The chat and moderation helpers are built on `sendCommand()`: `say()`, `tellraw()`,
`kick()`, `ban()`, `pardon()`, `op()`, `deop()`, `whitelistAdd()`, `whitelistRemove()`,
`saveAll()`. For a `tellraw @a` broadcast use `server.bridge.broadcast(message, prefix)`.

## Step 2: the console stream

```python
for line in server.streamConsole(history=20, timeout=60):
    print(line)              # '[12:00:05] [Server thread/INFO]: Steve joined the game'
```

| Argument | Meaning |
| --- | --- |
| `history` | replay the last N lines first (`True` = all HungerBridge keeps, 1000; default 0) |
| `timeout` | stop after that many seconds without a line (default: never) |
| `reconnect` | reconnect when the stream drops (default: the `stream_reconnect` config, `True`) |

Lines are plain text in HungerBridge's format, the same on every loader:
`[HH:mm:ss] [thread/LEVEL]: [logger] message` (the logger part is left out for
Minecraft's own messages); stack traces stay attached to their line. For callbacks in a
background thread use `onConsoleLine()`:

```python
stream = server.onConsoleLine(print, history=10)
...
stream.disconnect()
```

Need the fields rather than the text? `server.bridge.streamLogs()` yields
`hungerbridge.LogEvent` objects (`level`, `thread`, `logger`, `message`, `time`, `line`);
tutorial [16](16-logging-from-your-bot.md) uses them.

## Complete program

```python
from calagoapi import Panel
from calagoapi.extensions import enable

enable('minecraft', config={'bridge_token_id': 'calagoapi', 'bridge_token_secret': '9f2c...'})

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

    print(f'list -> {server.sendCommand("list")}')
    server.say('Hello from CalagoAPI')
    server.sendCommand('save-all', show_console=True)

    joined = []
    for line in server.streamConsole(history=5, timeout=10):
        print(f'console | {line}')
        if 'joined the game' in line:
            joined.append(line)
    print(f'{len(joined)} join message(s) seen')
```

## How it works

- `MinecraftServer.sendCommand(command, *, show_console=False)` keeps the base call
  `sendCommand(command)` working; the option is keyword-only and the return value widens
  from `None` to the output, so code written for `Server` runs on a `MinecraftServer`.
- HungerBridge runs the command with console permissions on the server thread (Folia: the
  global region) and waits up to 5 s for it, so the output arrives in the same call, without
  RCON. It captures the command's feedback from a dedicated command source; that is why the
  console stays quiet. A command the server does not run in time raises
  `HungerBridgeError` with `code == 'command_timeout'`.
- `streamConsole()` fails **when called** if no token is configured, not at the first line.
  A revoked token or a missing permission ends the stream with `HungerBridgeAuthError` /
  `HungerBridgeForbidden` and is not retried. After a network drop the stream reconnects and
  HungerBridge replays exactly the lines that were missed, so none are lost or repeated.
- When the bridge is down, the daemon console still works: `server.console` (tutorial 03)
  and `sendPanelCommand()`.

## Next

[13 · Monitoring](13-monitoring.md).
