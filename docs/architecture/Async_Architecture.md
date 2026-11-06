# Async Architecture

`AsyncPanel` reuses the synchronous API rather than maintaining a second set of
endpoint implementations. Its purpose is to keep blocking client operations off
an asyncio event loop while preserving the public method names and return
objects.

## Wrapping

`AsyncWrapper.__getattr__` inspects the wrapped value. Methods become
coroutines that call the synchronous method through `asyncio.to_thread()`;
coroutine functions are awaited directly. Arguments containing wrapped CalagoAPI
objects are unwrapped before the call. Returned models, lists, and `Page`
instances are wrapped recursively.

Plain attributes such as `.name` and `.data` remain ordinary attribute reads.
Getters are methods, so they are awaited. This distinction also explains why
requesting properties that perform I/O is discouraged in async code.

## Server and console handling

`AsyncServer` specializes wrapping for `streamConsole()` and `onConsoleLine()`.
`AsyncConsole` uses the native asyncio websocket API; streaming does not occupy
a worker thread for the lifetime of the connection. Other client operations
share the synchronous `Panel` held as `.target`.

`AsyncPanel` is an async context manager. Its `close()` closes async consoles
and then delegates the underlying HTTP client cleanup to a worker thread.

## Design tradeoff

One sync implementation avoids API drift and makes new ordinary methods
available asynchronously without duplication. The tradeoff is that operations
consume worker-pool capacity, and long-lived streaming must remain native async.
See the [Async reference](../reference/async.md).