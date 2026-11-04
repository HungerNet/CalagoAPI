# Files Review

## What You Will Learn

- Reinforce the server-to-file-manager relationship
- Read code and predict its effects
- Practice safe file inspection

## Prerequisites

[10 Working with Files](10_Working_With_Files.md).

## Estimated Time

15 minutes

## Concepts Introduced

- File resource ownership
- Read versus write effects
- Existence checks

## Concept Explanation

The server object selects the server. Its file manager scopes every path to
that server. Read-only inspection is a good first step before a write, copy,
rename, or delete operation.

## API Explanation

`listFiles()` returns file objects; `readFile()` returns text;
`writeFile()` replaces or creates contents; `exists()` returns a boolean.
Paths use `/` as the server root.

## Guided Example

```python
if server.files.exists('/eula.txt'):
    print(server.files.readFile('/eula.txt'))
```

## Exercise

1. What type of object does `server.files.listFiles('/')` contain?
2. What does this code do?

   ```python
   server.files.writeFile('/notes.txt', 'hello')
   ```

3. Why is `/home/me/notes.txt` not automatically a local path?
4. Write a check that prints `missing` only if `/logs/latest.log` is absent.

Hint: server file paths are not local computer paths.

## Answer

1. A page/list of `File` objects.
2. It creates or replaces `/notes.txt` on that server.
3. Because `server.files` operates inside the server filesystem; a local file
   is accessed with Python's local file APIs.
4. ```python
   if not server.files.exists('/logs/latest.log'):
       print('missing')
   ```

## Common Mistakes

- Assuming a `File` object is a local Python file handle.
- Writing over a configuration file without preserving unrelated values.
- Using a server path with `open()` instead of `server.files`.

## What You Learned

- File operations start from a server and stay within its filesystem.
- `exists()` can guard optional reads.
- Writes are state changes; inspect before modifying.

## Continue Learning

Next: [12 Backups](12_Backups.md)

## Navigation

Previous: [10 Working with Files](10_Working_With_Files.md)
Next: [12 Backups](12_Backups.md)
Reference Docs: [Files](../reference/files.md)
Related Examples: [files review answer](../../examples/tutorials/11_files_review/answer.py)