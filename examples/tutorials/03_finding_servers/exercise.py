import os
from calagoapi import Panel

# TODO: List accessible servers, then retrieve SERVER_ID and print its name.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass