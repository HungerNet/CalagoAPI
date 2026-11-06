import os
from calagoapi import Panel

# TODO: With an admin key, print panel stats and the names of all nodes.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass