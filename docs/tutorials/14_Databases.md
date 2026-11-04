# Databases

## What You Will Learn

- Distinguish hosted databases from database instances
- List and create hosted databases
- Keep connection credentials private

## Prerequisites

[13 Backups Review](13_Backups_Review.md). The server must have a database
host available and the key needs database permissions.

## Estimated Time

20 minutes

## Concepts Introduced

- Hosted database
- Database instance
- Database object and explorer
- Connection credentials

## Concept Explanation

Calagopus offers hosted databases on shared database hosts and dedicated
database instances that run as their own service. They are different resource
types. A hosted `Database` may expose an explorer; an instance manages its own
databases and users. Database passwords are credentials, not display data.

## API Explanation

Use `server.databases.getDatabases()` and `createDatabase(name)` for hosted
databases. Use `getTemplates()` and `createInstance(template, name)` for a
database instance. `Database.explorer` provides table, row, and SQL operations
when supported.

## Build a Hosted Database Setup

Start from the selected server and list its hosted databases. The manager is
scoped to that server, and each returned `Database` exposes safe metadata such
as its name and size:

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getServer(os.environ['SERVER_ID'])
  databases = server.databases.getDatabases()
  for database in databases:
    print(database.getName(), database.getSize(formatted=True))
```

For setup automation, check whether the named database already exists before
creating it. Creation may consume a server limit and returns connection
credentials, so do not print the connection string:

```python
  database = server.databases.getDatabaseByName('tutorial_stats')
  if database is None:
    database = server.databases.createDatabase('tutorial_stats')
  connection_string = database.getConnectionString()
  # Store this in an approved secret store; do not log it.
```

## Choosing an Instance Instead

For a dedicated database service, use the instance methods rather than
`createDatabase()`:

```python
templates = server.databases.getTemplates()
instance = server.databases.createInstance(templates[0], 'analytics')
print(instance.getName(), instance.getStatus())
```

Review available templates and limits before creating an instance.

## Common Mistakes

- Confusing a hosted database with a database instance.
- Printing passwords or full connection strings into logs.
- Creating a database repeatedly in a script without checking if it already
  exists.

## What You Learned

- `server.databases` manages resources for one server.
- Hosted databases and dedicated instances have distinct workflows.
- Connection strings contain secrets and should be protected.

## Continue Learning

Next: [15 Databases Review](15_Databases_Review.md)  

## Navigation

Previous: [13 Backups Review](13_Backups_Review.md)  
Next: [15 Databases Review](15_Databases_Review.md)  
Reference Docs: [Databases](../reference/databases.md)  
Related Examples: Code examples are embedded in this walkthrough.