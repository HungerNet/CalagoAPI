import os
from calagoapi import Panel

# TODO: If online, send a chat announcement and restart the server.
# This exercise sends a command and restarts the server.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass