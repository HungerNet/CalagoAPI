# Where to Go Next

## What You Will Learn

- Choose a next path based on your goals
- Find API details and contributor information
- Turn tutorial scripts into maintainable automation

## Prerequisites

[26 Final Review](26_Final_Review.md).

## Estimated Time

10 minutes

## Concepts Introduced

- Reference-led work
- Production hardening
- Contributor learning paths

## Concept Explanation

Completing the tutorials gives you a working model of CalagoAPI. Real tools
need additional decisions about permissions, logging, retries, secrets,
deployment, and failure recovery. Keep the reference nearby and build each
automation from the smallest observable operation upward.

## API Explanation

The [API reference](../reference/README.md) is organized by feature. Extension
users and authors can continue with [extension guides](../extensions/01_Extensions_Overview.md).
Contributors can explore the [architecture overview](../architecture/Architecture.md),
then the implementation-focused pages and the test suite.

## Add Error Handling to a Script

When adapting a walkthrough, keep the same object flow but make failures
visible to the caller. CalagoAPI raises typed exceptions, so handle a missing
server separately from other API errors:

```python
import os
from calagoapi import CalagoAPIError, NotFoundError, Panel

try:
   with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
      server = panel.servers.getServer(os.environ['SERVER_ID'])
      print(server.getName(), server.getStatus())
except NotFoundError:
   print('The configured server ID was not found or is not accessible.')
except CalagoAPIError as error:
   print('CalagoAPI request failed:', error.status_code, error.message)
```

Then review the matching reference page for exact parameters, request the
minimum permissions needed, and test against a fake or non-production panel
before enabling state-changing actions. The SDK already retries rate limits
and selected transient read failures; writes are not retried automatically.

## Common Mistakes

- Copying an example into production without adding configuration validation,
  logging, and failure handling.
- Giving a service account broader permissions than its workflow requires.
- Treating tutorial scripts as the only way to structure an application.

## What You Learned

- Reference docs are the source for exact API signatures and behavior.
- Projects are starting points that need production-specific controls.
- Architecture docs explain internals for contributors, not end-user workflows.

## Continue Learning

Next: Explore the [API reference](../reference/README.md),
[extensions](../extensions/01_Extensions_Overview.md), or
[contributor architecture](../architecture/Architecture.md).

## Navigation

Previous: [26 Final Review](26_Final_Review.md)
Next: [API Reference](../reference/README.md)
Reference Docs: [API Reference](../reference/README.md)
Related Examples: Code examples are embedded in this walkthrough.