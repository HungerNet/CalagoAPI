# Schedules

A Calagopus schedule has:

- **triggers**: what starts it (cron, a crash, a console line, a backup finishing, ...)
- a **condition**: checked before it runs (server online, file exists, ...)
- **steps**: actions run in order (send a command, wait, back up, restart, HTTP request, ...)

CalagoAPI ships builder helpers so you never write the JSON by hand:

```python
from calagoapi import triggers, conditions, actions, variable, backup_selectors
```

## Creating a schedule

```python
schedule = server.schedules.createSchedule(
    'Nightly restart',
    triggers=[triggers.cron('0 0 4 * * *')],
    condition=conditions.serverState('running'),
    steps=[
        actions.sendCommand('say Restarting in 1 minute'),
        actions.sleep(60_000),
        actions.createBackup('nightly', foreground=True),
        actions.sendPower('restart'),
    ],
)
```

Cron expressions have **6 fields, starting with seconds**:
`'0 0 4 * * *'` is every day at 04:00:00.

Durations and timeouts are in **milliseconds**.

## Managing schedules

```python
for schedule in server.schedules.getSchedules():
    print(schedule.getName(), schedule.isEnabled(), schedule.getLastRun())

schedule = server.schedules.getSchedule('Nightly restart')   # by name or UUID
schedule.run()                       # run now
schedule.run(skip_condition=True)
print(schedule.getStatus())          # {'running': ..., 'step': ..., 'errors': {...}}
schedule.isRunning()
schedule.abort()
schedule.enable()
schedule.disable()
schedule.rename('Daily restart')
schedule.update(triggers=[triggers.cron('0 30 3 * * *')])
copy = schedule.duplicate('Nightly restart (copy)')
schedule.delete()
```

### Steps

```python
for step in schedule.getSteps():
    print(step.getOrder(), step.getActionType(), step.getError())

schedule.addStep(actions.sendCommand('say Done'))
schedule.setSteps([actions.sendCommand('save-all'), actions.sleep(5000)])
schedule.orderSteps([step_c, step_a, step_b])
step.update(action=actions.sleep(10_000))
step.duplicate()
step.delete()
```

### Export and import

```python
data = schedule.export()
other_server.schedules.importSchedule(data)
```

## Triggers

| Helper | Fires when |
| --- | --- |
| `triggers.cron('0 0 * * * *')` | the cron expression matches |
| `triggers.powerAction('restart')` | a power action is sent |
| `triggers.serverState('offline')` | the server enters a state |
| `triggers.backupStatus('failed')` | a backup is `starting`, `finished` or `failed` |
| `triggers.databaseBackupStatus('finished')` | same, for database backups |
| `triggers.scheduleCompletion(other, successful=True)` | another schedule completes |
| `triggers.resourceUsage('memory', 'greater_than', 95, for_seconds=60)` | usage crosses a threshold |
| `triggers.consoleLine('joined the game', output_into=variable('line'))` | a console line matches |
| `triggers.crash()` | the server crashes |

## Conditions

| Helper | Matches when |
| --- | --- |
| `conditions.none()` | always (default) |
| `conditions.all(a, b, ...)` / `conditions.any(a, b, ...)` / `conditions.negate(a)` | combine conditions |
| `conditions.serverState('running')` | server is in a state |
| `conditions.uptime('greater_than', 3_600_000)` | uptime compares |
| `conditions.resourceUsage('cpu', 'smaller_than', 50)` | usage compares |
| `conditions.fileExists('/maintenance.flag')` | a file exists |
| `conditions.variableExists('x')`, `variableEquals`, `variableContains`, `variableStartsWith`, `variableEndsWith` | schedule variables |

Comparators: `smaller_than`, `smaller_than_or_equals`, `equal`, `greater_than`, `greater_than_or_equals`.

## Actions

Every action accepts `ignore_failure=True` to continue on errors.

| Group | Helpers |
| --- | --- |
| Flow | `sleep(ms)`, `ensure(condition)`, `ifCondition(condition)`, `elseIf(condition)`, `otherwise()`, `endIf()`, `exit(successful=True)` |
| Server | `sendCommand(cmd)`, `sendPower(action)`, `waitForState(state, timeout)`, `waitForConsoleLine(text, timeout, output_into=...)` |
| Backups | `createBackup(name)`, `restoreBackup(selector)`, `deleteBackup(selector)`, `moveBackup(selector, group)` |
| Database backups | `createDatabaseBackup(instance)`, `restoreDatabaseBackup(selector)`, `deleteDatabaseBackup(selector)`, `moveDatabaseBackup(selector, group)` |
| Files | `writeFile(file, content, append=False)`, `createDirectory(root, name)`, `copyFile(file, destination)`, `deleteFiles(root, files)`, `renameFiles(root, pairs)`, `compressFiles(root, files, name)`, `decompressFile(root, file)`, `pullFile(url, root)` |
| Startup | `updateStartupVariable(env, value)`, `updateStartupCommand(cmd)`, `updateDockerImage(image)` |
| Data | `format(template, output_into)`, `matchRegex(input, regex, output_into)`, `httpRequest(url, method, body, headers)` |

Backup selectors for backup actions:

```python
backup_selectors.latest()
backup_selectors.oldest(group)
backup_selectors.byId(backup)
backup_selectors.byName('nightly')
```

## Variables

Steps can capture values into variables and later steps can use them
anywhere a text parameter is accepted:

```python
steps = [
    actions.waitForConsoleLine('joined the game', timeout=600_000, output_into='line'),
    actions.matchRegex(variable('line'), r'(\w+) joined the game', ['player']),
    actions.sendCommand(variable('player')),
    actions.httpRequest('https://discord.com/api/webhooks/...',
                        body='{"content": "Someone joined"}',
                        headers={'Content-Type': 'application/json'}),
]
```

## Conditional steps

```python
steps = [
    actions.ifCondition(conditions.serverState('running')),
    actions.sendCommand('say Restarting'),
    actions.sendPower('restart'),
    actions.otherwise(),
    actions.sendPower('start'),
    actions.endIf(),
]
```
