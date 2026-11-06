# Extensions Architecture

The extension system is a process-wide registry that discovers installed
packages, resolves dependencies, validates configuration, and installs declared
members onto CalagoAPI classes.

## Declaration and discovery

Decorators in `extensions/members.py` attach `MemberSpec` metadata to a method,
property, or service class; they do not patch anything. `ExtensionRegistry`
loads Python entry points from the `calagoapi` group, or accepts explicit
`register()` calls for scripts and tests.

## Enablement transaction

The registry resolves dependencies first, builds and validates effective
configuration, gathers member specs, and checks for conflicts before patching
classes. It records each installed attribute in a `Registration`. If
installation or `on_enable()` fails, the changes from that attempt are rolled
back. Successful enablement is idempotent; re-enabling with incompatible config
or mode raises an error.

## Members and modes

Methods are installed as functions and properties as descriptors. Services use
a cached descriptor that constructs one service per object on first access.
Direct mode places methods and properties on the target class; namespace mode
places them under a cached namespace. Services are already namespaces and keep
their declared attribute in either mode.

Classes are patched, not instances. The registry checks built-in members,
instance attributes, subclass shadowing, async wrapper names, and other
extension registrations. The only built-in handoff is an explicit
`@migrated_to` marker.

## Async integration

`AsyncWrapper` detects extension services and namespaces and wraps them so
their synchronous methods become awaitable. Plain `def` extension methods are
the portable default; `async def` members run directly on the event loop.

The full design and tradeoffs are recorded in [PLAN.md](../../PLAN.md). User
guides start at [Extensions Overview](../extensions/01_Extensions_Overview.md).