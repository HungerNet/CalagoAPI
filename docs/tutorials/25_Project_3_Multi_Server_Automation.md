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

## Guided Example

Architecture:

```text
Panel -> ServerManager -> many GenericServer objects -> per-server checks
  -> Admin namespace -> panel-level statistics -> report
```

Design decisions: gather the accessible inventory from the user manager,
perform server-scoped checks through each server object, and keep the admin
call separate so permission failure is easy to understand.

## Exercise

Create a report containing each accessible server's name, short ID, state, and
whether `/server.properties` exists. Then include admin panel statistics.
Do not modify any server.

Hint: access each server's file manager through that server object.

## Answer

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

    try:
        print('panel stats:', panel.admin.getStats())
    except Exception as error:
        print('admin statistics unavailable:', type(error).__name__)
```

## Common Mistakes

- Assuming a user's server listing includes every server in the panel.
- Creating a resource manager separately instead of using the owning server's
  `files` property.
- Catching every error silently. The example identifies admin access failure
  but still names its exception type.
- Adding write actions to a fleet script before validating its target set.

## What You Learned

- Server iteration begins with the panel's manager and respects key access.
- Each server retains its own resource managers.
- Panel-wide administration is distinct from user-visible server operations.

## Continue Learning

Next: [26 Final Review](26_Final_Review.md)

## Navigation

Previous: [24 Project 2: Server Monitor](24_Project_2_Server_Monitor.md)
Next: [26 Final Review](26_Final_Review.md)
Reference Docs: [Servers](../reference/servers.md), [Files](../reference/files.md), [Administration](../reference/admin.md)
Related Examples: [multi-server answer](../../examples/tutorials/25_multi_server_automation/answer.py)