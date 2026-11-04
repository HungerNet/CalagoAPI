# Reading Status and Resources

## What You Will Learn

- Read power state and resource usage
- Choose a convenience check such as `isOnline()`
- Understand resource caching

## Prerequisites

[04 Understanding Server Objects](04_Understanding_Server_Objects.md).

## Estimated Time

15 minutes

## Concepts Introduced

- Power state
- Resource snapshot
- Cached resources
- Fresh status checks

## Concept Explanation

Status and resources answer different questions. Power state is a small label
such as `running` or `offline`; resources are measurements such as CPU, RAM,
disk, and uptime. `getStatus()` fetches a fresh state. Resource getters share a
cached resource response until `refresh()` is called.

## API Explanation

Use `isOnline()` or `isOffline()` when branching on a state; use `getStatus()`
when you need the exact label. `getRAM()` returns MiB by default,
`getRAMLimit()` returns the limit, `getCPU()` returns percent, and
`getUptime(formatted=True)` returns a readable duration.

## Guided Example

```python
if server.isOnline():
    print(server.getCPU(), '%')
    print(server.getRAM(), '/', server.getRAMLimit(), 'MiB')
else:
    print('power state:', server.getStatus())
```

## Exercise

Print the current state. If the server is online, print RAM used and the limit
in MiB. Refresh resources before reading them a second time.

Hint: call `server.refresh()` to update the resource cache.

## Answer

```python
state = server.getStatus()
print('state:', state)
if server.isOnline():
    print('RAM:', server.getRAM(), '/', server.getRAMLimit(), 'MiB')
    server.refresh()
    print('fresh CPU:', server.getCPU(), '%')
```

## Common Mistakes

- Calling `getStatus()` repeatedly when `isOnline()` expresses the condition
  more clearly. Both ask for fresh status.
- Assuming each resource getter makes a fresh request. Call `refresh()` when
  freshness matters.
- Mixing install lifecycle status with power status. `getInstallStatus()` is a
  separate concept from `getStatus()`.

## What You Learned

- State checks and resource measurements are different.
- `isOnline()` is a convenient branch condition.
- Resource getters share a cache; `refresh()` updates it.

## Continue Learning

Next: [06 Power Actions](06_Power_Actions.md)

## Navigation

Previous: [04 Understanding Server Objects](04_Understanding_Server_Objects.md)
Next: [06 Power Actions](06_Power_Actions.md)
Reference Docs: [Servers](../reference/servers.md)
Related Examples: [status answer](../../examples/tutorials/05_status/answer.py)