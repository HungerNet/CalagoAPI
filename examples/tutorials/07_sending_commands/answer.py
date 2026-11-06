import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    if server.isOnline():
        server.sendCommand('say Hello World')
        server.restart()
    else:
        print('Start the server before sending the command')