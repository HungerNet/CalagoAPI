'''
Example 10: the first-party extensions against a real panel.

Needs:
    pip install calagoapi calagoapi-version-changer calagoapi-hungerbridge

    set CALAGOPUS_URL, CALAGOPUS_API_KEY and CALAGOPUS_SERVER (a Minecraft server id)
    optionally HUNGERBRIDGE_TOKEN ("tokenId:secret") and HUNGERBRIDGE_URL

Run it:
    python examples/extensions/10_first_party_extensions.py

It only reads: nothing is installed or changed on the server.
Without the environment variables it explains what it needs and exits.
'''
import os
import sys

from calagoapi import Panel
from calagoapi.extensions import ExtensionNotFoundError, available, enable

url = os.environ.get('CALAGOPUS_URL')
api_key = os.environ.get('CALAGOPUS_API_KEY')
server_id = os.environ.get('CALAGOPUS_SERVER')
if not (url and api_key and server_id):
    print(__doc__)
    sys.exit(0)

print('installed extensions:', available())

# No imports of calagoapi_version_changer / calagoapi_hungerbridge: enable() finds
# them through their entry points.
try:
    enable('version_changer')
except ExtensionNotFoundError as e:
    print(e)              # tells you which package to pip install
    sys.exit(1)

with Panel(url=url, api_key=api_key) as panel:
    server = panel.servers.getMinecraftServer(server_id)

    build = server.installedVersion
    print('installed build:', build and build.get('name'))
    print('up to date:', server.isUpToDate())
    print('server types:', list(server.getVersionTypes())[:5])

    token = os.environ.get('HUNGERBRIDGE_TOKEN')
    if token:
        config = {'token': token}
        if os.environ.get('HUNGERBRIDGE_URL'):
            config['url'] = os.environ['HUNGERBRIDGE_URL']
        enable('hungerbridge', config=config)
        print('bridge url:', server.hungerbridge.getUrl())
        print('players:', server.hungerbridge.players())
        print('tps:', server.hungerbridge.tps())
