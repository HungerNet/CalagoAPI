# Backups Review

## What You Will Learn

- Reinforce backup state and ownership
- Predict what backup code does
- Design a cautious backup workflow

## Prerequisites

[12 Backups](12_Backups.md).

## Estimated Time

15 minutes

## Concepts Introduced

- Backup lifecycle
- Successful backup selection
- Restore safeguards

## Concept Explanation

Creating, completing, and restoring a backup are separate events. Automation
should wait, check success, and keep enough metadata to know which backup was
made. A restore should be planned and should not be used as a test of backup
creation.

## API Explanation

`getBackups()` lists `Backup` objects. `getLatestBackup()` returns the latest
successful backup by default. `waitUntilComplete()` waits for a created backup;
`restore()` applies it to server files.

## Guided Example

```python
backup = server.backups.getLatestBackup()
if backup is None:
    print('no successful backup yet')
else:
    print(backup.getName(), backup.getCreated())
```

## Exercise

1. Why should code wait after `createBackup()`?
2. What does `getLatestBackup()` select by default?
3. What is the extra risk of `restore(truncate_directory=True)`?
4. Write code that creates a backup and prints its size only after success.

Hint: `getSize(formatted=True)` returns a readable string.

## Answer

1. Backup creation runs in the background.
2. The most recent successful backup, or `None` if none exists.
3. It deletes current files before applying the restore.
4. ```python
   backup = server.backups.createBackup('review-checkpoint')
   backup.waitUntilComplete(timeout=3600)
   if backup.isSuccessful():
       print(backup.getSize(formatted=True))
   ```

## Common Mistakes

- Checking success before the job has completed.
- Choosing a backup by list position without checking its state or date.
- Combining backup creation and restore into a routine that runs without
  operator review.

## What You Learned

- Backups have an observable lifecycle.
- Select only completed successful backups when reliability matters.
- Restore behavior can remove current server data.

## Continue Learning

Next: [14 Databases](14_Databases.md)

## Navigation

Previous: [12 Backups](12_Backups.md)
Next: [14 Databases](14_Databases.md)
Reference Docs: [Backups](../reference/backups.md)
Related Examples: [backup review answer](../../examples/tutorials/13_backups_review/answer.py)