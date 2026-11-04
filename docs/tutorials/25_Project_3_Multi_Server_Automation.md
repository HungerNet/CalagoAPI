# Project 3: Multi-Server Automation

## What You Will Learn

- Iterate across accessible servers
- Combine file checks with server state
- Use an admin-only read to enrich a report

## Prerequisites

[24 Project 2: Server Monitor](24_Project_2_Server_Monitor.md). Admin statistics
in this project require an admin API key; remove that section for a user key.

## Estimated Time

45 minutes

## Concepts Introduced

- Multi-server iteration
- Read-only inventory report
- Permission-aware administration
- Aggregated automation output

## Concept Explanation

The project produces an inventory report for servers visible to the current
key. For each server it combines state and a file existence check. It then
reads panel-wide admin statistics once. This keeps the report read-only and
avoids broad write access; operational actions can be added later behind an
explicit review step.

## API Explanation

`panel.servers.getServers()` returns accessible server objects. Each object
provides fresh status and scoped file methods. `panel.admin.getStats()` is a
privileged read and will fail for a non-admin key.

## Architecture

```text
Panel -> ServerManager -> many GenericServer objects -> per-server checks
  -> Admin namespace -> panel-level statistics -> report
```

The report is read-only. It gathers the inventory visible to the current key,
performs server-scoped checks through each server's managers, and optionally
adds one panel-wide admin statistic. Keeping admin access separate makes its
permission requirement clear.

## Build the Inventory in Stages

Ask `panel.servers` for the servers visible to this API key. The result respects
the caller's access; it does not automatically include every server in the
panel:

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    servers = panel.servers.getServers()
```

For each server, collect its state and check the file through that server's
file manager. Keeping the results in dictionaries makes the report easy to
serialize or render later:

```python
    report = []
    for server in servers:
        report.append({
            'name': server.getName(),
            'short_id': server.getShortId(),
            'status': server.getStatus(),
            'has_properties': server.files.exists('/server.properties'),
        })

    for row in report:
        print(row)
```

With an admin key, add panel-wide statistics in a separate section:

```python
    print('panel stats:', panel.admin.getStats())
```

## Complete Script

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    report = []
    for server in panel.servers.getServers():
        report.append({
            'name': server.getName(),
            'short_id': server.getShortId(),
            'status': server.getStatus(),
            'has_properties': server.files.exists('/server.properties'),
        })

    for row in report:
        print(row)

    print('panel stats:', panel.admin.getStats())
```

## Common Mistakes

- Assuming a user's server listing includes every server in the panel.
- Creating a resource manager separately instead of using `server.files`.
- Giving a fleet script write access before validating its target set.

## What You Learned

- Server iteration begins with the panel manager and respects key access.
- Each server retains its own resource managers.
- Panel-wide administration is distinct from user-visible server operations.

## Continue Learning

Next: [26 Final Review](26_Final_Review.md)  

## Navigation

Previous: [24 Project 2: Server Monitor](24_Project_2_Server_Monitor.md)  
Next: [26 Final Review](26_Final_Review.md)  
Reference Docs: [Servers](../reference/servers.md), [Files](../reference/files.md), [Administration](../reference/admin.md)  
Related Examples: Code examples are embedded in this walkthrough.