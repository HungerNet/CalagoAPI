from calagoapi.backups.backup import Backup, BackupGroup
from calagoapi.utils.model import idOf


class BackupManager:
    '''
    Backup management for one server, available as `server.backups`.

    Args:
        server: The server to manage backups for.

    Example:
        backup = server.backups.createBackup('pre-update')
        for backup in server.backups.getBackups():
            print(backup.getName(), backup.getStatus())
    '''
    def __init__(self, server):
        self.server = server
        self.api = server.panel.api.backups

    @property
    def server_id(self):
        return self.server.server_id

    def _wrap(self, data):
        return Backup(self.server, data)

    # backups
    def getBackups(self, search: str = None, kind: str = None, ungrouped: bool = None, page: int = None, per_page: int = None):
        '''
        Lists the server's backups.

        Args:
            search: Filter by name.
            kind: 'server' for file backups or 'database_instance' for database backups.
            ungrouped: Only backups that are not in a backup group.
            page: Only fetch this page. By default every backup is returned.
            per_page: Page size.

        Returns:
            A Page (list) of Backup objects.
        '''
        return self.api.list(self.server_id, search, ungrouped, kind, page=page, per_page=per_page).map(self._wrap)

    def getSystemBackups(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists backups made by panel-wide backup policies rather than by the server's users.'''
        return self.api.system(self.server_id, search, page, per_page).map(self._wrap)

    def getBackup(self, backup_id: str) -> Backup:
        '''
        Returns a single backup.

        Example:
            backup = server.backups.getBackup('5f0c...')
        '''
        return self._wrap(self.api.get(self.server_id, backup_id))

    def getLatestBackup(self, successful_only: bool = True) -> Backup:
        '''
        Returns the most recent backup, or None.

        Args:
            successful_only: Skip backups that failed or are still running.
        '''
        backups = [b for b in self.getBackups() if b.isSuccessful() or not successful_only]
        return max(backups, key=lambda b: b.getCreated() or '', default=None)

    def createBackup(self, name: str = None, ignored_files: list = None, group=None, database_instance=None) -> Backup:
        '''
        Starts a new backup.

        The backup runs in the background, use `backup.waitUntilComplete()` to wait for it.

        Args:
            name: Backup name. Calagopus generates one when omitted.
            ignored_files: Extra ignore patterns, e.g. ['logs/*', '*.tmp'].
            group: BackupGroup or group UUID to put the backup in.
            database_instance: Back up a database instance instead of the server files.

        Returns:
            The new Backup.

        Example:
            backup = server.backups.createBackup('before-update', ignored_files=['logs'])
        '''
        return self._wrap(self.api.create(self.server_id, name, ignored_files, idOf(group), idOf(database_instance)))

    def deleteBackup(self, backup_id: str) -> None:
        '''Deletes a backup.'''
        return self.api.delete(self.server_id, idOf(backup_id))

    def deleteBackups(self, backup_ids: list) -> dict:
        '''
        Deletes several backups at once.

        Returns:
            dict with how many were queued and skipped.
        '''
        return self.api.deleteMany(self.server_id, [idOf(b) for b in backup_ids])

    def lockBackups(self, backup_ids: list) -> dict:
        '''Locks several backups at once.'''
        return self.api.updateMany(self.server_id, [idOf(b) for b in backup_ids], locked=True)

    def unlockBackups(self, backup_ids: list) -> dict:
        '''Unlocks several backups at once.'''
        return self.api.updateMany(self.server_id, [idOf(b) for b in backup_ids], locked=False)

    def moveBackups(self, backup_ids: list, group) -> dict:
        '''Moves several backups into a backup group.'''
        return self.api.updateMany(self.server_id, [idOf(b) for b in backup_ids], backup_group_uuid=idOf(group))

    def restoreBackup(self, backup_id: str, truncate_directory: bool = False, restore_startup: bool = None) -> None:
        '''
        Restores the server from a backup.

        Args:
            backup_id: Backup to restore.
            truncate_directory: Delete all current files first.
            restore_startup: Also restore the startup command and variables.
        '''
        return self.api.restore(self.server_id, idOf(backup_id), truncate_directory, restore_startup)

    def downloadBackup(self, backup_id: str, destination: str = None, archive_format: str = None):
        '''
        Downloads a backup.

        Args:
            destination: Local path to save to. If omitted the bytes are returned.
            archive_format: Optional archive format.
        '''
        return Backup(self.server, {'uuid': idOf(backup_id)}).download(destination, archive_format)

    def getDownloadUrl(self, backup_id: str, archive_format: str = None) -> str:
        '''Returns a signed, temporary download URL for a backup.'''
        return self.api.downloadUrl(self.server_id, idOf(backup_id), archive_format)

    def getUsage(self) -> dict:
        '''Returns how much backup storage and how many backup slots are in use.'''
        return self.api.usage(self.server_id)

    def unlockRestore(self) -> None:
        '''Clears a stuck backup-restore lock on the server.'''
        return self.api.unlock(self.server_id)

    # groups
    def getBackupGroups(self) -> list:
        '''Returns the server's backup groups.'''
        return [BackupGroup(self.server, data) for data in self.api.groups(self.server_id)]

    def getBackupGroup(self, group_id_or_name: str) -> BackupGroup:
        '''Returns a backup group by UUID or name, or None.'''
        for group in self.getBackupGroups():
            if group_id_or_name in (group.getUUID(), group.getName()):
                return group
        return None

    def createBackupGroup(self, name: str, retention: dict = None) -> BackupGroup:
        '''
        Creates a backup group.

        Args:
            name: Group name.
            retention: Optional retention policy with keys count, days, daily, weekly, monthly, yearly.

        Example:
            server.backups.createBackupGroup('weekly', retention={'weekly': 4})
        '''
        return BackupGroup(self.server, self.api.createGroup(self.server_id, name, retention))

    def deleteBackupGroup(self, group, lock_backups: bool = None) -> None:
        '''Deletes a backup group.'''
        return self.api.deleteGroup(self.server_id, idOf(group), lock_backups)

    def orderBackupGroups(self, groups: list) -> None:
        '''Sets the display order of backup groups.'''
        return self.api.orderGroups(self.server_id, [idOf(g) for g in groups])
