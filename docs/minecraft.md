# Minecraft servers

`MinecraftServer` is a `GenericServer` with Minecraft helpers.

```python
server = panel.servers.getMinecraftServer('abc123')

# optional: the address players use, if it is not the allocation address
server = panel.servers.getMinecraftServer('abc123', server_domain='play.example.com', server_port=25565)
server.getAddress()  # 'play.example.com:25565'
```

You can also construct it directly: `MinecraftServer(panel, 'abc123')`.

## Console helpers

```python
server.say('Restarting in 5 minutes')        # same as broadcast()
server.tellraw('@a', {'text': 'Hello', 'color': 'gold'})
server.kick('Steve', 'AFK')
server.ban('Griefer', 'Griefing')
server.pardon('Griefer')
server.op('Alex')
server.deop('Alex')
server.whitelistAdd('Steve')
server.whitelistRemove('Steve')
server.saveAll()
```

## server.properties

Values are read and written as strings, booleans become `true`/`false`.
Comments and order are preserved. Changes apply after a restart.

```python
properties = server.getProperties()
print(properties['max-players'])

server.getProperty('difficulty', default='normal')
server.setProperty('pvp', False)
server.setProperties({'max-players': 100, 'motd': 'Welcome!'})
server.getMOTD()
server.setMOTD('Season 3 is live!')

server.acceptEula()
server.isEulaAccepted()
```

## Version changer

Calagopus ships the Minecraft Version Changer extension, which can install
any server build (Paper, Purpur, Fabric, Forge, Vanilla, ...). In CalagoAPI it
is provided by the `calagoapi-version-changer` extension package:

```bash
pip install calagoapi-version-changer
```

```python
from calagoapi.extensions import enable
enable('version_changer')                    # once, at startup

server.getInstalledVersion()                 # {'build': ..., 'latest': ...}, or None
server.installedVersion                      # the installed build, or None
server.isUpToDate()                          # True / False / None
server.getVersionTypes()                     # available types

versions = server.getVersions('PAPER', page=1, per_page=10)
builds = server.getBuilds('PAPER', '1.21.1', page=1, per_page=5)

server.installVersion(builds[0])                         # keeps your files
server.installVersion(builds[0], truncate_directory=True)  # clean install
```

Admins can configure the extension with
`panel.admin.extensions.getVersionChangerSettings()` and
`updateVersionChangerSettings(...)`.

Without `enable('version_changer')` these methods still exist (they used to be
built in) but emit an `ExtensionDeprecationWarning` and will be removed in a
future major release. See [First-party extensions](learning/first_party_extensions.md)
for every method and option (such as `auto_backup`).

## HungerBridge

The `calagoapi-hungerbridge` extension talks to the
[HungerBridge](https://github.com/hungernet/hungerbridge) mod inside the server:
commands without RCON, players, TPS, memory, and installing the mod itself.

```python
enable('hungerbridge', config={'token': 'bot:9f2c...'})

server.hungerbridge.players()          # ['Steve', 'Alex']
server.hungerbridge.tps()              # {'tps': 20.0, ...}
server.hungerbridge.run('list')        # console output lines
server.hungerbridge.install()          # downloads the right jar into plugins/ or mods/
```

## Example: safe update

```python
import time
from calagoapi.extensions import enable

enable('version_changer')

server.say('Updating in 1 minute')
time.sleep(60)
server.stop()
server.waitForOffline(timeout=120)

backup = server.createBackup('pre-update')
backup.waitUntilComplete()

latest = server.getBuilds('PAPER', '1.21.1', page=1, per_page=1)[0]
server.installVersion(latest)
server.start()
```
