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

## Build a Configuration Inspection

Combine an existence check, file metadata, and a text read. The manager still
belongs to the server object, and the path remains server-relative:

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
   server = panel.servers.getServer(os.environ['SERVER_ID'])
   path = '/server.properties'

   if not server.files.exists(path):
      print('configuration file is absent')
   else:
      file = server.files.getFile(path)
      print('size:', file.getSize(formatted=True))
      print(server.files.readFile(path)[:300])
```

`File` represents server-side metadata; it is not a local file handle. If you
later add `writeFile()`, treat that as a separate state-changing operation and
preserve unrelated configuration entries.

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
Related Examples: Code examples are embedded in this walkthrough.