# Migrating calagoapi-minecraft 1.x to 2.0

calagoapi-minecraft 2.0 follows HungerBridge 5 and HungerBridgePy 2 (protocol v2). Update
the server jar too: `server.installBridge(minecraft_version=..., loader=...)` installs
HungerBridge 5 from Modrinth. Backward compatibility was deliberately not kept.

## Tokens

```python
# 1.x
enable('minecraft', config={'bridge_token': 'bot:9f2c...'})
MinecraftServer(panel, 'abc123', bridge_token='bot:9f2c...')
server.connectBridge(url, 'bot:9f2c...')
token = server.createBridgeToken()            # 'bot:9f2c...'

# 2.0
enable('minecraft', config={'bridge_token_id': 'bot', 'bridge_token_secret': '9f2c...'})
MinecraftServer(panel, 'abc123', bridge_token_id='bot', bridge_token_secret='9f2c...')
server.connectBridge(url, token_id='bot', token_secret='9f2c...')
token = server.createBridgeToken()            # hungerbridge.Credentials: token.token_id, token.token_secret
```

## Installing HungerBridge

```python
# 1.x: detected from the Version Changer, the running bridge, the egg name or startup variables
server.installBridge()
server.installBridge('1.21.11', 'PURPUR', release='v4-alpha.94')

# 2.0: explicit, resolved on Modrinth
server.installBridge(minecraft_version='1.21.11', loader='purpur')
server.installBridge(minecraft_version='1.21.11', loader='paper', version='5-alpha.1')
```

It returns a `hungerbridge.BridgeRelease` (`version_number`, `filename`, `url`, `sha512`,
`directory`) instead of a `ReleaseAsset`. `findBridgeRelease()` is gone: use
`hungerbridge.findRelease(minecraft_version=..., loader=...)`. The `release`, `repository`
and `github_api` config keys are removed.

## Version Changer

The Minecraft Version Changer integration is removed: `server.versions`,
`panel.minecraft.versionChanger`, `VersionManager`, `VersionChangerAdmin`,
`VersionChangerAPI`, `PANEL_EXTENSION` and the `auto_backup`, `backup_name` and
`backup_timeout` config keys. Change the server software with the panel or your egg; for a
backup first, use `server.backups.createBackup()` (tutorial 14 shows the full flow).

## Commands and console

| 1.x | 2.0 |
|---|---|
| `sendCommand(cmd, silent=True)` | removed (output is always returned) |
| `sendCommand(cmd, showConsole=True)` | `sendCommand(cmd, show_console=True)`; without it the output stays off the server console (in 1.x it was always printed) |
| `streamConsole(..., sanitize=True)` | no `sanitize`: lines are always plain text |
| lines `[12:00:05 INFO]: message` | `[12:00:05] [Server thread/INFO]: message` (plus `[logger]` for non-Minecraft loggers) |
| `history` ≤ 200 | `history=True` = everything HungerBridge keeps (1000) |

## Methods moved to server.bridge

These only renamed HungerBridgePy calls and are removed; call HungerBridgePy directly:

| 1.x `server.` | 2.0 `server.bridge.` |
|---|---|
| `getBridgeInfo()`, `getPlatform()`, `getMinecraftVersion()` | `getServerMeta()`, `getPlatform()`, `getMinecraftVersion()` |
| `getBridgeTokenInfo()` | `getTokenInfo()` |
| `writeLog(message, level, thread)` | `log(message, level, thread, logger=None, normalize=False)` |
| `broadcast(message, prefix)` | `broadcast(message, prefix)` |
| `getPlayers()`, `getPlayerCount()`, `getMaxPlayers()` | the same names |
| `getTPS(mode)`, `getMSPT()` | `getTPS(window)`, `getMSPT()` |
| `getPerformance()` | `getTPSStats()`, `getMSPT()`, `getPlayerStats()` |
| `getWorldTime()`, `getWorldTimeInfo()`, `getWeather()` | `getWorldTime()`, `getWorldTimeInfo()`, `getWorldWeather()` |
| `getLoadedChunks()`, `getLoadedEntities()` | the same names |
| `getMemoryInfo(unit)` (`used`, `total`, `free`, `max`) | `getMemoryStats(unit)` (`heap_used`, `heap_committed`, `heap_free`, `heap_max`) |
| `getProcessorInfo()` | `getCPUStats()` |
| `getThreadInfo()`, `getGarbageCollectorInfo()`, `getNetworkInfo()` | `getThreadStats()`, `getGCStats()`, `getNetworkStats()` |
| `getProcessInfo()`, `getJVMUptime()` | `getMemoryStats()["process_used"]`, `getUptime()` |

The panel's `getRAM()`, `getCPU()`, `getUptime()` and `stop()` are unchanged.
