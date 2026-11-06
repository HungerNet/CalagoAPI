import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    print(panel.admin.getStats())
    for node in panel.admin.nodes.getNodes():
        print(node.getName())