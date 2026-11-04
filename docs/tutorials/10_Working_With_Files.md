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
  
## Build a File Inspection Script  
  
Start with the familiar panel and server lookup. The server owns `files`, so  
the path is interpreted inside this server rather than on the computer running  
Python:  
  
```python  
import os  
from calagoapi import Panel  
  
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:  
  server = panel.servers.getServer(os.environ['SERVER_ID'])  
```  
  
List the root directory. Each result is a `File` object, allowing the script to  
distinguish directories and files without another lookup:  
  
```python  
  for item in server.files.listFiles('/'):  
    kind = 'directory' if item.isDirectory() else 'file'  
    print(kind, item.getName())  
```  
  
Before reading an optional configuration file, check for it. `readFile()` then  
returns text that ordinary Python string methods can process:  
  
```python  
  if server.files.exists('/server.properties'):  
    text = server.files.readFile('/server.properties')  
    print('\n'.join(text.splitlines()[:3]))  
```  
  
This inspection workflow is read-only. Add `writeFile()` only when you are  
ready to replace or create server-side contents.  
  
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
Related Examples: Code examples are embedded in this walkthrough.