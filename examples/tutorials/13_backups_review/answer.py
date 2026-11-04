import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    backup = server.backups.createBackup('review-checkpoint')
    backup.waitUntilComplete(timeout=3600)
    if backup.isSuccessful():
        print(backup.getSize(formatted=True))
    else:
        print('backup failed:', backup.getStatus())