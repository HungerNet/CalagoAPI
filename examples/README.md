# Examples

| Folder | What | Runs |
| --- | --- | --- |
| [extensions/](extensions/README.md) | the extension system, one feature per script, plus a pip-installable template | offline (`python examples/extensions/01_basic_extension.py`) |
| [minecraft/](minecraft/README.md) | `calagoapi-minecraft`: connecting HungerBridge, commands and console, monitoring, an async bot | against your panel (environment variables); without them they print how to run |

Every script here is run by the test suite: the extension examples directly, the
Minecraft examples' `main()` functions against a fake panel and a fake HungerBridge.
They follow the [tutorials](../docs/tutorials/README.md).
