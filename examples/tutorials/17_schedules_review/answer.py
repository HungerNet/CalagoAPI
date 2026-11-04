import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    for schedule in server.schedules.getSchedules():
        print(schedule.getName(), schedule.isEnabled())