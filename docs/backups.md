# Backups

`server.backups` is a `BackupManager`.

## Creating and waiting

```python
backup = server.backups.createBackup('before-update', ignored_files=['logs', '*.tmp'])
backup.waitUntilComplete(timeout=3600)

print(backup.getStatus())        # 'in_progress', 'successful' or 'failed'
if backup.isSuccessful():
    print(backup.getSize(formatted=True), backup.getFileCount(), backup.getChecksum())
```

`server.createBackup(name)` is a shortcut.

## Listing

```python
for backup in server.backups.getBackups():
    print(backup.getName(), backup.getStatus(), backup.isLocked())

server.backups.getBackups(search='nightly')
server.backups.getBackups(kind='database_instance')
server.backups.getLatestBackup()
server.backups.getBackup(backup_id)
server.backups.getSystemBackups()      # made by admin backup policies
server.backups.getUsage()
```

## Backup actions

```python
backup.restore(truncate_directory=True, restore_startup=True)
backup.download('backup.tar.gz')
backup.download('backup.zip', archive_format='zip')
backup.getDownloadUrl()
backup.exportToServer('/exports/backup.tar.gz')
backup.rename('stable')
backup.lock()
backup.unlock()
backup.delete()
backup.refresh()
```

| Getters | State checks |
| --- | --- |
| `getName`, `getSize(formatted=False)`, `getFileCount`, `getChecksum`, `getKind`, `getDatabaseType`, `getGroupId`, `getIgnoredFiles`, `getCompleted`, `getCreated`, `getStatus` | `isCompleted`, `isInProgress`, `isSuccessful`, `isFailed`, `isLocked`, `isBrowsable`, `isStreaming` |

## Bulk actions

```python
old = [b for b in server.backups.getBackups() if b.getCreated() < '2026-01-01']
server.backups.deleteBackups(old)
server.backups.lockBackups([backup_a, backup_b])
server.backups.unlockBackups([backup_a])
```

## Backup groups

Groups hold backups with their own retention policy (0 = unlimited).

```python
group = server.backups.createBackupGroup('daily', retention={'daily': 7, 'weekly': 4})
backup = server.backups.createBackup('nightly', group=group)

group.setRetention(daily=14)
group.getBackups()
backup.moveToGroup(group)
server.backups.moveBackups([b1, b2], group)
server.backups.orderBackupGroups([group, other])
group.delete(lock_backups=True)
```
