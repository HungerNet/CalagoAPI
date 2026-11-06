import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    print({
        'name': server.getName(),
        'state': server.getStatus(),
        'has_properties': server.files.exists('/server.properties'),
    })