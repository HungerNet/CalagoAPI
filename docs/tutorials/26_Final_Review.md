# Final Review

## What You Will Learn

- Revisit the full CalagoAPI object hierarchy
- Reason about combined workflows
- Identify the right reference page for an API question

## Prerequisites

[25 Project 3: Multi-Server Automation](25_Project_3_Multi_Server_Automation.md).

## Estimated Time

25 minutes

## Concepts Introduced

- End-to-end workflow review
- Object ownership
- Safe automation design

## Concept Explanation

The course has moved from a connection to managers, servers, and server-owned
resources, then to automation and administration. A reliable script chooses
the right owner for every operation, checks state before acting, protects
credentials, and verifies asynchronous work before relying on its result.

## API Explanation

Use the API reference to look up signatures and details: [servers](../reference/servers.md),
[files](../reference/files.md), [backups](../reference/backups.md),
[schedules](../reference/schedules.md), [async](../reference/async.md), and
[administration](../reference/admin.md).

## Object Flow

```text
Panel -> Manager -> Server -> Resource
                 -> Automation -> Extension -> Administration
```

## Build a Server Readiness Report

This final script follows the object hierarchy from connection to resources.
It gets a server through the panel manager, reads its power state, checks a
server-owned file, and asks the backup manager for the latest successful
recovery point:

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
   server = panel.servers.getServer(os.environ['SERVER_ID'])
   state = server.getStatus()
   has_properties = server.files.exists('/server.properties')
   backup = server.backups.getLatestBackup()

   report = {
      'name': server.getName(),
      'status': state,
      'has_properties': has_properties,
      'latest_successful_backup': backup.getName() if backup else None,
      'ready_for_maintenance': state == 'running' and backup is not None,
   }
   print(report)
```

The readiness condition is only an example policy. A real maintenance tool
should also check the expected maintenance window, permissions, and any
application-specific health signals. The report itself makes no changes.

## Common Mistakes

- Calling a resource method from the wrong manager.
- Treating a request's return as proof that a background operation completed.
- Writing fleet automation without validating targets and permissions.
- Assuming optional extensions are installed and enabled automatically.

## What You Learned

- CalagoAPI is an object model, not just a collection of endpoint calls.
- Managers locate resources; resource objects perform scoped work.
- Automation combines state checks, resource operations, and verification.

## Continue Learning

Next: [27 Where to Go Next](27_Where_To_Go_Next.md)

## Navigation

Previous: [25 Project 3: Multi-Server Automation](25_Project_3_Multi_Server_Automation.md)
Next: [27 Where to Go Next](27_Where_To_Go_Next.md)
Reference Docs: [API Reference](../reference/README.md)
Related Examples: Code examples are embedded in this walkthrough.