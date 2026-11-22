# CalagoAPI tutorials

Fifteen tutorials in three tracks. Each one builds a small, complete program and then
explains the part of the architecture that makes it work. Work through them in order:
every tutorial uses what the previous ones introduced. The [reference guides](../README.md)
list every method; the tutorials teach how the pieces fit together.

```
Track 1: the core SDK           Track 2: extending CalagoAPI        Track 3: Minecraft
(any game)                      (any game)                          (calagoapi-minecraft)

01 First script                 06 Using extensions                 11 Minecraft setup
02 Server control       ──►     07 Your first extension     ──►     12 Commands and console
03 Live console                 08 Services and namespaces          13 Monitoring
04 Files and backups            09 Configuration and dependencies   14 Versions and installs
05 Going async                  10 Packaging and publishing         15 Capstone: community bot
```

## Track 1: the core SDK

Everything here works for every game the panel hosts.

| # | Tutorial | You build | You learn |
| --- | --- | --- | --- |
| 01 | [First script](basics/01-first-script.md) | a server status table | `Panel`, managers, objects, `Server` |
| 02 | [Server control](basics/02-server-control.md) | a safe-restart script | power actions, waiting for states, the resource cache |
| 03 | [Live console](basics/03-live-console.md) | a startup watcher and an error relay | the daemon websocket, `streamConsole()`, callbacks |
| 04 | [Files and backups](basics/04-files-and-backups.md) | a "backup, then edit config" tool | managers, `File` objects, waiting for backups |
| 05 | [Going async](basics/05-going-async.md) | a concurrent status checker | `AsyncPanel`, worker threads, the native async console |

## Track 2: extending CalagoAPI

How separately installed packages add features, and how to write one.

| # | Tutorial | You build | You learn |
| --- | --- | --- | --- |
| 06 | [Using extensions](extensions/06-using-extensions.md) | a script that uses an installed extension | `enable()`, modes, config, introspection |
| 07 | [Your first extension](extensions/07-your-first-extension.md) | a `monitoring` extension | `@method`, `@propertyExtension`, class patching, testing |
| 08 | [Services and namespaces](extensions/08-services-and-namespaces.md) | a per-server `notes` service | `@classExtension`, caching, namespace mode, async |
| 09 | [Configuration and dependencies](extensions/09-configuration-and-dependencies.md) | an `alerts` extension built on `monitoring` | `default_config`, `validateConfig`, `onEnable`, dependencies, aliases |
| 10 | [Packaging and publishing](extensions/10-packaging-and-publishing.md) | a pip-installable package | entry points, discovery, conflicts, game-extension pattern |

## Track 3: Minecraft

Requires `pip install calagoapi-minecraft` and, for most of it, the
[HungerBridge](https://modrinth.com/project/hungerbridge) plugin/mod on the server.
The code of these tutorials is in [examples/minecraft/](../../examples/minecraft/README.md)
and is tested against a fake panel and a fake HungerBridge.

| # | Tutorial | You build | You learn |
| --- | --- | --- | --- |
| 11 | [Minecraft setup](minecraft/11-minecraft-setup.md) | a connection check that creates its own bridge token | `MinecraftServer`, the two channels, HungerBridgePy |
| 12 | [Commands and console](minecraft/12-commands-and-console.md) | a command runner and a join watcher | `sendCommand()` output, `streamConsole()`, `sendPanelCommand()` |
| 13 | [Monitoring](minecraft/13-monitoring.md) | a health report | `getRAM()` vs `server.bridge.getMemoryStats()`, TPS/MSPT |
| 14 | [Installing HungerBridge](minecraft/14-installing-hungerbridge.md) | an install-and-upgrade script | `installBridge(minecraft_version, loader)`, Modrinth releases, `waitForBridge()` |
| 15 | [Capstone: community bot](minecraft/15-community-bot.md) | an asyncio bot | every track together |
| 16 | [Logging from your bot](minecraft/16-logging-from-your-bot.md) | a maintenance bot with its own log lines | `log(level, thread, logger, normalize)`, `LogEvent`s |

## Conventions used in the tutorials

- Code uses 4-space indentation, single quotes and f-strings, like CalagoAPI itself.
- Replace `https://panel.example.com`, `c7sp_...` and `abc123` with your panel URL, API
  key and a server id. Scripts that change things say so before they do.
- Methods are camelCase (`getServer()`), attributes and parameters snake_case
  (`server.server_id`, `per_page=`).
