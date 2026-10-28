from calagoapi.utils.resource import AdminResource, AdminManager
from calagoapi.servers.admin import AdminServer
from calagoapi.utils.model import idOf


class Node(AdminResource):
    '''
    A node (machine running the Calagopus daemon). Requires an admin API key.

    Example:
        node = panel.admin.nodes.getNode('...')
        print(node.getName(), node.getSystemOverview()['version'])
        node.createAllocations('0.0.0.0', range(25565, 25576))
        node.enableMaintenance()
        node.restartAllServers()
    '''
    collection = 'nodes'

    def _admin(self):
        return self.panel.api.admin

    # getters
    def getURL(self) -> str:
        '''Returns the internal daemon URL.'''
        return self.data.get('url')

    def getPublicURL(self) -> str:
        '''Returns the public daemon URL browsers use, if different.'''
        return self.data.get('public_url')

    def getLocation(self) -> dict:
        '''Returns the node's location.'''
        return self.data.get('location', {})

    def getLocationId(self) -> str:
        '''Returns the node's location UUID.'''
        return self.getLocation().get('uuid')

    def getMemory(self) -> int:
        '''Returns the total memory available for servers, in MiB.'''
        return self.data.get('memory')

    def getDisk(self) -> int:
        '''Returns the total disk available for servers, in MiB.'''
        return self.data.get('disk')

    def getSftpHost(self) -> str:
        '''Returns the SFTP host shown to users.'''
        return self.data.get('sftp_host')

    def getSftpPort(self) -> int:
        '''Returns the SFTP port.'''
        return self.data.get('sftp_port')

    def getBackupConfiguration(self) -> dict:
        '''Returns the backup configuration used by the node, if any.'''
        return self.data.get('backup_configuration')

    def isDeploymentEnabled(self) -> bool:
        '''Returns True if new servers may be deployed on the node.'''
        return bool(self.data.get('deployment_enabled'))

    def isInMaintenance(self) -> bool:
        '''Returns True if the node is in maintenance mode.'''
        return bool(self.data.get('maintenance_enabled'))

    # settings
    def duplicate(self, name: str) -> 'Node':
        '''Creates a copy of the node configuration under a new name.'''
        return self._duplicate(name=name)

    def enableMaintenance(self) -> 'Node':
        '''Puts the node into maintenance mode.'''
        return self.update(maintenance_enabled=True)

    def disableMaintenance(self) -> 'Node':
        '''Ends maintenance mode.'''
        return self.update(maintenance_enabled=False)

    def enableDeployment(self) -> 'Node':
        '''Allows automatic deployment of new servers.'''
        return self.update(deployment_enabled=True)

    def disableDeployment(self) -> 'Node':
        '''Prevents automatic deployment of new servers.'''
        return self.update(deployment_enabled=False)

    def setLocation(self, location) -> 'Node':
        '''Moves the node to another location.'''
        return self.update(location_uuid=idOf(location))

    def getConfig(self) -> dict:
        '''Returns the daemon configuration file and which paths are locked.'''
        return self._admin().nodeConfig(self.getUUID())

    def updateConfig(self, config: dict) -> bool:
        '''Applies changes to the daemon configuration. Returns True if applied.'''
        return self._admin().updateNodeConfig(self.getUUID(), config)

    # system
    def getSystemOverview(self) -> dict:
        '''Returns daemon version, CPU, memory, kernel and server counts.'''
        return self._admin().nodeGet(self.getUUID(), 'system/overview')

    def getSystemStats(self) -> dict:
        '''Returns live CPU, memory, disk and network statistics.'''
        return self._admin().nodeGet(self.getUUID(), 'system/stats')['stats']

    def getSystemIPs(self) -> list:
        '''Returns the IP addresses of the machine.'''
        return self._admin().nodeGet(self.getUUID(), 'system/ips')['ips']

    def getSystemLogs(self) -> list:
        '''Returns the daemon log files.'''
        return self._admin().nodeGet(self.getUUID(), 'system/logs')['log_files']

    def getSystemLog(self, file: str, lines: int = None) -> str:
        '''Returns the contents of a daemon log file.'''
        return self._admin().nodeSystemLog(self.getUUID(), file, lines)

    def getCapacity(self) -> dict:
        '''Returns the node's limits and how much is allocated to servers.'''
        return self._admin().nodeGet(self.getUUID(), 'capacity')

    def getBandwidth(self) -> dict:
        '''Returns whether bandwidth limiting is available on the node.'''
        return self._admin().nodeGet(self.getUUID(), 'bandwidth')

    def getTransfers(self) -> dict:
        '''Returns running server transfers.'''
        return self._admin().nodeGet(self.getUUID(), 'transfers')['transfers']

    def getTransferringServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns servers currently being transferred to or from this node.'''
        return self._api().related(self.getUUID(), 'transfers/servers', 'servers', search, page, per_page).map(
            lambda data: AdminServer(self.panel, data)
        )

    # tokens and pairing
    def getToken(self) -> dict:
        '''Returns the daemon token (token_id, token).'''
        return self._admin().nodeGet(self.getUUID(), 'token')

    def resetToken(self) -> dict:
        '''Generates a new daemon token. The daemon must be reconfigured.'''
        return self._admin().nodePost(self.getUUID(), 'reset-token')

    def createEnrollmentCode(self, remote: str = None) -> dict:
        '''Creates a one-time code the daemon can use to enroll itself (code, expires).'''
        return self._admin().nodePost(self.getUUID(), 'enrollment', {'remote': remote})

    def pair(self, pairing_code: str, remote: str = None) -> None:
        '''Pairs the node with a daemon showing `pairing_code`.'''
        return self._admin().nodePost(self.getUUID(), 'pair', {'pairing_code': pairing_code, 'remote': remote})

    # servers
    def getServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the servers on this node as AdminServer objects.'''
        return self._api().related(self.getUUID(), 'servers', 'servers', search, page, per_page).map(
            lambda data: AdminServer(self.panel, data)
        )

    def getServerResources(self) -> dict:
        '''Returns live resource usage of every server on the node.'''
        return self._admin().nodeGet(self.getUUID(), 'servers/resources')['resources']

    def powerServers(self, action: str, servers: list = None) -> int:
        '''
        Sends a power action to servers on the node.

        Args:
            action: start, stop, restart or kill.
            servers: Servers (objects or ids). Every server on the node when omitted.

        Returns:
            Number of affected servers.
        '''
        return self._admin().nodeServerPower(self.getUUID(), action, [idOf(s) for s in servers] if servers else None)

    def startAllServers(self) -> int:
        '''Starts every server on the node.'''
        return self.powerServers('start')

    def stopAllServers(self) -> int:
        '''Stops every server on the node.'''
        return self.powerServers('stop')

    def restartAllServers(self) -> int:
        '''Restarts every server on the node.'''
        return self.powerServers('restart')

    def transferServers(self, node, servers: list = None, allocation_mode: str = 'preserve_ports',
                        transfer_backups: bool = True, delete_source_backups: bool = False,
                        archive_format: str = 'tar_zstd', compression_level: str = None, multiplex_channels: int = 0) -> None:
        '''
        Moves servers from this node to another node.

        Args:
            node: Target node.
            servers: Servers to move. Every server when omitted.
            allocation_mode: none, random_primary, random_all, preserve_ports,
                egg_config_deployment or egg_config_self_assign_range.
            transfer_backups: Move backups along.
            delete_source_backups: Delete moved backups from this node.
        '''
        selector = {'type': 'uuids', 'uuids': [idOf(s) for s in servers]} if servers else {'type': 'all'}
        return self._admin().nodeServerTransfer(
            self.getUUID(),
            servers=selector,
            node_uuid=idOf(node),
            allocation_mode=allocation_mode,
            transfer_backups=transfer_backups,
            delete_source_backups=delete_source_backups,
            archive_format=archive_format,
            compression_level=compression_level,
            multiplex_channels=multiplex_channels,
        )

    # allocations
    def getAllocations(self, search: str = None, ip: str = None, port_from: int = None, port_to: int = None,
                       assigned: bool = None, page: int = None, per_page: int = None):
        '''
        Returns the node's allocations.

        Args:
            ip: Only this IP.
            port_from: Lowest port.
            port_to: Highest port.
            assigned: True for allocations used by servers, False for free ones.
        '''
        return self._admin().nodeAllocations(self.getUUID(), search, ip, port_from, port_to, assigned, page, per_page)

    def getAvailableAllocations(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns allocations not assigned to any server.'''
        return self._admin().nodeAvailableAllocations(self.getUUID(), search, page, per_page)

    def getAllocationIPs(self) -> list:
        '''Returns the IPs that have allocations.'''
        return self._admin().nodeAllocationIps(self.getUUID())

    def createAllocations(self, ip: str, ports, ip_alias: str = None) -> int:
        '''
        Creates allocations.

        Args:
            ip: IP address.
            ports: Iterable of ports, e.g. range(25565, 25600).
            ip_alias: Hostname shown to users.

        Returns:
            Number of allocations created.
        '''
        return self._admin().createNodeAllocations(self.getUUID(), ip, list(ports), ip_alias)

    def setAllocationAlias(self, ip: str, ip_alias: str = None, allocations: list = None) -> dict:
        '''Changes the IP and/or alias of allocations (all when `allocations` is omitted).'''
        return self._admin().updateNodeAllocations(self.getUUID(), _allocationSelector(allocations), ip, ip_alias)

    def deleteAllocations(self, allocations: list = None, force: bool = False) -> dict:
        '''
        Deletes allocations.

        Args:
            allocations: Allocations (dicts or UUIDs). Every allocation when omitted.
            force: Also delete allocations that are assigned to servers.
        '''
        return self._admin().deleteNodeAllocations(self.getUUID(), _allocationSelector(allocations), force)

    # mounts, devices and database hosts
    def getMounts(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the mounts attached to the node.'''
        return self._api().related(self.getUUID(), 'mounts', 'mounts', search, page, per_page)

    def attachMount(self, mount) -> None:
        '''Attaches a mount to the node.'''
        return self._api().attach(self.getUUID(), 'mounts', 'mount_uuid', idOf(mount))

    def detachMount(self, mount) -> None:
        '''Detaches a mount from the node.'''
        return self._api().detach(self.getUUID(), 'mounts', idOf(mount))

    def isMountAllowed(self, mount) -> bool:
        '''Returns True if the daemon allows the mount's source path.'''
        return self._admin().nodeGet(self.getUUID(), f'mounts/{idOf(mount)}/allowed')['allowed']

    def getDevices(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the devices attached to the node.'''
        return self._api().related(self.getUUID(), 'devices', 'devices', search, page, per_page)

    def attachDevice(self, device) -> None:
        '''Attaches a device to the node.'''
        return self._api().attach(self.getUUID(), 'devices', 'device_uuid', idOf(device))

    def detachDevice(self, device) -> None:
        '''Detaches a device from the node.'''
        return self._api().detach(self.getUUID(), 'devices', idOf(device))

    def isDeviceAllowed(self, device) -> bool:
        '''Returns True if the daemon allows the device.'''
        return self._admin().nodeGet(self.getUUID(), f'devices/{idOf(device)}/allowed')['allowed']

    def getDatabaseHosts(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns database hosts linked to the node.'''
        return self._api().related(self.getUUID(), 'database-hosts', 'database_hosts', search, page, per_page)

    def attachDatabaseHost(self, database_host) -> None:
        '''Links a database host to the node.'''
        return self._api().attach(self.getUUID(), 'database-hosts', 'database_host_uuid', idOf(database_host))

    def detachDatabaseHost(self, database_host) -> None:
        '''Unlinks a database host.'''
        return self._api().detach(self.getUUID(), 'database-hosts', idOf(database_host))

    def getDatabaseAgentHosts(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns database agent hosts linked to the node.'''
        return self._api().related(self.getUUID(), 'database-agent-hosts', 'database_agent_hosts', search, page, per_page)

    def attachDatabaseAgentHost(self, host) -> None:
        '''Links a database agent host to the node.'''
        return self._api().attach(self.getUUID(), 'database-agent-hosts', 'database_agent_host_uuid', idOf(host))

    def detachDatabaseAgentHost(self, host) -> None:
        '''Unlinks a database agent host.'''
        return self._api().detach(self.getUUID(), 'database-agent-hosts', idOf(host))

    # backups
    def getBackups(self, detached: bool = None, search: str = None, page: int = None, per_page: int = None):
        '''Returns backups stored on the node. `detached=True` for backups whose server is gone.'''
        return self._admin().nodeBackups(self.getUUID(), detached, search, page, per_page)

    def getBackup(self, backup_id: str) -> dict:
        '''Returns one backup stored on the node.'''
        return self._admin().nodeBackup(self.getUUID(), backup_id)

    def getBackupArchiveInfo(self, backup_id: str) -> dict:
        '''Returns the archive format and size a backup download would have.'''
        return self._admin().nodeBackupAction(self.getUUID(), backup_id, 'query', 'GET')

    def getBackupDownloadUrl(self, backup_id: str) -> str:
        '''Returns a signed download URL for a backup.'''
        return self._admin().nodeBackupAction(self.getUUID(), backup_id, 'download', 'GET')['url']

    def restoreBackup(self, backup_id: str, server, truncate_directory: bool = False, restore_startup: bool = None) -> None:
        '''Restores a node backup onto a server.'''
        return self._admin().nodeBackupAction(self.getUUID(), backup_id, 'restore', json={
            'server_uuid': idOf(server),
            'truncate_directory': truncate_directory,
            'restore_startup': restore_startup,
        })

    def exportBackup(self, backup_id: str, server, path: str, archive_format: str = None, foreground: bool = None) -> dict:
        '''Writes a node backup as an archive into a server's files.'''
        return self._admin().nodeBackupAction(self.getUUID(), backup_id, 'export', json={
            'server_uuid': idOf(server),
            'path': path,
            'archive_format': archive_format,
            'foreground': foreground,
        })

    def detachBackup(self, backup_id: str) -> None:
        '''Detaches a backup from its server, keeping the backup.'''
        return self._admin().nodeBackupAction(self.getUUID(), backup_id, 'detach')

    def reattachBackup(self, backup_id: str, server) -> None:
        '''Attaches a detached backup to a server.'''
        return self._admin().nodeBackupAction(self.getUUID(), backup_id, 'reattach', json={'server_uuid': idOf(server)})

    def reassignBackup(self, backup_id: str, database_instance) -> None:
        '''Assigns a database backup to another database instance.'''
        return self._admin().nodeBackupAction(self.getUUID(), backup_id, 'reassign', json={'database_instance_uuid': idOf(database_instance)})

    def deleteBackup(self, backup_id: str, force: bool = False) -> None:
        '''Deletes a backup stored on the node.'''
        return self._admin().nodeBackupAction(self.getUUID(), backup_id, None, 'DELETE', json={'force': force})

    def deleteFailedBackups(self, force: bool = False, detached: bool = None) -> int:
        '''Deletes failed backups on the node. Returns how many were queued.'''
        return self._admin().nodeDeleteFailedBackups(self.getUUID(), force, detached)

    # tunnel
    def getTunnel(self) -> dict:
        '''Returns the node tunnel and its status.'''
        return self._admin().nodeTunnel(self.getUUID())

    def createTunnel(self, host: str, port: int) -> dict:
        '''Creates the node tunnel endpoint.'''
        return self._admin().nodeTunnel(self.getUUID(), 'POST', {'host': host, 'port': port})['tunnel']

    def updateTunnel(self, host: str = None, port: int = None) -> dict:
        '''Changes the tunnel endpoint.'''
        return self._admin().nodeTunnel(self.getUUID(), 'PATCH', {'host': host, 'port': port})['tunnel']

    def deleteTunnel(self) -> None:
        '''Removes the node tunnel.'''
        return self._admin().nodeTunnel(self.getUUID(), 'DELETE')

    def getTunnelMetrics(self) -> dict:
        '''Returns tunnel traffic metrics for the node and its peers.'''
        return self._admin().nodeTunnel(self.getUUID(), suffix='/metrics')

    def rotateTunnel(self) -> None:
        '''Rotates the tunnel credentials.'''
        return self._admin().nodeTunnel(self.getUUID(), 'POST', suffix='/rotate')


class NodeManager(AdminManager):
    '''
    Node management, available as `panel.admin.nodes`.

    Example:
        node = panel.admin.nodes.createNode('node-1', location, 'https://node1.example.com:8080', memory=65536, disk=1048576)
        print(node.createEnrollmentCode()['code'])
    '''
    model = Node

    def getNodes(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists nodes as a Page of Node objects.'''
        return self._list(search, page, per_page)

    def getNode(self, node_id: str) -> Node:
        '''Returns a node by UUID.'''
        return self._get(node_id)

    def getNodeByName(self, name: str) -> Node:
        '''Returns a node by exact name, or None.'''
        return self._find(name)

    def createNode(self, name: str, location, url: str, memory: int, disk: int, sftp_port: int = 2022,
                   deployment_enabled: bool = True, maintenance_enabled: bool = False, description: str = None,
                   public_url: str = None, sftp_host: str = None, backup_configuration=None) -> Node:
        '''
        Creates a node.

        Args:
            name: Node name.
            location: Location object or UUID.
            url: Daemon URL, e.g. "https://node1.example.com:8080".
            memory: Memory available for servers, in MiB.
            disk: Disk available for servers, in MiB.
            sftp_port: SFTP port.
        '''
        return self._create(
            name=name,
            location_uuid=idOf(location),
            url=url,
            memory=memory,
            disk=disk,
            sftp_port=sftp_port,
            deployment_enabled=deployment_enabled,
            maintenance_enabled=maintenance_enabled,
            description=description,
            public_url=public_url,
            sftp_host=sftp_host,
            backup_configuration_uuid=idOf(backup_configuration),
        )

    def deleteNode(self, node) -> None:
        '''Deletes a node. It must not have servers.'''
        return self._delete(node)

    def getCapacities(self) -> dict:
        '''Returns allocated resources of every node.'''
        return self.admin.nodeCapacities()

    def probe(self, url: str, pairing_code: str) -> dict:
        '''Checks whether a daemon at `url` is reachable and shows `pairing_code`.'''
        return self.admin.probeNode(url, pairing_code)

    def updateConfigs(self, nodes: list, config: dict) -> dict:
        '''Applies the same daemon configuration change to several nodes.'''
        return self.admin.updateNodesConfig([idOf(n) for n in nodes], config)


def _allocationSelector(allocations):
    if not allocations:
        return {'type': 'all'}
    return {'type': 'uuids', 'uuids': [a.get('uuid') if isinstance(a, dict) else idOf(a) for a in allocations]}
