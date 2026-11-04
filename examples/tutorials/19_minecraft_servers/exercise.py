import os
from calagoapi import Panel

# TODO: Use MinecraftServer to print max-players and the MOTD without changes.
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    pass