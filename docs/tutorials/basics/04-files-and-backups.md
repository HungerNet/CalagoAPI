# 04 · Files and backups

This builds on [03](03-live-console.md): you can control a server and watch its console.

## What you will build

A "safe config change" tool: back up the server, wait until the backup succeeded,
change a setting in a config file, and restart. If the backup fails, nothing is changed.

## Step 1: read and write files

```python
for file in server.files.listFiles('/'):
    kind = 'dir ' if file.isDirectory() else 'file'
    print(f'{kind} {file.getName()} {file.getSize(formatted=True)}')

text = server.files.readFile('/config/server.cfg')
server.files.writeFile('/config/server.cfg', text.replace('max_players=20', 'max_players=32'))
```

`server.files` is a `FileManager`. The most common methods also exist directly on the
server (`server.readFile()`, `server.writeFile()`), with the names HungerLib used.

## Step 2: back up and wait

```python
backup = server.backups.createBackup('before-config-change')
backup.waitUntilComplete(timeout=1800)
if not backup.isSuccessful():
    raise SystemExit(f'backup {backup.getName()} failed, nothing changed')
```

`createBackup()` returns immediately with a `Backup` object; the daemon works in the
background. `waitUntilComplete()` polls until it finishes.

## Complete program

```python
from calagoapi import Panel

CONFIG = '/config/server.cfg'
SETTING, VALUE = 'max_players', '32'


def setSetting(text: str, key: str, value: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.split('=', 1)[0].strip() == key:
            line = f'{key}={value}'
        lines.append(line)
    return '\n'.join(lines) + '\n'


with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    server = panel.servers.getServer('abc123')

    backup = server.backups.createBackup(f'before {SETTING}={VALUE}')
    backup.waitUntilComplete(timeout=1800)
    if not backup.isSuccessful():
        raise SystemExit(f'backup failed, {CONFIG} was not changed')
    print(f'backup {backup.getName()} done ({backup.getSize(formatted=True)})')

    server.files.writeFile(CONFIG, setSetting(server.files.readFile(CONFIG), SETTING, VALUE))
    server.restart()
    print(f'{SETTING} is now {VALUE}; restored with server.backups.restoreBackup({backup.getUUID()!r}) if needed')
```

## How it works

- Every server feature area is a **manager** on the server: `files`, `backups`,
  `databases`, `schedules`, `users` (subusers), `network` and `tunnel`. Managers return
  **objects** (`File`, `Backup`, `Schedule`, ...) that hold the panel data and offer
  getters, state checks and actions (`backup.lock()`, `backup.download()`).
- Anywhere a method takes an id, it also takes the object:
  `server.backups.deleteBackup(backup)`.
- Uploads and downloads go to the node daemon through signed URLs that the panel
  issues; CalagoAPI handles that for you.
- Game extensions build on the same managers. `calagoapi-minecraft`'s
  `setProperties()` is exactly this read-edit-write pattern on `server.properties`, and
  its Version Changer can take the backup for you ([14](../minecraft/14-versions-and-installs.md)).

## Next

[05 · Going async](05-going-async.md): check many servers at once.
