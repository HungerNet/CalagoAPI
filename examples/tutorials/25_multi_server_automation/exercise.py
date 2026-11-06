import os
from calagoapi import Panel

# TODO: Build a read-only report with server name, id, status, and a file check.
# Admin statistics are an optional privileged read.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass