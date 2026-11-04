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

## Guided Example

```python
for db in server.databases.getDatabases():
    print(db.getName(), bool(db.getConnectionString()))
```

Do not print connection strings in a shared terminal; the boolean above only
demonstrates whether one is available.

## Exercise

1. Which object owns `getDatabases()`?
2. What is a database instance used for?
3. What is the default value of the explorer query's `read_only` argument?
4. Write code that lists instance names and statuses.

Hint: use `getInstances()` and inspect the methods on each instance.

## Answer

1. `server.databases`, a `DatabaseManager`.
2. A dedicated database server with its own databases, users, and lifecycle.
3. `True`.
4. ```python
   for instance in server.databases.getInstances():
       print(instance.getName(), instance.getStatus())
   ```

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
Related Examples: [database review answer](../../examples/tutorials/15_databases_review/answer.py)