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

## Guided Example

Architecture:

```text
Panel -> Server -> status/resources + console listener -> notify adapter
```

The loop below makes one resource request per iteration and reports only when
RAM exceeds the chosen fraction of its limit. The notification function prints
for demonstration; replace its body with a protected integration.

## Exercise

Write a monitor that samples every 60 seconds, notifies when RAM usage exceeds
90% of the limit, and reports console status changes. Ensure the console
listener stops when the loop exits.

Hint: convert MiB values to a ratio and wrap the loop in `try/finally`.

## Answer

```python
import os
import time
from calagoapi import Panel

def notify(message):
    print(message)  # Replace with an approved notification transport.

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

- Making a new status request for every metric when one refreshed resource
  snapshot is sufficient.
- Sending secrets or full console lines to a public channel without filtering.
- Forgetting to call `stop()` on a background listener.
- Treating an example `print()` as a production notification system.

## What You Learned

- One server object can coordinate status, resources, and live console events.
- Notification delivery should be isolated from monitoring decisions.
- Background work needs an explicit shutdown path.

## Continue Learning

Next: [25 Project 3: Multi-Server Automation](25_Project_3_Multi_Server_Automation.md)

## Navigation

Previous: [23 Project 1: Nightly Backup System](23_Project_1_Backup_System.md)
Next: [25 Project 3: Multi-Server Automation](25_Project_3_Multi_Server_Automation.md)
Reference Docs: [Servers](../reference/servers.md), [Live console](../reference/console.md)
Related Examples: [monitor answer](../../examples/tutorials/24_server_monitor/answer.py)