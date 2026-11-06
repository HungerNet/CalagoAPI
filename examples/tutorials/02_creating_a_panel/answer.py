import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    print('panel responds:', panel.ping())
    print('key valid:', panel.validateAPI())