# Backups

## What You Will Learn

- Create and inspect a server backup
- Wait for asynchronous completion
- Understand restore and retention risks

## Prerequisites

[11 Files Review](11_Files_Review.md). The API key needs backup permissions.

## Estimated Time

20 minutes

## Concepts Introduced

- `BackupManager`
- Background operation
- Backup state and result
- Restore safety

## Concept Explanation

A backup is a resource belonging to a server. Creating one starts work on the
panel and returns before the archive is necessarily complete. Wait for its
state before relying on it. Restoring is a separate, destructive operation,
especially with `truncate_directory=True`.

## API Explanation

`server.backups.createBackup(name, ignored_files=None)` returns a `Backup`.
Call `waitUntilComplete(timeout=...)`, then inspect `isSuccessful()`,
`getSize()`, and `getChecksum()`. `restore()` and `delete()` modify or remove
server data and should be deliberate.

## Build a Backup Workflow

Start from the panel and select the server whose files need protection. A
backup is created from that server's backup manager:

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])
  backup = server.backups.createBackup('before-maintenance')
```

Creation starts a background operation. Wait before trusting the backup, then
branch on its final status:

```python
  backup.waitUntilComplete(timeout=3600)
  if backup.isSuccessful():
    print('created:', backup.getName())
    print('size:', backup.getSize(formatted=True))
  else:
    print('backup did not succeed:', backup.getStatus())
```

## Complete Script

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])
  backup = server.backups.createBackup('before-maintenance')
  backup.waitUntilComplete(timeout=3600)

  if backup.isSuccessful():
    print('created:', backup.getName())
    print('size:', backup.getSize(formatted=True))
  else:
    print('backup did not succeed:', backup.getStatus())
```

This workflow deliberately does not restore or delete anything. Those actions
change or remove data and should be handled separately.

## Common Mistakes

- Assuming a returned backup is already complete.
- Restoring the backup when the intention was only to create one.
- Using `truncate_directory=True` without understanding that it removes current
  files before restore.
- Printing secrets embedded in configuration files while inspecting backups.

## What You Learned

- Backup creation is asynchronous.
- A `Backup` object represents state and actions for one archive.
- Restore and delete require more care than listing or creating.

## Continue Learning

Next: [13 Backups Review](13_Backups_Review.md)  

## Navigation

Previous: [11 Files Review](11_Files_Review.md)  
Next: [13 Backups Review](13_Backups_Review.md)  
Reference Docs: [Backups](../reference/backups.md)  
Related Examples: Code examples are embedded in this walkthrough.