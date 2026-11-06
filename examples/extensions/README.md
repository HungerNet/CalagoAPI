# Extension examples

Runnable, heavily commented examples of the CalagoAPI extension system. Every
numbered script runs offline (no panel needed) except `10_first_party_extensions.py`.

```bash
pip install -e .            # from the repository root
python examples/extensions/01_basic_extension.py
```

| Script | Shows |
| --- | --- |
| [01_basic_extension.py](01_basic_extension.py) | The smallest extension: one method, `register()`, `enable()` |
| [02_method_extensions.py](02_method_extensions.py) | Methods on several classes, `name=`, calling siblings, async |
| [03_property_extensions.py](03_property_extensions.py) | Read-only properties and properties with setters |
| [04_service_extensions.py](04_service_extensions.py) | Services (`@class_extension`), caching, per-object state, config |
| [05_dependencies.py](05_dependencies.py) | Dependencies, optional dependencies, missing and circular errors |
| [06_direct_mode.py](06_direct_mode.py) | Direct mode and conflict errors |
| [07_namespace_mode.py](07_namespace_mode.py) | Namespace mode, overriding the mode |
| [08_aliases.py](08_aliases.py) | Renaming an extension with aliases and deprecation warnings |
| [09_configuration_and_lifecycle.py](09_configuration_and_lifecycle.py) | Config, `validate_config`, `on_enable`, re-enabling, introspection |
| [10_first_party_extensions.py](10_first_party_extensions.py) | `version_changer` and `hungerbridge` against a real panel (read-only) |
| [packaged_extension/](packaged_extension/) | A complete pip-installable extension with an entry point: copy it to start your own |

Each numbered script is a single file, so it uses `register()`. Published
extensions use an entry point instead (see `packaged_extension/pyproject.toml`),
so their users only write `enable('...')`.

The guides are in [docs/extensions/](../../docs/extensions/01_Extensions_Overview.md).
