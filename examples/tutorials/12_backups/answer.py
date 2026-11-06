import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    backup = server.backups.createBackup('tutorial-checkpoint')
    backup.waitUntilComplete(timeout=3600)
    print('successful:', backup.isSuccessful())
    print('status:', backup.getStatus())