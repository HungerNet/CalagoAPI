# Introduction

## What You Will Learn

- How the course is organized
- The CalagoAPI object hierarchy
- How to work through exercises without an automatic grader

## Prerequisites

None. Basic familiarity with using a computer is enough to begin.

## Estimated Time

5 minutes

## Concepts Introduced

- Panel
- Managers
- Servers
- Resources
- Reference documentation versus tutorials

## Concept Explanation

CalagoAPI is a Python SDK for a Calagopus panel. The learning path follows the
objects you will use: `Panel` gives access to managers; managers find `Server`
objects; servers expose resources such as files, backups, databases, schedules,
and network settings. Later lessons combine these pieces into automation,
extensions, and administration.

Each tutorial is deliberately small. Read the explanation, type the exercise
yourself, compare it with the answer, then continue. No runner or automatic
validation is required. The [reference section](../reference/README.md) is a
lookup manual, not a replacement for the learning order.

## API Explanation

The course begins at `Panel`, the connection and lifetime boundary. A call such
as `panel.servers.getServer(...)` goes through a manager and returns a server
object. That object owns managers such as `server.files` and `server.backups`.

## Guided Example

```text
Panel -> panel.servers -> GenericServer -> server.files / server.backups / ...
```

## Exercise

In your own words, explain what each part represents: `Panel`, `ServerManager`,
`GenericServer`, and `FileManager`.

Hint: Think about connection, lookup, one server, and one server resource.

## Answer

- `Panel` represents a connection to a Calagopus panel.
- `ServerManager` looks up and lists servers accessible to that panel key.
- `GenericServer` represents one server and its actions and state.
- `FileManager` manages files belonging to that server.

## Common Mistakes

- Treating reference pages and tutorials as the same thing. Reference pages
  describe individual APIs; tutorials explain a workflow in sequence.
- Assuming every API key can access every server or action. Permissions are
  enforced by the panel.

## What You Learned

- The course follows Panel -> Managers -> Servers -> Resources.
- Exercises are for practice and include full answers for review.
- The reference is available whenever you need a method lookup.

## Continue Learning

Next: [01 Installation](01_Installation.md)

## Navigation

Previous: Start here
Next: [01 Installation](01_Installation.md)
Reference Docs: [Getting started](../reference/getting-started.md)
Related Examples: [object model answer](../../examples/tutorials/00_introduction/answer.py)