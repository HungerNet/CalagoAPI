import os

from calagoapi.files.file import File, splitPath
from calagoapi.utils.model import idOf
from calagoapi.utils.exceptions import NotFoundError


class FileManager:
    '''
    File management for one server, available as `server.files`.

    Paths are always absolute paths inside the server, e.g. "/plugins/config.yml".

    Args:
        server: The server to manage files for.

    Example:
        files = server.files.listFiles('/')
        props = server.files.readFile('/server.properties')
        server.files.writeFile('/eula.txt', 'eula=true')
        server.files.uploadFile('/plugins', 'MyPlugin.jar')
    '''
    def __init__(self, server):
        self.server = server
        self.api = server.panel.api.files

    @property
    def server_id(self):
        return self.server.server_id

    # browsing
    def listFiles(self, directory: str = '/', sort: str = None, page: int = None, per_page: int = None):
        '''
        Lists the contents of a directory.

        Args:
            directory: Directory to list, defaults to the server root.
            sort: Optional Calagopus sorting mode.
            page: Only fetch this page. By default every entry is returned.
            per_page: Page size.

        Returns:
            A Page (list) of File objects.

        Example:
            for file in server.files.listFiles('/world'):
                print(file.getName(), file.isDirectory())
        '''
        _, entries = self.api.list(self.server_id, directory, sort, page, per_page)
        return entries.map(lambda entry: File(self.server, entry, directory))

    def getFile(self, path: str) -> File:
        '''
        Returns details about a single file or directory.

        Example:
            file = server.files.getFile('/server.properties')
            print(file.getSize(formatted=True), file.getModified())
        '''
        directory, name = splitPath(path)
        entries = self.api.stat(self.server_id, [name], directory)
        return File(self.server, entries[0], directory) if entries else None

    def exists(self, path: str) -> bool:
        '''Returns True if the file or directory exists.'''
        try:
            return self.getFile(path) is not None
        except NotFoundError:
            return False

    def getFilesystemInfo(self, directory: str = '/') -> dict:
        '''
        Returns information about the server filesystem.

        Returns:
            dict with is_filesystem_primary, is_filesystem_writable, is_filesystem_fast
            and the list of in-progress uploads.
        '''
        result, _ = self.api.list(self.server_id, directory, page=1, per_page=1)
        return {k: v for k, v in result.items() if k != 'entries'}

    def searchFiles(self, query: str = None, root: str = '/', include: list = None, exclude: list = None,
                    min_size: int = None, max_size: int = None, case_insensitive: bool = True, context_lines: int = None):
        '''
        Searches files by path and/or contents.

        Args:
            query: Text to search for inside files.
            root: Directory to search in.
            include: Glob patterns of paths to include, e.g. ['*.yml'].
            exclude: Glob patterns of paths to exclude.
            min_size: Minimum file size in bytes.
            max_size: Maximum file size in bytes.
            case_insensitive: Ignore case for path patterns and contents.
            context_lines: Lines of context to return around content matches.

        Returns:
            dict with `entries` (matching files) and `content_matches`.

        Example:
            result = server.files.searchFiles('max-players', include=['*.properties'])
        '''
        path_filter = None
        if include or exclude:
            path_filter = {'include': include or [], 'exclude': exclude or [], 'case_insensitive': case_insensitive}
        size_filter = None
        if min_size is not None or max_size is not None:
            size_filter = {'min': min_size or 0, 'max': max_size if max_size is not None else 2**53}
        content_filter = None
        if query:
            content_filter = {'query': query, 'max_search_size': 10 * 1024 * 1024, 'include_unmatched': False, 'case_insensitive': case_insensitive}
        match_context = None
        if context_lines is not None:
            match_context = {'before': context_lines, 'after': context_lines, 'max_matches': 100}
        result = self.api.search(self.server_id, root, path_filter, size_filter, content_filter, match_context)
        result['entries'] = [File(self.server, entry, root) for entry in result.get('entries') or []]
        return result

    def getDirectorySizes(self, directory: str = '/', depth: int = None) -> dict:
        '''
        Returns a size breakdown of a directory tree.

        Args:
            directory: Directory to measure.
            depth: How many levels of children to include.
        '''
        return self.api.directorySizes(self.server_id, directory, depth)

    def getLargestDirectories(self, directory: str = '/') -> list:
        '''Returns the largest directories under `directory`, biggest first.'''
        return self.api.largestDirectories(self.server_id, directory)

    def getFingerprint(self, path: str, algorithm: str = None) -> str:
        '''
        Returns a checksum of a file.

        Args:
            path: File to hash.
            algorithm: Hash algorithm, e.g. 'sha256', 'md5'. Uses the panel default if omitted.
        '''
        return self.api.fingerprint(self.server_id, path, algorithm)

    # reading and writing
    def readFile(self, path: str) -> str:
        '''
        Returns the contents of a text file.

        Example:
            properties = server.files.readFile('/server.properties')
        '''
        return self.api.contents(self.server_id, path)

    def readLines(self, path: str, start_line: int = None, end_line: int = None) -> dict:
        '''
        Reads a range of lines from a large file without downloading all of it.

        Returns:
            dict with content, start_line, end_line and eof.

        Example:
            chunk = server.files.readLines('/logs/latest.log', 1, 100)
            print(chunk['content'])
        '''
        return self.api.lines(self.server_id, path, start_line, end_line)

    def writeFile(self, path: str, content) -> None:
        '''
        Creates or replaces a file.

        Args:
            path: File to write.
            content: Text (str) or bytes.

        Example:
            server.files.writeFile('/eula.txt', 'eula=true')
        '''
        return self.api.write(self.server_id, path, content)

    def getRevisions(self, path: str) -> list:
        '''Returns the saved revisions (edit history) of a file.'''
        return self.api.revisions(self.server_id, path)

    def getRevision(self, path: str, revision_id: str) -> str:
        '''Returns the contents of a file at a previous revision.'''
        return self.api.revision(self.server_id, path, revision_id)

    # transfer
    def getDownloadUrl(self, path: str, archive_format: str = None) -> str:
        '''
        Returns a signed, temporary URL to download a file or directory.

        Args:
            path: File or directory to download.
            archive_format: Archive format used for directories, e.g. 'zip'.
        '''
        directory, name = splitPath(path)
        return self.api.downloadUrl(self.server_id, [name], directory, archive_format=archive_format)

    def downloadFile(self, path: str, destination: str = None):
        '''
        Downloads a file.

        Args:
            path: File on the server.
            destination: Local path to save to. If omitted the bytes are returned.

        Returns:
            bytes, or the destination path.

        Example:
            server.files.downloadFile('/world.zip', 'world.zip')
        '''
        r = self.api.fetch(self.getDownloadUrl(path), stream=destination is not None)
        if destination is None:
            return r.content
        with open(destination, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                f.write(chunk)
        return destination

    def getUploadUrl(self) -> str:
        '''Returns a signed, temporary URL that accepts multipart uploads.'''
        return self.api.uploadUrl(self.server_id)

    def uploadFile(self, directory: str, file, name: str = None):
        '''
        Uploads a file into a directory.

        Args:
            directory: Target directory on the server.
            file: Local file path, bytes, or an open binary file.
            name: File name on the server. Defaults to the local file name.

        Example:
            server.files.uploadFile('/plugins', 'build/MyPlugin.jar')
            server.files.uploadFile('/', b'eula=true', name='eula.txt')
        '''
        if isinstance(file, (str, os.PathLike)):
            with open(file, 'rb') as f:
                return self.api.upload(self.server_id, directory, [(name or os.path.basename(file), f.read())])
        if name is None:
            name = os.path.basename(getattr(file, 'name', '')) or 'upload'
        data = file.read() if hasattr(file, 'read') else file
        return self.api.upload(self.server_id, directory, [(name, data)])

    def pullFile(self, url: str, directory: str = '/', name: str = None, use_header: bool = None, foreground: bool = None):
        '''
        Makes the server download a file from a URL.

        Args:
            url: Remote URL.
            directory: Directory to save into.
            name: File name, defaults to the name from the URL.
            use_header: Use the Content-Disposition header for the name.
            foreground: Wait for the download to finish before returning.

        Example:
            server.files.pullFile('https://example.com/plugin.jar', '/plugins')
        '''
        return self.api.pull(self.server_id, url, directory, name, use_header, foreground)

    def queryPull(self, url: str) -> dict:
        '''Inspects a remote URL before pulling it (file name, size, ...).'''
        return self.api.queryPull(self.server_id, url)

    # management
    def deleteFiles(self, root: str, files: list) -> None:
        '''
        Deletes several files from one directory.

        Example:
            server.files.deleteFiles('/logs', ['old.log', 'older.log'])
        '''
        return self.api.delete(self.server_id, root, files)

    def deleteFile(self, path: str) -> None:
        '''
        Deletes a single file or directory.

        Example:
            server.files.deleteFile('/world/session.lock')
        '''
        directory, name = splitPath(path)
        return self.api.delete(self.server_id, directory, [name])

    def renameFiles(self, root: str, files: list) -> None:
        '''
        Renames or moves several files.

        Args:
            root: Directory the paths are relative to.
            files: List of {'from': ..., 'to': ...} dicts or (from, to) tuples.

        Example:
            server.files.renameFiles('/', [('world', 'world_old')])
        '''
        return self.api.rename(self.server_id, root, self._pairs(files))

    def renameFile(self, path: str, new_path: str) -> None:
        '''
        Renames or moves a single file.

        Example:
            server.files.renameFile('/server.jar', '/server.old.jar')
        '''
        return self.api.rename(self.server_id, '/', [{'from': path.lstrip('/'), 'to': new_path.lstrip('/')}])

    def moveFiles(self, root: str, files: list) -> None:
        '''Moves files, same as renameFiles(). Kept for HungerLib compatibility.'''
        return self.renameFiles(root, files)

    def copyFile(self, path: str, destination: str = None, overwrite: bool = None, foreground: bool = None):
        '''
        Copies a single file.

        Args:
            path: File to copy.
            destination: Target path. Calagopus picks a "copy" name when omitted.
            overwrite: Replace the destination if it exists.
        '''
        result = self.api.copy(self.server_id, path, destination, overwrite, foreground)
        return File(self.server, result['entry'], splitPath(destination or path)[0]) if result and result.get('entry') else result

    def copyFiles(self, root: str, files: list, overwrite: bool = None, foreground: bool = None) -> dict:
        '''
        Copies several files.

        Args:
            root: Directory the paths are relative to.
            files: List of {'from': ..., 'to': ...} dicts or (from, to) tuples.

        Returns:
            dict with the number copied and the files skipped.
        '''
        return self.api.copyMany(self.server_id, root, self._pairs(files), overwrite, foreground)

    def copyToServer(self, files: list, destination_server, destination: str = '/', root: str = '/', foreground: bool = None):
        '''
        Copies files to another server.

        Args:
            files: List of {'from': ..., 'to': ...} dicts or (from, to) tuples.
            destination_server: Server object or server id.
            destination: Target directory on the other server.
            root: Source directory the paths are relative to.
        '''
        return self.api.copyRemote(self.server_id, root, self._pairs(files), destination, idOf(destination_server), foreground)

    def copyToServers(self, files: list, destination_servers: list, destination: str = '/', root: str = '/') -> list:
        '''Copies files to several servers at once.'''
        servers = [idOf(s) for s in destination_servers]
        return self.api.copyRemoteMany(self.server_id, root, self._pairs(files), destination, servers)

    def createFolder(self, directory: str, name: str) -> None:
        '''
        Creates a directory.

        Example:
            server.files.createFolder('/', 'backups')
        '''
        return self.api.createDirectory(self.server_id, directory, name)

    def createDirectory(self, path: str) -> None:
        '''Creates a directory from a full path, e.g. "/plugins/MyPlugin".'''
        directory, name = splitPath(path)
        return self.api.createDirectory(self.server_id, directory, name)

    def createSymlink(self, link: str, target: str, root: str = '/') -> None:
        '''Creates a symbolic link at `link` pointing to `target`.'''
        return self.api.createSymlink(self.server_id, root, link, target)

    def compress(self, root: str, files: list, format: str = 'tar_gz', name: str = None, foreground: bool = None):
        '''
        Compresses files into an archive.

        Args:
            root: Directory containing the files.
            files: File names inside root.
            format: tar, tar_gz, tar_xz, tar_bz2, tar_lz4, tar_zstd, zip or seven_zip.
            name: Archive name. Generated when omitted.

        Returns:
            The created archive as a File, when the panel returns it.

        Example:
            archive = server.files.compress('/', ['world'], format='zip')
        '''
        result = self.api.compress(self.server_id, root, files, format, name, foreground)
        return File(self.server, result['entry'], root) if result and result.get('entry') else result

    def decompress(self, file_path: str, foreground: bool = None) -> None:
        '''
        Extracts an archive into the directory it lives in.

        Example:
            server.files.decompress('/uploads/world.zip')
        '''
        directory, name = splitPath(file_path)
        return self.api.decompress(self.server_id, directory, name, foreground)

    def chmod(self, root: str, files: list) -> None:
        '''
        Changes permissions of several files.

        Args:
            files: List of {'file': name, 'mode': '755', 'recursive': False} dicts.
        '''
        return self.api.chmod(self.server_id, root, files)

    def chmodFile(self, path: str, mode: str, recursive: bool = False) -> None:
        '''
        Changes the permissions of one file.

        Example:
            server.files.chmodFile('/start.sh', '755')
        '''
        directory, name = splitPath(path)
        return self.api.chmod(self.server_id, directory, [{'file': name, 'mode': str(mode), 'recursive': recursive}])

    def querySQLite(self, path: str, query: str, rows: int = None, read_only: bool = True) -> list:
        '''
        Runs a SQL query against a SQLite database file on the server.

        Example:
            rows = server.files.querySQLite('/plugins/LuckPerms/luckperms-sqlite.db',
                                           'SELECT * FROM luckperms_players LIMIT 10')
        '''
        return self.api.sqliteQuery(self.server_id, path, query, rows, read_only)

    def cancelOperation(self, operation_id: str) -> None:
        '''Cancels a background file operation (compression, pull, copy...).'''
        return self.api.cancelOperation(self.server_id, operation_id)

    # helpers
    @staticmethod
    def _pairs(files):
        return [f if isinstance(f, dict) else {'from': f[0], 'to': f[1]} for f in files]
