import os
from calagoapi import Panel

# TODO: Create a named backup, wait for completion, then print success and status.
# This creates a backup resource on the panel.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass