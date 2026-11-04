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

## Guided Example

```python
for database in server.databases.getDatabases():
    print(database.getName(), database.getSize(formatted=True))
```

## Exercise

List hosted databases and print their names. Then create a hosted database
named `tutorial_stats` and store its connection string in a secret manager;
do not print it.

Hint: creation needs a configured host and may consume a server limit.

## Answer

```python
for database in server.databases.getDatabases():
    print(database.getName())

database = server.databases.createDatabase('tutorial_stats')
connection_string = database.getConnectionString()
# Save connection_string to your approved secret store; do not log it.
```

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
Related Examples: [database answer](../../examples/tutorials/14_databases/answer.py)