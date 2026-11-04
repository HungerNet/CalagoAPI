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

## Build a Schedule Review Report

Before enabling automation, inspect the schedule stored on the server. The
manager lists `Schedule` objects; each object provides its enabled state,
trigger configuration, condition, and ordered steps.

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])
  for schedule in server.schedules.getSchedules():
    print(schedule.getName(), 'enabled=', schedule.isEnabled())
    print('triggers:', schedule.getTriggers())
    print('condition:', schedule.getCondition())
    for step in schedule.getSteps():
      print(' ', step.getOrder(), step.getActionType())
```

The trigger starts evaluation; the condition filters whether a run proceeds;
the steps then execute in order. `enable()` and `run()` change behavior, so
keep this report read-only until the configured workflow has been reviewed.

## Common Mistakes

- Reviewing only a trigger and overlooking its condition and ordered steps.
- Assuming a condition starts a server; it only checks whether a condition
  matches.
- Enabling a schedule before confirming its time and effects.

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
Related Examples: Code examples are embedded in this walkthrough.