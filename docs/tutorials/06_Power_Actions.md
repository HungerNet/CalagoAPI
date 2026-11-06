# Power Actions

## What You Will Learn

- Start, stop, restart, and kill a server
- Wait for a state transition
- Recognize the risk of a mutating action

## Prerequisites

[05 Reading Status and Resources](05_Reading_Status_And_Resources.md). The API
key needs the relevant control permission.

## Estimated Time

15 minutes

## Concepts Introduced

- Power actions
- Transitional states
- State waiting
- Permission errors

## Concept Explanation

Power actions request a change; they do not prove the change has completed.
After `restart()`, the server may pass through `stopping` and `starting` before
it is online. Wait helpers poll the state and return `False` on timeout.

## API Explanation

`start()`, `stop()`, `restart()`, and `kill()` map to supported panel actions.
`kill()` is immediate and should not be used as a routine graceful stop.
`waitForOnline(timeout=...)` and `waitForOffline(...)` report whether the
target state was reached.

## Guided Example

```python
server.restart()
if server.waitForOnline(timeout=180):
    print('server is back')
else:
    print('restart did not finish in time')
```

## Exercise

Write a script that starts the server only when it is offline, then waits up to
two minutes for it to come online. Do not send a start request if it is already
running.

Hint: use `isOffline()` before `start()`.

## Answer

```python
if server.isOffline():
    server.start()
    if not server.waitForOnline(timeout=120):
        print('server did not become online in time')
elif server.isOnline():
    print('server is already running')
else:
    print('server is transitioning:', server.getStatus())
```

## Common Mistakes

- Treating a successful method return as proof that the server reached its
  target state. Use a wait helper.
- Issuing repeated starts while the server is transitioning. Check state first.
- Using `kill()` where a graceful `stop()` is appropriate.

## What You Learned

- Power actions request transitions, while wait helpers observe completion.
- Check the current state before sending an action.
- Permissions and timeouts are part of real automation.

## Continue Learning

Next: [07 Sending Commands](07_Sending_Commands.md)

## Navigation

Previous: [05 Reading Status and Resources](05_Reading_Status_And_Resources.md)
Next: [07 Sending Commands](07_Sending_Commands.md)
Reference Docs: [Servers](../reference/servers.md), [Errors and utilities](../reference/errors-and-utilities.md)
Related Examples: [power action answer](../../examples/tutorials/06_power_actions/answer.py)