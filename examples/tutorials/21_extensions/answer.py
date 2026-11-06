import os
from calagoapi import Panel
from calagoapi.extensions import enable

enable('version_changer')
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getMinecraftServer(os.environ['SERVER_ID'])
    print(server.getInstalledVersion())