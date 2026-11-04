import os
import time
from calagoapi import Panel

def notify(message):
    print(message)  # Replace with an approved notification transport.

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    server.console.onStatus(lambda state: notify(f'{server.getName()} state: {state}'))
    server.console.onConsoleLine(lambda line: print('console:', line))
    server.console.listen(background=True, history=False)
    try:
        while True:
            if server.isOnline():
                server.refresh()
                used, limit = server.getRAM(), server.getRAMLimit()
                if limit and used is not None and used / limit >= 0.9:
                    notify(f'{server.getName()} RAM at {used:.0f}/{limit:.0f} MiB')
            time.sleep(60)
    except KeyboardInterrupt:
        pass
    finally:
        server.console.stop()