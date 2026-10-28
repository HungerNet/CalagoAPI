import posixpath

from calagoapi.utils.model import Model
from calagoapi.utils.convert import formatBytes


def splitPath(path: str) -> tuple:
    '''Splits '/plugins/config.yml' into ('/plugins', 'config.yml')'''
    path = '/' + path.strip('/')
    return posixpath.dirname(path) or '/', posixpath.basename(path)


def joinPath(directory: str, name: str) -> str:
    '''Joins a directory and a file name into an absolute server path'''
    return posixpath.join('/' + directory.strip('/'), name)


class File(Model):
    '''
    A file or directory on a server.

    Returned by `server.files.listFiles()` and `server.files.getFile()`.

    Args:
        server: The server the file lives on.
        data: Raw directory entry from Calagopus.
        directory: The directory containing this entry.

    Example:
        for file in server.files.listFiles('/plugins'):
            if file.isFile() and file.getName().endswith('.jar'):
                print(file.getName(), file.getSize(formatted=True))
    '''
    def __init__(self, server, data: dict, directory: str = '/'):
        super().__init__(server.panel, data)
        self.server = server
        self.directory = '/' + directory.strip('/')

    def __repr__(self):
        kind = 'Directory' if self.isDirectory() else 'File'
        return f'<{kind} {self.getPath()!r}>'

    def __eq__(self, other):
        if not isinstance(other, File):
            return NotImplemented
        return self.server.server_id == other.server.server_id and self.getPath() == other.getPath()

    def __hash__(self):
        return hash((self.server.server_id, self.getPath()))

    # getters
    def getName(self) -> str:
        '''Returns the file name, e.g. "server.properties".'''
        return self.data.get('name')

    def getPath(self) -> str:
        '''Returns the absolute path on the server, e.g. "/plugins/config.yml".'''
        return joinPath(self.directory, self.getName())

    def getDirectory(self) -> str:
        '''Returns the directory containing this file.'''
        return self.directory

    def getSize(self, formatted: bool = False):
        '''
        Returns the size in bytes.

        Args:
            formatted: Return a human readable string like "1.5 MiB" instead.
        '''
        size = self.data.get('size')
        return formatBytes(size) if formatted else size

    def getPhysicalSize(self) -> int:
        '''Returns the size the file actually takes on disk, in bytes.'''
        return self.data.get('size_physical')

    def getMode(self) -> str:
        '''Returns the permission string, e.g. "-rw-r--r--".'''
        return self.data.get('mode')

    def getModeBits(self) -> str:
        '''Returns the octal permission bits, e.g. "644".'''
        return self.data.get('mode_bits')

    def getMimeType(self) -> str:
        '''Returns the detected mime type, e.g. "text/plain".'''
        return self.data.get('mime')

    def getModified(self) -> str:
        '''Returns the last modification time as an ISO-8601 string.'''
        return self.data.get('modified')

    def getExtension(self) -> str:
        '''Returns the file extension without the dot, or an empty string.'''
        return posixpath.splitext(self.getName() or '')[1].lstrip('.')

    # state checks
    def isDirectory(self) -> bool:
        '''Returns True if this entry is a directory.'''
        return bool(self.data.get('directory'))

    def isFile(self) -> bool:
        '''Returns True if this entry is a regular file.'''
        return bool(self.data.get('file'))

    def isSymlink(self) -> bool:
        '''Returns True if this entry is a symbolic link.'''
        return bool(self.data.get('symlink'))

    def isEditable(self) -> bool:
        '''Returns True if the panel allows editing this file as text.'''
        return bool(self.data.get('editable'))

    def isArchive(self) -> bool:
        '''Returns True if this looks like an archive the panel can decompress.'''
        name = (self.getName() or '').lower()
        return name.endswith(('.zip', '.tar', '.tar.gz', '.tgz', '.tar.xz', '.tar.bz2', '.tar.zst', '.tar.lz4', '.7z', '.gz', '.xz', '.bz2', '.zst', '.rar'))

    # actions
    def read(self) -> str:
        '''
        Returns the file contents as text.

        Example:
            print(server.files.getFile('/server.properties').read())
        '''
        return self.server.files.readFile(self.getPath())

    def write(self, content) -> None:
        '''Replaces the file contents.'''
        return self.server.files.writeFile(self.getPath(), content)

    def download(self, destination: str = None):
        '''
        Downloads the file (or the directory, as an archive).

        Args:
            destination: Optional local path to save to.

        Returns:
            The bytes if no destination was given, otherwise the destination path.
        '''
        return self.server.files.downloadFile(self.getPath(), destination)

    def listFiles(self):
        '''Lists the contents of this directory.'''
        return self.server.files.listFiles(self.getPath())

    def rename(self, new_name: str) -> 'File':
        '''
        Renames the file inside its current directory.

        Example:
            file.rename('server.properties.bak')
        '''
        self.server.files.renameFile(self.getPath(), joinPath(self.directory, new_name))
        self.data['name'] = new_name
        return self

    def move(self, destination: str) -> 'File':
        '''
        Moves the file to another path.

        Args:
            destination: New absolute path, e.g. "/backups/world.zip".
        '''
        self.server.files.renameFile(self.getPath(), destination)
        self.directory, self.data['name'] = splitPath(destination)
        return self

    def copy(self, destination: str = None):
        '''Copies the file. Without a destination Calagopus picks a "copy" name next to it.'''
        return self.server.files.copyFile(self.getPath(), destination)

    def delete(self) -> None:
        '''Deletes the file or directory.'''
        return self.server.files.deleteFile(self.getPath())

    def chmod(self, mode: str, recursive: bool = False) -> None:
        '''
        Changes the file permissions.

        Args:
            mode: Octal mode, e.g. "755".
            recursive: Apply to everything inside a directory.
        '''
        return self.server.files.chmodFile(self.getPath(), mode, recursive)

    def compress(self, format: str = 'tar_gz', name: str = None):
        '''Compresses this file into an archive next to it.'''
        return self.server.files.compress(self.directory, [self.getName()], format, name)

    def decompress(self):
        '''Extracts this archive into its directory.'''
        return self.server.files.decompress(self.getPath())
