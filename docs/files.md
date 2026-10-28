# Files

`server.files` is a `FileManager`. Paths are absolute paths inside the
server, like `/plugins/config.yml`.

## Browsing

```python
for file in server.files.listFiles('/plugins'):
    kind = 'dir ' if file.isDirectory() else 'file'
    print(kind, file.getName(), file.getSize(formatted=True), file.getModified())

file = server.files.getFile('/server.properties')
server.files.exists('/world')
```

`File` objects:

| Getters | State checks | Actions |
| --- | --- | --- |
| `getName`, `getPath`, `getDirectory`, `getSize(formatted=False)`, `getPhysicalSize`, `getMode`, `getModeBits`, `getMimeType`, `getModified`, `getExtension` | `isFile`, `isDirectory`, `isSymlink`, `isEditable`, `isArchive` | `read`, `write`, `download`, `listFiles`, `rename`, `move`, `copy`, `delete`, `chmod`, `compress`, `decompress` |

## Reading and writing

```python
text = server.files.readFile('/server.properties')
server.files.writeFile('/eula.txt', 'eula=true')
server.files.writeFile('/data.bin', b'\x00\x01')

chunk = server.files.readLines('/logs/latest.log', start_line=1, end_line=200)
print(chunk['content'], chunk['eof'])

for revision in server.files.getRevisions('/server.properties'):
    print(revision)
old = server.files.getRevision('/server.properties', revision_id)
```

## Upload and download

```python
server.files.uploadFile('/plugins', 'build/MyPlugin.jar')          # local path
server.files.uploadFile('/', b'eula=true', name='eula.txt')        # bytes
with open('world.zip', 'rb') as f:
    server.files.uploadFile('/', f)                                 # open file

data = server.files.downloadFile('/server.properties')             # bytes
server.files.downloadFile('/world.zip', 'backups/world.zip')        # save to disk
url = server.files.getDownloadUrl('/world', archive_format='zip')  # signed URL

server.files.pullFile('https://example.com/plugin.jar', '/plugins')  # server downloads it
```

## Managing files

```python
server.files.createDirectory('/plugins/MyPlugin')
server.files.createFolder('/', 'backups')            # HungerLib style
server.files.renameFile('/server.jar', '/server.old.jar')
server.files.renameFiles('/', [('world', 'world_old'), ('logs', 'logs_old')])
server.files.copyFile('/config.yml', '/config.backup.yml')
server.files.copyFiles('/', [('a.txt', 'b.txt')])
server.files.deleteFile('/world/session.lock')
server.files.deleteFiles('/logs', ['old.log', 'older.log'])
server.files.chmodFile('/start.sh', '755')
server.files.createSymlink('/latest.log', '/logs/latest.log')
```

### Archives

```python
archive = server.files.compress('/', ['world', 'world_nether'], format='zip', name='worlds.zip')
server.files.decompress('/uploads/world.zip')
```

Formats: `tar`, `tar_gz`, `tar_xz`, `tar_lzip`, `tar_bz2`, `tar_lz4`, `tar_zstd`, `zip`, `seven_zip`.

### Copying to other servers

```python
server.files.copyToServer([('world', 'world')], other_server, destination='/')
server.files.copyToServers([('plugins/Shared.jar', 'Shared.jar')], [lobby, survival], destination='/plugins')
```

## Searching and analysing

```python
result = server.files.searchFiles('max-players', include=['*.properties'], context_lines=2)
for file in result['entries']:
    print(file.getPath())

server.files.getDirectorySizes('/', depth=2)
server.files.getLargestDirectories('/')
server.files.getFingerprint('/server.jar', algorithm='sha256')
```

## SQLite

```python
rows = server.files.querySQLite('/plugins/LuckPerms/luckperms-sqlite.db',
                                'SELECT username FROM luckperms_players LIMIT 10')
```

`read_only=True` is the default; pass `read_only=False` to modify data.
