# 13 · Monitoring

This builds on [12](12-commands-and-console.md).

## What you will build

A health report that combines what the panel sees (the container) with what HungerBridge
sees (the Java process and the game), and flags low TPS or a nearly full heap.
Code: [examples/minecraft/03_monitoring.py](../../../examples/minecraft/03_monitoring.py).

```text
Survival
  container  RAM 3120.5 / 4096.0 MiB, CPU 87.5 %
  java       heap 2780 / 3072 MiB, CPU load 22 % of 8 cores, 61 threads
  game       TPS 17.2 (1m), MSPT 58.1, 14/50 players
  WARNING    TPS 17.2 is below 18.0
  WARNING    heap is 90% full
```

## Two views of the same server

| Question | Panel: `server.…` (CalagoAPI) | HungerBridge: `server.bridge.…` (HungerBridgePy) |
| --- | --- | --- |
| memory | `getRAM()`, `getRAMLimit()`: the container, MiB | `getMemoryStats(unit)`: `heap_*`, `nonheap_*`, `jvm_*`, `process_*`, `heap_free` |
| CPU | `getCPU()`, `getCPULimit()`: container %, 100 = one core | `getCPUStats()`: JVM process `load` 0–1, `processors` |
| uptime | `getUptime()`: the container | `getUptime()`: the JVM, ms |
| threads / GC | | `getThreadStats()`, `getGCStats()` |
| network | `getNetworkIn()`, `getNetworkOut()`: container totals | `getNetworkStats()`: host rates (Linux) |
| game | | `getTPS(window)`, `getTPSStats()`, `getMSPT()`, `getPlayers()`, `getPlayerCount()`, `getPlayerStats()`, `getWorldTimeInfo()`, `getWorldWeather()`, `getLoadedChunks()`, `getLoadedEntities()` |

The panel methods stay CalagoAPI's on purpose: they work without the plugin, match what the
panel shows, and describe the resource limits you pay for. HungerBridge's view is
**additional**. A full heap with plenty of container RAM means `-Xmx` is too low; high
container CPU with low JVM load points at something else in the container.

## Complete program

```python
from calagoapi import Panel
from calagoapi.extensions import enable

TPS_WARNING = 18.0
HEAP_WARNING = 0.9

enable('minecraft', config={'bridge_token_id': 'calagoapi', 'bridge_token_secret': '9f2c...'})


def report(server) -> list:
    server.refresh()                                   # one fresh panel resources call
    bridge = server.bridge
    tps = bridge.getTPSStats()
    players = bridge.getPlayerStats()
    memory = bridge.getMemoryStats()                   # MiB by default
    cpu = bridge.getCPUStats()
    threads = bridge.getThreadStats()

    print(server.name)
    print(f'  container  RAM {server.getRAM()} / {server.getRAMLimit()} MiB, CPU {server.getCPU()} %')
    print(f'  java       heap {memory["heap_used"]:.0f} / {memory["heap_max"]:.0f} MiB, '
          f'CPU load {cpu["load"] * 100:.0f} % of {cpu["processors"]} cores, {threads["current"]} threads')
    print(f'  game       TPS {tps["1m"]} (1m), MSPT {bridge.getMSPT()}, {players["count"]}/{players["max"]} players')

    warnings = []
    if 0 <= tps['1m'] < TPS_WARNING:
        warnings.append(f'TPS {tps["1m"]} is below {TPS_WARNING}')
    if memory['heap_max'] and memory['heap_used'] / memory['heap_max'] > HEAP_WARNING:
        warnings.append(f'heap is {memory["heap_used"] / memory["heap_max"]:.0%} full')
    for warning in warnings:
        print(f'  WARNING    {warning}')
    return warnings


with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    report(panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913'))
```

## How it works

- Every bridge metric is one HungerBridgePy call. `getTPSStats()` reads all four TPS
  windows and `getPlayerStats()` the counts and names in one request each.
- Metrics HungerBridge cannot measure are `-1` (e.g. TPS before the first ticks); the
  report treats them as unknown, not as lag.
- Panel resources are cached (tutorial 01): `refresh()` once, then read many values.
  Bridge calls are never cached.
- HungerBridge permission nodes limit what a token can read (`world.*`, `system.*`, ...).
  A missing node raises `HungerBridgeForbidden`. Create read-only tokens for dashboards.

## Next

[14 · Installing HungerBridge](14-installing-hungerbridge.md).
