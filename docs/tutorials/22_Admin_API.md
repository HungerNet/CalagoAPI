# Admin API

## What You Will Learn

- Access administration through `panel.admin`
- Understand admin object managers
- Separate read-only inspection from privileged changes

## Prerequisites

[21 Extensions](21_Extensions.md). You need an administrator's API key with
the matching admin permissions.

## Estimated Time

25 minutes

## Concepts Introduced

- Admin namespace
- Admin managers and resources
- Privileged operations

## Concept Explanation

`panel.admin` is a separate namespace for panel-wide administration. It does
not replace `panel.servers`; it exposes managers for users, servers, nodes,
locations, eggs, settings, and other administrative resources. Admin keys can
make high-impact changes, so begin with read operations and request only the
permissions your automation needs.

## API Explanation

Managers under `panel.admin` list and retrieve admin resource objects. For
example, `panel.admin.nodes.getNodes()` returns node objects, while
`panel.admin.getStats()` reads panel-wide statistics. Creation and update
methods require the corresponding permission and may affect many users.

## Guided Example

```python
stats = panel.admin.getStats()
print(stats)
for node in panel.admin.nodes.getNodes():
    print(node.getName())
```

## Exercise

Using an admin key, print panel statistics and list node names. Do not create,
delete, or update any resource.

Hint: the admin namespace is `panel.admin`.

## Answer

```python
print(panel.admin.getStats())
for node in panel.admin.nodes.getNodes():
    print(node.getName())
```

## Common Mistakes

- Assuming a normal user API key can call admin endpoints.
- Treating SDK extensions (`calagoapi.extensions`) as panel extensions
  (`panel.admin.extensions`).
- Using broad admin permissions for a script that only needs read access.

## What You Learned

- Admin functionality is grouped under a dedicated namespace.
- Admin resources have managers and model objects too.
- Privileged changes need narrowly scoped permission and deliberate review.

## Continue Learning

Next: [23 Project 1: Nightly Backup System](23_Project_1_Backup_System.md)

## Navigation

Previous: [21 Extensions](21_Extensions.md)
Next: [23 Project 1: Nightly Backup System](23_Project_1_Backup_System.md)
Reference Docs: [Administration](../reference/admin.md)
Related Examples: [admin answer](../../examples/tutorials/22_admin_api/answer.py)