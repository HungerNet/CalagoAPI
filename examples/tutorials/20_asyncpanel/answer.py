import asyncio
import os
from calagoapi import AsyncPanel

async def main():
    async with AsyncPanel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
        servers = await panel.servers.getServers()
        statuses = await asyncio.gather(*(server.getStatus() for server in servers))
        for server, status in zip(servers, statuses):
            print(server.name, status)

asyncio.run(main())