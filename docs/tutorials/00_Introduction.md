# Introduction  
  
## What You Will Learn  
  
- How the course is organized  
- The CalagoAPI object hierarchy  
- How lessons and reference pages support different learning needs  
  
## Prerequisites  
  
None. Basic familiarity with using a computer is enough to begin.  
  
## Estimated Time  
  
5 minutes  
  
## Concepts Introduced  
  
- Panel  
- Managers  
- Servers  
- Resources  
- Reference documentation versus tutorials  
  
## Concept Explanation  
  
CalagoAPI is a Python SDK for a Calagopus panel. The learning path follows the  
objects you will use: `Panel` gives access to managers; managers find `Server`  
objects; servers expose resources such as files, backups, databases, schedules,  
and network settings. Later lessons combine these pieces into automation,  
extensions, and administration.  
  
Each tutorial explains a feature by building a script around it. Follow the  
code blocks in order and use the runnable companion example when you want to  
see the complete workflow. The [reference section](../reference/README.md) is  
a lookup manual, not a replacement for the learning order.  
  
## API Explanation  
  
The course begins at `Panel`, the connection and lifetime boundary. A call such  
as `panel.servers.getServer(...)` goes through a manager and returns a server  
object. That object owns managers such as `server.files` and `server.backups`.  
  
## Follow One Object Through the API  
  
Every script starts from a `Panel`. The panel exposes a `ServerManager` at  
`panel.servers`; that manager finds a `GenericServer`. The server then owns  
resource managers such as `server.files` and `server.backups`.  
  
```python  
from calagoapi import Panel  
  
panel = Panel(url='https://panel.example.com', api_key='...')  
server = panel.servers.getServer('server-id')  
files = server.files  
```  
  
The snippet shows the ownership path. In a real script, load credentials from  
the environment and close the connection with a context manager, as the next  
lessons demonstrate. The reference manual describes each object; the tutorials  
show how to combine them into a workflow.  
  
## Common Mistakes  
  
- Treating reference pages and tutorials as the same thing. Reference pages  
  describe individual APIs; tutorials explain a workflow in sequence.  
- Assuming every API key can access every server or action. Permissions are  
  enforced by the panel.  
  
## What You Learned  
  
- The course follows Panel -> Managers -> Servers -> Resources.  
- Runnable examples complement the walkthroughs without a grading runner.  
- The reference is available whenever you need a method lookup.  
  
## Continue Learning  
  
Next: [01 Installation](01_Installation.md)  
  
## Navigation  
  
Previous: Start here  
Next: [01 Installation](01_Installation.md)  
Reference Docs: [Getting started](../reference/getting-started.md)  
Related Examples: Code examples are embedded in this walkthrough.