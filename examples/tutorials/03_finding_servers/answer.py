import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    for server in panel.servers.getServers():
        print(server.getName(), server.getShortId())
    selected = panel.servers.getServer(os.environ['SERVER_ID'])
    print('selected:', selected.getName())