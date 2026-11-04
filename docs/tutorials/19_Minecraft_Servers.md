# Minecraft Servers  
  
## What You Will Learn  
  
- Use `MinecraftServer` helpers  
- Read and update `server.properties`  
- Understand where optional version features come from  
  
## Prerequisites  
  
[18 Networking](18_Networking.md). Your target server must use a Minecraft egg.  
  
## Estimated Time  
  
20 minutes  
  
## Concepts Introduced  
  
- `MinecraftServer`  
- Server properties  
- EULA  
- Optional version changer  
  
## Concept Explanation  
  
`MinecraftServer` extends `GenericServer`; it is still the same server object  
with the same managers, plus Minecraft-specific commands and properties  
helpers. Use `getMinecraftServer()` when you want those helpers. Property  
updates change a server file and typically take effect after restart.  
  
## API Explanation  
  
`getProperties()` returns a mapping of property names to strings.  
`setProperty()` and `setProperties()` write changes. Helpers such as `say()`,  
`saveAll()`, and `acceptEula()` provide common operations. Version installation  
is an optional extension, not part of this core helper set.  
  
## Build a Properties Report  
  
Use the Minecraft-specific manager method to get a `MinecraftServer`, then  
read the relevant values from its properties file:  
  
```python  
import os  
from calagoapi import Panel  
  
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:  
  server = panel.servers.getMinecraftServer(os.environ['SERVER_ID'])  
  properties = server.getProperties()  
  print('max-players:', properties.get('max-players'))  
  print('motd:', server.getMOTD())  
```  
  
To change a value, `setProperty()` writes the file. Most Minecraft properties  
take effect after a server restart, so an automation should separate the file  
change from the decision to restart.  
  
```python  
# Example of a deliberate change; leave commented in a read-only report.  
# server.setProperty('motd', 'Season 3 is live!')  
```  
  
## Common Mistakes  
  
- Expecting a generic `GenericServer` object to have Minecraft-only helpers.  
- Assuming `setProperty()` changes the already-running process immediately.  
- Assuming version lookup/install methods exist without enabling their  
  optional extension.  
  
## What You Learned  
  
- Minecraft servers are specialized server objects, not a separate hierarchy  
  from the Panel and managers.  
- Properties are file-backed settings.  
- Version changer features are taught as an extension after core APIs.  
  
## Continue Learning  
  
Next: [20 AsyncPanel](20_AsyncPanel.md)  
  
## Navigation  
  
Previous: [18 Networking](18_Networking.md)  
Next: [20 AsyncPanel](20_AsyncPanel.md)  
Reference Docs: [Minecraft servers](../reference/minecraft.md), [Servers](../reference/servers.md)  
Related Examples: Code examples are embedded in this walkthrough.