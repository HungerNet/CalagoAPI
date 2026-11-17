# Extension examples

Runnable, heavily commented examples of the CalagoAPI extension system. Every numbered
script runs offline (no panel needed) and targets the game-agnostic `Server` class.

```bash
pip install -e .            # from the repository root
python examples/extensions/01_basic_extension.py
```

| Script | Shows | Tutorial |
| --- | --- | --- |
| [01_basic_extension.py](01_basic_extension.py) | The smallest extension: one method, `register()`, `enable()` | 07 |
| [02_method_extensions.py](02_method_extensions.py) | Methods on base classes and several classes, `name=`, calling siblings, async | 07 |
| [03_property_extensions.py](03_property_extensions.py) | Read-only properties and properties with setters | 07 |
| [04_service_extensions.py](04_service_extensions.py) | Services (`@classExtension`), caching, per-object state, config | 08 |
| [05_dependencies.py](05_dependencies.py) | Dependencies, optional dependencies, missing and circular errors | 09 |
| [06_direct_mode.py](06_direct_mode.py) | Direct mode and conflict errors | 08 |
| [07_namespace_mode.py](07_namespace_mode.py) | Namespace mode, overriding the mode | 08 |
| [08_aliases.py](08_aliases.py) | Renaming an extension with aliases and deprecation warnings | 09 |
| [09_configuration_and_lifecycle.py](09_configuration_and_lifecycle.py) | Config, `validateConfig`, `onEnable`, re-enabling, introspection | 09 |
| [packaged_extension/](packaged_extension/) | A complete pip-installable extension with an entry point: copy it to start your own | 06, 10 |

Each numbered script is a single file, so it uses `register()`. Published extensions
use an entry point instead (see `packaged_extension/pyproject.toml`), so their users only
write `enable('...')`.

Reference: [docs/extensions.md](../../docs/extensions.md). A full game extension built
the same way: [calagoapi-minecraft](../../src/extensions/calagoapi-minecraft/README.md).
