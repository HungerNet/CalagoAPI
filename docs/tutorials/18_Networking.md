# Networking

## What You Will Learn

- Inspect server allocations
- Understand the roles of firewall rules and tunnels
- Treat network changes as operational changes

## Prerequisites

[17 Schedules Review](17_Schedules_Review.md). Your key needs network read
permissions.

## Estimated Time

20 minutes

## Concepts Introduced

- Allocation
- Primary address
- Firewall
- Tunnel
- Subuser permissions

## Concept Explanation

Network resources connect a server to clients and to other servers. An
allocation is an address and port assigned to a server. Firewalls allow or deny
traffic; tunnels expose configured ports between servers. These resources are
managed under `server.network` or `server.tunnel`, not as standalone panel
objects.

## API Explanation

`getAllocations()` lists `Allocation` objects, and `getPrimaryAllocation()`
returns the main allocation. Firewall operations depend on node support.
Tunnel operations depend on tunnel support. Creating or deleting network
resources changes reachability and should be reviewed before applying.

## Guided Example

```python
for allocation in server.network.getAllocations():
    print(allocation.getAddress(), allocation.isPrimary())
```

## Exercise

Print the primary allocation address if present, then list each allocation's
address and notes. Do not create or delete allocations.

Hint: `getPrimaryAllocation()` can return `None`.

## Answer

```python
primary = server.network.getPrimaryAllocation()
if primary is not None:
    print('primary:', primary.getAddress())

for allocation in server.network.getAllocations():
    print(allocation.getAddress(), allocation.getNotes())
```

## Common Mistakes

- Assuming every node supports firewall or tunnel features.
- Changing a primary allocation without understanding which clients use it.
- Treating subusers as server network objects; permissions are managed through
  `server.users`.

## What You Learned

- Allocations represent address/port assignments.
- Network managers are attached to a server.
- Support checks and permission checks matter before network changes.

## Continue Learning

Next: [19 Minecraft Servers](19_Minecraft_Servers.md)

## Navigation

Previous: [17 Schedules Review](17_Schedules_Review.md)
Next: [19 Minecraft Servers](19_Minecraft_Servers.md)
Reference Docs: [Network](../reference/network.md)
Related Examples: [network answer](../../examples/tutorials/18_networking/answer.py)