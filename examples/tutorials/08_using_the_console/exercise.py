import os
from calagoapi import Panel

# TODO: Send `list` through the live console and wait for `There are`.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass