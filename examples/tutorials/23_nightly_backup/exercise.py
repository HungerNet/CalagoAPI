import os
from calagoapi import Panel, actions, conditions, triggers

# TODO: Find the named schedule and create it only when absent. Leave it disabled.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass