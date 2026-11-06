import os
from calagoapi import Panel

# TODO: List database instance names and their statuses.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass