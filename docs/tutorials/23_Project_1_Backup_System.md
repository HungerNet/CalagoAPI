# Project 1: Nightly Backup System

## What You Will Learn

- Combine servers, backups, and schedules
- Design a panel-owned recurring workflow
- Avoid duplicate schedules and unsafe restore behavior

## Prerequisites

[22 Admin API](22_Admin_API.md). Review [Backups](12_Backups.md) and
[Schedules](16_Schedules.md).

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

## Guided Example

Architecture:

```text
Environment credentials -> Panel -> ServerManager -> GenericServer
  -> ScheduleManager -> daily trigger -> condition -> backup action
```

Design decisions: use a stable schedule name, create it disabled, keep secrets
outside source, and wait for each backup before treating it as valid. Retention
can be added later with a backup group and an explicit policy.

## Exercise

Build an idempotent setup script that finds a server by ID and creates a
disabled daily backup schedule only when it does not already exist.

Hint: use `getSchedule(name)` before `createSchedule()`.

## Answer

```python
import os
from calagoapi import Panel, actions, conditions, triggers

schedule_name = 'Nightly tutorial backup'
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    schedule = server.schedules.getSchedule(schedule_name)
    if schedule is None:
        schedule = server.schedules.createSchedule(
            schedule_name,
            triggers=[triggers.cron('0 0 3 * * *')],
            condition=conditions.serverState('running'),
            steps=[actions.createBackup('nightly')],
            enabled=False,
        )
        print('created disabled schedule:', schedule.getName())
    else:
        print('schedule already exists:', schedule.getName())
```

After reviewing the trigger, condition, and backup name in the panel, an
authorized operator can enable the schedule. To verify a run, list backups and
wait for the backup to finish before checking `isSuccessful()`.

## Common Mistakes

- Running setup repeatedly without checking for an existing schedule.
- Enabling automation before reviewing its cron expression and action.
- Assuming a started backup is already complete.
- Adding a restore or `truncate_directory=True` to a routine backup workflow.

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
Related Examples: [backup project answer](../../examples/tutorials/23_nightly_backup/answer.py)