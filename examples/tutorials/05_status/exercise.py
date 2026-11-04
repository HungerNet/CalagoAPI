import os
from calagoapi import Panel

# TODO: Print status and, when online, RAM usage and limit.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass