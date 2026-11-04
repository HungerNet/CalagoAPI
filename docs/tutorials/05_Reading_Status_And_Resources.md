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

## Build the Script

Start with the connection settings. Keeping these in environment variables
means the script can be shared without sharing a credential:

```python
import os
from calagoapi import Panel

url = os.environ['CALAGOPUS_URL']
api_key = os.environ['CALAGOPUS_API_KEY']
server_id = os.environ['SERVER_ID']
```

Next, open the panel and ask its server manager for one server. The manager
returns a `GenericServer` object, which will own the status and resource calls:

```python
with Panel(url=url, api_key=api_key) as panel:
  server = panel.servers.getServer(server_id)
```

Read status once, then use that value to decide which measurements make sense.
`getStatus()` fetches a fresh resource snapshot as well, so the resource
getters below can use the same cached snapshot:

```python
  state = server.getStatus()
  print('state:', state)

  if state == 'running':
    print('CPU:', server.getCPU(), '%')
    print('RAM:', server.getRAM(), '/', server.getRAMLimit(), 'MiB')
    print('uptime:', server.getUptime(formatted=True))
```

## Complete Script

```python
import os
from calagoapi import Panel

with Panel(
  url=os.environ['CALAGOPUS_URL'],
  api_key=os.environ['CALAGOPUS_API_KEY'],
) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])
  state = server.getStatus()
  print('state:', state)

  if state == 'running':
    print('CPU:', server.getCPU(), '%')
    print('RAM:', server.getRAM(), '/', server.getRAMLimit(), 'MiB')
    print('uptime:', server.getUptime(formatted=True))
```

If the script runs for a while and needs a newer measurement, call
`server.refresh()` before reading the resource getters again.

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
Related Examples: Code examples are embedded in this walkthrough.