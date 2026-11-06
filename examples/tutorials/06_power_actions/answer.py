import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    if server.isOffline():
        server.start()
        print('online:', server.waitForOnline(timeout=120))
    elif server.isOnline():
        print('server is already running')
    else:
        print('transitioning:', server.getStatus())