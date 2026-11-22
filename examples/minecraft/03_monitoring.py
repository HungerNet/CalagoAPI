'''
Minecraft example 3: a health report that combines panel and HungerBridge data.

    CALAGOPUS_URL=... CALAGOPUS_API_KEY=... MC_SERVER=... HB_URL=... HB_TOKEN_ID=... HB_TOKEN_SECRET=... \
        python examples/minecraft/03_monitoring.py

getRAM() and getCPU() describe the container (the panel's view). server.bridge's
getMemoryStats() and getCPUStats() describe the Java process inside it (HungerBridge's
view). Both are useful: a full heap with plenty of container RAM means -Xmx is too low.
'''
from calagoapi import Panel
from calagoapi.extensions import enable

import _env

TPS_WARNING = 18.0
HEAP_WARNING = 0.9


def report(server) -> list:
    '''Returns a list of warnings and prints a short report.'''
    server.refresh()                                     # one fresh panel resources call
    bridge = server.bridge
    tps = bridge.getTPSStats()
    players = bridge.getPlayerStats()
    memory = bridge.getMemoryStats()                     # MiB by default
    cpu = bridge.getCPUStats()
    threads = bridge.getThreadStats()

    print(f'{server.name}')
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


def main(panel, server_id, **connection):
    server = panel.minecraft.getServer(server_id, **connection)
    return report(server)


if __name__ == '__main__':
    config = _env.settings()
    if config:
        enable('minecraft')
        with Panel(url=config['url'], api_key=config['api_key']) as panel:
            main(panel, config['server_id'], **config['connection'])
