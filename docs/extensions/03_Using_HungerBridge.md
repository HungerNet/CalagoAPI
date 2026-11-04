# Using HungerBridge

HungerBridge is a Minecraft mod with its own authenticated HTTP API. The
`calagoapi-hungerbridge` package adds a `server.hungerbridge` service; it is
different from CalagoAPI's daemon-backed live console.

## Install and configure

```bash
pip install calagoapi-hungerbridge
```

The package depends on the version changer extension for its install helper.
Create a HungerBridge token in the mod and keep the secret outside source
control:

```python
import os
from calagoapi import Panel
from calagoapi.extensions import enable

enable('hungerbridge', config={'token': os.environ['HUNGERBRIDGE_TOKEN']})
with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
  server = panel.servers.getMinecraftServer(os.environ['SERVER_ID'])
  print('players:', server.hungerbridge.players())
  print('tps:', server.hungerbridge.tps())
```

The service also supports `ping()`, `status()`, `run()`, system metrics, and
`install()`. Installing the mod changes server files, so confirm the server
type and Minecraft version before running it, then restart the server.

## Common Mistakes

- Confusing `server.console` (daemon websocket) with `server.hungerbridge`
  (the mod's HTTP service).
- Putting the token in a committed script or diagnostic output.
- Assuming the default bridge URL works when the server address is private or
  overridden; configure the URL when needed.

## What You Learned

- HungerBridge is an optional service attached to a Minecraft server.
- Extension configuration is process-wide and should be set once.
- Credentials belong in environment or secret configuration, not source code.

## Navigation

Previous: [21 Extensions](../tutorials/21_Extensions.md)
Next: [22 Admin API](../tutorials/22_Admin_API.md)
Reference Docs: [First-party extensions](06_First_Party_Extensions.md)
Related Examples: [first-party extension example](../../examples/extensions/10_first_party_extensions.py)