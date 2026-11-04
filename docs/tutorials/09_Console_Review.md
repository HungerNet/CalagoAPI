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

## Guided Example

```python
if server.isOnline():
    with server.console as console:
        console.sendCommand('list')
        print(console.waitFor('There are', timeout=15))
```

## Exercise

1. What is the difference between `getStatus()` and `getInstallStatus()`?
2. What does `server.sendCommand()` return when the command prints a line?
3. What would this do?

   ```python
   if server.isOffline():
       server.start()
   ```

4. Write a short script that sends `list` only when online and waits for
   output containing `There are`.

Hint: `sendCommand()` does not return the response; use `waitFor()`.

## Answer

1. `getStatus()` reports power state. `getInstallStatus()` reports whether an
   installation or restore is in progress or failed.
2. It returns `None`; output arrives separately through logs or the live
   console.
3. It requests a start only if the server is fully offline. It does not wait
   for startup to finish.
4. One solution:

   ```python
   if server.isOnline():
       with server.console as console:
           console.sendCommand('list')
           print(console.waitFor('There are', timeout=15))
   ```

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
Related Examples: [console review answer](../../examples/tutorials/09_console_review/answer.py)