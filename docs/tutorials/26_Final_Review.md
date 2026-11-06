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

## Guided Example

```text
Panel -> Manager -> Server -> Resource
                 -> Automation -> Extension -> Administration
```

## Exercise

1. What object owns `getServers()`?
2. Where should a file listing for one server begin?
3. What is the difference between a schedule trigger and condition?
4. What should code do after `createBackup()` before trusting the backup?
5. What is the safest way to use an API key in a script?
6. What would this code do?

   ```python
   backup = server.backups.createBackup('pre-change')
   backup.waitUntilComplete(timeout=3600)
   if backup.isSuccessful():
       server.restart()
   ```

Hint: Follow the object chain and read each line in order.

## Answer

1. `panel.servers`, the `ServerManager`.
2. `server.files.listFiles(...)`.
3. A trigger starts evaluation; a condition decides whether the workflow may
   proceed.
4. Wait for completion and check success.
5. Load it from a secret store or environment variable and never log it.
6. It starts a backup, waits up to an hour, and restarts the server only if
   that backup succeeds. A production workflow should also handle timeout and
   backup failure explicitly.

## Common Mistakes

- Calling a resource method from the wrong manager.
- Treating a request's return as proof that a background operation completed.
- Writing fleet automation without dry review, target checks, or least
  privilege.
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
Related Examples: [final review answer](../../examples/tutorials/26_final_review/answer.py)