import os
from calagoapi import Panel

# TODO: Print every schedule name and whether it is enabled.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass