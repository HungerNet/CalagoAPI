# API Layer

The API layer is the only CalagoAPI layer that constructs panel URLs and speaks
HTTP. It keeps endpoint details out of public models and managers.

## Request flow

```text
Panel manager or model
  -> panel.api.<area>
    -> API module
      -> Client
        -> requests.Session
```

Feature modules under `src/calagoapi/api/` define endpoint-specific methods.
They pass identifiers and payload values to `Client`; callers above that layer
receive ordinary dictionaries, lists, and `Page` instances. Endpoint modules
unwrap response envelopes before returning data.

## Client responsibilities

`Client` owns the base URL, bearer authorization, session, timeout, TLS
verification, JSON parsing, typed errors, retries, pagination, and URL segment
encoding. `clean()` omits fields whose value is `None`, allowing the panel to
apply its own defaults.

Retry policy is intentionally method-sensitive: 429 responses can be retried
for any request; connection errors and selected 5xx statuses are retried only
for GET. Writes are not repeated automatically because repeating a power action
or backup creation could cause duplicate effects.

## Adding an endpoint

1. Confirm method, path, parameters, and schemas in `openapi.json`.
2. Add the endpoint to the owning API module.
3. Expose it through the appropriate manager or model, returning a public
   object where one exists.
4. Add a docstring and reference entry.
5. Run the contract and scenario tests.

The generated OpenAPI client is a verification aid, not a runtime dependency.
See [Architecture](Architecture.md#the-generated-client) and
[Errors and utilities](../reference/errors-and-utilities.md).