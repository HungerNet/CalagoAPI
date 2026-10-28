# Servers

## Getting servers

```python
server = panel.servers.getServer('abc123')          # by UUID or short id
server = panel.servers.getServerByName('Survival')  # exact name, or None

for server in panel.servers.getServers():           # every server you can access
    print(server)

page = panel.servers.getServers(page=1, per_page=25, search='smp')
```

`getServers(all_servers=True)` also lists servers you do not own or have
access to (admins only).

`panel.servers.getServer()` returns a `GenericServer`. Use
`panel.servers.getMinecraftServer()` for the [Minecraft helpers](minecraft.md).

## Status

| Method | Returns |
| --- | --- |
| `getStatus()` / `getPowerState()` | `'running'`, `'offline'`, `'starting'` or `'stopping'` (always fresh) |
| `isOnline()` / `isRunning()` | running |
| `isOffline()` / `isStopped()` | offline |
| `isStarting()`, `isStopping()` | transitional states |
| `getInstallStatus()` | `None` when installed, otherwise `'installing'`, `'install_failed'`, `'reinstall_failed'` or `'restoring_backup'` |
| `isInstalled()`, `isInstalling()`, `isInstallFailed()`, `isRestoringBackup()` | install state checks |
| `isSuspended()`, `isTransferring()`, `isOwner()`, `isNodeInMaintenance()` | other flags |

```python
status = server.getStatus()
if server.isOnline():
    server.sendCommand('say Hi')
```

### Waiting for a state

```python
server.restart()
if server.waitForOnline(timeout=180):
    server.sendCommand('say Back online!')

server.stop()
server.waitForOffline()
server.waitForState('starting', timeout=30, interval=1)
```

## Resources

Resource getters use a cache so several calls cost one request. Call
`refresh()` to update it. `getStatus()` always refreshes.

```python
server.refresh()                     # fetch fresh resources
server.getCPU()                      # 37.5 (percent, 100 = one core)
server.getCPULimit()                 # 200
server.getRAM()                      # 1843.2 (MiB)
server.getRAM(gb=True)               # 1.8 (GiB)
server.getRAMLimit()
server.getDisk(), server.getDiskLimit()
server.getNetworkIn(), server.getNetworkOut()
server.getUptime()                   # milliseconds
server.getUptime(formatted=True)     # '3h 12m'
server.resources()                   # the raw cached dict
```

## Power and console

```python
server.start()
server.stop()
server.restart()
server.kill()
server.powerAction('restart')        # raises InvalidActionError for unknown actions

server.sendCommand('say Hello')
server.sendCommands(['save-all', 'say Saved'])
print(server.getLogs(lines=100))

for line in server.streamConsole():  # live output, see Live console
    print(line)
server.onConsoleLine(print)          # live output via callback
```

See [Live console](console.md) for waiting on output, callbacks for status
and stats, and every other daemon event.

## Details

Server details are fetched once and cached. `refreshDetails()` reloads them.

```python
server.getName(), server.getDescription()
server.getUUID(), server.getShortId()
server.getNodeName(), server.getLocationName()
server.getEggName(), server.getEgg()
server.getLimits(), server.getFeatureLimits()
server.getDockerImage(), server.getDockerImages()
server.getStartupCommand()
server.getAddress()                  # 'play.example.com:25565'
server.getPrimaryAllocation()
server.getSftpHost(), server.getSftpPort()
server.getPermissions(), server.hasPermission('file.read')
server.getActivity(page=1, per_page=20)
server.getAnnouncements()
server.getNodeResources()
```

## Settings

```python
server.setName('Survival')
server.setDescription('Main world')
server.setTimezone('Europe/Berlin')
server.setAutoStart('unless_stopped')    # 'always', 'unless_stopped', 'never'
server.setAutoKill(True, seconds=60)
server.reinstall(truncate_directory=False, start_on_completion=True)
server.cancelInstall()
server.unlockInstall()
```

## Startup

```python
for variable in server.getStartupVariables():
    print(variable['env_variable'], variable['value'])

server.getStartupVariable('SERVER_JARFILE')
server.updateStartupVariable('SERVER_JARFILE', 'paper.jar')
server.updateStartupVariables({'MINECRAFT_VERSION': '1.21.1', 'BUILD_NUMBER': 'latest'})
server.setStartupCommand('java -Xms128M -jar {{SERVER_JARFILE}}')
server.setDockerImage('ghcr.io/pterodactyl/yolks:java_21')
```

## Mounts and devices

```python
server.getMounts()
server.attachMount(mount_uuid)
server.detachMount(mount_uuid)
server.getDevices()
server.attachDevice(device_uuid)
```

## Server groups

Groups are personal folders in the panel sidebar.

```python
group = panel.servers.createGroup('Minigames', [lobby, bedwars])
group.addServer(skywars)
group.removeServer(bedwars)
group.rename('Games')
for server in group.getServers():
    print(server.getName())
panel.servers.orderGroups([group, other_group])
```

## Shortcuts

For HungerLib compatibility the most common manager methods are also on the
server itself:

| Server shortcut | Full method |
| --- | --- |
| `listFiles`, `readFile`, `writeFile`, `uploadFile`, `downloadFile`, `deleteFiles`, `renameFiles`, `copyFiles`, `moveFiles`, `createFolder`, `compress`, `decompress` | `server.files.*` |
| `listBackups`, `getBackups`, `getBackup`, `createBackup`, `deleteBackup`, `restoreBackup`, `downloadBackup` | `server.backups.*` |
| `listDatabases`, `getDatabases`, `createDatabase`, `rotateDatabasePassword`, `deleteDatabase` | `server.databases.*` |
| `listSchedules`, `getSchedules`, `getSchedule`, `createSchedule`, `updateSchedule`, `deleteSchedule`, `runSchedule`, `enableSchedule`, `disableSchedule` | `server.schedules.*` |
| `getSubusers` | `server.users.getSubusers` |
| `getAllocations` | `server.network.getAllocations` |
