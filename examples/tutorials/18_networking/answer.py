import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    primary = server.network.getPrimaryAllocation()
    if primary is not None:
        print('primary:', primary.getAddress())
    for allocation in server.network.getAllocations():
        print(allocation.getAddress(), allocation.getNotes())