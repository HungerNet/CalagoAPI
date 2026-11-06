import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getMinecraftServer(os.environ['SERVER_ID'])
    print('max-players:', server.getProperty('max-players'))
    print('motd:', server.getMOTD())