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

## Guided Example

```python
from calagoapi import actions, conditions, triggers

schedule = server.schedules.createSchedule(
    'Nightly save',
    triggers=[triggers.cron('0 0 3 * * *')],
    condition=conditions.serverState('running'),
    steps=[actions.sendCommand('save-all')],
)
print(schedule.getName(), schedule.isEnabled())
```

## Exercise

Create a disabled schedule called `Tutorial backup` that runs every day at
03:00 and creates a backup named `nightly`. Do not add a restart action.

Hint: `enabled=False`; use `actions.createBackup()` for the step.

## Answer

```python
from calagoapi import actions, conditions, triggers

schedule = server.schedules.createSchedule(
    'Tutorial backup',
    triggers=[triggers.cron('0 0 3 * * *')],
    condition=conditions.serverState('running'),
    steps=[actions.createBackup('nightly')],
    enabled=False,
)
print(schedule.getName(), schedule.isEnabled())
```

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
Related Examples: [schedule answer](../../examples/tutorials/16_schedules/answer.py)