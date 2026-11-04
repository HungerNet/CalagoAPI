# Creating a Panel

## What You Will Learn

- Create a `Panel` connection
- Use an API key safely
- Close connections with a context manager

## Prerequisites

[01 Installation](01_Installation.md). A Calagopus panel URL and API key.

## Estimated Time

15 minutes

## Concepts Introduced

- `Panel`
- API keys and permissions
- Context managers
- Panel health checks

## Concept Explanation

`Panel` is the root of the CalagoAPI object model. It stores connection details
and creates top-level managers such as `servers`, `account`, and `admin`. The
API key determines which operations the panel permits. Treat it as a secret;
do not commit it to source control.

## API Explanation

`Panel(url, api_key, name=None, timeout=10, verify=True, max_retries=3)`
creates the connection. `ping()` checks whether the panel responds;
`validateAPI()` checks whether the key works. A `with` block calls `close()`
when its body finishes.

## Guided Example

```python
import os
from calagoapi import Panel

with Panel(
    url=os.environ['CALAGOPUS_URL'],
    api_key=os.environ['CALAGOPUS_API_KEY'],
) as panel:
    print('panel responds:', panel.ping())
    print('key valid:', panel.validateAPI())
```

## Exercise

Create a panel using environment variables and print both health-check results.
Do not print the API key.

Hint: set `CALAGOPUS_URL` and `CALAGOPUS_API_KEY` in your shell first.

## Answer

```python
import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    print(panel.ping())
    print(panel.validateAPI())
```

## Common Mistakes

- Passing a server URL instead of the panel base URL.
- Giving a key too few permissions for the next operation.
- Printing or committing a key. Load it from a secret store or environment.
- Forgetting to close a long-lived panel connection; prefer `with Panel(...)`.

## What You Learned

- `Panel` is the entry point and owns the client lifetime.
- Health and key validation are separate checks.
- API key permissions control what managers can do.

## Continue Learning

Next: [03 Finding Servers](03_Finding_Servers.md)

## Navigation

Previous: [01 Installation](01_Installation.md)
Next: [03 Finding Servers](03_Finding_Servers.md)
Reference Docs: [Getting started](../reference/getting-started.md), [Account](../reference/account.md)
Related Examples: [panel answer](../../examples/tutorials/02_creating_a_panel/answer.py)