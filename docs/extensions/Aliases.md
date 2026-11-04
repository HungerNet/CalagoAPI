# Aliases

Aliases are extra names an extension can be enabled with. Their main use is
**renaming an extension without breaking its users**.

```python
class VersionChangerExtension(Extension):
    extension_id = 'minecraft_version_manager'   # the new id
    aliases = ['version_changer']                # the old id keeps working
```

```python
enable('version_changer')              # works
enable('minecraft_version_manager')    # works, same extension, same instance
```

Runnable example: [08_aliases.py](../../examples/extensions/08_aliases.py).

## Deprecated aliases

Use `Alias(..., deprecated=True)` to tell users to move to the new id:

```python
from calagoapi.extensions import Alias

aliases = [
    'mc_versions',                                     # plain alias, no warning
    Alias('version_changer', deprecated=True,
          message='The old name will stop working in 3.0.'),
]
```

Using a deprecated alias emits an `ExtensionDeprecationWarning` (a
`DeprecationWarning`) that points at the user's `enable()` line:

```text
app.py:12: ExtensionDeprecationWarning: Extension name 'version_changer' is deprecated,
use 'minecraft_version_manager' instead. The old name will stop working in 3.0.
```

Python hides `DeprecationWarning`s outside `__main__` by default. Run with
`python -W default` (or `-W error` in tests) to see them everywhere.

## Renaming an extension, step by step

1. Change `extension_id` to the new id.
2. Add the old id to `aliases` (deprecated or not).
3. In `pyproject.toml`, rename the entry point to the new id:

   ```toml
   [project.entry-points."calagoapi"]
   minecraft_version_manager = "my_package.extension:VersionChangerExtension"
   ```

   Old code calling `enable('version_changer')` still works: when no entry point
   has that name, CalagoAPI loads every installed extension once and finds the
   alias inside the class. (You may keep a second entry point with the old name
   pointing at the same class to skip that scan.)
4. If the namespace name matters to your users, set `namespace` explicitly:
   it defaults to the id, so renaming the id would move `server.version_changer`
   to `server.minecraft_version_manager` in namespace mode.

   ```python
   namespace = 'version_changer'
   ```

5. Release, and document the rename in your changelog.

## Rules

- Ids and aliases share **one global namespace**. An alias equal to another
  extension's id or alias is an `ExtensionConflictError` when the second
  extension is loaded.
- An alias must look like an id (lowercase letters, digits, `_`).
- An alias cannot equal its own extension's id.
- Everything that accepts an id accepts an alias: `enable()`, `get_extension()`,
  `is_enabled()`, `dependencies`, `registry.registrations(owner=...)`.
- Re-enabling through an alias is the same as through the id: same instance,
  same configuration rules.

## Common mistakes

- **Forgetting the namespace** when renaming (step 4).
- **Taking someone else's old name** as an alias: it conflicts as soon as both
  are installed. Only alias names you have published yourself.
- **Removing an alias too early**: keep deprecated aliases for at least one major
  version.
