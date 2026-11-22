# Minecraft examples

Examples for [calagoapi-minecraft](../../src/extensions/calagoapi-minecraft/README.md),
matching the [Minecraft tutorials](../../docs/tutorials/README.md#track-3-minecraft).

```bash
pip install calagoapi calagoapi-minecraft
export CALAGOPUS_URL=https://panel.example.com CALAGOPUS_API_KEY=c7sp_... MC_SERVER=abc123
export HB_URL=http://10.0.0.5:1913 HB_TOKEN_ID=calagoapi HB_TOKEN_SECRET=9f2c...   # see 01_connect.py for creating a token
python examples/minecraft/03_monitoring.py
```

Without `CALAGOPUS_URL` each script only prints this setup. They are read-only, except for
chat messages (`say`, `broadcast`), `save-all`, log lines (`06`), `01_connect.py` creating a
token when none is set, and `05_install_bridge.py` (installs the jar and restarts).

| Script | Shows | Tutorial |
| --- | --- | --- |
| [01_connect.py](01_connect.py) | the two channels, `createBridgeToken()`, `server.bridge` | 11 |
| [02_commands_and_console.py](02_commands_and_console.py) | `sendCommand()` output and `show_console`, chat helpers, `streamConsole()` | 12 |
| [03_monitoring.py](03_monitoring.py) | panel resources vs JVM information, TPS/MSPT, warnings | 13 |
| [05_install_bridge.py](05_install_bridge.py) | `installBridge(minecraft_version, loader)` from Modrinth, `waitForBridge()` (`MC_VERSION`, `MC_LOADER`) | 14 |
| [04_async_welcome_bot.py](04_async_welcome_bot.py) | `AsyncPanel`, concurrent console stream and metrics | 15 |
| [06_bot_logging.py](06_bot_logging.py) | `log()` with level, thread, logger and `normalize`; `LogEvent`s from `streamLogs()` | 16 |

Each script's `main()` is also run by
`src/extensions/calagoapi-minecraft/tests/test_minecraft_examples.py` against a fake panel,
a fake HungerBridge and a fake Modrinth.
