import os
from calagoapi import Panel

# TODO: Print `missing` only when /logs/latest.log is absent.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass