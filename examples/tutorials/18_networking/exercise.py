import os
from calagoapi import Panel

# TODO: Print the primary allocation, then list each address and its notes.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass