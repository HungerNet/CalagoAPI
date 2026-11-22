# PLAN: calagoapi-minecraft 2.0

The ecosystem plan (HungerBridge, HungerBridgePy, CalagoAPI) lives in HungerBridge, the
source of truth: [HungerBridge/PLAN.md](https://github.com/HungerNet/HungerBridge/blob/main/PLAN.md)
(locally `../HungerBridge-1/PLAN.md`). This file lists CalagoAPI's part of it. The
previous content of this file (the CalagoAPI 2.0 design record) is in git history.

## What changes here

| Area | Change | Plan section |
|---|---|---|
| Version Changer | removed: `server.versions`, `panel.minecraft.versionChanger`, `VersionManager`, `VersionChangerAdmin`, `VersionChangerAPI`, `PANEL_EXTENSION`, `auto_backup`/`backup_*` config; the contract test lists the panel extension's endpoints as intentionally not wrapped | §1.4, §13.3 |
| Authentication | `bridge_token` → `bridge_token_id` + `bridge_token_secret` (config, `MinecraftServer(...)`, `connectBridge(token_id=, token_secret=)`); validated by HungerBridgePy's `Credentials`; `createBridgeToken()` returns `Credentials` | §8 |
| `installBridge()` | `installBridge(minecraft_version, loader, *, version=None, replace=True)`; no detection; Modrinth through HungerBridgePy `findRelease()`; `findBridgeRelease()` and the `release`/`repository`/`github_api` config removed | §5 |
| Commands and console | `sendCommand(command, *, show_console=False)`; `streamConsole()`/`onConsoleLine()` yield the bridge's canonical plain lines (`sanitize` removed) | §6.3, §7 |
| Duplicated API | MinecraftServer methods that only renamed HungerBridgePy calls are removed; use `server.bridge.<method>` | §1.2 (A1), §14 |
| Docs | extension README, Minecraft tutorials 11–15 (14 replaced), new logging tutorial, `docs/migrating-minecraft-2.0.md`, examples | §11 |

The core package (`calagoapi`) is game-agnostic and keeps its API; only its contract test
and documentation change.
