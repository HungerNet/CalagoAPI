import os
from calagoapi import Panel

# TODO: Create a disabled daily schedule with a backup action.
# Review the schedule before enabling it in the panel.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass