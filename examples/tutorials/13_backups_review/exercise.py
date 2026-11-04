import os
from calagoapi import Panel

# TODO: Create a backup and print its size only after successful completion.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass