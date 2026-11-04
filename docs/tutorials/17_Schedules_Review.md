# Schedules Review

## What You Will Learn

- Reinforce schedule composition
- Predict whether a schedule runs
- Practice reviewing actions before enabling automation

## Prerequisites

[16 Schedules](16_Schedules.md).

## Estimated Time

15 minutes

## Concepts Introduced

- Schedule inspection
- Conditions and action order
- Disabled schedule review

## Concept Explanation

A schedule is a small workflow stored by the panel. The trigger does not
guarantee execution: its condition must also pass. Steps run in order, and a
step can fail or change server state. Review the whole flow before enabling it.

## API Explanation

`getSchedules()` lists schedules. A `Schedule` exposes `getTriggers()`,
`getSteps()`, `isEnabled()`, and `getStatus()`. `enable()` and `run()` change
behavior, so use them intentionally.

## Guided Example

```python
for schedule in server.schedules.getSchedules():
    print(schedule.getName(), 'enabled=', schedule.isEnabled())
```

## Exercise

1. What are the three main parts of a schedule?
2. If a cron trigger fires but the condition is false, should its steps run?
3. What does this order do?

   ```python
   steps=[actions.createBackup('nightly'), actions.sendCommand('say Backup done')]
   ```

4. Write a disabled schedule that backs up a running server once per day.

Hint: place the backup action after the trigger and condition arguments.

## Answer

1. Trigger, condition, and ordered steps.
2. No; the condition filters whether the schedule runs.
3. It starts a backup, then sends the announcement command as the next step.
4. ```python
   from calagoapi import actions, conditions, triggers

   schedule = server.schedules.createSchedule(
       'Daily review backup',
       triggers=[triggers.cron('0 0 3 * * *')],
       condition=conditions.serverState('running'),
       steps=[actions.createBackup('nightly')],
       enabled=False,
   )
   ```

## Common Mistakes

- Reviewing only the trigger and overlooking the actions.
- Assuming a condition starts a server; it only checks state.
- Forgetting to distinguish a schedule being configured from a run being
  completed.

## What You Learned

- A schedule is a workflow owned by a server.
- Conditions filter a triggered run; actions perform its work.
- Disabled schedules can be reviewed before activation.

## Continue Learning

Next: [18 Networking](18_Networking.md)

## Navigation

Previous: [16 Schedules](16_Schedules.md)
Next: [18 Networking](18_Networking.md)
Reference Docs: [Schedules](../reference/schedules.md)
Related Examples: [schedule review answer](../../examples/tutorials/17_schedules_review/answer.py)