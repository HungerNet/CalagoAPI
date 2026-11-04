'''
Example 8: aliases (renaming an extension without breaking users).

Run it:
    python examples/extensions/08_aliases.py

Scenario: an extension was published as "version_changer". The author renames it
to "minecraft_version_manager". Existing code still calls
enable('version_changer'), so the old id becomes an alias.

Covers:
    - plain aliases (no warning)
    - deprecated aliases (ExtensionDeprecationWarning pointing at your code)
    - both names returning the same extension instance
    - ids and aliases must be globally unique
'''
import warnings

from calagoapi.extensions import (
    Alias,
    Extension,
    ExtensionConflictError,
    ExtensionMetadata,
    enable,
    is_enabled,
    register,
)

# DeprecationWarnings are hidden by default outside __main__; show them all here.
warnings.simplefilter('always')


class MinecraftVersionManager(Extension):
    extension_id = 'minecraft_version_manager'       # the new, public id
    aliases = [
        'mc_versions',                                # a plain alias: no warning
        Alias('old_version_tool', deprecated=True,    # an old name being phased out
              message='The old name will stop working in 3.0.'),
    ]
    metadata = ExtensionMetadata(author='you', version='2.0.0', schema=1)
    members = []


register(MinecraftVersionManager)

first = enable('minecraft_version_manager')
second = enable('mc_versions')                     # same extension, no warning
third = enable('old_version_tool')                 # same extension, warns
print(first is second is third)                    # True: one extension, one instance
print(is_enabled('old_version_tool'))              # True

# Ids and aliases share one global namespace. Another extension cannot claim
# a name that is already taken:
class Impostor(Extension):
    extension_id = 'impostor'
    aliases = ['mc_versions']
    members = []


try:
    register(Impostor)
except ExtensionConflictError as e:
    print('ExtensionConflictError:', e)

# For published packages, also keep the old entry point name if you can:
#
#   [project.entry-points."calagoapi"]
#   minecraft_version_manager = "my_package.extension:MinecraftVersionManager"
#
# If an entry point is not found by name, CalagoAPI loads every installed
# extension once and checks their aliases, so a single entry point still works.
