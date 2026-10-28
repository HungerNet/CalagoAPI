# Errors, retries, pagination and utilities

## Errors

Every error inherits from `CalagoAPIError`.

| Exception | When |
| --- | --- |
| `BadRequestError` | 400, invalid parameters |
| `AuthenticationError` | 401, invalid or expired API key |
| `PermissionDeniedError` | 403, the key lacks a permission |
| `NotFoundError` | 404 |
| `ConflictError` | 409, e.g. the server is installing or transferring |
| `RateLimitError` | 429 after all retries, see `retry_after` |
| `ServerError` | 5xx |
| `PanelConnectionError` | the panel could not be reached |
| `ConsoleError` | the [live console](console.md) could not connect, authenticate or send |
| `InvalidActionError` | invalid argument, e.g. an unknown power action (also a `ValueError`) |
| `WaitTimeoutError` | a wait helper timed out (also a `TimeoutError`) |

Each error has `message`, `status_code`, `errors` (the messages Calagopus
returned) and `response`.

```python
import time
from calagoapi import CalagoAPIError, NotFoundError, RateLimitError

try:
    server = panel.servers.getServer('abc123')
except NotFoundError:
    print('No such server')
except RateLimitError as e:
    time.sleep(e.retry_after or 5)
except CalagoAPIError as e:
    print(e.status_code, e.errors)
```

## Retries

CalagoAPI retries requests that are safe to repeat:

| Situation | Retried? |
| --- | --- |
| 429 rate limit, any method | yes, after the panel's `Retry-After` (capped at 60s) |
| Connection error or 502/503/504 on a GET | yes, after 0.5s, 1s, 2s, ... |
| Connection error or 5xx on POST/PUT/PATCH/DELETE | **no**, a power action or backup is never sent twice |

`Panel(max_retries=3)` sets the number of retries, `max_retries=0` turns
them off. A `RateLimitError` is only raised once the retries are used up.

## Closing connections

```python
with Panel(url=..., api_key=...) as panel:
    ...
# or
panel.close()
```

`close()` also closes every open live console.

## Pagination

List methods return a `Page`, a normal list with pagination info.

```python
servers = panel.servers.getServers()                # every page, combined
page = panel.servers.getServers(page=2, per_page=25)  # one page

page.getTotal()        # total results on the panel
page.getPage()
page.getPageCount()
page.hasNextPage()
len(page)
```

## Raw data

Every object keeps the full panel response:

```python
backup.get('checksum')
backup['bytes']
backup.toDict()
```

## Raw requests

For anything not wrapped yet:

```python
panel.get('/api/client/permissions')
panel.post('/api/client/servers/abc/command', json={'command': 'say hi'})

panel.api.servers.resources(server_id)   # internal API modules
```

## Utilities

```python
from calagoapi import utils, convert, formatBytes, formatDuration, waitForOnline

formatBytes(1536)                       # '1.5 KiB'
formatDuration(3_900_000)               # '1h 5m'
convert.byte(2048, 'mib', 'gib')        # 2.0
convert.time(90_000, 'ms', 'min')       # 1.5

waitForOnline(server, timeout=120)      # also server.waitForOnline()
utils.secsUntil(target_datetime)
utils.minsUntil(target_datetime)
```

## Logging requests

CalagoAPI uses `requests`. Enable its debug logging to see every request:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
