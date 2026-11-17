# 10 · Packaging and publishing

This builds on [07–09](../README.md#track-2-extending-calagoapi): you have working extensions in scripts.

## What you will build

A pip-installable `calagoapi-monitoring` package, so users write only
`enable('monitoring')`. At the end you will see how the same pattern scales up to
a whole game, which is how `calagoapi-minecraft` is built.

## Step 1: the layout

```
calagoapi-monitoring/
├── pyproject.toml
├── README.md
├── calagoapi_monitoring/
│   ├── __init__.py          keep it light: users never import it
│   └── extension.py         members + MonitoringExtension
└── tests/
    └── test_monitoring.py
```

Convention: `calagoapi-<name>` on PyPI, `calagoapi_<name>` as the package, and the
extension id `<name>`.

## Step 2: the entry point

```toml
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "calagoapi-monitoring"
version = "1.0.0"
requires-python = ">=3.9"
dependencies = ["calagoapi>=2.0.dev1"]

[project.entry-points."calagoapi"]
monitoring = "calagoapi_monitoring.extension:MonitoringExtension"

[tool.setuptools]
packages = ["calagoapi_monitoring"]
```

That one entry point is the whole discovery mechanism: group `calagoapi`, name = the
extension id, value = `module:ExtensionClass`.

## Step 3: install and use

```bash
pip install -e calagoapi-monitoring
python -c "from calagoapi.extensions import enable, available; print(available()); enable('monitoring')"
```

Remove the `register()` calls from your scripts. `enable('monitoring')` now finds the
package by itself.

## Step 4: test it like CalagoAPI does

- Use a fresh `ExtensionRegistry()` per test and `registry.register(YourExtension)`, so
  tests never depend on what is installed (see tutorial 07).
- Build servers from local data (`Server(panel, 'abc', data={...})`) or run against a
  fake HTTP server.
- Check `registry.ownerOf(Server, 'getMemoryPercent') == 'monitoring'`.

A complete template is in
[examples/extensions/packaged_extension/](../../../examples/extensions/packaged_extension/).

## Conflicts: what users may see

| Message | Meaning | Fix |
| --- | --- | --- |
| `cannot add method 'start' to Server: Server already defines 'start'` | your name shadows a built-in | rename, or ship in `namespace` mode |
| `... it is already provided by extension 'other'` | two extensions want one name | users enable one in `namespace` mode |
| `ExtensionLoadError: Could not load entry point 'monitoring' ...` | your package fails to import | the message carries the original error |

## Scaling up: a game extension

A game is a bigger extension built from the same parts. `calagoapi-minecraft` is the
reference:

```
calagoapi_minecraft/
├── server.py      class MinecraftServer(Server)         game features; overrides sendCommand()/streamConsole()
├── manager.py     @classExtension(Panel, 'minecraft')   panel.minecraft.getServer() → server_class=MinecraftServer
├── extension.py   MinecraftExtension                    id 'minecraft', config, secret bridge_token
├── aio.py         registerAsyncType(MinecraftServer, AsyncMinecraftServer)
└── ...            game-specific client: depends on HungerBridgePy, never core
```

The rules it follows:

1. **Subclass `Server`** for game behaviour; do not patch Minecraft methods onto every
   `Server`. Overrides keep the base call working (extra arguments are keyword-only).
2. **Build servers through core**: `panel.servers.getServer(id, server_class=YourServer, **options)`.
3. **Register async types** so `AsyncPanel` returns your async wrapper.
4. **Dependencies point one way**: your package depends on `calagoapi` and on the
   game's client library; `calagoapi` depends on neither.

## How it works

- `pip install` writes the entry point into the package metadata. `enable('x')` lists
  entry points once (no imports), loads only the one named `x`, and loads all of them
  once if `x` is an alias.
- A broken package raises `ExtensionLoadError` only when someone asks for it; it never
  stops other extensions from loading.
- `registry.discover()` rescans after installing packages while a program runs.

Reference: [Extensions](../../extensions.md). Next: track 3, [11 · Minecraft setup](../minecraft/11-minecraft-setup.md).
