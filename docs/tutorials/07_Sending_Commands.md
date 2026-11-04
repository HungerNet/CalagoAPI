# Sending Commands

## What You Will Learn

- Use `sendCommand()` for a one-off command
- Send commands in order
- Distinguish HTTP commands from a live console session

## Prerequisites

[06 Power Actions](06_Power_Actions.md). The server must be running and the key
needs console-control permission.

## Estimated Time

15 minutes

## Concepts Introduced

- Console command
- One-off request
- Command permissions

## Concept Explanation

A server command is an instruction interpreted by the server software. It can
change world state or affect players, so treat it like any other operational
action. `sendCommand()` is convenient for a single command; it does not wait
for the server's textual response.

## API Explanation

`server.sendCommand(command)` sends one command through the panel API.
`sendCommands([...])` sends multiple commands in order, and `getLogs()` reads
recent output. For matching a response or reacting continuously, use
`server.console`; the next lesson covers it.

## Build a Command Workflow

```python
server.sendCommand('say Maintenance starts in five minutes')
print(server.getLogs(lines=20))
```

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])
  if server.isOnline():
    server.sendCommand('say Hello World')
    server.restart()
  else:
    print('Start the server before sending the command')
```

The command is sent without a leading slash. This example couples the
announcement and restart for demonstration; operational scripts should keep
these decisions separate when a message must not trigger a restart.

## Common Mistakes

- Adding `/` as if this were an in-game chat input. The API expects the command
  without that prefix.
- Expecting `sendCommand()` to return console output. Read logs or use
  `waitFor()` in a live console session.
- Sending commands to an offline server or without console permission.

## What You Learned

- `sendCommand()` handles one-off actions; `sendCommands()` preserves order.
- Commands may change live server state.
- The live console is the right tool when you need a response.

## Continue Learning

Next: [08 Using the Console](08_Using_The_Console.md)

## Navigation

Previous: [06 Power Actions](06_Power_Actions.md)
Next: [08 Using the Console](08_Using_The_Console.md)
Reference Docs: [Servers](../reference/servers.md), [Live console](../reference/console.md)
Related Examples: Code examples are embedded in this walkthrough.