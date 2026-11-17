'''
Example 8: aliases (renaming an extension without breaking users).

Run it:
    python examples/extensions/08_aliases.py

Scenario: an extension was published as "backup_tool". The author renames it to
"backup_manager". Existing code still calls enable('backup_tool'), so the old id
becomes an alias.

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
    isEnabled,
    register,
)

# DeprecationWarnings are hidden by default outside __main__; show them all here.
warnings.simplefilter('always')


class BackupManager(Extension):
    extension_id = 'backup_manager'                  # the new, public id
    aliases = [
        'backups_plus',                              # a plain alias: no warning
        Alias('backup_tool', deprecated=True,        # the old name being phased out
              message='The old name will stop working in 3.0.'),
    ]
    metadata = ExtensionMetadata(author='you', version='2.0.0', schema=1)
    members = []


register(BackupManager)

first = enable('backup_manager')
second = enable('backups_plus')                      # same extension, no warning
third = enable('backup_tool')                        # same extension, warns
print(first is second is third)                      # True: one extension, one instance
print(isEnabled('backup_tool'))                      # True


# Ids and aliases share one global namespace. Another extension cannot claim
# a name that is already taken:
class Impostor(Extension):
    extension_id = 'impostor'
    aliases = ['backups_plus']
    members = []


try:
    register(Impostor)
except ExtensionConflictError as e:
    print(f'ExtensionConflictError: {e}')

# For published packages, also keep the old entry point name if you can:
#
#   [project.entry-points."calagoapi"]
#   backup_manager = "my_package.extension:BackupManager"
#
# If an entry point is not found by name, CalagoAPI loads every installed
# extension once and checks their aliases, so a single entry point still works.
#
# When the API changed completely, an alias would be misleading. Let the old id
# fail instead and say what replaced it in your release notes (CalagoAPI 2.0 did
# this for 'hungerbridge' and 'version_changer', which became 'minecraft').
