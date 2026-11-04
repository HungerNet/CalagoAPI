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

## Guided Example

```python
server = panel.servers.getMinecraftServer(server_id)
print(server.getMOTD())
print(server.getProperty('max-players'))
```

## Exercise

Read `max-players` and the MOTD. Do not change properties. Explain why the
method call `setProperty()` may require a restart before the server reflects
the change.

Hint: property values are read from `/server.properties`.

## Answer

```python
server = panel.servers.getMinecraftServer(server_id)
properties = server.getProperties()
print('max-players:', properties.get('max-players'))
print('motd:', server.getMOTD())
```

The file is updated immediately, but the Minecraft process generally reads
these settings when it starts.

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
Related Examples: [Minecraft answer](../../examples/tutorials/19_minecraft_servers/answer.py)