# Working with Files

## What You Will Learn

- Navigate server files through the server's file manager
- Read and write text files
- Recognize file operations that modify a live server

## Prerequisites

[09 Console Review](09_Console_Review.md). Your API key needs file permissions.

## Estimated Time

20 minutes

## Concepts Introduced

- `FileManager`
- Absolute server paths
- `File` resource objects
- Read and write operations

## Concept Explanation

Files are resources owned by one server. Access them through `server.files`,
not directly through the panel. Paths are absolute within the server, such as
`/plugins` or `/server.properties`; they are not local machine paths.

## API Explanation

`listFiles(directory)` returns `File` objects. `readFile(path)` returns text,
and `writeFile(path, content)` creates or replaces a file. `exists(path)` checks
for a file or directory. Use `getFile()` when you need metadata such as size or
modified time.

## Guided Example

```python
for item in server.files.listFiles('/'):
    print(item.getName(), 'directory' if item.isDirectory() else 'file')

if server.files.exists('/server.properties'):
    print(server.files.readFile('/server.properties')[:200])
```

## Exercise

List the root directory and print each item's name. If `/server.properties`
exists, read it and print only the first three lines.

Hint: `str.splitlines()` turns file text into lines.

## Answer

```python
for item in server.files.listFiles('/'):
    print(item.getName())

if server.files.exists('/server.properties'):
    text = server.files.readFile('/server.properties')
    print('\n'.join(text.splitlines()[:3]))
```

## Common Mistakes

- Passing a local filesystem path instead of a server path.
- Forgetting `writeFile()` replaces existing contents. Preserve the old text if
  you need to make a small edit.
- Writing files while the server is using them without checking the expected
  file format or restart requirements.

## What You Learned

- `server.files` is scoped to one server.
- `FileManager` methods use server-absolute paths.
- Listing returns resource objects; reading returns text.

## Continue Learning

Next: [11 Files Review](11_Files_Review.md)

## Navigation

Previous: [09 Console Review](09_Console_Review.md)
Next: [11 Files Review](11_Files_Review.md)
Reference Docs: [Files](../reference/files.md)
Related Examples: [files answer](../../examples/tutorials/10_working_with_files/answer.py)