import os
from calagoapi import Panel

# TODO: List hosted database names, then create tutorial_stats.
# Creation consumes a database slot and may reveal a credential to your process.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass