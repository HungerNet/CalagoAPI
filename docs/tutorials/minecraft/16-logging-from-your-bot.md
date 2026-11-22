# 16 · Logging from your bot

This builds on [12](12-commands-and-console.md) (the console stream) and
[15](15-community-bot.md) (a bot next to the server).

## What you will build

A maintenance bot that writes its own, clearly attributed lines into the server log, relays
a chat-style message as plain text, and reads its own lines back from the stream.
Code: [examples/minecraft/06_bot_logging.py](../../../examples/minecraft/06_bot_logging.py).

```text
[02:00:00] [HungerBridge/INFO]: [NightlyBot] starting nightly maintenance
[02:00:04] [Backups/BACKUP]: [NightlyBot] world saved
[02:00:05] [HungerBridge/INFO]: [NightlyBot] maintenance in 5 minutes
```

## Step 1: level, thread and logger

```python
bridge = server.bridge
bridge.log('starting nightly maintenance', logger='NightlyBot')
bridge.log('world saved', level='BACKUP', thread='Backups', logger='NightlyBot')
```

| Argument | Default | Shown as |
| --- | --- | --- |
| `message` | required | the text |
| `level` | `'INFO'` | `/LEVEL]`: a built-in level or your own name (letters, digits, `_`); custom levels always show |
| `thread` | `'HungerBridge'` | `[thread/` |
| `logger` | `'HungerBridge'` | `[logger]` before the message |

The format above is what the log stream shows on every loader and what Fabric's console
prints. Paper's console uses its own layout for the same line:
`[02:00:04 BACKUP]: [NightlyBot] world saved`.

Invalid names (spaces, control characters, more than 64 characters) raise
`HungerBridgeError` with status 400, so a typo never produces a garbled console.

## Step 2: normalize relayed messages

When your bot relays text from elsewhere (a chat bridge, another server, a web hook), it
may carry Minecraft decorations. `normalize=True` asks HungerBridge to reduce it to plain
text before logging, and `log()` returns what was logged:

```python
bridge.log('System chat: maintenance in 5 minutes', normalize=True)    # 'maintenance in 5 minutes'
bridge.log('{"text":"Hello ","extra":[{"text":"world","color":"gold"}]}', normalize=True)   # 'Hello world'
```

HungerBridge flattens JSON text components, removes `§` colour codes and ANSI escapes, and
strips leading chat decorations (`System chat:`, `[System]`, `[CHAT]`, `[Not Secure]`,
`[Server]`, `[Rcon]`). It runs on the server, so every loader and every client gets the same
result.

## Step 3: read your own lines back

```python
for event in bridge.streamLogs(history=50, timeout=10):
    if event.logger == 'NightlyBot':
        print(event.level, event.thread, event.message)
```

`streamLogs()` yields `hungerbridge.LogEvent` objects: `level`, `thread`, `logger`,
`message`, `time` (epoch ms) and `line` (the text above). Filtering on `event.logger` is
exact, where matching text in a line would be guesswork. `server.streamConsole()` gives the
same lines as plain strings.

## Complete program

```python
from calagoapi import Panel
from calagoapi.extensions import enable

LOGGER = 'NightlyBot'

enable('minecraft', config={'bridge_token_id': 'calagoapi', 'bridge_token_secret': '9f2c...'})

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')
    bridge = server.bridge

    bridge.log('starting nightly maintenance', logger=LOGGER)
    bridge.log('world saved', level='BACKUP', thread='Backups', logger=LOGGER)
    relayed = bridge.log('System chat: maintenance in 5 minutes', normalize=True, logger=LOGGER)
    print(f'relayed as: {relayed!r}')

    mine = []
    for event in bridge.streamLogs(history=50, timeout=10):
        if event.logger == LOGGER:
            print(f'{event.level:<7} {event.thread:<14} {event.message}')
            mine.append(event)
        if len(mine) == 3:
            break
```

## How it works

- `log()` needs the `server.log` permission node; reading the stream needs `server.stream`.
- HungerBridge writes the line through Log4j as logger `NightlyBot` and publishes the same
  fields to its stream, so console, stream, history and replay agree.
- The stream keeps the last 1000 events; `history=50` replays the 50 newest, so your three
  lines are found even though they were written before the loop started.

## Next

Back to the [tutorial index](../README.md).
