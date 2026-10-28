def _values(row: dict) -> list:
    # {'name': 'Steve'} -> [{'column': 'name', 'value': 'Steve'}]
    return [{'column': column, 'value': None if value is None else str(value)} for column, value in row.items()]


class DatabaseExplorer:
    '''
    Browse and edit a database's tables and rows, available as `database.explorer`.

    Works the same for hosted databases and databases inside a database instance.

    Args:
        panel: The Panel.
        base: Internal API path of the database.

    Example:
        explorer = server.databases.getDatabase('...').explorer
        print(explorer.getTables())
        rows = explorer.getRows('players', limit=10)
        explorer.insertRow('players', {'name': 'Steve', 'score': 10})
        explorer.query('SELECT COUNT(*) FROM players')
    '''
    def __init__(self, panel, base: str):
        self.panel = panel
        self.api = panel.api.databases
        self.base = base

    # schema
    def getSchema(self) -> dict:
        '''Returns every table with its columns. `truncated` is True for very large schemas.'''
        return self.api.schema(self.base)

    def getTables(self) -> list:
        '''Returns the list of tables.'''
        return self.getSchema().get('tables', [])

    def getTableTypes(self) -> list:
        '''Returns the column types this database supports, e.g. ['INT', 'VARCHAR', ...].'''
        return self.api.tableTypes(self.base)

    # querying
    def query(self, sql: str, rows: int = None, read_only: bool = False) -> list:
        '''
        Runs a raw SQL query.

        Args:
            sql: The query.
            rows: Maximum rows to return.
            read_only: Run inside a read-only transaction.

        Returns:
            List of result sets.

        Example:
            explorer.query('SELECT * FROM players WHERE score > 100', read_only=True)
        '''
        return self.api.query(self.base, sql, rows, read_only)

    def getRows(self, table: str, limit: int = None, offset: int = None, order_by: str = None,
                descending: bool = None, filters: list = None, schema: str = None) -> dict:
        '''
        Browses rows of a table.

        Args:
            table: Table name.
            limit: Maximum rows.
            offset: Rows to skip.
            order_by: Column to sort by.
            descending: Sort descending.
            filters: List of {'column': ..., 'operator': ..., 'value': ...}. Operators:
                eq, ne, gt, gte, lt, lte, contains, starts_with, ends_with, is_null, not_null.
            schema: Schema name (PostgreSQL).

        Example:
            explorer.getRows('players', filters=[{'column': 'name', 'operator': 'eq', 'value': 'Steve'}])
        '''
        return self.api.rows(self.base, table, schema, order_by, descending, limit, offset, filters)

    # rows
    def insertRow(self, table: str, values: dict, schema: str = None) -> int:
        '''
        Inserts a row.

        Example:
            explorer.insertRow('players', {'name': 'Steve', 'score': 10})

        Returns:
            Number of affected rows.
        '''
        return self.api.insertRows(self.base, table, [{'values': _values(values)}], schema)

    def insertRows(self, table: str, rows: list, schema: str = None) -> int:
        '''Inserts several rows, each given as a dict of column -> value.'''
        return self.api.insertRows(self.base, table, [{'values': _values(row)} for row in rows], schema)

    def updateRow(self, table: str, where: dict, values: dict, schema: str = None) -> int:
        '''
        Updates the row matching `where`.

        Example:
            explorer.updateRow('players', where={'id': 1}, values={'score': 20})
        '''
        return self.api.updateRows(self.base, table, [{'keys': _values(where), 'values': _values(values)}], schema)

    def deleteRow(self, table: str, where: dict, schema: str = None) -> int:
        '''
        Deletes the row matching `where`.

        Example:
            explorer.deleteRow('players', where={'id': 1})
        '''
        return self.api.deleteRows(self.base, table, [{'keys': _values(where)}], schema)

    def deleteRows(self, table: str, rows: list, schema: str = None) -> int:
        '''Deletes several rows, each identified by a dict of key columns.'''
        return self.api.deleteRows(self.base, table, [{'keys': _values(row)} for row in rows], schema)

    # tables
    def createTable(self, table: str, columns: list, schema: str = None) -> None:
        '''
        Creates a table.

        Args:
            columns: List of {'name', 'type', 'nullable', 'primary_key', 'auto_increment'} dicts.

        Example:
            explorer.createTable('players', [
                {'name': 'id', 'type': 'INT', 'primary_key': True, 'auto_increment': True},
                {'name': 'name', 'type': 'VARCHAR(32)'},
            ])
        '''
        return self.api.createTable(self.base, table, columns, schema)

    def renameTable(self, table: str, name: str, schema: str = None) -> None:
        '''Renames a table.'''
        return self.api.renameTable(self.base, table, name, schema)

    def deleteTable(self, table: str, schema: str = None) -> None:
        '''Drops a table.'''
        return self.api.deleteTable(self.base, table, schema)

    def addColumn(self, table: str, name: str, type: str, nullable: bool = True, primary_key: bool = False,
                  auto_increment: bool = False, schema: str = None) -> None:
        '''
        Adds a column to a table.

        Example:
            explorer.addColumn('players', 'last_seen', 'TIMESTAMP')
        '''
        column = {'name': name, 'type': type, 'nullable': nullable, 'primary_key': primary_key, 'auto_increment': auto_increment}
        return self.api.addColumn(self.base, table, column, schema)

    def renameColumn(self, table: str, column: str, name: str, schema: str = None) -> None:
        '''Renames a column.'''
        return self.api.renameColumn(self.base, table, column, name, schema)

    def deleteColumn(self, table: str, column: str, schema: str = None) -> None:
        '''Drops a column.'''
        return self.api.deleteColumn(self.base, table, column, schema)
