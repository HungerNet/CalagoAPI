import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    for item in server.files.listFiles('/'):
        print(item.getName())
    if server.files.exists('/server.properties'):
        content = server.files.readFile('/server.properties')
        print('\n'.join(content.splitlines()[:3]))