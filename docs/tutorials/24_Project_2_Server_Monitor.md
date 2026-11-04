# Project 2: Server Monitor

## What You Will Learn

- Combine status, resource snapshots, console events, and notifications
- Keep notification delivery separate from monitoring logic
- Cleanly stop a background listener

## Prerequisites

[23 Project 1: Nightly Backup System](23_Project_1_Backup_System.md).

## Estimated Time

45 minutes

## Concepts Introduced

- Monitoring loop
- Threshold checks
- Console callbacks
- Notification adapter

## Concept Explanation

The monitor samples one server's state and resources, then emits a notification
when a condition matters. `notify()` is deliberately a small adapter: connect
it to your approved email, chat, or incident service without coupling that
transport to CalagoAPI calls. Console callbacks can report status changes and
output lines in the background.

## API Explanation

`getStatus()` returns fresh power state. `refresh()` refreshes resource data;
then `getRAM()` and `getRAMLimit()` share that snapshot. `server.console` can
register `onStatus()` and `onConsoleLine()` callbacks and start a reconnecting
listener with `listen()`.

## Architecture

```text
Panel -> Server -> status/resources + console listener -> notify adapter
```

The monitor samples state and resources, then emits notifications when a
condition matters. Keep the notification transport separate from CalagoAPI so
the example can be connected to an approved email, chat, or incident service.

## Build the Monitor in Stages

Start with a notification adapter. Keeping it separate makes it easy to
connect an approved chat or incident transport later without changing the
monitoring logic:

```python
def notify(message):
    print(message)  # Replace with your approved notification integration.
```

Next, register callbacks for live status changes and console lines. The
console listener runs in the background while the monitor samples resources:

```python
server.console.onStatus(lambda state: notify(f'{server.getName()} state: {state}'))
server.console.onConsoleLine(lambda line: print('console:', line))
server.console.listen(background=True, history=False)
```

Each polling cycle checks whether the server is online, refreshes the resource
snapshot, and compares RAM use with its limit. A `try/finally` guarantees the
listener is stopped when the program exits:

```python
try:
    while True:
        if server.isOnline():
            server.refresh()
            used, limit = server.getRAM(), server.getRAMLimit()
            if limit and used is not None and used / limit >= 0.9:
                notify(f'{server.getName()} RAM at {used:.0f}/{limit:.0f} MiB')
        time.sleep(60)
finally:
    server.console.stop()
```

## Complete Script

```python
import os
import time
from calagoapi import Panel

def notify(message):
    print(message)

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    server.console.onStatus(lambda state: notify(f'{server.getName()} state: {state}'))
    server.console.onConsoleLine(lambda line: print('console:', line))
    server.console.listen(background=True, history=False)
    try:
        while True:
            if server.isOnline():
                server.refresh()
                used, limit = server.getRAM(), server.getRAMLimit()
                if limit and used is not None and used / limit >= 0.9:
                    notify(f'{server.getName()} RAM at {used:.0f}/{limit:.0f} MiB')
            time.sleep(60)
    except KeyboardInterrupt:
        pass
    finally:
        server.console.stop()
```

## Common Mistakes

- Sampling resource values repeatedly without refreshing the shared snapshot.
- Sending secrets or unfiltered console lines to a public channel.
- Forgetting to stop the background console listener during shutdown.
- Treating the `print()` notification adapter as a production delivery system.

## What You Learned

- One server object coordinates status, resources, and live console events.
- Notification delivery should be separate from monitoring decisions.
- Long-running listeners need an explicit shutdown path.

## Continue Learning

Next: [25 Project 3: Multi-Server Automation](25_Project_3_Multi_Server_Automation.md)

## Navigation

Previous: [23 Project 1: Nightly Backup System](23_Project_1_Backup_System.md)
Next: [25 Project 3: Multi-Server Automation](25_Project_3_Multi_Server_Automation.md)
Reference Docs: [Servers](../reference/servers.md), [Live console](../reference/console.md)
Related Examples: Code examples are embedded in this walkthrough.