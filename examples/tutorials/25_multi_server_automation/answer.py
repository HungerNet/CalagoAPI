import os
from calagoapi import Panel

with Panel(os.environ['CALAGOPUS_URL'], os.environ['CALAGOPUS_API_KEY']) as panel:
    report = []
    for server in panel.servers.getServers():
        report.append({
            'name': server.getName(),
            'short_id': server.getShortId(),
            'status': server.getStatus(),
            'has_properties': server.files.exists('/server.properties'),
        })

    for row in report:
        print(row)

    try:
        print('panel stats:', panel.admin.getStats())
    except Exception as error:
        print('admin statistics unavailable:', type(error).__name__)