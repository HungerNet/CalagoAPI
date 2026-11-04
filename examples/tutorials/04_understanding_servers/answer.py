import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    print(server.getName(), server.getUUID())
    print(type(server.files).__name__)
    print(type(server.backups).__name__)