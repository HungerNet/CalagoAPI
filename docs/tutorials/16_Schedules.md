# Schedules  
  
## What You Will Learn  
  
- Build a schedule from triggers, conditions, and steps  
- Use builders instead of writing JSON by hand  
- Understand cron and duration units  
  
## Prerequisites  
  
[15 Databases Review](15_Databases_Review.md). Your key needs schedule  
permissions.  
  
## Estimated Time  
  
25 minutes  
  
## Concepts Introduced  
  
- Trigger  
- Condition  
- Ordered action steps  
- Schedule builder helpers  
  
## Concept Explanation  
  
A schedule belongs to one server. Triggers say when it starts, a condition  
filters whether it may run, and ordered steps perform actions. This composition  
lets the panel own timing and execution rather than relying on a Python process  
to stay alive.  
  
## API Explanation  
  
Import `triggers`, `conditions`, and `actions` from `calagoapi`. `cron()` uses  
six fields including seconds. Action durations and timeouts are milliseconds.  
`createSchedule()` returns a `Schedule` object that can be enabled, run, or  
updated.  
  
## Build a Backup Schedule  
  
Schedules are made of three parts: a trigger, a condition, and ordered action  
steps. Begin by importing the builders, connecting to the panel, and selecting  
the server that will own the schedule:  
  
```python  
import os  
from calagoapi import Panel, actions, conditions, triggers  
  
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:  
  server = panel.servers.getServer(os.environ['SERVER_ID'])  
```  
  
The six-field cron expression below runs daily at 03:00. The condition makes  
the backup conditional on the server already running. A backup action is the  
only step, so the schedule does not restart the server:  
  
```python  
  schedule = server.schedules.createSchedule(  
    'Tutorial backup',  
    triggers=[triggers.cron('0 0 3 * * *')],  
    condition=conditions.serverState('running'),  
    steps=[actions.createBackup('nightly')],  
    enabled=False,  
  )  
  print(schedule.getName(), schedule.isEnabled())  
```  
  
New schedules are created disabled here so an operator can inspect the  
trigger and steps before enabling them. Schedule action durations and timeouts  
are expressed in milliseconds.  
  
## Common Mistakes  
  
- Writing a five-field cron expression. Calagopus schedule cron expressions  
  have six fields, starting with seconds.  
- Passing seconds where an action expects milliseconds.  
- Creating an enabled schedule before reviewing its trigger and effects.  
  
## What You Learned  
  
- Schedules compose timing, conditions, and ordered steps.  
- Builder helpers make schedule payloads readable.  
- Schedules execute through the panel and may be created disabled for review.  
  
## Continue Learning  
  
Next: [17 Schedules Review](17_Schedules_Review.md)  
  
## Navigation  
  
Previous: [15 Databases Review](15_Databases_Review.md)  
Next: [17 Schedules Review](17_Schedules_Review.md)  
Reference Docs: [Schedules](../reference/schedules.md)  
Related Examples: Code examples are embedded in this walkthrough.