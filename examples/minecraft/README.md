# Minecraft examples

Examples for [calagoapi-minecraft](../../src/extensions/calagoapi-minecraft/README.md),
matching the [Minecraft tutorials](../../docs/tutorials/README.md#track-3-minecraft).

```bash
pip install calagoapi calagoapi-minecraft
export CALAGOPUS_URL=https://panel.example.com CALAGOPUS_API_KEY=c7sp_... MC_SERVER=abc123
export HB_URL=http://10.0.0.5:1913 HB_TOKEN=calagoapi:9f2c...      # see 01_connect.py for creating a token
python examples/minecraft/03_monitoring.py
```

Without `CALAGOPUS_URL` each script only prints this setup. They are read-only, except for
chat messages (`say`, `broadcast`), `save-all`, and `01_connect.py` creating a token
when `HB_TOKEN` is not set.

| Script | Shows | Tutorial |
| --- | --- | --- |
| [01_connect.py](01_connect.py) | the two channels, `createBridgeToken()`, bridge info | 11 |
| [02_commands_and_console.py](02_commands_and_console.py) | `sendCommand()` output, chat helpers, `streamConsole()` | 12 |
| [03_monitoring.py](03_monitoring.py) | panel resources vs JVM information, TPS/MSPT, warnings | 13 |
| [04_async_welcome_bot.py](04_async_welcome_bot.py) | `AsyncPanel`, concurrent console stream and metrics | 15 |

Each script's `main()` is also run by
`src/extensions/calagoapi-minecraft/tests/test_minecraft_examples.py` against a fake panel
and a fake HungerBridge.
