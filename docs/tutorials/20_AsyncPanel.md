# AsyncPanel  
  
## What You Will Learn  
  
- Use CalagoAPI from an asyncio application  
- Await manager and model methods  
- Run independent requests concurrently  
  
## Prerequisites  
  
[19 Minecraft Servers](19_Minecraft_Servers.md). Basic familiarity with  
`async` and `await` in Python is helpful.  
  
## Estimated Time  
  
20 minutes  
  
## Concepts Introduced  
  
- Coroutine  
- `AsyncPanel`  
- `async with`  
- `asyncio.gather()`  
  
## Concept Explanation  
  
`AsyncPanel` exposes the same object model as `Panel`. Methods are awaited;  
plain attributes such as `.name` are read normally. Most synchronous requests  
run in worker threads so they do not block the event loop. The live console has  
a native asyncio implementation.  
  
## API Explanation  
  
Create `AsyncPanel` with the same connection arguments. `async with` closes  
connections at exit. Returned server and resource objects are async wrappers,  
so getters and actions require `await`. Use `asyncio.gather()` when independent  
requests can run concurrently.  
  
## Build an Async Status Report  
  
Begin with an `async` function and an `AsyncPanel` context. It has the same  
manager hierarchy as `Panel`; method calls become awaitable:  
  
```python  
import asyncio  
import os  
from calagoapi import AsyncPanel  
  
async def main():  
    async with AsyncPanel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:  
        servers = await panel.servers.getServers()  
```  
  
Each status request is independent, so gather them concurrently. `server.name`  
is a plain attribute and needs no `await`:  
  
```python  
        statuses = await asyncio.gather(*(server.getStatus() for server in servers))  
        for server, status in zip(servers, statuses):  
            print(server.name, status)  
  
asyncio.run(main())  
```  
  
The context manager closes the wrapped HTTP client and any async consoles when  
the coroutine exits.  
  
## Common Mistakes  
  
- Forgetting `await` on a method, including getters.  
- Adding `await` to ordinary attributes such as `.name` or `.data`.  
- Calling synchronous `Panel` methods directly inside an event-loop callback.  
- Treating long-lived console streaming like an ordinary worker-thread call.  
  
## What You Learned  
  
- `AsyncPanel` keeps the same managers and object relationships as `Panel`.  
- Methods are awaitable while plain attributes are read directly.  
- Independent requests can run concurrently with `asyncio.gather()`.  
  
## Continue Learning  
  
Next: [21 Extensions](21_Extensions.md)  
  
## Navigation  
  
Previous: [19 Minecraft Servers](19_Minecraft_Servers.md)  
Next: [21 Extensions](21_Extensions.md)  
Reference Docs: [Async](../reference/async.md)  
Related Examples: Code examples are embedded in this walkthrough.