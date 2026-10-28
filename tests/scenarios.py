'''
Realistic usage scenarios. Each function takes a Panel connected to the fake
panel and asserts on behaviour. They are run by test_scenarios.py and also
count towards endpoint coverage in test_contract.py.
'''
import os
import tempfile

from calagoapi import Page, InvalidActionError, triggers, conditions, actions, variable, backup_selectors
from contract import UUID


def scenarioQuickStart(panel):
    server = panel.servers.getServer('abc123')
    assert server.getName() == 'sample'
    server.restart()
    server.sendCommand('say Hello')
    # the fake answers with the first enum value of the state: 'offline'
    assert server.getStatus() == 'offline'
    assert server.getPowerState() == 'offline'
    assert server.isOffline() and not server.isOnline()
    assert server.getCPU() == 1.5
    assert server.getUptime(formatted=True) == '0s'
    backup = server.createBackup()
    assert backup.getName() == 'sample' and backup.isSuccessful()
    try:
        server.powerAction('explode')
        raise AssertionError('powerAction accepted an invalid action')
    except InvalidActionError:
        pass


def scenarioPagination(panel):
    page = panel.servers.getServers(page=1, per_page=10)
    assert isinstance(page, Page)
    assert page.getTotal() == 1 and page.getPageCount() == 1 and not page.hasNextPage()
    assert len(panel.servers.getServers()) == 1


def scenarioFiles(panel):
    server = panel.servers.getServer(UUID)
    files = server.files.listFiles('/plugins')
    assert files[0].getPath() == '/plugins/sample'

    folder = tempfile.mkdtemp()
    local = os.path.join(folder, 'plugin.jar')
    with open(local, 'wb') as f:
        f.write(b'jar')
    server.files.uploadFile('/plugins', local)
    server.files.uploadFile('/', b'eula=true', name='eula.txt')
    assert server.files.downloadFile('/server.properties') == b'filedata'
    saved = server.files.downloadFile('/world.zip', os.path.join(folder, 'world.zip'))
    with open(saved, 'rb') as f:
        assert f.read() == b'filedata'

    server.files.writeFile('/eula.txt', 'eula=true')
    server.files.renameFile('/a.txt', '/b/a.txt')
    server.files.renameFiles('/', [('world', 'world_old'), {'from': 'x', 'to': 'y'}])
    server.files.searchFiles('max-players', include=['*.properties'], min_size=1, context_lines=2)
    server.files.chmodFile('/start.sh', 755)
    server.files.copyToServer([('world', 'world')], server)


def scenarioSchedules(panel):
    server = panel.servers.getServer(UUID)
    schedule = server.schedules.createSchedule(
        'Nightly restart',
        triggers=[triggers.cron('0 0 4 * * *'), triggers.resourceUsage('memory', 'greater_than', 95, for_seconds=60)],
        condition=conditions.all(conditions.serverState('running'), conditions.variableEquals('mode', 'prod')),
        steps=[
            actions.sendCommand('say Restarting in 1 minute'),
            actions.sleep(60_000),
            actions.createBackup('nightly', foreground=True, output_into='backup'),
            actions.ifCondition(conditions.uptime('greater_than', 3_600_000)),
            actions.sendPower('restart'),
            actions.otherwise(),
            actions.exit(True),
            actions.endIf(),
            actions.deleteBackup(backup_selectors.oldest()),
            actions.waitForConsoleLine('Done', output_into='line'),
            actions.sendCommand(variable('line')),
            actions.httpRequest('https://example.com/hook', body='{"content": "ok"}', headers={'Content-Type': 'application/json'}),
        ],
    )
    server.schedules.createSchedule('Simple', triggers=[triggers.crash()])
    schedule.addStep(actions.writeFile('/log.txt', 'restarted', append=True))
    schedule.disable()
    schedule.run(skip_condition=True)


