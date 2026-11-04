# Creating extensions

This guide builds a complete, installable extension step by step. It assumes you
have read [Extensions](01_Extensions_Overview.md).

A finished version of what we build is in
[examples/extensions/packaged_extension/](../../examples/extensions/packaged_extension/).

## 1. The package layout

```text
calagoapi-server-notes/
├── pyproject.toml
├── README.md
└── calagoapi_server_notes/
    ├── __init__.py
    └── extension.py
```

Naming convention:

| What | Convention | Example |
| --- | --- | --- |
| PyPI name | `calagoapi-<name>` | `calagoapi-server-notes` |
| Python package | `calagoapi_<name>` | `calagoapi_server_notes` |
| Extension id | `<name>` in snake_case | `server_notes` |

## 2. pyproject.toml

```toml
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "calagoapi-server-notes"
version = "1.0.0"
requires-python = ">=3.9"
dependencies = ["calagoapi>=1.0.dev2"]

[project.entry-points."calagoapi"]
server_notes = "calagoapi_server_notes.extension:ServerNotesExtension"

[tool.setuptools]
packages = ["calagoapi_server_notes"]
```

The `[project.entry-points."calagoapi"]` table is what makes
`enable('server_notes')` work without an import. See [Discovery](Discovery.md).

## 3. The members

Decide what the extension adds, and declare it with a decorator:

```python
# calagoapi_server_notes/extension.py
from calagoapi import GenericServer
from calagoapi.extensions import class_extension, property_extension


@class_extension(GenericServer, 'notes')
class ServerNotes:
    def __init__(self, server):
        self.server = server

    def add(self, text):
        ...

    def list(self):
        ...


@property_extension(GenericServer)
def lastNote(self):
    notes = self.notes.list()
    return notes[-1] if notes else None
```

| Decorator | Adds | Guide |
| --- | --- | --- |
| `@method(Target)` | a method | [Method extensions](Method_Extensions.md) |
| `@property_extension(Target)` | a property | [Property extensions](Property_Extensions.md) |
| `@class_extension(Target, 'name')` | a service | [Service extensions](Service_Extensions.md) |

Decorators have **no side effects**. They label the function or class, nothing
more. The classes are only changed when a user calls `enable()`.

Which class to target:

| Target | Reaches |
| --- | --- |
| `GenericServer` | every server, including Minecraft servers |
| `MinecraftServer` | Minecraft servers only (`getMinecraftServer()`) |
| `Panel` | the panel object |
| `FileManager`, `BackupManager`, ... | `server.files`, `server.backups`, ... |
| `ExtensionManager`, `Admin`, ... | `panel.admin.extensions`, `panel.admin`, ... |

## 4. The Extension class

```python
from calagoapi.extensions import ConfigurationError, Extension, ExtensionMetadata


class ServerNotesExtension(Extension):
    extension_id = 'server_notes'
    metadata = ExtensionMetadata(
        author='you',
        version='1.0.0',
        schema=1,
        description='Keep notes on servers',
        package='calagoapi-server-notes',
    )
    aliases = []                    # other names, see aliases.md
    dependencies = []               # other extensions, see dependencies.md
    default_mode = 'direct'         # or 'namespace'
    default_config = {'path': 'calagoapi-notes.json'}
    secret_config = ()              # config keys to mask in diagnostics, e.g. ('token',)

    def validate_config(self, config):
        if not config['path'].endswith('.json'):
            raise ConfigurationError('server_notes: path must be a .json file')
        return config

    def on_enable(self):
        pass
```

Every attribute:

| Attribute | Required | Meaning |
| --- | --- | --- |
| `extension_id` | yes | Public id for `enable()`. Lowercase letters, digits, `_`, starting with a letter. Globally unique. |
| `metadata` | recommended | `ExtensionMetadata(author, version, schema=1, description, package, homepage)` |
| `aliases` | no | Other ids (strings or `Alias(...)`), see [Aliases](Aliases.md) |
| `dependencies` | no | Extension ids (strings or `Dependency(...)`), see [Dependencies](Dependencies.md) |
| `default_mode` | no | `'direct'` (default) or `'namespace'` |
| `namespace` | no | Attribute used in namespace mode, defaults to `extension_id` |
| `default_config` | no | Every config key with its default |
| `allow_unknown_config` | no | Accept keys missing from `default_config` (default `False`) |
| `secret_config` | no | Keys shown as `***` in `describe()` and errors |
| `members` | no | Explicit list of decorated members; `None` collects them automatically |

You never create the instance yourself. CalagoAPI does it in `enable()`, then
sets `config` (read-only), `mode`, `namespace` and `enabled_by` on it.

### Where members come from

With `members = None` (the default), CalagoAPI collects every decorated member
found in the module that defines the Extension class, including members
imported there from other modules **of the same package**:

```python
# calagoapi_server_notes/extension.py
from calagoapi_server_notes.service import ServerNotes   # collected
from calagoapi_server_notes.props import lastNote        # collected
```

