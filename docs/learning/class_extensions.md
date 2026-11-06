# Class (service) extensions

A class extension attaches a **service**, an object with its own state and
methods, to every instance of a CalagoAPI class. CalagoAPI itself works this way:
`server.files`, `server.backups` and `server.console` are services.

```python
from calagoapi import MinecraftServer
from calagoapi.extensions import class_extension


@class_extension(MinecraftServer, 'hungerbridge')
class HungerBridge:
    def __init__(self, server):
        self.server = server
        self.session = None

    def players(self):
        ...

    def status(self):
        ...
```

```python
server.hungerbridge.players()
server.hungerbridge.status()
```

Runnable example: [04_service_extensions.py](../../examples/extensions/04_service_extensions.py).

## Options

```python
class_extension(target, name=None)
```

| Argument | Meaning |
| --- | --- |
| `target` | A class, or a list/tuple of classes |
| `name` | Attribute name; defaults to the class name in lowercase |

## How the service is created

- On **first access** to `server.hungerbridge`, CalagoAPI calls
  `HungerBridge(server)`, passing the object the service belongs to.
- The instance is stored on that object and **reused**:

  ```python
  server.hungerbridge is server.hungerbridge   # True
  ```

- Every object gets **its own** service:

  ```python
  survival.hungerbridge is creative.hungerbridge   # False
  ```

- Creation is thread-safe: two threads touching `server.hungerbridge` at the same
  time still get one instance.
- If `__init__` raises, nothing is cached and the next access tries again.
- Objects created before `enable()` get the service too, on first access.

Keep `__init__` cheap (store references, do not connect yet) and open connections
lazily, on first use. The HungerBridge service creates its HTTP client the first
time a request is made.

## Services and modes

A service already is a namespace, so the extension's mode does not move it:
`server.hungerbridge` stays `server.hungerbridge` in direct and namespace mode.
Only methods and properties move under `server.<namespace>` in namespace mode.

## Reading configuration

```python
@class_extension(MinecraftServer, 'hungerbridge')
class HungerBridge:
    def getUrl(self):
        config = HungerBridgeExtension.get().config
        return config['url'] or f'http://{self.server.getAddress().split(":")[0]}:{config["port"]}'
```

Per-object settings (a different token for one server) belong on the service:

```python
server.hungerbridge.connect('http://10.0.0.6:1913', 'other:41ab...')
```

## Async

On `AsyncPanel` objects the service's methods become awaitable, and the service is
cached there as well:

```python
server = await panel.servers.getMinecraftServer('abc123')
await server.hungerbridge.players()
server.hungerbridge is server.hungerbridge    # True
```

## Service or methods?

| Use a service when | Use methods when |
| --- | --- |
| the feature needs state (connection, token, cache) | each call stands alone |
| there are many related operations | there are a few |
| the names are short and generic (`players`, `status`) | the names are specific (`installVersion`) |
| it talks to something other than the panel | it extends what the object already does |

## Common mistakes

- **A service name that is already taken** (`files`, `console`, `network`):
  `ExtensionConflictError`.
- **Heavy work in `__init__`**: it runs on first attribute access, often in
  places users do not expect (`dir(server)`, debuggers, `hasattr`).
- **Storing the service globally**: each object has its own; do not share state
  through class attributes unless that is the point.
- **Targets with `__slots__`**: services are cached in the object's `__dict__`;
  CalagoAPI classes have one, slotted classes cannot get services.
