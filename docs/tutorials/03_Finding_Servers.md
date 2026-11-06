# Finding Servers

## What You Will Learn

- Use `panel.servers` to find servers
- List all accessible servers or search by name
- Handle a server lookup that returns `None`

## Prerequisites

[02 Creating a Panel](02_Creating_A_Panel.md). Set `SERVER_ID` to a server
visible to your API key for the direct lookup example.

## Estimated Time

15 minutes

## Concepts Introduced

- `ServerManager`
- Server IDs and names
- Paginated listings

## Concept Explanation

`panel.servers` is a manager owned by the panel. It locates server objects; it
does not represent a server itself. A server ID is the stable way to request a
specific server. Searching by exact name is useful for interactive scripts but
names can change and need not be unique.

## API Explanation

`getServers(search=None, page=None, per_page=None)` returns a `Page` of
`GenericServer` objects. By default CalagoAPI retrieves all pages.
`getServer(id)` fetches one server by UUID or short ID, and
`getServerByName(name)` returns an exact match or `None`.

## Guided Example

```python
for server in panel.servers.getServers(search='survival'):
    print(server.getName(), server.getShortId())

server = panel.servers.getServerByName('Survival')
if server is None:
    print('No exact match')
```

## Exercise

List the servers your key can access and print each name and short ID. Then
look up one by the ID stored in `SERVER_ID`.

Hint: use `getServers()` for the list and `getServer()` for one known ID.

## Answer

```python
import os

for item in panel.servers.getServers():
    print(item.getName(), item.getShortId())

server = panel.servers.getServer(os.environ['SERVER_ID'])
print('selected:', server.getName())
```

## Common Mistakes

- Treating a search result as a server ID. `getServerByName()` searches for an
  exact name and can return `None`.
- Assuming a user key sees every panel server. The result is permission-scoped.
- Asking for one page and expecting all results. Omit `page` for the combined
  list, or inspect `Page` metadata when paging manually.

## What You Learned

- `panel.servers` is the lookup manager.
- A server object is returned after a lookup.
- Search results reflect the key's access and may be paginated.

## Continue Learning

Next: [04 Understanding Server Objects](04_Understanding_Server_Objects.md)

## Navigation

Previous: [02 Creating a Panel](02_Creating_A_Panel.md)
Next: [04 Understanding Server Objects](04_Understanding_Server_Objects.md)
Reference Docs: [Servers](../reference/servers.md)
Related Examples: [server listing answer](../../examples/tutorials/03_finding_servers/answer.py)