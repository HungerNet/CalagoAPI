# Project 1: Nightly Backup System  
  
## What You Will Learn  
  
- Combine servers, backups, and schedules  
- Design a panel-owned recurring workflow  
- Avoid duplicate schedules and unsafe restore behavior  
  
## Prerequisites  
  
[17 Schedules Review](17_Schedules_Review.md). Review [Backups](12_Backups.md)  
and [Schedules](16_Schedules.md). The API key needs backup and schedule  
permissions for the target server.  
  
## Estimated Time  
  
45 minutes  
  
## Concepts Introduced  
  
- Automation architecture  
- Idempotent setup  
- Scheduled backup action  
- Operational review  
  
## Concept Explanation  
  
The project creates a named daily backup schedule for one server. Python is  
used to configure the workflow once; Calagopus owns the recurring execution.  
The script avoids creating a duplicate if the named schedule already exists.  
It does not restore data or restart the server.  
  
## API Explanation  
  
The script retrieves a `GenericServer` through `panel.servers`, then uses its  
`schedules` manager. A cron trigger defines the time, a server-state condition  
filters execution, and `actions.createBackup()` is the only step. It creates  
the schedule disabled so an operator can inspect it before enabling.  
  
## Architecture  
  
```text  
Environment credentials -> Panel -> ServerManager -> GenericServer  
  -> ScheduleManager -> daily trigger -> condition -> backup action  
```  
  
Python configures the workflow once; Calagopus owns recurring execution. Use a  
stable schedule name, check for an existing schedule before creating one, and  
leave new automation disabled until its trigger and action have been reviewed.  
Retention can be added later with a backup group and an explicit policy.  
  
## Build the Script in Stages  
  
First create the connection and resolve the target server. Keeping the server  
ID in configuration avoids depending on a display name:  
  
```python  
import os  
from calagoapi import Panel, actions, conditions, triggers  
  
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:  
    server = panel.servers.getServer(os.environ['SERVER_ID'])  
```  
  
Give the schedule a stable name and look it up before creating it. This makes  
running the setup script repeatedly safe from duplicate schedules:  
  
```python  
    name = 'Nightly tutorial backup'  
    schedule = server.schedules.getSchedule(name)  
    if schedule is None:  
        schedule = server.schedules.createSchedule(  
            name,  
            triggers=[triggers.cron('0 0 3 * * *')],  
            condition=conditions.serverState('running'),  
            steps=[actions.createBackup('nightly')],  
            enabled=False,  
        )  
        print('created disabled schedule:', schedule.getName())  
    else:  
        print('schedule already exists:', schedule.getName())  
```  
  
The trigger uses a six-field cron expression. The condition prevents the  
backup step from running unless the server is already running.  
  
## Common Mistakes  
  
- Creating a duplicate schedule every time the setup script runs.  
- Enabling automation before reviewing its trigger and action.  
- Assuming a started backup is already complete.  
- Adding restore or `truncate_directory=True` to a routine backup workflow.  
  
## What You Learned  
  
- A project is assembled from a panel connection, manager, server, and resource.  
- Schedules let the panel execute a recurring backup.  
- Safe automation avoids duplicate setup and separates configuration from  
  activation.  
  
## Continue Learning  
  
Next: [24 Project 2: Server Monitor](24_Project_2_Server_Monitor.md)  
  
## Navigation  
  
Previous: [22 Admin API](22_Admin_API.md)  
Next: [24 Project 2: Server Monitor](24_Project_2_Server_Monitor.md)  
Reference Docs: [Backups](../reference/backups.md), [Schedules](../reference/schedules.md)  
Related Examples: Code examples are embedded in this walkthrough.