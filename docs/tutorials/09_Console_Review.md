# Console Review

## What You Will Learn

- Reinforce server state, commands, and live console behavior
- Explain the difference between log snapshots and streamed output
- Practice a small command-and-response workflow

## Prerequisites

[08 Using the Console](08_Using_The_Console.md).

## Estimated Time

15 minutes

## Concepts Introduced

- Review checkpoints
- Power state checks
- Command output matching

## Concept Explanation

The console workflow starts with a server object. Check its state before
sending a command, then use a live console when you need to observe the response.
`getLogs()` is a recent-output snapshot; `waitFor()` waits for new websocket
output.

## API Explanation

`isOnline()` gives a boolean condition. `sendCommand()` sends a one-off command.
`server.console.waitFor(text, timeout)` waits for a matching line and raises
`WaitTimeoutError` if the deadline expires.

## Walk Through a Console Request

Build on the earlier lessons by retrieving the server, checking its current
power state, and using the live console only when it is running. The response
is a separate event; `sendCommand()` itself does not return console text.

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    state = server.getStatus()
    print('power state:', state)

    if state == 'running':
        with server.console as console:
            console.sendCommand('list')
            print(console.waitFor('There are', timeout=15))
    else:
        print('The server must be running to query its player list.')
```

Notice that `getStatus()` is distinct from `getInstallStatus()`: this workflow
needs power state, not installation state. The context manager also ensures
the websocket is closed after the matching line is handled.

## Common Mistakes

- Treating a command request as a response channel.
- Assuming a power action is complete as soon as the method returns.
- Keeping a console open indefinitely when a context manager is enough.

## What You Learned

- Status, install lifecycle, and console output are separate signals.
- Use a live console when your workflow depends on output.
- Check state before sending an action.

## Continue Learning

Next: [10 Working with Files](10_Working_With_Files.md)  

## Navigation

Previous: [08 Using the Console](08_Using_The_Console.md)  
Next: [10 Working with Files](10_Working_With_Files.md)  
Reference Docs: [Servers](../reference/servers.md), [Live console](../reference/console.md)  
Related Examples: Code examples are embedded in this walkthrough.