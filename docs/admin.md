# Administration

`panel.admin` exposes the Calagopus admin API. The API key must belong to an
admin and have the matching admin permissions.

All admin objects share these methods:

| Method | Description |
| --- | --- |
| `getUUID()`, `getName()`, `getDescription()`, `getCreated()` | common getters |
| `refresh()` | reload from the panel |
| `update(**fields)` | change any field Calagopus accepts, only given fields change |
| `rename(name)`, `setName(name)`, `setDescription(text)` | shortcuts for `update()` |
| `delete()` | delete the object |
| `duplicate(...)` | copy, where Calagopus supports it |
| `get(key)`, `obj['key']`, `toDict()` | raw data |

Managers list with `getX(search=None, page=None, per_page=None)` (all pages
unless `page` is given) and fetch with `getX(id)`.

## Users

```python
user = panel.admin.users.createUser('steve', 'steve@example.com', password='hunter22')
user = panel.admin.users.getUser(uuid)
user = panel.admin.users.getUserByUsername('steve')
user = panel.admin.users.getUserByExternalId('billing-42')

user.suspend()
user.unsuspend()
user.freeze()
user.setPassword('new-password')
user.setAdmin(True)
user.setRole(panel.admin.roles.getRoleByName('Support'))
user.disableTwoFactor()
user.sendPasswordReset()
user.getServers(owned=True)
user.getActivity()
user.delete()
```

## Servers

```python
server = panel.admin.servers.createServer(
    'Survival',
    owner=user,
    egg=panel.admin.nests.findEgg('Paper'),
    node=node,
    allocation=node.getAvailableAllocations(page=1, per_page=1)[0]['uuid'],
    memory=4096, disk=20480, cpu=200,
    backups=3, databases=1,
)

# or let Calagopus pick the node and allocation
server = panel.admin.servers.deployServer('Lobby', user, egg, locations=[location], memory=2048)
```

Startup command, image and variables default to the egg's defaults. Extra
Calagopus fields (`description`, `external_id`, `skip_installer`,
`start_on_completion`, `timezone`, `labels`, ...) can be passed as keyword
arguments.

```python
server = panel.admin.servers.getServer(uuid)
server.getOwner(), server.getNode(), server.getEgg(), server.getLimits()

server.setLimits(memory=8192, cpu=400)
server.setFeatureLimits(backups=10)
server.setOwner(other_user)
server.setEgg(egg)
server.setVariable('SERVER_JARFILE', 'paper.jar')
server.suspend()
server.unsuspend()
server.addAllocation(allocation_uuid)
server.transfer(other_node, allocation=new_allocation)
server.cancelTransfer()
server.getInstallLogs()
server.clearState()
server.delete(delete_backups=True)

server.asServer().restart()     # regular GenericServer
```

## Nodes

```python
node = panel.admin.nodes.createNode('node-1', location, 'https://node1.example.com:8080',
                                    memory=65536, disk=1048576)
print(node.createEnrollmentCode()['code'])     # paste into the daemon to enroll

node = panel.admin.nodes.getNodeByName('node-1')
node.getSystemOverview()
node.getSystemStats()
node.getCapacity()
node.getSystemLogs()
node.getSystemLog('wings.log', lines=200)

node.createAllocations('0.0.0.0', range(25565, 25600), ip_alias='play.example.com')
node.getAllocations(assigned=False)
node.deleteAllocations([allocation_uuid])

node.enableMaintenance()
node.restartAllServers()
node.powerServers('stop', servers=[server_a, server_b])
node.transferServers(other_node)

node.getConfig()
node.updateConfig({...})
node.resetToken()
node.getTunnel(), node.createTunnel('tunnel.example.com', 4443)
node.getBackups(detached=True)
node.attachMount(mount)
```

## Locations, nests and eggs

```python
location = panel.admin.locations.createLocation('Frankfurt', flag='de')
location.getNodes()

nest = panel.admin.nests.createNest('Minecraft', author='me@example.com')
nest.importEggsFromUrls(['https://example.com/egg-paper.json'])
egg = nest.getEgg('Paper')
egg = panel.admin.nests.findEgg('Paper')       # search every nest

egg.getDockerImages(), egg.getStartupCommands()
for variable in egg.getVariables():
    print(variable.getEnvVariable(), variable.getDefaultValue())
egg.createVariable('Server Jar', 'SERVER_JARFILE', 'server.jar', rules=['required', 'string'])
egg.updateFromUrl('https://example.com/egg-paper.json')
data = egg.export()
egg.duplicate('Paper (beta)')
egg.move(other_nest)
```

