# Console Architecture

The live console is separate from the panel HTTP API: it connects directly to
the node daemon over the Calagopus Wings websocket protocol. The panel API is
used first to obtain the websocket URL and short-lived token.

## Connection lifecycle

`Console.connect()` opens the websocket, sends an `auth` event, and waits for
the daemon's authentication result. Messages use JSON text frames containing
an event name and argument list. Token-expiring events cause CalagoAPI to
request fresh credentials and authenticate again.

## Event and line APIs

`ConsoleEvent` preserves the daemon event name and string arguments, with a
helper to decode JSON arguments such as resource stats. `events()` yields all
events; `lines()` filters to console output. `waitFor()` consumes events until
a matching line arrives or the timeout expires.

Callbacks are dispatched by `listen()`, optionally on a background thread.
The listener can reconnect with backoff; exceptions from callbacks are logged
without terminating the listener. `Panel.close()` closes registered sync
consoles.

## Async implementation

`AsyncConsole` mirrors the public operations using an asyncio websocket and
background task. It does not use a thread per streaming server. See the
[console reference](../reference/console.md) and
[async architecture](Async_Architecture.md).