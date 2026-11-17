'''
Minecraft example 3: a health report that combines panel and HungerBridge data.

    CALAGOPUS_URL=... CALAGOPUS_API_KEY=... MC_SERVER=... HB_URL=... HB_TOKEN=... \
        python examples/minecraft/03_monitoring.py

getRAM() and getCPU() describe the container (the panel's view). getMemoryInfo()
and getProcessorInfo() describe the Java process inside it (HungerBridge's view).
Both are useful: a full heap with plenty of container RAM means -Xmx is too low.
'''
from calagoapi import Panel
from calagoapi.extensions import enable

import _env

TPS_WARNING = 18.0
HEAP_WARNING = 0.9


def report(server) -> list:
    '''Returns a list of warnings and prints a short report.'''
    server.refresh()                                     # one fresh panel resources call
    performance = server.getPerformance()
    memory = server.getMemoryInfo()
    cpu = server.getProcessorInfo()
    threads = server.getThreadInfo()

    print(f'{server.name}')
    print(f'  container  RAM {server.getRAM()} / {server.getRAMLimit()} MiB, CPU {server.getCPU()} %')
    print(f'  java       heap {memory["used"]:.0f} / {memory["max"]:.0f} MiB, '
          f'CPU load {cpu["load"] * 100:.0f} % of {cpu["processors"]} cores, {threads["current"]} threads')
    print(f'  game       TPS {performance["tps"]["1m"]} (1m), MSPT {performance["mspt"]}, '
          f'{performance["players"]}/{performance["max_players"]} players')

    warnings = []
    if 0 <= performance['tps']['1m'] < TPS_WARNING:
        warnings.append(f'TPS {performance["tps"]["1m"]} is below {TPS_WARNING}')
    if memory['max'] and memory['used'] / memory['max'] > HEAP_WARNING:
        warnings.append(f'heap is {memory["used"] / memory["max"]:.0%} full')
    for warning in warnings:
        print(f'  WARNING    {warning}')
    return warnings


def main(panel, server_id, bridge_url=None, bridge_token=None):
    server = panel.minecraft.getServer(server_id, bridge_url=bridge_url, bridge_token=bridge_token)
    return report(server)


if __name__ == '__main__':
    config = _env.settings()
    if config:
        enable('minecraft')
        with Panel(url=config['url'], api_key=config['api_key']) as panel:
            main(panel, config['server_id'], config['bridge_url'], config['bridge_token'])