### Egg repositories

```python
repo = panel.admin.egg_repositories.createEggRepository('Pelican', 'https://github.com/pelican-eggs/minecraft')
repo.sync()
repo.installEggs(repo.getEggs(), nest)
```

## Mounts, devices, roles

```python
mount = panel.admin.mounts.createMount('Shared maps', '/srv/maps', '/home/container/maps', read_only=True)
node.attachMount(mount)

gpu = panel.admin.devices.createDevice('GPU', '/dev/dri', '/dev/dri', permissions='rwm')

role = panel.admin.roles.createRole('Support', admin_permissions=['users.read', 'servers.read'])
role.getUsers()
```

## Announcements

```python
panel.admin.announcements.createAnnouncement(
    'Maintenance', 'All nodes reboot at **02:00 UTC**.',
    type='warning', locations=[location],
)
```

## Databases and backups infrastructure

```python
host = panel.admin.database_hosts.createDatabaseHost('mysql-1', 'mysql', credentials={...})
host.test()

agent = panel.admin.database_agent_hosts.getDatabaseAgentHost(uuid)
agent.getSystemOverview()
agent.getInstances()

config = panel.admin.backup_configurations.createBackupConfiguration('S3', 's3', {...})
config.getStats()

policy = panel.admin.backup_policies.createBackupPolicy('Nightly', '0 0 3 * * *')
policy.attachLocation(location)
policy.trigger()
```

## OAuth providers

```python
settings = panel.admin.oauth.discover('https://accounts.google.com')
provider = panel.admin.oauth.createProvider(name='Google', client_id='...', client_secret='...', **settings)
provider.disable()
```

## Subdomain domains

```python
domain = panel.admin.subdomain_domains.createDomain('example.com', 'cloudflare', {'api_token': '...'})
domain.test()
```

## Settings, stats and system

```python
settings = panel.admin.getSettings()
settings['app']['name'] = 'My Hosting'
panel.admin.updateSettings(app=settings['app'])

panel.admin.getStats()
panel.admin.getBackupStats()
panel.admin.getActivity()

panel.admin.system.getOverview()
panel.admin.system.getHealth()
panel.admin.system.getUpdates()
panel.admin.system.recheckUpdates()
panel.admin.system.setDebug(True)
```

## Email

```python
panel.admin.email.sendTestEmail('me@example.com')
panel.admin.email.getTemplates()
panel.admin.email.updateTemplate('password_reset', subject='Reset your password')
panel.admin.email.createVariable('support_url', 'https://example.com/support')
```

## Extensions and assets

```python
panel.admin.extensions.getExtensions()
panel.admin.extensions.disable('dev.0x7d8.subdomainmanager')
panel.admin.extensions.install('my-extension.c7s.zip', accept_license=True)
build_id = panel.admin.extensions.rebuild()
panel.admin.extensions.getBuildLogs(build_id)
panel.admin.extensions.restart()

panel.admin.assets.upload('logo.png', directory='branding')
panel.admin.assets.getAssets()
```

## Manager reference

| Attribute | Manager | Object |
| --- | --- | --- |
| `users` | `UserManager` | `User` |
| `servers` | `AdminServerManager` | `AdminServer` |
| `nodes` | `NodeManager` | `Node` |
| `locations` | `LocationManager` | `Location` |
| `nests` | `NestManager` | `Nest`, `Egg`, `EggVariable` |
| `mounts` | `MountManager` | `Mount` |
| `devices` | `DeviceManager` | `Device` |
| `roles` | `RoleManager` | `Role` |
| `announcements` | `AnnouncementManager` | `Announcement` |
| `oauth` | `OAuthProviderManager` | `OAuthProvider` |
| `database_hosts` | `DatabaseHostManager` | `DatabaseHost` |
| `database_agent_hosts` | `DatabaseAgentHostManager` | `DatabaseAgentHost` |
| `database_templates` | `DatabaseAgentTemplateManager` | `DatabaseAgentTemplate` |
| `backup_configurations` | `BackupConfigurationManager` | `BackupConfiguration` |
| `backup_policies` | `BackupPolicyManager` | `BackupPolicy` |
| `egg_repositories` | `EggRepositoryManager` | `EggRepository` |
| `egg_configurations` | `EggConfigurationManager` | `EggConfiguration` |
| `subdomain_domains` | `SubdomainDomainManager` | `SubdomainDomain` |
| `system` | `SystemManager` | |
| `email` | `EmailManager` | |
| `extensions` | `ExtensionManager` | |
| `assets` | `AssetManager` | |
