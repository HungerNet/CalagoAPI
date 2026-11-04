import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    server = panel.servers.getServer(os.environ['SERVER_ID'])
    for database in server.databases.getDatabases():
        print(database.getName())
    database = server.databases.getDatabaseByName('tutorial_stats')
    if database is None:
        database = server.databases.createDatabase('tutorial_stats')
    connection_string = database.getConnectionString()
    # Store this in an approved secret store; never print it.