def scenarioDatabases(panel):
    server = panel.servers.getServer(UUID)
    db = server.databases.createDatabase('stats')
    assert db.getConnectionString().startswith('mysql://')
    db.explorer.insertRow('players', {'name': 'Steve', 'score': 10})
    db.explorer.updateRow('players', where={'id': 1}, values={'score': None})

    instance = server.databases.createInstance({'uuid': UUID}, 'main-db')
    instance.start()
    database = instance.createDatabase('players')
    explorer = database.explorer
    explorer.getSchema()
    explorer.getTableTypes()
    explorer.query('SELECT 1', rows=10, read_only=True)
    explorer.getRows('players', limit=5, filters=[{'column': 'name', 'operator': 'eq', 'value': 'Steve'}])
    explorer.insertRows('players', [{'name': 'a'}, {'name': 'b'}])
    explorer.updateRow('players', where={'id': 1}, values={'name': 'c'})
    explorer.deleteRow('players', where={'id': 1})
    explorer.createTable('t', [{'name': 'id', 'type': 'INT', 'primary_key': True}])
    explorer.addColumn('t', 'name', 'TEXT')
    explorer.renameColumn('t', 'name', 'title')
    explorer.deleteColumn('t', 'title')
    explorer.renameTable('t', 't2')
    explorer.deleteTable('t2')
    database.importDump(b'-- sql', wipe=True)
    user = instance.createUser('app', databases={database: 'read_write'})
    user.setPermission(database, 'read_only')


def scenarioNetwork(panel):
    server = panel.servers.getServer(UUID)
    server.network.createSubdomain('survival', 'sample')
    server.network.addFirewallRule('deny', sources=['203.0.113.7/32'])
    server.users.addSubuser('friend@example.com', ['control.console'])
    server.tunnel.setPorts([25565, {'port': 19132, 'protocols': ['udp']}])
    server.tunnel.connect(server)
    server.tunnel.disconnect(server, incoming=True)


def scenarioMinecraft(panel):
    server = panel.servers.getMinecraftServer('abc123', server_domain='play.example.com')
    assert server.getAddress() == 'play.example.com:25565'
    server.say('hi')
    server.tellraw('@a', {'text': 'hi', 'color': 'gold'})
    server.installVersion({'uuid': UUID})
    server.getVersions('PAPER', page=1, per_page=5)
    server.getBuilds('PAPER', '1.21.1', page=1, per_page=5)


def scenarioAuth(panel):
    panel.auth.getSecurityKeyOptions('steve')
    panel.auth.getSecurityKeyOptions()
    panel.auth.loginWithSecurityKey(UUID, {}, discoverable=True)
    assert panel.auth.getOAuthLoginUrl(UUID).endswith(f'/api/auth/oauth/redirect/{UUID}')


def scenarioAdmin(panel):
    admin = panel.admin
    server = admin.servers.createServer('Survival', owner=UUID, egg=UUID, node=UUID, allocation=UUID, memory=4096)
    admin.servers.deployServer('Lobby', UUID, UUID, locations=[UUID], variables={'SERVER_JARFILE': 'paper.jar'})
    server.setLimits(memory=8192)
    server.suspend()
    server.transfer(UUID, allocation=UUID)
    server.getMounts(available=True)
    server.getDevices(available=True)

    node = admin.nodes.createNode('node-1', UUID, 'https://node1.example.com:8080', memory=65536, disk=1048576)
    node.createAllocations('0.0.0.0', range(25565, 25570), ip_alias='play.example.com')
    node.deleteAllocations()
    node.restartAllServers()
    node.transferServers(UUID, servers=[UUID])
    node.getSystemLog('wings.log', lines=100)

    user = admin.users.createUser('steve', 'steve@example.com', password='hunter22', role=UUID)
    user.suspend()
    admin.announcements.createAnnouncement('Maintenance', 'Reboot at 02:00 UTC', type='warning')
    admin.email.updateTemplate('password reset', subject='Reset')
    admin.email.createVariable('brand', 'HungerNet')
    admin.locations.createLocation('Frankfurt', flag='de').duplicate('Frankfurt 2')
    egg = admin.nests.findEgg('sample')
    egg.duplicate('Paper copy')
    egg.createVariable('Jar', 'SERVER_JARFILE', 'server.jar', rules=['required', 'string'])


SCENARIOS = [
    scenarioQuickStart,
    scenarioPagination,
    scenarioFiles,
    scenarioSchedules,
    scenarioDatabases,
    scenarioNetwork,
    scenarioMinecraft,
    scenarioAuth,
    scenarioAdmin,
]
