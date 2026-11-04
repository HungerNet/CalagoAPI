# Tutorial Examples

Each topic folder contains `exercise.py` for hands-on practice and `answer.py`
with a complete reference solution. These scripts are not auto-graded. Run one
from the repository root, for example:

```bash
python examples/tutorials/03_finding_servers/answer.py
```

Most scripts need `CALAGOPUS_URL` and `CALAGOPUS_API_KEY`; server lessons also
need `SERVER_ID`. Set them in your shell or secret manager. Never commit real
credentials. Read the corresponding tutorial before running an answer.

Some examples make changes: `06_power_actions`, `07_sending_commands`,
`12_backups`, `14_databases`, and `16_schedules`. Review each script before
running it against a live panel. Schedule creation examples create disabled
schedules. The monitoring example runs until interrupted.

## Topics

- [00 Introduction](00_introduction/answer.py)
- [01 Installation](01_installation/answer.py)
- [02 Creating a Panel](02_creating_a_panel/answer.py)
- [03 Finding Servers](03_finding_servers/answer.py)
- [04 Understanding Servers](04_understanding_servers/answer.py)
- [05 Status](05_status/answer.py)
- [06 Power Actions](06_power_actions/answer.py)
- [07 Sending Commands](07_sending_commands/answer.py)
- [08 Using the Console](08_using_the_console/answer.py)
- [09 Console Review](09_console_review/answer.py)
- [10 Working with Files](10_working_with_files/answer.py)
- [11 Files Review](11_files_review/answer.py)
- [12 Backups](12_backups/answer.py)
- [13 Backups Review](13_backups_review/answer.py)
- [14 Databases](14_databases/answer.py)
- [15 Databases Review](15_databases_review/answer.py)
- [16 Schedules](16_schedules/answer.py)
- [17 Schedules Review](17_schedules_review/answer.py)
- [18 Networking](18_networking/answer.py)
- [19 Minecraft Servers](19_minecraft_servers/answer.py)
- [20 AsyncPanel](20_asyncpanel/answer.py)
- [21 Extensions](21_extensions/answer.py)
- [22 Admin API](22_admin_api/answer.py)
- [23 Nightly Backup Project](23_nightly_backup/answer.py)
- [24 Server Monitor Project](24_server_monitor/answer.py)
- [25 Multi-Server Project](25_multi_server_automation/answer.py)
- [26 Final Review](26_final_review/answer.py)
- [27 Where to Go Next](27_where_to_go_next/answer.py)

The reviews reuse the examples for the feature they reinforce. Extension
packaging examples are in [examples/extensions](../extensions/README.md).