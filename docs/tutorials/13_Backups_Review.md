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
  
## Build a Backup Inventory  
  
Once backups exist, a useful follow-up script reports which completed backup  
is currently the best recovery point. `getLatestBackup()` selects the latest  
successful backup by default and returns `None` when no successful backup is  
available.  
  
```python  
import os  
from calagoapi import Panel  
  
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:  
    server = panel.servers.getServer(os.environ['SERVER_ID'])  
    backup = server.backups.getLatestBackup()  
  
    if backup is None:  
        print('no successful backup yet')  
    else:  
        print('name:', backup.getName())  
        print('created:', backup.getCreated())  
        print('size:', backup.getSize(formatted=True))  
```  
  
The report is read-only. Restoring is a separate workflow; in particular,  
`truncate_directory=True` removes current files before applying the backup.  
  
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
Related Examples: Code examples are embedded in this walkthrough.