Members imported from *other* packages (for example another extension) are not
collected. Set `members = [...]` to be explicit, and always do so when one module
defines more than one extension.

## 5. Lifecycle

`enable()` runs these steps, in order, under a lock:

1. find the extension (and warn if a deprecated alias was used);
2. enable its dependencies;
3. create the Extension instance;
4. merge the config with `default_config`, call `validate_config(config)`;
5. collect members and check every name for conflicts;
6. add the members to the classes;
7. call `on_enable()`.

If step 4 or 5 fails, nothing was changed. If step 6 or 7 fails, everything
added in step 6 is removed again and the error is raised. So an extension is
either fully enabled or not at all.

Hooks:

| Hook | Use it to |
| --- | --- |
| `validate_config(self, config)` | Check and normalize config. Return the config (or `None` for "unchanged"); raise `ConfigurationError`. |
| `on_enable(self)` | One-time setup after the members exist (open a shared client, log a message). |

Future hooks will be added the same way, as optional methods with a default
implementation, so existing extensions keep working.

## 6. Reading the configuration

Inside any member, ask the Extension class:

```python
@method(MinecraftServer)
def installVersion(self, build):
    config = VersionChangerExtension.get().config
    if config['auto_backup']:
        ...
```

`Extension.get()` returns the enabled instance (and raises
`ExtensionNotEnabledError` otherwise). From outside the extension, use
`get_extension('id')`.

## 7. Trying it without publishing

In a script or notebook, `register()` replaces the entry point:

```python
from calagoapi.extensions import enable, register
from calagoapi_server_notes.extension import ServerNotesExtension

register(ServerNotesExtension)
enable('server_notes')
```

Or install your package in editable mode, and then `enable()` finds it by itself:

```bash
pip install -e .
python -c "from calagoapi.extensions import enable; enable('server_notes')"
```

## 8. Testing

Use a private registry so tests do not leak into each other, and remove what it
installed afterwards:

```python
import pytest
from calagoapi.extensions import ExtensionRegistry
from calagoapi_server_notes.extension import ServerNotesExtension


@pytest.fixture
def extensions():
    registry = ExtensionRegistry()
    registry._entry_points = {}        # ignore installed extensions
    yield registry
    registry._reset_for_tests()        # test-only: undo every change


def test_notes(extensions, tmp_path):
    extensions.register(ServerNotesExtension)
    extensions.enable('server_notes', config={'path': str(tmp_path / 'n.json')})
    ...
```

Because decorated functions stay normal functions, you can also call them
directly: `lastNote(server)`.

The first-party extensions' tests (`src/extensions/*/tests/`) are complete
examples, including a fake panel.

## 9. Publishing

```bash
python -m build
twine upload dist/*
```

Before publishing:

- [ ] `extension_id` is unique (search PyPI for `calagoapi-` packages)
- [ ] `metadata.version` matches your package version
- [ ] the entry point name equals `extension_id`
- [ ] `default_config` lists every key, with safe defaults
- [ ] tokens/passwords are in `secret_config`
- [ ] the README lists every member, the config keys, and the default mode
- [ ] `dependencies` in pyproject.toml include the packages of your extension dependencies

## Best practices

- **Prefer methods over properties for anything slow.** A property that makes an
  HTTP request runs on every read and blocks in async code.
- **Write plain `def` methods.** They work with `Panel` and are awaitable on
  `AsyncPanel` automatically. `async def` methods only work with `AsyncPanel`.
- **Call sibling members directly** (`getInstalledVersion(self)`), not through
  `self.getInstalledVersion()`. In namespace mode the second form does not reach
  your extension.
- **Choose specific names.** `server.players()` is likely to clash with another
  extension; `server.hungerbridge.players()` will not. Use a service or
  `default_mode = 'namespace'` for short names.
- **Keep CalagoAPI's style**: camelCase methods, snake_case attributes, docstrings
  with an example.
- **Never rely on import side effects.** Importing your package must not change
  anything; only `enable()` does.

## Common mistakes

| Mistake | Symptom | Fix |
| --- | --- | --- |
| Using a name CalagoAPI already has (`say`, `files`, `console`) | `ExtensionConflictError` naming `calagoapi` as owner | Pick another name or use namespace mode |
| Two extensions in one module without `members` | `ExtensionDefinitionError: ... already belongs to extension` | Give each extension an explicit `members` list |
| `@method` without parentheses | `ExtensionDefinitionError: Use @method(TargetClass)` | `@method(MinecraftServer)` |
| Mutating `self.config` | `TypeError` | Config is read-only; keep state on the instance or in a service |
| Forgetting the entry point | `ExtensionNotFoundError` after `pip install` | Add `[project.entry-points."calagoapi"]` and reinstall |
| Entry point name differs from the id | Works, but every unknown name loads all extensions | Use the id as the entry point name |
