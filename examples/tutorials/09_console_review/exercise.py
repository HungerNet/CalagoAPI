import os
from calagoapi import Panel

# TODO: If online, send `list` and wait for a matching console response.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass