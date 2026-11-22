import json
import threading
import time

from hungerbridge import BridgeClient, HungerBridgeError, ReleaseAsset, Stream, redeem_pickup
from hungerbridge.protocol import MAX_HISTORY
from hungerbridge.releases import find_release, parse_asset_name

from calagoapi import Server
from calagoapi.console import Console
from calagoapi.utils.convert import formatDuration
from calagoapi.utils.exceptions import NotFoundError, WaitTimeoutError

from calagoapi_minecraft import bridge as _bridge
from calagoapi_minecraft import properties as _properties
from calagoapi_minecraft.config import checkToken, settings
from calagoapi_minecraft.exceptions import BridgeNotConfiguredError, MinecraftError
from calagoapi_minecraft.versions import VersionManager


# default Minecraft port, used when an address has none
DEFAULT_PORT = 25565


def _history(history) -> int:
    '''streamConsole(history=...) -> the bridge's ?history=N (None for none)'''
    if history is True:
        return MAX_HISTORY
    return int(history) if history else None


class MinecraftServer(Server):
    '''
    A Minecraft server: everything a Server has, plus Minecraft features.

    Two channels are used, and every method uses exactly one of them:

    - the panel / node daemon (inherited from Server): power (start, stop, ...),
      resources (getRAM, getCPU, ...), files, backups, server.properties, the
      Version Changer (`server.versions`), sendPanelCommand() and `server.console`;
    - HungerBridge, the plugin/mod inside the game, through HungerBridgePy
      (`server.bridge`): sendCommand() with output, streamConsole(), players,
      TPS/MSPT, world and JVM metrics, writeLog().

    Bridge methods need a token: `enable('minecraft', config={'bridge_token': ...})`,
    `bridge_token=` here, connectBridge(), or createBridgeToken(). Without one they
    raise BridgeNotConfiguredError. Errors from the bridge are HungerBridgePy's
    `hungerbridge.HungerBridgeError` subclasses.

    Args:
        panel: The Panel the server lives on.
        server_id: Server UUID (or short id).
        name: Optional display name.
        data: Optional server data, if already fetched.
        address: Address players use ("host" or "host:port"); overrides getAddress().
        bridge_url: HungerBridge URL, e.g. "http://10.0.0.5:1913". Defaults to the
            `bridge_url` config, then the server's address with `bridge_port`.
        bridge_token: "tokenId:secret" for this server; defaults to the `bridge_token` config.

    Example:
        enable('minecraft', config={'bridge_token': 'bot:9f2c...'})
        server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913')

        print(server.sendCommand('list'))         # output of the command
        print(f'{server.getPlayerCount()} online, TPS {server.getTPS()}')
        print(f'container RAM {server.getRAM()} MiB, JVM heap {server.getMemoryInfo()["used"]} MiB')
    '''
    def __init__(self, panel, server_id: str = None, name: str = None, data: dict = None, *,
                 address: str = None, bridge_url: str = None, bridge_token: str = None):
        super().__init__(panel, server_id, name, data)
        checkToken(bridge_token, 'bridge_token')
        self.address = address
        self.versions = VersionManager(self)
        self._bridge_url = bridge_url.rstrip('/') if bridge_url else None
        self._bridge_token = bridge_token
        self._bridge = None
        self._bridge_lock = threading.RLock()

    def getAddress(self) -> str:
        '''Returns the address players use: `address` if set (port 25565 by default), else the allocation.'''
        if self.address:
            return self.address if ':' in self.address else f'{self.address}:{DEFAULT_PORT}'
        return super().getAddress()


    # HungerBridge connection
    def getBridgeUrl(self) -> str:
        '''
        Returns the HungerBridge URL for this server: bridge_url, else the `bridge_url`
        config, else the server's host with the `bridge_port` config (1913).

        HungerBridge binds 127.0.0.1 by default; set its `bind-address` (or a proxy) so
        the URL is reachable from where your code runs.
        '''
        if self._bridge_url:
            return self._bridge_url
        config = settings()
        if config['bridge_url']:
            return config['bridge_url'].rstrip('/')
        address = self.getAddress()
        if not address:
            raise BridgeNotConfiguredError(f'{self.name} has no address to reach HungerBridge on; pass bridge_url')
        host = address.rsplit(':', 1)[0]
        return f'http://{host}:{config["bridge_port"]}'

    def hasBridge(self) -> bool:
        '''Returns True if a bridge client or token is configured (no request is made).'''
        return self._bridge is not None or bool(self._bridge_token or settings()['bridge_token'])

    @property
    def bridge(self) -> BridgeClient:
        '''
        The HungerBridgePy client of this server (`hungerbridge.BridgeClient`), created
        on first use. Everything HungerBridgePy offers is available here.

        Raises:
            BridgeNotConfiguredError: No bridge token is configured.

        Example:
            server.bridge.getTokenInfo()
            server.bridge.stopServer()     # HungerBridge's stop; server.stop() is the panel's
        '''
        with self._bridge_lock:
            if self._bridge is None:
                token = self._bridge_token or settings()['bridge_token']
                if not token:
                    raise BridgeNotConfiguredError(
                        f'{self.name} has no HungerBridge token. Use enable("minecraft", config={{"bridge_token": '
                        f'"id:secret"}}), server.connectBridge(url, "id:secret") or server.createBridgeToken().')
                self._bridge = _bridge.newClient(self.getBridgeUrl(), token)
            return self._bridge

    def connectBridge(self, url: str = None, token: str = None, **options) -> BridgeClient:
        '''
        Sets the bridge URL and/or token for this server and returns the new client.

        Args:
            url: HungerBridge URL; keeps the current one when None.
            token: "tokenId:secret"; keeps the current one when None.
            **options: BridgeClient options, e.g. timeout=(5, 30), static_delay=0.2.

        Example:
            server.connectBridge('http://10.0.0.5:1913', 'bot:9f2c...')
        '''
        checkToken(token, 'token')
        with self._bridge_lock:
            if url:
                self._bridge_url = url.rstrip('/')
            if token:
                self._bridge_token = token
            self.closeBridge()
            if options:
                token = self._bridge_token or settings()['bridge_token']
                if not token:
                    raise BridgeNotConfiguredError(f'{self.name} has no HungerBridge token; pass token=')
                self._bridge = _bridge.newClient(self.getBridgeUrl(), token, **options)
            return self.bridge

    def setBridge(self, client: BridgeClient) -> 'MinecraftServer':
        '''Uses an existing HungerBridgePy client for this server.'''
        with self._bridge_lock:
            if client is not self._bridge:
                self.closeBridge()
            self._bridge = client
        return self

    def closeBridge(self) -> None:
        '''Closes the bridge client's connections. The next bridge call opens a new client.'''
        with self._bridge_lock:
            client, self._bridge = self._bridge, None
        if client is not None:
            _bridge.closeClient(client)

    def isBridgeReachable(self) -> bool:
        '''Returns True if HungerBridge answers an authenticated ping.'''
        try:
            return self.bridge.isOk()
        except (HungerBridgeError, BridgeNotConfiguredError):
            return False

    def waitForBridge(self, timeout: float = 120, interval: float = 2) -> bool:
        '''
        Blocks until HungerBridge answers (after a start, restart or installBridge()).
        Returns False on timeout.

        Example:
            server.restart()
            server.waitForBridge(timeout=180)
        '''
        deadline = time.monotonic() + timeout
        while True:
            if self.isBridgeReachable():
                return True
            if time.monotonic() + interval > deadline:
                return False
            time.sleep(interval)

    def redeemBridgePickup(self, pickup_url: str) -> BridgeClient:
        '''
        Redeems a one-time token pickup and connects the bridge with the new token.

        Args:
            pickup_url: The full URL, or the "/pickup/<id>?passkey=<hex>" part printed by
                `hb token create` (resolved against getBridgeUrl()).
        '''
        url = pickup_url if pickup_url.startswith(('http://', 'https://')) else f'{self.getBridgeUrl()}{pickup_url}'
        token_id, secret = redeem_pickup(url)
        return self.connectBridge(token=f'{token_id}:{secret}')

    def createBridgeToken(self, token_id: str = 'calagoapi', policy: str = 'admin', expiry: int = None,
                          timeout: float = 30, url: str = None) -> str:
        '''
        Creates a HungerBridge token through the server console and connects the bridge with it.

        Runs `hb token create <token_id> <policy> [expiry]` over the daemon console (the
        command is console-only), reads the pickup URL it prints, redeems it, and returns
        the token so you can store it (e.g. as the `bridge_token` config).

        Args:
            token_id: Id of the new token.
            policy: Policy from HungerBridge's policies.yaml ('admin' needs to exist there).
            expiry: Lifetime in seconds; None uses the policy default.
            timeout: Seconds to wait for the pickup URL.
            url: Bridge URL to use for this server (see getBridgeUrl()).

        Returns:
            The token, "tokenId:secret".

        Raises:
            MinecraftError: No pickup URL appeared (bridge not installed, unknown policy, ...).

        Example:
            token = server.createBridgeToken(url='http://10.0.0.5:1913')
            save_somewhere(token)
        '''
        if url:
            self._bridge_url = url.rstrip('/')
        command = f'hb token create {token_id} {policy}' + (f' {int(expiry)}' if expiry else '')
        deadline = time.monotonic() + timeout
        pickup = None
        with Console(self) as console:
            console.sendCommand(command)
            while pickup is None:
                remaining = deadline - time.monotonic()
                try:
                    line = console.waitFor('/pickup/', timeout=max(remaining, 0.01)) if remaining > 0 else None
                except WaitTimeoutError:
                    line = None
                if line is None:
                    raise MinecraftError(
                        f'No HungerBridge pickup URL appeared on the console of {self.name} within {timeout}s after '
                        f'"{command}". Is HungerBridge installed and does policy {policy!r} exist?')
                pickup = _bridge.findPickup(line)
        client = self.redeemBridgePickup(pickup)
        return f'{client.credentials.token_id}:{client.credentials.secret}'

    def getBridgeInfo(self) -> dict:
        '''Returns platform, minecraft_version, bridge_version, port and protocol_version.'''
        return self.bridge.getServerMeta()

    def getBridgeTokenInfo(self) -> dict:
        '''Returns the token's token_id, policy_id, permissions and expiry.'''
        return self.bridge.getTokenInfo()

    def getPlatform(self) -> str:
        '''Returns 'paper', 'folia' or 'fabric' (as reported by HungerBridge).'''
        return self.bridge.getPlatform()

    def getMinecraftVersion(self) -> str:
        '''Returns the running Minecraft version, e.g. '1.21.11' (as reported by HungerBridge).'''
        return self.bridge.getMinecraftVersion()


    # commands and console (HungerBridge)
    def sendCommand(self, command: str, *, silent: bool = False, showConsole: bool = False):
        '''
        Runs a console command through HungerBridge and returns its output.

        The command runs as the console on the server thread (Folia: the global region);
        HungerBridge waits up to 5 seconds for it. Uses HungerBridgePy's runCommand().

        Args:
            command: The command, without a leading slash.
            silent: Do not capture output (returns None).
            showConsole: Also print the command and its output to the server console.

        Returns:
            The captured output lines joined with newlines, or None when silent.

        Example:
            print(server.sendCommand('list'))
            server.sendCommand('save-all', silent=True)
        '''
        return self.bridge.runCommand(command, showConsole=showConsole, silent=silent)

    def sendCommands(self, commands: list, *, silent: bool = False, showConsole: bool = False) -> list:
        '''Runs several commands in order. Returns their outputs.'''
        return [self.sendCommand(command, silent=silent, showConsole=showConsole) for command in commands]

    def sendPanelCommand(self, command: str) -> None:
        '''
        Sends a command through the panel instead of HungerBridge (Server.sendCommand).

        Works without HungerBridge, returns no output. Use it when the bridge is not
        installed or not running.
        '''
        return Server.sendCommand(self, command)

    def streamConsole(self, history: int = 0, timeout: float = None, *, reconnect: bool = None, sanitize: bool = True):
        '''
        Yields console log lines live, from HungerBridge's log stream (HungerBridgePy streamLogs()).

        Args:
            history: Replay this many recent lines first (at most 200; True means 200).
            timeout: Stop when nothing is logged for this many seconds. None streams forever.
            reconnect: Reconnect (and replay only missed lines) when the stream drops.
                None uses the `stream_reconnect` config (default True).
            sanitize: Strip colours and unescape line breaks.

        Lines look like "[12:00:05 INFO]: Steve joined the game". Permanent errors (bad
        token, missing permission) are raised as HungerBridgeError subclasses.

        Example:
            for line in server.streamConsole(history=20):
                if 'joined the game' in line:
                    server.say('Welcome!')
        '''
        if reconnect is None:
            reconnect = settings()['stream_reconnect']
        return self.bridge.streamLogs(_history(history), timeout=timeout, reconnect=reconnect, sanitize=sanitize)

    def onConsoleLine(self, callback, history: int = 0, *, reconnect: bool = None, sanitize: bool = True) -> Stream:
        '''
        Calls `callback(line)` for every console log line, in a background thread.

        Returns the HungerBridgePy Stream; call `.disconnect()` on it to stop.

        Example:
            stream = server.onConsoleLine(print, history=10)
            ...
            stream.disconnect()
        '''
        if reconnect is None:
            reconnect = settings()['stream_reconnect']

        def deliver(line):
            callback(Stream.sanitize(line) if sanitize else line)

        def deliverHistory(lines):
            for line in lines:
                deliver(line)

        stream = self.bridge.openStream(history_handler=deliverHistory, new_log_handler=deliver)
        stream.connect(history=_history(history), reconnect=reconnect)
        return stream

    def writeLog(self, message: str, level: str = 'info', thread: str = None) -> dict:
        '''
        Writes a line to the server log (any level name, e.g. 'INFO', 'WARN' or a custom 'BOT').

        Example:
            server.writeLog('backup finished', level='BOT', thread='calagoapi')
        '''
        return self.bridge.log(message, level=level, thread=thread)


    # chat and players (commands through HungerBridge)
    def say(self, message: str):
        '''Broadcasts a chat message as the server.'''
        return self.sendCommand(f'say {message}')

    def broadcast(self, message: str, prefix: str = None):
        '''
        Shows a message to every player with tellraw (HungerBridgePy broadcast()).

        Example:
            server.broadcast('Event starts now', prefix='[Event] ')
        '''
        return self.bridge.broadcast(message, prefix)

    def tellraw(self, target: str, component):
        '''
        Sends a JSON text component.

        Example:
            server.tellraw('@a', {'text': 'Hello', 'color': 'gold'})
        '''
        if not isinstance(component, str):
            component = json.dumps(component, ensure_ascii=False)
        return self.sendCommand(f'tellraw {target} {component}')

    def kick(self, player: str, reason: str = None):
        '''Kicks a player.'''
        return self.sendCommand(f'kick {player} {reason}' if reason else f'kick {player}')

    def ban(self, player: str, reason: str = None):
        '''Bans a player.'''
        return self.sendCommand(f'ban {player} {reason}' if reason else f'ban {player}')

    def pardon(self, player: str):
        '''Unbans a player.'''
        return self.sendCommand(f'pardon {player}')

    def op(self, player: str):
        '''Gives a player operator status.'''
        return self.sendCommand(f'op {player}')

    def deop(self, player: str):
        '''Removes operator status from a player.'''
        return self.sendCommand(f'deop {player}')

    def whitelistAdd(self, player: str):
        '''Adds a player to the whitelist.'''
        return self.sendCommand(f'whitelist add {player}')

    def whitelistRemove(self, player: str):
        '''Removes a player from the whitelist.'''
        return self.sendCommand(f'whitelist remove {player}')

    def saveAll(self):
        '''Saves every world.'''
        return self.sendCommand('save-all')

    def getPlayers(self) -> list:
        '''Returns the names of the online players (capped by HungerBridge's players.max-list).'''
        return self.bridge.getPlayers('list') or []

    def getPlayerCount(self) -> int:
        '''Returns how many players are online.'''
        return self.bridge.getPlayers('count')

    def getMaxPlayers(self) -> int:
        '''Returns the number of player slots.'''
        return self.bridge.getMaxPlayers()


    # game performance and world (HungerBridge)
    def getTPS(self, mode: str = 'current') -> float:
        '''
        Returns ticks per second: mode 'current', '1m', '5m' or '15m' (-1 if unavailable).

        Example:
            if server.getTPS('1m') < 18:
                print('lagging')
        '''
        return self.bridge.getTPS(mode)

    def getMSPT(self) -> float:
        '''Returns milliseconds per tick.'''
        return self.bridge.getMSPT()

    def getPerformance(self) -> dict:
        '''
        Returns one snapshot for dashboards (three bridge calls):
        {'tps': {'current', '1m', '5m', '15m'}, 'mspt', 'players', 'max_players'}.
        '''
        players = self.bridge.getPlayerStats()
        return {
            'tps': self.bridge.getTPSStats(),
            'mspt': self.bridge.getMSPT(),
            'players': players['count'],
            'max_players': players['max'],
        }

    def getWorldTime(self) -> int:
        '''Returns the overworld time of day in ticks (0-23999).'''
        return self.bridge.getWorldTime()

    def getWorldTimeInfo(self) -> dict:
        '''Returns time (tick of day), full_time, day and server_time.'''
        return self.bridge.getWorldTimeInfo()

    def getWeather(self) -> str:
        '''Returns 'clear', 'rain' or 'thunder'.'''
        return self.bridge.getWorldWeather()

    def getLoadedChunks(self) -> dict:
        '''Returns loaded chunks: total, world, world_nether, world_the_end.'''
        return self.bridge.getLoadedChunks()

    def getLoadedEntities(self) -> dict:
        '''Returns loaded entities: total, world, world_nether, world_the_end.'''
        return self.bridge.getLoadedEntities()


    # JVM information (HungerBridge) - additional to getRAM()/getCPU()/getUptime() (panel)
    def getMemoryInfo(self, unit: str = 'mib') -> dict:
        '''
        Returns JVM memory: heap_*, nonheap_*, jvm_*, process_* and the summary keys used,
        total (committed heap), free and max, in `unit` ('b', 'kib', 'mib', 'gib', 'mb', ...).

        getRAM() stays the container's memory as the panel reports it.
        '''
        return self.bridge.getMemoryStats(unit)

    def getProcessInfo(self, unit: str = 'mib') -> dict:
        '''Returns the server process: process_used, process_virtual (in `unit`) and uptime_ms.'''
        info = self.bridge.getProcessMemory(unit)
        info['uptime_ms'] = self.bridge.getUptime()
        return info

    def getProcessorInfo(self) -> dict:
        '''
        Returns load (the JVM process's CPU load, 0-1) and processors (available cores).

        getCPU() stays the container's CPU usage as the panel reports it.
        '''
        return self.bridge.getCPUStats()

    def getThreadInfo(self) -> dict:
        '''Returns JVM thread counts: current, peak, daemon.'''
        return self.bridge.getThreadStats()

    def getGarbageCollectorInfo(self) -> dict:
        '''Returns gc_type, gc_count, gc_time_ms, last_gc_pause_ms and avg_gc_pause_ms.'''
        return self.bridge.getGCStats()

    def getNetworkInfo(self) -> dict:
        '''Returns bytes_in_per_sec, bytes_out_per_sec, total_bytes_in and total_bytes_out (host, Linux only).'''
        return self.bridge.getNetworkStats()

    def getJVMUptime(self, formatted: bool = False):
        '''Returns how long the JVM runs, in milliseconds, or like "3h 12m" with formatted=True.'''
        uptime = self.bridge.getUptime()
        return formatDuration(uptime) if formatted and uptime is not None else uptime


    # installing HungerBridge (panel files + HungerBridgePy release lookup)
    def findBridgeRelease(self, minecraft_version: str, loader: str, release: str = None) -> ReleaseAsset:
        '''
        Finds the HungerBridge jar for a Minecraft version and loader (HungerBridgePy find_release()).

        Args:
            minecraft_version: e.g. '1.21.11', or 'latest'.
            loader: 'paper' or 'fabric' (server types such as 'PURPUR' work too).
            release: Release tag; None uses the `release` config ('latest').
        '''
        config = settings()
        return find_release(minecraft_version, loader, release or config['release'],
                            repository=config['repository'], api_url=config['github_api'])

    def installBridge(self, minecraft_version: str = None, loader: str = None, release: str = None,
                      replace: bool = True) -> ReleaseAsset:
        '''
        Downloads the matching HungerBridge jar into /plugins (Paper, Purpur, Folia) or
        /mods (Fabric). Restart the server afterwards.

        The loader and Minecraft version are detected unless given: from the Version
        Changer, a running bridge, or the egg name and startup variables.

        Args:
            minecraft_version: e.g. '1.21.11', or 'latest'.
            loader: 'paper' or 'fabric'.
            release: HungerBridge release tag; None uses the `release` config.
            replace: Delete other HungerBridge jars in that directory first.

        Returns:
            The installed hungerbridge.ReleaseAsset (name, url, loader, minecraft_version, release).

        Example:
            server.installBridge()
            server.restart()
            server.waitForBridge()
        '''
        loader, minecraft_version = _bridge.detectPlatform(self, loader, minecraft_version)
        if loader is None or minecraft_version is None:
            raise MinecraftError(
                f'Cannot tell which HungerBridge jar {self.name} needs (loader={loader!r}, '
                f'minecraft_version={minecraft_version!r}). Pass them, e.g. installBridge("1.21.11", "paper").')
        asset = self.findBridgeRelease(minecraft_version, loader, release)
        if replace:
            try:
                old = [f.getName() for f in self.files.listFiles(asset.directory)
                       if f.getName() != asset.name and parse_asset_name(f.getName())]
            except NotFoundError:
                old = []
            if old:
                self.files.deleteFiles(asset.directory, old)
        self.files.pullFile(asset.url, asset.directory, name=asset.name)
        return asset


    # server.properties and EULA (panel files)
    def getProperties(self) -> dict:
        '''
        Reads server.properties.

        Returns:
            dict of property name -> string value.

        Example:
            print(server.getProperties()['max-players'])
        '''
        return _properties.parse(self.files.readFile('/server.properties'))

    def getProperty(self, key: str, default=None) -> str:
        '''Returns one server.properties value.'''
        return self.getProperties().get(key, default)

    def setProperty(self, key: str, value) -> None:
        '''Changes one server.properties value. Takes effect after a restart.'''
        return self.setProperties({key: value})

    def setProperties(self, values: dict) -> None:
        '''
        Changes several server.properties values, keeping comments and order.

        Example:
            server.setProperties({'motd': 'Welcome!', 'max-players': 100, 'pvp': False})
        '''
        text = self.files.readFile('/server.properties')
        return self.files.writeFile('/server.properties', _properties.update(text, values))

    def getMOTD(self) -> str:
        '''Returns the message of the day from server.properties.'''
        return self.getProperty('motd')

    def setMOTD(self, motd: str) -> None:
        '''Sets the message of the day.'''
        return self.setProperty('motd', motd)

    def acceptEula(self) -> None:
        '''Writes eula=true to eula.txt.'''
        return self.files.writeFile('/eula.txt', 'eula=true\n')

    def isEulaAccepted(self) -> bool:
        '''Returns True if eula.txt contains eula=true.'''
        try:
            return 'eula=true' in self.files.readFile('/eula.txt').replace(' ', '').lower()
        except NotFoundError:
            return False
