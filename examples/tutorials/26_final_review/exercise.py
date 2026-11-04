import os
from calagoapi import Panel

# TODO: Build a read-only summary with server name, state, and file presence.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass