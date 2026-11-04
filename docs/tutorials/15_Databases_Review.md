# Databases Review

## What You Will Learn

- Reinforce database object relationships
- Explain the difference between data exploration and raw SQL
- Practice safe credential handling

## Prerequisites

[14 Databases](14_Databases.md).

## Estimated Time

15 minutes

## Concepts Introduced

- Database managers
- Hosted versus dedicated resources
- Read-only queries

## Concept Explanation

The server's database manager owns database resources. The explorer is a
convenience API for schema and row operations, while a database instance has
its own lifecycle and user management. Prefer read-only inspection until you
understand which database and table you are addressing.

## API Explanation

`getDatabases()` returns hosted `Database` objects. `getInstances()` returns
`DatabaseInstance` objects. `db.explorer.query(sql, read_only=True)` runs a
read-only query by default.

## Build a Database Inventory

Use the server's `DatabaseManager` to inspect each database type without
printing credentials. Hosted database details and dedicated instance
lifecycle are separate, so the script reports them in separate loops:

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])

  print('hosted databases:')
  for database in server.databases.getDatabases():
    print(database.getName(), database.getSize(formatted=True))

  print('database instances:')
  for instance in server.databases.getInstances():
    print(instance.getName(), instance.getStatus())
```

When inspecting table data, use the database's `explorer`. Its raw SQL query
is read-only by default; keep that default unless the workflow explicitly
needs to write data.

## Common Mistakes

- Using an instance method on a hosted `Database` or vice versa.
- Forgetting the manager relationship and reaching for a panel-level database
  collection that does not represent the server's resources.
- Treating a read-only flag as a substitute for protecting credentials.

## What You Learned

- Hosted databases and database instances are separate object types.
- The explorer is attached to a database resource.
- Read-only defaults reduce accidental data changes.

## Continue Learning

Next: [16 Schedules](16_Schedules.md)

## Navigation

Previous: [14 Databases](14_Databases.md)
Next: [16 Schedules](16_Schedules.md)
Reference Docs: [Databases](../reference/databases.md)
Related Examples: Code examples are embedded in this walkthrough.