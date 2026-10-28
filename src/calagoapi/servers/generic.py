from calagoapi.utils.model import Model, idOf
from calagoapi.utils.convert import formatDuration
from calagoapi.utils.exceptions import InvalidActionError
from calagoapi.utils import time as _time
from calagoapi.files import FileManager
from calagoapi.backups import BackupManager
from calagoapi.databases import DatabaseManager
from calagoapi.schedules import ScheduleManager
from calagoapi.users import SubuserManager, Activity
from calagoapi.network import NetworkManager, Allocation
from calagoapi.tunnels import TunnelManager
from calagoapi.console import Console


POWER_ACTIONS = ('start', 'restart', 'stop', 'kill')


class GenericServer(Model):
    '''
    A Calagopus server.

    Usually obtained with `panel.servers.getServer()`. Every feature of a
    server is reachable from here, either directly (power, console, status,
    resources, settings) or through a sub-manager:

    - `server.files`       FileManager
    - `server.backups`     BackupManager
    - `server.databases`   DatabaseManager
    - `server.schedules`   ScheduleManager
    - `server.users`       SubuserManager
    - `server.network`     NetworkManager (allocations, subdomains, firewall)
    - `server.tunnel`      TunnelManager
    - `server.console`     Console (live console over websocket)

    The most common operations are also available directly on the server,
    with the same names HungerLib uses (createBackup, listFiles, ...).

    Args:
        panel: The Panel the server lives on.
        server_id: Server UUID (or short id).
        name: Optional display name. Defaults to the name on the panel.
        data: Optional server data, if already fetched.

    Example:
        server = panel.servers.getServer('abc123')

        server.restart()
        server.sendCommand('say Hello')

        if server.isOnline():
            print(server.getStatus(), server.getRAM(), server.getUptime(formatted=True))

        backup = server.createBackup('before-update')
    '''
    def __init__(self, panel, server_id: str = None, name: str = None, data: dict = None):
        super().__init__(panel, data)
        self.server_id = server_id or self.data.get('uuid')
        if not self.server_id:
            raise ValueError('A server_id is required')
        self.name = name or self.data.get('name') or self.server_id

        self._cached_resources = None

        # managers
        self.files = FileManager(self)
        self.backups = BackupManager(self)
        self.databases = DatabaseManager(self)
        self.schedules = ScheduleManager(self)
        self.users = SubuserManager(self)
        self.network = NetworkManager(self)
        self.tunnel = TunnelManager(self)
        self.console = Console(self)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name!r} ({self.server_id})>'

    def __str__(self):
        return f'{self.name} ({self.server_id})'

    def __eq__(self, other):
        if not isinstance(other, GenericServer):
            return NotImplemented
        return self.getUUID() == other.getUUID()

    def __hash__(self):
        return hash(self.getUUID())

    @property
    def api(self):
        return self.panel.api.servers


    # server details
    def details(self) -> dict:
        '''Returns cached server details, fetching them on first use.'''
        if not self.data.get('uuid'):
            self.refreshDetails()
        return self.data

    def refreshDetails(self) -> dict:
        '''Forces a refetch of the server details, caches, then returns them.'''
        self.data = self.api.get(self.server_id)
        return self.data

    def get(self, key: str, default=None):
        '''Returns a raw field from the server details.'''
        return self.details().get(key, default)

    def getUUID(self) -> str:
        '''Returns the full server UUID.'''
        return self.data.get('uuid') or self.server_id

    def getShortId(self) -> str:
        '''Returns the short server id shown in the panel URL.'''
        return self.get('uuid_short')

    def getName(self) -> str:
        '''Returns the server name from the panel.'''
        return self.get('name')

    def getDescription(self) -> str:
        '''Returns the server description.'''
        return self.get('description')

    def getNodeName(self) -> str:
        '''Returns the name of the node the server runs on.'''
        return self.get('node_name')

    def getNodeId(self) -> str:
        '''Returns the UUID of the node the server runs on.'''
        return self.get('node_uuid')

    def getLocationName(self) -> str:
        '''Returns the name of the server's location.'''
        return self.get('location_name')

    def getEgg(self) -> dict:
        '''Returns the egg (server type) information.'''
        return self.get('egg', {})

    def getEggName(self) -> str:
        '''Returns the egg name, e.g. "Paper".'''
        return self.getEgg().get('name')

    def getLimits(self) -> dict:
        '''Returns the resource limits (cpu, memory, swap, disk, ...).'''
        return self.get('limits', {})

    def getFeatureLimits(self) -> dict:
        '''Returns the feature limits (allocations, databases, backups, schedules, ...).'''
        return self.get('feature_limits', {})

    def getDockerImage(self) -> str:
        '''Returns the docker image the server runs in.'''
        return self.get('image')

    def getDockerImages(self) -> dict:
        '''Returns the docker images the egg allows, as {name: image}.'''
        return self.getEgg().get('docker_images', {})

    def getStartupCommand(self) -> str:
        '''Returns the startup command.'''
        return self.get('startup')

    def getTimezone(self) -> str:
        '''Returns the server timezone, or None for the node default.'''
        return self.get('timezone')

    def getAutoKill(self) -> dict:
        '''Returns the auto-kill settings.'''
        return self.get('auto_kill')

    def getAutoStartBehavior(self) -> str:
        '''Returns "always", "unless_stopped" or "never".'''
        return self.get('auto_start_behavior')

    def getSftpHost(self) -> str:
        '''Returns the SFTP host.'''
        return self.get('sftp_host')

    def getSftpPort(self) -> int:
        '''Returns the SFTP port.'''
        return self.get('sftp_port')

    def getPermissions(self) -> list:
        '''Returns the permissions the current API key has on this server.'''
        return self.get('permissions', [])

    def hasPermission(self, permission: str) -> bool:
        '''Returns True if the current API key has the permission (owners and admins have "*").'''
        permissions = self.getPermissions()
        return '*' in permissions or permission in permissions

    def getPrimaryAllocation(self) -> Allocation:
        '''Returns the primary allocation, or None.'''
        data = self.get('allocation')
        return Allocation(self, data) if data else None

    def getAddress(self) -> str:
        '''
        Returns the address players connect to, e.g. "play.example.com:25565".

        Uses the IP alias when one is set.
        '''
        allocation = self.getPrimaryAllocation()
        return allocation.getAddress() if allocation else None

    def getInstallStatus(self) -> str:
        '''
        Returns the server's lifecycle status.

        Returns:
            None when installed and ready, otherwise a status such as
            'installing', 'install_failed', 'reinstall_failed' or 'restoring_backup'.
        '''
        return self.refreshDetails().get('status')

    def getNodeResources(self) -> dict:
        '''Returns resource usage of the node the server runs on.'''
        return self.api.nodeResources(self.getNodeId())


    # resource and status
    def refresh(self) -> dict:
        '''Forces refetch of resources, caches, then returns them.'''
        self._cached_resources = self.api.resources(self.server_id)
        return self._cached_resources

    def resources(self) -> dict:
        '''Returns cached resources (fetched on first use, see refresh()).'''
        return self._cached_resources or self.refresh()

    def getResources(self) -> dict:
        '''
        Returns fresh resource usage.

        Returns:
            dict with memory_bytes, memory_limit_bytes, disk_bytes, cpu_absolute,
            cpu_limit_absolute, network (rx_bytes, tx_bytes, ...), uptime and state.
        '''
        return self.refresh()

    @staticmethod
    def _size(value, rounding, gb):
        if value is None:
            return None
        div = 1024 * 1024 * (1024 if gb else 1)
        return round(value / div, rounding)

    def getRAM(self, rounding: int = 2, gb: bool = False) -> float:
        '''Returns current RAM usage in MiB (or GiB with gb=True).'''
        return self._size(self.resources().get('memory_bytes'), rounding, gb)

    def getRAMLimit(self, rounding: int = 2, gb: bool = False) -> float:
        '''Returns the RAM limit in MiB (or GiB with gb=True).'''
        return self._size(self.resources().get('memory_limit_bytes'), rounding, gb)

    def getCPU(self, rounding: int = 2) -> float:
        '''Returns current CPU usage in percent (100 = one core).'''
        cpu = self.resources().get('cpu_absolute')
        return round(cpu, rounding) if cpu is not None else None

    def getCPULimit(self) -> float:
        '''Returns the CPU limit in percent (0 = unlimited).'''
        return self.resources().get('cpu_limit_absolute')

    def getDisk(self, rounding: int = 2, gb: bool = False) -> float:
        '''Returns current disk usage in MiB (or GiB with gb=True).'''
        return self._size(self.resources().get('disk_bytes'), rounding, gb)

    def getDiskLimit(self, rounding: int = 2, gb: bool = False) -> float:
        '''Returns the disk limit in MiB (or GiB with gb=True), 0 means unlimited.'''
        disk = self.getLimits().get('disk')
        if disk is None:
            return None
        return round(disk / 1024, rounding) if gb else disk

    def getNetworkIn(self, rounding: int = 2, gb: bool = False) -> float:
        '''Returns received network traffic in MiB (or GiB with gb=True).'''
        return self._size((self.resources().get('network') or {}).get('rx_bytes'), rounding, gb)

    def getNetworkOut(self, rounding: int = 2, gb: bool = False) -> float:
        '''Returns sent network traffic in MiB (or GiB with gb=True).'''
        return self._size((self.resources().get('network') or {}).get('tx_bytes'), rounding, gb)

    def getUptime(self, formatted: bool = False):
        '''
        Returns current uptime.

        Args:
            formatted: Return a string like "3h 12m" instead of milliseconds.
        '''
        uptime = self.resources().get('uptime')
        if uptime is None or not formatted:
            return uptime
        return formatDuration(uptime)

    def getStatus(self) -> str:
        '''
        Returns the server's current power state (always fresh).

        Returns:
            'running', 'offline', 'starting' or 'stopping'.

        Example:
            print(server.getStatus())
        '''
        return self.refresh().get('state')

    def getPowerState(self) -> str:
        '''Alias of getStatus().'''
        return self.getStatus()


    # state helpers
    def isOnline(self) -> bool:
        '''Returns True if the server is running.'''
        return self.getStatus() == 'running'

    def isOffline(self) -> bool:
        '''Returns True if the server is fully offline.'''
        return self.getStatus() == 'offline'

    def isRunning(self) -> bool:
        '''Alias of isOnline().'''
        return self.isOnline()

    def isStopped(self) -> bool:
        '''Alias of isOffline().'''
        return self.isOffline()

    def isStarting(self) -> bool:
        '''Returns True while the server is starting.'''
        return self.getStatus() == 'starting'

    def isStopping(self) -> bool:
        '''Returns True while the server is stopping.'''
        return self.getStatus() == 'stopping'

    def isInstalled(self) -> bool:
        '''Returns True when installation has finished and the server is usable.'''
        return self.getInstallStatus() is None

    def isInstalling(self) -> bool:
        '''Returns True while the server is (re)installing.'''
        return self.getInstallStatus() == 'installing'

    def isInstallFailed(self) -> bool:
        '''Returns True if the last (re)install failed.'''
        return self.getInstallStatus() in ('install_failed', 'reinstall_failed')

    def isRestoringBackup(self) -> bool:
        '''Returns True while a backup is being restored.'''
        return self.getInstallStatus() == 'restoring_backup'

    def isSuspended(self) -> bool:
        '''Returns True if the server is suspended.'''
        return bool(self.refreshDetails().get('is_suspended'))

    def isTransferring(self) -> bool:
        '''Returns True while the server is being moved to another node.'''
        return bool(self.refreshDetails().get('is_transferring'))

    def isOwner(self) -> bool:
        '''Returns True if the API key's user owns this server.'''
        return bool(self.get('is_owner'))

    def isNodeInMaintenance(self) -> bool:
        '''Returns True if the server's node is in maintenance mode.'''
        return bool(self.refreshDetails().get('node_maintenance_enabled'))

    def waitForState(self, state: str, timeout: int = 60, interval: int = 2) -> bool:
        '''Blocks until the server reaches a power state. Returns False on timeout.'''
        return _time.waitForState(self, state, timeout, interval)

    def waitForOnline(self, timeout: int = 60, interval: int = 2) -> bool:
        '''
        Blocks until the server is running. Returns False on timeout.

        Example:
            server.start()
            server.waitForOnline(timeout=120)
        '''
        return _time.waitForOnline(self, timeout, interval)

    def waitForOffline(self, timeout: int = 60, interval: int = 2) -> bool:
        '''Blocks until the server is offline. Returns False on timeout.'''
        return _time.waitForOffline(self, timeout, interval)


    # power actions
    def powerAction(self, action: str) -> None:
        '''
        Executes a power action on the server. Valid actions:
        - start
        - restart
        - stop
        - kill
        '''
        if action not in POWER_ACTIONS:
            raise InvalidActionError(f'Invalid power action "{action}", expected one of: {", ".join(POWER_ACTIONS)}')
        return self.api.power(self.server_id, action)

    def start(self) -> None:
        '''Starts the server.'''
        return self.powerAction('start')

    def restart(self) -> None:
        '''Restarts the server.'''
        return self.powerAction('restart')

    def stop(self) -> None:
        '''Stops the server gracefully.'''
        return self.powerAction('stop')

    def kill(self) -> None:
        '''Kills the server process immediately.'''
        return self.powerAction('kill')


    # console
    def sendCommand(self, command: str) -> None:
        '''
        Sends a command to the server console.

        Example:
            server.sendCommand('say Hello')
        '''
        return self.api.command(self.server_id, command)

    def sendCommands(self, commands: list) -> None:
        '''Sends several commands in order.'''
        for command in commands:
            self.sendCommand(command)

    def getLogs(self, lines: int = None) -> str:
        '''
        Returns the recent console output.

        Args:
            lines: Number of lines to return.
        '''
        return self.api.logs(self.server_id, lines)

    def getWebsocket(self) -> dict:
        '''
        Returns credentials for the live console websocket.

        You rarely need this, `server.console` handles the websocket for you.

        Returns:
            dict with `url` and `token`.
        '''
        return self.api.websocket(self.server_id)

    def streamConsole(self, history: bool = True, timeout: float = None):
        '''
        Yields console lines live, as they are printed.

        Args:
            history: Start with the recent lines the daemon still has.
            timeout: Stop when nothing is printed for this many seconds. None streams forever.

        Example:
            for line in server.streamConsole():
                if 'joined the game' in line:
                    print(line)
        '''
        with Console(self) as console:
            yield from console.lines(history, timeout)

    def onConsoleLine(self, callback, history: bool = False) -> Console:
        '''
        Calls `callback(line)` for every console line, in a background thread.

        Reconnects automatically. Call `server.console.stop()` to end it.

        Example:
            server.onConsoleLine(print)
        '''
        self.console.onConsoleLine(callback)
        return self.console.listen(history=history)

    def getActivity(self, search: str = None, user=None, page: int = 1, per_page: int = 50):
        '''
        Returns the server activity log as a Page of Activity objects.

        Args:
            user: Only show events of this user (UUID).
            page: Page number (1 = newest). Pass None for every entry.
        '''
        return self.api.activity(self.server_id, idOf(user), search, page, per_page).map(
            lambda data: Activity(self.panel, data)
        )

    def getAnnouncements(self) -> list:
        '''Returns active panel announcements relevant to this server.'''
        return self.api.announcements(self.server_id)


    # settings
    def rename(self, name: str = None, description: str = None) -> 'GenericServer':
        '''Changes the server name and/or description.'''
        self.api.rename(self.server_id, name, description)
        if name:
            self.name = name
        return self._update({'name': name, 'description': description})

    def setName(self, name: str) -> 'GenericServer':
        '''Changes the server name.'''
        return self.rename(name=name)

    def setDescription(self, description: str) -> 'GenericServer':
        '''Changes the server description.'''
        return self.rename(description=description)

    def setTimezone(self, timezone: str) -> 'GenericServer':
        '''Sets the server timezone, e.g. "Europe/Berlin". None resets to the node default.'''
        self.api.setTimezone(self.server_id, timezone)
        self.data['timezone'] = timezone
        return self

    def setAutoKill(self, enabled: bool, seconds: int = None) -> None:
        '''
        Configures auto-kill: kill the server if it takes too long to stop.

        Args:
            enabled: Turn auto-kill on or off.
            seconds: Grace period before killing.
        '''
        return self.api.setAutoKill(self.server_id, enabled, seconds)

    def setAutoStart(self, behavior: str) -> None:
        '''Sets auto-start after node reboots: "always", "unless_stopped" or "never".'''
        return self.api.setAutoStart(self.server_id, behavior)

    def reinstall(self, truncate_directory: bool = False, start_on_completion: bool = None) -> None:
        '''
        Reinstalls the server using its egg's install script.

        Args:
            truncate_directory: Delete every file first.
            start_on_completion: Start the server once installed.
        '''
        return self.api.reinstall(self.server_id, truncate_directory, start_on_completion)

    def cancelInstall(self) -> None:
        '''Cancels a running (re)install.'''
        return self.api.cancelInstall(self.server_id)

    def unlockInstall(self) -> None:
        '''Clears a failed install state so the server can be used again.'''
        return self.api.unlockInstall(self.server_id)


    # startup variables
    def getStartupVariables(self) -> list:
        '''
        Returns the startup variables.

        Each variable is a dict with name, env_variable, value, default_value,
        is_editable, is_secret and rules.
        '''
        return self.api.startupVariables(self.server_id)

    def getStartupVariable(self, key: str) -> str:
        '''
        Returns the value of one startup variable.

        Example:
            server.getStartupVariable('SERVER_JARFILE')
        '''
        for variable in self.getStartupVariables():
            if variable.get('env_variable') == key:
                return variable.get('value')
        return None

    def updateStartupVariable(self, key: str, value: str) -> None:
        '''
        Changes a startup variable.

        Example:
            server.updateStartupVariable('MINECRAFT_VERSION', '1.21.1')
        '''
        return self.api.updateStartupVariables(self.server_id, [{'env_variable': key, 'value': str(value)}])

    def updateStartupVariables(self, variables: dict) -> None:
        '''Changes several startup variables at once, given as {env_variable: value}.'''
        return self.api.updateStartupVariables(
            self.server_id, [{'env_variable': k, 'value': str(v)} for k, v in variables.items()]
        )

    def setStartupCommand(self, command: str) -> None:
        '''Changes the startup command.'''
        return self.api.setStartupCommand(self.server_id, command)

    def setDockerImage(self, image: str) -> None:
        '''Changes the docker image, see getDockerImages() for allowed values.'''
        return self.api.setDockerImage(self.server_id, image)


    # mounts and devices
    def getMounts(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the mounts available to this server.'''
        return self.panel.api.attachments.mounts(self.server_id, search, page, per_page)

    def attachMount(self, mount) -> None:
        '''Attaches a mount (UUID or dict) to the server.'''
        return self.panel.api.attachments.attachMount(self.server_id, _uuid(mount))

    def detachMount(self, mount) -> None:
        '''Detaches a mount from the server.'''
        return self.panel.api.attachments.detachMount(self.server_id, _uuid(mount))

    def getDevices(self, search: str = None, page: int = None, per_page: int = None):
        '''Returns the devices available to this server.'''
        return self.panel.api.attachments.devices(self.server_id, search, page, per_page)

    def attachDevice(self, device) -> None:
        '''Attaches a device (UUID or dict) to the server.'''
        return self.panel.api.attachments.attachDevice(self.server_id, _uuid(device))

    def detachDevice(self, device) -> None:
        '''Detaches a device from the server.'''
        return self.panel.api.attachments.detachDevice(self.server_id, _uuid(device))


    # file manager shortcuts
    def listFiles(self, directory: str = '/'):
        '''Lists a directory. See `server.files.listFiles()`.'''
        return self.files.listFiles(directory)

    def readFile(self, path: str) -> str:
        '''Returns a text file's contents. See `server.files.readFile()`.'''
        return self.files.readFile(path)

    def writeFile(self, path: str, content) -> None:
        '''Creates or replaces a file. See `server.files.writeFile()`.'''
        return self.files.writeFile(path, content)

    def downloadFile(self, path: str, destination: str = None):
        '''Downloads a file. See `server.files.downloadFile()`.'''
        return self.files.downloadFile(path, destination)

    def uploadFile(self, directory: str, file_data, name: str = None):
        '''Uploads a file. See `server.files.uploadFile()`.'''
        return self.files.uploadFile(directory, file_data, name)

    def deleteFiles(self, root: str, files: list) -> None:
        '''Deletes files from a directory. See `server.files.deleteFiles()`.'''
        return self.files.deleteFiles(root, files)

    def renameFiles(self, root: str, files: list) -> None:
        '''Renames files. See `server.files.renameFiles()`.'''
        return self.files.renameFiles(root, files)

    def copyFiles(self, root: str, files: list):
        '''Copies files. See `server.files.copyFiles()`.'''
        return self.files.copyFiles(root, files)

    def moveFiles(self, root: str, files: list) -> None:
        '''Moves files. See `server.files.moveFiles()`.'''
        return self.files.moveFiles(root, files)

    def createFolder(self, directory: str, name: str) -> None:
        '''Creates a directory. See `server.files.createFolder()`.'''
        return self.files.createFolder(directory, name)

    def compress(self, root: str, files: list, format: str = 'tar_gz', name: str = None):
        '''Compresses files into an archive. See `server.files.compress()`.'''
        return self.files.compress(root, files, format, name)

    def decompress(self, file_path: str) -> None:
        '''Extracts an archive. See `server.files.decompress()`.'''
        return self.files.decompress(file_path)


    # backup shortcuts
    def listBackups(self):
        '''Returns every backup. See `server.backups.getBackups()`.'''
        return self.backups.getBackups()

    def getBackups(self, search: str = None):
        '''Returns every backup. See `server.backups.getBackups()`.'''
        return self.backups.getBackups(search)

    def getBackup(self, backup_id: str):
        '''Returns one backup. See `server.backups.getBackup()`.'''
        return self.backups.getBackup(backup_id)

    def createBackup(self, name: str = None, ignored_files: list = None, group=None):
        '''
        Starts a new backup and returns it.

        Example:
            backup = server.createBackup('before-update')
            backup.waitUntilComplete()
        '''
        return self.backups.createBackup(name, ignored_files, group)

    def deleteBackup(self, backup_id: str) -> None:
        '''Deletes a backup.'''
        return self.backups.deleteBackup(backup_id)

    def restoreBackup(self, backup_id: str, truncate_directory: bool = False) -> None:
        '''Restores a backup. See `server.backups.restoreBackup()`.'''
        return self.backups.restoreBackup(backup_id, truncate_directory)

    def downloadBackup(self, backup_id: str, destination: str = None):
        '''Downloads a backup. See `server.backups.downloadBackup()`.'''
        return self.backups.downloadBackup(backup_id, destination)


    # database shortcuts
    def listDatabases(self):
        '''Returns every database. See `server.databases.getDatabases()`.'''
        return self.databases.getDatabases()

    def getDatabases(self, include_password: bool = False):
        '''Returns every database. See `server.databases.getDatabases()`.'''
        return self.databases.getDatabases(include_password=include_password)

    def createDatabase(self, name: str, host=None):
        '''Creates a database. See `server.databases.createDatabase()`.'''
        return self.databases.createDatabase(name, host)

    def rotateDatabasePassword(self, db_id: str) -> str:
        '''Generates a new database password and returns it.'''
        return self.databases.rotateDatabasePassword(db_id)

    def deleteDatabase(self, db_id: str) -> None:
        '''Deletes a database.'''
        return self.databases.deleteDatabase(db_id)


    # schedule shortcuts
    def listSchedules(self):
        '''Returns every schedule. See `server.schedules.getSchedules()`.'''
        return self.schedules.getSchedules()

    def getSchedules(self):
        '''Returns every schedule. See `server.schedules.getSchedules()`.'''
        return self.schedules.getSchedules()

    def getSchedule(self, schedule_id: str):
        '''Returns a schedule by UUID or name. See `server.schedules.getSchedule()`.'''
        return self.schedules.getSchedule(schedule_id)

    def createSchedule(self, name: str, triggers: list = None, condition: dict = None, steps: list = None, enabled: bool = True):
        '''Creates a schedule. See `server.schedules.createSchedule()`.'''
        return self.schedules.createSchedule(name, triggers, condition, steps, enabled)

    def updateSchedule(self, schedule_id: str, **fields) -> None:
        '''Updates a schedule (name, enabled, triggers, condition).'''
        return self.schedules.updateSchedule(schedule_id, **fields)

    def deleteSchedule(self, schedule_id: str) -> None:
        '''Deletes a schedule.'''
        return self.schedules.deleteSchedule(schedule_id)

    def runSchedule(self, schedule_id: str) -> None:
        '''Runs a schedule now.'''
        return self.schedules.runSchedule(schedule_id)

    def enableSchedule(self, schedule_id: str) -> None:
        '''Enables a schedule.'''
        return self.schedules.enableSchedule(schedule_id)

    def disableSchedule(self, schedule_id: str) -> None:
        '''Disables a schedule.'''
        return self.schedules.disableSchedule(schedule_id)


    # other shortcuts
    def getSubusers(self):
        '''Returns every subuser. See `server.users.getSubusers()`.'''
        return self.users.getSubusers()

    def getAllocations(self):
        '''Returns every allocation. See `server.network.getAllocations()`.'''
        return self.network.getAllocations()


def _uuid(value):
    return value.get('uuid') if isinstance(value, dict) else idOf(value)
