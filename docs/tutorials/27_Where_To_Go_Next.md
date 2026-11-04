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

## Guided Example

Suggested next steps:

1. Turn a project answer into a small module with configuration and logging.
2. Add explicit handling for timeouts, permission failures, and retryable
   errors.
3. Test the workflow against a fake panel before using a live panel.
4. Review the matching reference page before adding a new API call.

## Exercise

Choose one project and write down: the API permissions it needs, which
operations change state, how it detects failure, and where its secrets are
stored.

Hint: separate read-only setup from actions such as power changes, writes, and
restores.

## Answer

Answers depend on the chosen project. A sound plan names the required key
permissions, marks every state-changing call, checks each asynchronous result,
uses protected environment/secret storage, and describes what happens when an
operation fails or times out.

## Common Mistakes

- Copying an example into production without adding configuration validation,
  logging, and failure handling.
- Giving a service account broader permissions than its workflow requires.
- Treating tutorial answers as the only way to structure an application.

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
Related Examples: [next steps answer](../../examples/tutorials/27_where_to_go_next/answer.py)