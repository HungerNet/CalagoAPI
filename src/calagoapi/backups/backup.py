import time

from calagoapi.utils.model import Model, idOf
from calagoapi.utils.convert import formatBytes
from calagoapi.utils.exceptions import WaitTimeoutError


class Backup(Model):
    '''
    A server backup.

    Returned by `server.createBackup()`, `server.backups.getBackups()` and friends.

    Args:
        server: The server the backup belongs to.
        data: Raw backup data from Calagopus.

    Example:
        backup = server.createBackup('before-update')
        backup.waitUntilComplete()
        if backup.isSuccessful():
            print(backup.getName(), backup.getSize(formatted=True))
    '''
    def __init__(self, server, data: dict):
        super().__init__(server.panel, data)
        self.server = server

    @property
    def backup_id(self):
        return self.getUUID()

    # getters
    def getName(self) -> str:
        '''Returns the backup name.'''
        return self.data.get('name')

    def getSize(self, formatted: bool = False):
        '''
        Returns the backup size in bytes.

        Args:
            formatted: Return a human readable string like "1.2 GiB" instead.
        '''
        size = self.data.get('bytes')
        return formatBytes(size) if formatted else size

    def getFileCount(self) -> int:
        '''Returns how many files the backup contains.'''
        return self.data.get('files')

    def getChecksum(self) -> str:
        '''Returns the backup checksum, once completed.'''
        return self.data.get('checksum')

    def getKind(self) -> str:
        '''Returns "server" for file backups or "database_instance" for database backups.'''
        return self.data.get('kind')

    def getDatabaseType(self) -> str:
        '''Returns the database type for database backups, otherwise None.'''
        return self.data.get('database_type')

    def getGroupId(self) -> str:
        '''Returns the UUID of the backup group this backup is in, or None.'''
        return self.data.get('backup_group_uuid')

    def getIgnoredFiles(self) -> list:
        '''Returns the ignore patterns used when creating the backup.'''
        return self.data.get('ignored_files', [])

    def getCompleted(self) -> str:
        '''Returns when the backup finished, or None while it is running.'''
        return self.data.get('completed')

    def getStatus(self) -> str:
        '''
        Returns the backup status.

        Returns:
            'in_progress', 'successful' or 'failed'.
        '''
        if not self.data.get('completed'):
            return 'in_progress'
        return 'successful' if self.data.get('is_successful') else 'failed'

    # state checks
    def isCompleted(self) -> bool:
        '''Returns True once the backup has finished (successfully or not).'''
        return self.getStatus() != 'in_progress'

    def isInProgress(self) -> bool:
        '''Returns True while the backup is still being created.'''
        return self.getStatus() == 'in_progress'

    def isSuccessful(self) -> bool:
        '''Returns True if the backup completed successfully.'''
        return self.getStatus() == 'successful'

    def isFailed(self) -> bool:
        '''Returns True if the backup completed but failed.'''
        return self.getStatus() == 'failed'

    def isLocked(self) -> bool:
        '''Returns True if the backup is locked against deletion.'''
        return bool(self.data.get('is_locked'))

    def isBrowsable(self) -> bool:
        '''Returns True if the backup contents can be browsed.'''
        return bool(self.data.get('is_browsable'))

    def isStreaming(self) -> bool:
        '''Returns True if the backup can be streamed during download.'''
        return bool(self.data.get('is_streaming'))

    # actions
    def refresh(self) -> 'Backup':
        '''Re-fetches the backup from the panel.'''
        self.data = self.panel.api.backups.get(self.server.server_id, self.backup_id)
        return self

    def waitUntilComplete(self, timeout: int = 3600, interval: int = 5) -> 'Backup':
        '''
        Blocks until the backup finishes.

        Args:
            timeout: Maximum seconds to wait.
            interval: Seconds between checks.

        Raises:
            WaitTimeoutError: The backup did not finish in time.
        '''
        deadline = time.monotonic() + timeout
        while self.refresh().isInProgress():
            if time.monotonic() >= deadline:
                raise WaitTimeoutError(f'Backup {self.getName()!r} did not finish within {timeout}s')
            time.sleep(interval)
        return self

    def restore(self, truncate_directory: bool = False, restore_startup: bool = None, database_instance=None) -> None:
        '''
        Restores the server from this backup.

        Args:
            truncate_directory: Delete all current files before restoring.
            restore_startup: Also restore the startup command and variables.
            database_instance: For database backups, the instance to restore into.

        Example:
            backup.restore(truncate_directory=True)
        '''
        return self.panel.api.backups.restore(
            self.server.server_id, self.backup_id, truncate_directory, restore_startup, idOf(database_instance)
        )

    def rename(self, name: str) -> 'Backup':
        '''Renames the backup.'''
        self.panel.api.backups.update(self.server.server_id, self.backup_id, name=name)
        return self._update({'name': name})

    def setName(self, name: str) -> 'Backup':
        '''Alias of rename().'''
        return self.rename(name)

    def lock(self) -> 'Backup':
        '''Locks the backup so it cannot be deleted.'''
        self.panel.api.backups.update(self.server.server_id, self.backup_id, locked=True)
        return self._update({'is_locked': True})

    def unlock(self) -> 'Backup':
        '''Unlocks the backup.'''
        self.panel.api.backups.update(self.server.server_id, self.backup_id, locked=False)
        return self._update({'is_locked': False})

    def moveToGroup(self, group) -> 'Backup':
        '''
        Moves the backup into a backup group.

        Args:
            group: A BackupGroup or group UUID.
        '''
        group_id = idOf(group)
        self.panel.api.backups.update(self.server.server_id, self.backup_id, backup_group_uuid=group_id)
        return self._update({'backup_group_uuid': group_id})

    def getDownloadUrl(self, archive_format: str = None) -> str:
        '''
        Returns a signed, temporary download URL.

        Args:
            archive_format: Optional archive format, e.g. 'tar_gz' or 'zip'.
        '''
        return self.panel.api.backups.downloadUrl(self.server.server_id, self.backup_id, archive_format)

    def download(self, destination: str = None, archive_format: str = None):
        '''
        Downloads the backup.

        Args:
            destination: Local file to save to. If omitted the bytes are returned.
            archive_format: Optional archive format.

        Example:
            backup.download('backup.tar.gz')
        '''
        r = self.panel.api.files.fetch(self.getDownloadUrl(archive_format), stream=destination is not None)
        if destination is None:
            return r.content
        with open(destination, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                f.write(chunk)
        return destination

    def exportToServer(self, path: str, archive_format: str = None, foreground: bool = None):
        '''
        Writes the backup as an archive into the server's own file system.

        Args:
            path: Destination path on the server, e.g. "/exports/backup.tar.gz".
        '''
        return self.panel.api.backups.export(self.server.server_id, self.backup_id, path, archive_format, foreground)

    def getArchiveInfo(self) -> dict:
        '''Returns the archive format and size the panel would serve for download.'''
        return self.panel.api.backups.query(self.server.server_id, self.backup_id)

    def delete(self) -> None:
        '''Deletes the backup.'''
        return self.panel.api.backups.delete(self.server.server_id, self.backup_id)


class BackupGroup(Model):
    '''
    A named group of backups with its own retention policy.

    Example:
        group = server.backups.createBackupGroup('daily', retention={'daily': 7})
        backup = server.createBackup('nightly', group=group)
    '''
    def __init__(self, server, data: dict):
        super().__init__(server.panel, data)
        self.server = server

    def getName(self) -> str:
        '''Returns the group name.'''
        return self.data.get('name')

    def getOrder(self) -> int:
        '''Returns the display order.'''
        return self.data.get('order')

    def getRetention(self) -> dict:
        '''Returns the retention policy (count, days, daily, weekly, monthly, yearly).'''
        return self.data.get('retention', {})

    def getTotalBackups(self) -> int:
        '''Returns the number of backups in the group.'''
        return self.data.get('total_backups')

    def getUsableBackups(self) -> int:
        '''Returns the number of successful backups in the group.'''
        return self.data.get('usable_backups')

    def getBackups(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the backups in this group.'''
        return self.panel.api.backups.groupBackups(
            self.server.server_id, self.getUUID(), search, page, per_page
        ).map(lambda data: Backup(self.server, data))

    def rename(self, name: str) -> 'BackupGroup':
        '''Renames the group.'''
        self.panel.api.backups.updateGroup(self.server.server_id, self.getUUID(), name=name)
        return self._update({'name': name})

    def setRetention(self, count: int = 0, days: int = 0, daily: int = 0, weekly: int = 0, monthly: int = 0, yearly: int = 0) -> 'BackupGroup':
        '''
        Sets how many backups the group keeps. 0 means unlimited.

        Example:
            group.setRetention(daily=7, weekly=4)
        '''
        retention = {'count': count, 'days': days, 'daily': daily, 'weekly': weekly, 'monthly': monthly, 'yearly': yearly}
        self.panel.api.backups.updateGroup(self.server.server_id, self.getUUID(), retention=retention)
        return self._update({'retention': retention})

    def delete(self, lock_backups: bool = None) -> None:
        '''
        Deletes the group.

        Args:
            lock_backups: Lock the group's backups so they survive without a retention policy.
        '''
        return self.panel.api.backups.deleteGroup(self.server.server_id, self.getUUID(), lock_backups)
