from calagoapi.utils.resource import AdminResource, AdminManager
from calagoapi.servers.generic import GenericServer
from calagoapi.utils.model import idOf
from calagoapi.utils.exceptions import NotFoundError


class AdminServer(AdminResource):
    '''
    A server as seen by an administrator.

    Gives access to everything a server owner cannot change: limits, owner,
    egg, node, suspension, transfers, allocations and more. Use
    `asServer()` to get the regular GenericServer for power, files, etc.

    Example:
        server = panel.admin.servers.getServer('abc123')
        server.setLimits(memory=8192)
        server.suspend()
        server.transfer(other_node)
    '''
    collection = 'servers'

    def __repr__(self):
        return f'<AdminServer {self.getName()!r} ({self.getUUID()})>'

    # getters
    def getShortId(self) -> str:
        '''Returns the short id.'''
        return self.data.get('uuid_short')

    def getExternalId(self) -> str:
        '''Returns the external id used by billing systems.'''
        return self.data.get('external_id')

    def getOwner(self) -> dict:
        '''Returns the owner user.'''
        return self.data.get('owner', {})

    def getOwnerId(self) -> str:
        '''Returns the owner's UUID.'''
        return self.getOwner().get('uuid')

    def getNode(self) -> dict:
        '''Returns the node the server runs on.'''
        return self.data.get('node', {})

    def getNodeId(self) -> str:
        '''Returns the node UUID.'''
        return self.getNode().get('uuid')

    def getEgg(self) -> dict:
        '''Returns the egg.'''
        return self.data.get('egg', {})

    def getNest(self) -> dict:
        '''Returns the nest the egg belongs to.'''
        return self.data.get('nest', {})

    def getLimits(self) -> dict:
        '''Returns resource limits: cpu, memory, memory_overhead, swap, disk, io_weight, bandwidth.'''
        return self.data.get('limits', {})

    def getFeatureLimits(self) -> dict:
        '''Returns feature limits: allocations, databases, backups, schedules, subdomains.'''
        return self.data.get('feature_limits', {})

    def getStartupCommand(self) -> str:
        '''Returns the startup command.'''
        return self.data.get('startup')

    def getDockerImage(self) -> str:
        '''Returns the docker image.'''
        return self.data.get('image')

    def getLabels(self) -> dict:
        '''Returns the server labels.'''
        return self.data.get('labels', {})

    def getPinnedCPUs(self) -> list:
        '''Returns the CPU cores the server is pinned to.'''
        return self.data.get('pinned_cpus', [])

    def getInstallStatus(self) -> str:
        '''Returns None when installed, otherwise e.g. 'installing' or 'install_failed'.'''
        return self.data.get('status')

    # state checks
    def isSuspended(self) -> bool:
        '''Returns True if the server is suspended.'''
        return bool(self.data.get('is_suspended'))

    def isTransferring(self) -> bool:
        '''Returns True while the server is being transferred.'''
        return bool(self.data.get('is_transferring'))

    def isInstalled(self) -> bool:
        '''Returns True when the server is installed.'''
        return self.getInstallStatus() is None

    # settings
    def asServer(self):
        '''
        Returns the regular GenericServer for this server.

        Example:
            panel.admin.servers.getServer(server_id).asServer().restart()
        '''
        return GenericServer(self.panel, self.getUUID())

    def suspend(self) -> 'AdminServer':
        '''Suspends the server.'''
        return self.update(suspended=True)

    def unsuspend(self) -> 'AdminServer':
        '''Lifts a suspension.'''
        return self.update(suspended=False)

    def setLimits(self, **limits) -> 'AdminServer':
        '''
        Changes resource limits. Unspecified limits keep their value.

        Example:
            server.setLimits(memory=4096, cpu=200, disk=20480)
        '''
        return self.update(limits={**self.getLimits(), **limits})

    def setFeatureLimits(self, **limits) -> 'AdminServer':
        '''
        Changes feature limits. Unspecified limits keep their value.

        Example:
            server.setFeatureLimits(backups=5, databases=2)
        '''
        return self.update(feature_limits={**self.getFeatureLimits(), **limits})

    def setOwner(self, user) -> 'AdminServer':
        '''Transfers ownership to another user (User object or UUID).'''
        return self.update(owner_uuid=idOf(user))

    def setEgg(self, egg, startup: str = None, image: str = None) -> 'AdminServer':
        '''Changes the egg, optionally with a new startup command and image.'''
        return self.update(egg_uuid=idOf(egg), startup=startup, image=image)

    def setStartupCommand(self, startup: str) -> 'AdminServer':
        '''Changes the startup command.'''
        return self.update(startup=startup)

    def setDockerImage(self, image: str) -> 'AdminServer':
        '''Changes the docker image.'''
        return self.update(image=image)

    def setExternalId(self, external_id: str) -> 'AdminServer':
        '''Sets the external id.'''
        return self.update(external_id=external_id)

    def setLabels(self, labels: dict) -> 'AdminServer':
        '''Replaces the server labels.'''
        return self.update(labels=labels)

    def setBackupConfiguration(self, backup_configuration) -> 'AdminServer':
        '''Changes where backups are stored.'''
        return self.update(backup_configuration_uuid=idOf(backup_configuration))

    def clearState(self) -> None:
        '''Resets a stuck install/restore/transfer state.'''
        return self.panel.api.admin.clearServerState(self.getUUID())

    def delete(self, force: bool = False, delete_backups: bool = False) -> None:
        '''
        Deletes the server.

        Args:
            force: Delete from the panel even if the node cannot be reached.
            delete_backups: Also delete the server's backups.
        '''
        return self._api().delete(self.getUUID(), force=force, delete_backups=delete_backups)

    # transfers
    def transfer(self, node, allocation=None, allocations: list = None, backups: list = None,
                 delete_source_backups: bool = False, archive_format: str = 'tar_zstd',
                 compression_level: str = None, multiplex_channels: int = 0) -> None:
        '''
        Moves the server to another node.

        Args:
            node: Target node (object or UUID).
            allocation: Primary allocation on the target node.
            allocations: Extra allocations on the target node.
            backups: Backups (objects or UUIDs) to move along.
            delete_source_backups: Delete moved backups from the old node.
            archive_format: Archive format used for the transfer.
            compression_level: best_speed, good_speed, good_compression or best_compression.
            multiplex_channels: Parallel transfer streams.
        '''
        return self.panel.api.admin.transferServer(
            self.getUUID(),
            node_uuid=idOf(node),
            allocation_uuid=idOf(allocation),
            allocation_uuids=[idOf(a) for a in allocations or []],
            backups=[idOf(b) for b in backups or []],
            delete_source_backups=delete_source_backups,
            archive_format=archive_format,
            compression_level=compression_level,
            multiplex_channels=multiplex_channels,
        )

    def cancelTransfer(self) -> None:
        '''Cancels a running transfer.'''
        return self.panel.api.admin.cancelServerTransfer(self.getUUID())

    # allocations
    def getAllocations(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the server's allocations.'''
        return self.panel.api.admin.serverAllocations(self.getUUID(), search, page, per_page)

    def addAllocation(self, allocation) -> dict:
        '''Assigns a node allocation to the server.'''
        return self.panel.api.admin.addServerAllocation(self.getUUID(), idOf(allocation))

    def removeAllocation(self, allocation) -> None:
        '''Removes an allocation from the server.'''
        return self.panel.api.admin.removeServerAllocation(self.getUUID(), idOf(allocation))

    def setPrimaryAllocation(self, allocation) -> None:
        '''Makes an allocation the primary one.'''
        return self.panel.api.admin.updateServerAllocation(self.getUUID(), idOf(allocation), primary=True)

    # variables
    def getVariables(self) -> list:
        '''Returns every startup variable, including hidden ones.'''
        return self.panel.api.admin.serverVariables(self.getUUID())

    def setVariables(self, variables: dict) -> None:
        '''Sets startup variables, given as {env_variable: value}.'''
        return self.panel.api.admin.setServerVariables(
            self.getUUID(), [{'env_variable': k, 'value': str(v)} for k, v in variables.items()]
        )

    def setVariable(self, key: str, value) -> None:
        '''Sets one startup variable.'''
        return self.setVariables({key: value})

    # logs, backups, databases
    def getLogs(self, lines: int = None) -> str:
        '''Returns console output.'''
        return self.panel.api.admin.serverLogs(self.getUUID(), lines)

    def getInstallLogs(self, lines: int = None) -> str:
        '''Returns the output of the last install script run.'''
        return self.panel.api.admin.serverLogs(self.getUUID(), lines, install=True)

    def getBackups(self, partially_detached: bool = None, search: str = None, page: int = None, per_page: int = None):
        '''Returns the server's backups.'''
        return self.panel.api.admin.serverBackups(self.getUUID(), partially_detached, search, page, per_page)

    def deleteFailedBackups(self, force: bool = False) -> int:
        '''Deletes every failed backup. Returns how many were queued.'''
        return self.panel.api.admin.serverDeleteFailedBackups(self.getUUID(), force)

    def getDatabases(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the server's hosted databases.'''
        return self.panel.api.admin.serverDatabases(self.getUUID(), search, page, per_page)

    def getDatabaseInstances(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the server's database instances.'''
        return self.panel.api.admin.serverDatabaseInstances(self.getUUID(), search, page, per_page)

    # mounts and devices
    def getMounts(self, available: bool = False, search: str = None, page: int = None, per_page: int = None):
        '''Returns attached mounts, or mounts that could be attached with available=True.'''
        return self.panel.api.admin.serverMounts(self.getUUID(), available, search, page, per_page)

    def attachMount(self, mount) -> None:
        '''Attaches a mount.'''
        return self._api().attach(self.getUUID(), 'mounts', 'mount_uuid', idOf(mount))

    def detachMount(self, mount) -> None:
        '''Detaches a mount.'''
        return self._api().detach(self.getUUID(), 'mounts', idOf(mount))

    def getDevices(self, available: bool = False, search: str = None, page: int = None, per_page: int = None):
        '''Returns attached devices, or devices that could be attached with available=True.'''
        return self.panel.api.admin.serverDevices(self.getUUID(), available, search, page, per_page)

    def attachDevice(self, device) -> None:
        '''Attaches a device.'''
        return self._api().attach(self.getUUID(), 'devices', 'device_uuid', idOf(device))

    def detachDevice(self, device) -> None:
        '''Detaches a device.'''
        return self._api().detach(self.getUUID(), 'devices', idOf(device))


class AdminServerManager(AdminManager):
    '''
    Admin server management, available as `panel.admin.servers`.

    Example:
        server = panel.admin.servers.createServer(
            name='Survival',
            owner=user,
            egg=paper_egg,
            node=node,
            allocation=allocation,
            memory=4096,
            disk=20480,
        )
    '''
    model = AdminServer

    def getServers(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists every server on the panel as a Page of AdminServer objects.'''
        return self._list(search, page, per_page)

    def getServer(self, server_id: str) -> AdminServer:
        '''Returns a server by UUID.'''
        return self._get(server_id)

    def getServerByExternalId(self, external_id: str) -> AdminServer:
        '''Returns a server by external id.'''
        return self._wrap(self.admin.serverByExternalId(external_id))

    def _eggDefaults(self, egg_id):
        for entry in self.admin.allEggs():
            for egg in entry.get('eggs', []):
                if egg.get('uuid') == egg_id:
                    return entry['nest']['uuid'], egg
        raise NotFoundError(f'Egg {egg_id} not found')

    def _build(self, name, owner, egg, memory, disk, cpu, swap, io_weight, memory_overhead, startup, image,
               variables, allocations_limit, databases, backups, schedules, extra):
        egg_id = idOf(egg)
        if startup is None or image is None or variables is None:
            nest_id, egg_data = self._eggDefaults(egg_id)
            if startup is None:
                startup = next(iter(egg_data.get('startup_commands', {}).values()), '')
            if image is None:
                image = next(iter(egg_data.get('docker_images', {}).values()), '')
            defaults = {
                v['env_variable']: v.get('default_value') or ''
                for v in self.admin.eggVariables(nest_id, egg_id).listAll()
            }
            variables = {**defaults, **(variables or {})}

        fields = {
            'name': name,
            'owner_uuid': idOf(owner),
            'egg_uuid': egg_id,
            'limits': {'cpu': cpu, 'memory': memory, 'memory_overhead': memory_overhead, 'swap': swap, 'disk': disk, 'io_weight': io_weight},
            'feature_limits': {'allocations': allocations_limit, 'databases': databases, 'backups': backups, 'schedules': schedules},
            'startup': startup,
            'image': image,
            'variables': [{'env_variable': k, 'value': str(v)} for k, v in variables.items()],
            'pinned_cpus': [],
            'hugepages_passthrough_enabled': False,
            'kvm_passthrough_enabled': False,
            'start_on_completion': True,
            'skip_installer': False,
        }
        fields.update(extra)
        return fields

    def createServer(self, name: str, owner, egg, node, allocation=None, allocations: list = None,
                     memory: int = 1024, disk: int = 10240, cpu: int = 100, swap: int = 0, io_weight: int = None,
                     memory_overhead: int = 0, startup: str = None, image: str = None, variables: dict = None,
                     allocations_limit: int = 0, databases: int = 0, backups: int = 0, schedules: int = 0,
                     **extra) -> AdminServer:
        '''
        Creates a server on a specific node.

        Startup command, docker image and variables default to the egg's defaults.

        Args:
            name: Server name.
            owner: User object or UUID.
            egg: Egg object or UUID.
            node: Node object or UUID.
            allocation: Primary allocation (object or UUID).
            allocations: Extra allocations.
            memory: Memory limit in MiB (0 = unlimited).
            disk: Disk limit in MiB (0 = unlimited).
            cpu: CPU limit in percent, 100 = one core (0 = unlimited).
            swap: Swap in MiB (-1 = unlimited).
            io_weight: Block IO weight (10-1000).
            memory_overhead: Extra memory for the container in MiB.
            startup: Startup command.
            image: Docker image.
            variables: Startup variables as {env_variable: value}.
            allocations_limit: How many allocations the owner may add.
            databases: How many databases the owner may create.
            backups: How many backups the owner may keep.
            schedules: How many schedules the owner may create.
            **extra: Any other Calagopus field, e.g. description, external_id,
                start_on_completion, skip_installer, timezone, labels.
        '''
        fields = self._build(name, owner, egg, memory, disk, cpu, swap, io_weight, memory_overhead, startup, image,
                             variables, allocations_limit, databases, backups, schedules, extra)
        fields['node_uuid'] = idOf(node)
        fields['allocation_uuid'] = idOf(allocation)
        fields['allocation_uuids'] = [idOf(a) for a in allocations or []]
        return self._create(**fields)

    def deployServer(self, name: str, owner, egg, locations: list, allow_overallocation: bool = False,
                     memory: int = 1024, disk: int = 10240, cpu: int = 100, swap: int = 0, io_weight: int = None,
                     memory_overhead: int = 0, startup: str = None, image: str = None, variables: dict = None,
                     allocations_limit: int = 0, databases: int = 0, backups: int = 0, schedules: int = 0,
                     **extra) -> AdminServer:
        '''
        Creates a server and lets Calagopus pick the node and allocation.

        Args:
            locations: Locations (objects or UUIDs) the server may be placed in.
            allow_overallocation: Allow nodes that are already full.

        All other arguments are the same as createServer().

        Example:
            panel.admin.servers.deployServer('Lobby', user, egg, locations=[eu_location], memory=2048)
        '''
        fields = self._build(name, owner, egg, memory, disk, cpu, swap, io_weight, memory_overhead, startup, image,
                             variables, allocations_limit, databases, backups, schedules, extra)
        fields['deployment'] = {
            'location_uuids': [idOf(l) for l in locations],
            'allow_overallocation': allow_overallocation,
        }
        return self._wrap(self.admin.deployServer(**fields))

    def deleteServer(self, server, force: bool = False, delete_backups: bool = False) -> None:
        '''Deletes a server.'''
        return self._delete(server, force=force, delete_backups=delete_backups)
