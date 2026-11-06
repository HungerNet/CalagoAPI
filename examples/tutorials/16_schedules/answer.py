import os
from calagoapi import Panel, actions, conditions, triggers

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    name = 'Tutorial backup'
    schedule = server.schedules.getSchedule(name)
    if schedule is None:
        schedule = server.schedules.createSchedule(
            name,
            triggers=[triggers.cron('0 0 3 * * *')],
            condition=conditions.serverState('running'),
            steps=[actions.createBackup('nightly')],
            enabled=False,
        )
    print(schedule.getName(), schedule.isEnabled())