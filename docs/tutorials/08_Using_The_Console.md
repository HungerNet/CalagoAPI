# Using the Console

## What You Will Learn

- Connect to the daemon-backed live console
- Wait for a matching output line
- Close a console connection cleanly

## Prerequisites

[07 Sending Commands](07_Sending_Commands.md). The server must be running and
the key needs console permission.

## Estimated Time

20 minutes

## Concepts Introduced

- Websocket console
- Console events and lines
- `waitFor()` and timeout
- Context-managed connections

## Concept Explanation

The live console connects to the node daemon, not the panel's ordinary HTTP
endpoint. It is useful when your program must react to output. A `with` block
closes the connection even if the body raises an exception.

## API Explanation

`server.console` is a reusable console manager. `connect()` opens it,
`sendCommand()` sends a command over the websocket, `waitFor(text, timeout)`
returns the matching line, and `lines()` yields output. `waitFor()` raises
`WaitTimeoutError` if no line matches before the deadline.

## Guided Example

```python
with server.console as console:
    console.sendCommand('save-all')
    line = console.waitFor('Saved the game', timeout=30)
    print(line)
```

## Exercise

Use the console context manager to send `list` and wait for output containing
`There are` for up to 15 seconds. Print the matching line.

Hint: call `waitFor()` on the console object, not the server.

## Answer

```python
with server.console as console:
    console.sendCommand('list')
    line = console.waitFor('There are', timeout=15)
    print(line)
```

## Common Mistakes

- Using `getLogs()` when you need future output. Logs are a snapshot; the live
  console streams events.
- Leaving a listener running in the background. Call `stop()` when finished.
- Forgetting that the daemon must be reachable and the key must have console
  permissions.

## What You Learned

- `server.console` manages a live daemon websocket.
- `waitFor()` pairs a command with its output without polling logs.
- A context manager reliably closes a one-off console connection.

## Continue Learning

Next: [09 Console Review](09_Console_Review.md)

## Navigation

Previous: [07 Sending Commands](07_Sending_Commands.md)
Next: [09 Console Review](09_Console_Review.md)
Reference Docs: [Live console](../reference/console.md), [Async](../reference/async.md)
Related Examples: [console answer](../../examples/tutorials/08_using_the_console/answer.py)