import os
from calagoapi import Panel

# TODO: Start SERVER_ID only if offline; wait up to 120 seconds for online.
# This exercise changes server state. Review the target before running.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass