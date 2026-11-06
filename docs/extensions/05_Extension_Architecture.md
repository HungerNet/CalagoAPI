# Extension Architecture

This page is the extension-focused contributor overview. The detailed system
description lives in [Extensions Architecture](../architecture/Extensions_Architecture.md);
the user-facing path begins with [Extensions Overview](01_Extensions_Overview.md).

## Core pieces

- `base.py` defines extension metadata, aliases, dependencies, and validation.
- `members.py` decorates and describes methods, properties, and services.
- `discovery.py` reads `calagoapi` package entry points.
- `registry.py` owns enablement, dependency resolution, conflict checks,
  registrations, and rollback.
- `compat.py` implements explicit handover for deprecated built-in methods.

The registry is process-global. Enabling patches classes, not individual
objects, and records the owner and target of every installed member. This makes
conflicts visible and lets async wrappers adapt extension services.

## Design constraints

Decorators must remain side-effect free. Conflict detection happens before
patching. Failed activation must remove any members added in that activation.
Services are lazy and cached per object. Configuration is immutable after
enablement, and secret values are masked in diagnostics.

For detailed lifecycle and compatibility rationale, read [PLAN.md](../../PLAN.md)
and the [extension architecture reference](../architecture/Extensions_Architecture.md).