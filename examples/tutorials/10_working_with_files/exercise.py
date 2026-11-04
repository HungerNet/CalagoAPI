import os
from calagoapi import Panel

# TODO: List the server root. If server.properties exists, print its first 3 lines.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass