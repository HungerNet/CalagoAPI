# Network, subusers and tunnels

## Allocations

`server.network` is a `NetworkManager`.

```python
for allocation in server.network.getAllocations():
    print(allocation.getAddress(), allocation.isPrimary(), allocation.getNotes())

primary = server.network.getPrimaryAllocation()
extra = server.network.createAllocation()     # auto-assigned, if your limit allows it
extra.setNotes('Dynmap')
extra.makePrimary()
extra.delete()
```

`Allocation`: `getIP`, `getAlias`, `getPort`, `getAddress`, `getNotes`,
`isPrimary`, `setNotes`, `makePrimary`, `delete`.

## Subdomains

Requires the Subdomain Manager extension.

```python
server.network.getAvailableDomains()
sub = server.network.createSubdomain('survival', 'example.com')    # uses the primary allocation
print(sub.getAddress())    # 'survival.example.com'
sub.setAllocation(extra)
sub.delete()
```

## Firewall

```python
if server.network.isFirewallSupported():
    server.network.addFirewallRule('allow', ports=[25565], protocols=['tcp'])
    server.network.addFirewallRule('deny', sources=['203.0.113.7/32'])

server.network.getFirewallRules()
server.network.setFirewallRules([
    {'action': 'allow', 'protocols': ['tcp', 'udp'], 'sources': ['10.0.0.0/8'], 'ports': [25565]},
])
server.network.clearFirewallRules()
```

## Tunnels

`server.tunnel` is a `TunnelManager`. Tunnels expose ports through the
node's tunnel and let servers reach each other privately, for example a
proxy reaching its backend servers.

```python
if server.tunnel.isSupported() and not server.tunnel.exists():
    server.tunnel.createTunnel('survival')

server.tunnel.setPorts([25565, {'port': 19132, 'protocols': ['udp']}])
print(server.tunnel.getAddress(), server.tunnel.getAlias())

# let the proxy reach this server
proxy.tunnel.connect(server)
server.tunnel.getIncoming()
proxy.tunnel.getOutgoing()

proxy.tunnel.disconnect(server)
server.tunnel.deleteTunnel()
```

## Subusers

`server.users` is a `SubuserManager`. Use
`panel.account.getPermissions()['server_permissions']` to see every
permission.

```python
subuser = server.users.addSubuser('friend@example.com', ['control.console', 'control.start'])
subuser.addPermissions(['file.read'])
subuser.removePermissions(['control.start'])
subuser.setIgnoredFiles(['secrets/*'])
print(subuser.getUsername(), subuser.getPermissions(), subuser.hasPermission('file.read'))

server.users.getSubusers()
server.users.getSubuser('friend')
subuser.delete()
```
