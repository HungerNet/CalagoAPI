import os
from calagoapi import Panel

# TODO: Retrieve SERVER_ID and print its name, UUID, and manager class names.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass