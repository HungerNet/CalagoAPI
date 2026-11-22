import json
import threading
import time

from hungerbridge import BridgeClient, BridgeRelease, Credentials, HungerBridgeError, Stream, findRelease, redeemPickup

from calagoapi import Server
from calagoapi.console import Console
from calagoapi.utils.exceptions import NotFoundError, WaitTimeoutError

from calagoapi_minecraft import bridge as _bridge
from calagoapi_minecraft import properties as _properties
from calagoapi_minecraft.config import credentials as _credentials, settings
from calagoapi_minecraft.exceptions import BridgeNotConfiguredError, MinecraftError


# default Minecraft port, used when an address has none
DEFAULT_PORT = 25565


class MinecraftServer(Server):
    '''
    A Minecraft server: everything a Server has, plus Minecraft features.

    Two channels are used, and every method uses exactly one of them:

    - the panel / node daemon (inherited from Server): power, resources, files, backups,
      server.properties, installBridge(), sendPanelCommand() and `server.console`;
    - HungerBridge, the plugin/mod inside the game, through HungerBridgePy: `server.bridge`
      is a `hungerbridge.BridgeClient` with the whole HungerBridge API (players, TPS, JVM
      metrics, log(), ...). MinecraftServer adds sendCommand() and streamConsole() on top,
      the bridge versions of Server's panel methods.

    Bridge methods need a token: `enable('minecraft', config={'bridge_token_id': ...,
    'bridge_token_secret': ...})`, the arguments here, connectBridge() or createBridgeToken().
    Without one they raise BridgeNotConfiguredError. Errors from the bridge are
    HungerBridgePy's `hungerbridge.HungerBridgeError` subclasses.

    Args:
        panel: The Panel the server lives on.
        server_id: Server UUID (or short id).
        name: Optional display name.
        data: Optional server data, if already fetched.
        address: Address players use ("host" or "host:port"); overrides getAddress().
        bridge_url: HungerBridge URL, e.g. "http://10.0.0.5:1913". Defaults to the
            `bridge_url` config, then the server's address with `bridge_port`.
        bridge_token_id, bridge_token_secret: HungerBridge token for this server; default to
            the config.

    Example:
        server = panel.minecraft.getServer('abc123', bridge_url='http://10.0.0.5:1913',
                                           bridge_token_id='bot', bridge_token_secret='9f2c...')
        print(server.sendCommand('list'))                # output of the command
        print(server.bridge.getTPS('1m'), server.bridge.getPlayers())
    '''
    def __init__(self, panel, server_id: str = None, name: str = None, data: dict = None, *,
                 address: str = None, bridge_url: str = None, bridge_token_id: str = None,
                 bridge_token_secret: str = None):
        super().__init__(panel, server_id, name, data)
        self.address = address
        self._bridge_url = bridge_url.rstrip('/') if bridge_url else None
        self._credentials = _credentials(bridge_token_id, bridge_token_secret, 'bridge_token_id/bridge_token_secret')
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

    def _configuredCredentials(self):
        if self._credentials is not None:
            return self._credentials
        config = settings()
        return _credentials(config['bridge_token_id'], config['bridge_token_secret'])

    def hasBridge(self) -> bool:
        '''Returns True if a bridge client or token is configured (no request is made).'''
        return self._bridge is not None or self._configuredCredentials() is not None

    @property
    def bridge(self) -> BridgeClient:
        '''
        The HungerBridgePy client of this server (`hungerbridge.BridgeClient`), created on
        first use. Everything HungerBridge offers is available here.

        Raises:
            BridgeNotConfiguredError: No bridge token is configured.

        Example:
            server.bridge.getTPS('1m')
            server.bridge.log('backup finished', level='BACKUP', logger='Backups')
        '''
        with self._bridge_lock:
            if self._bridge is None:
                credentials = self._configuredCredentials()
                if credentials is None:
                    raise BridgeNotConfiguredError(
                        f'{self.name} has no HungerBridge token. Use enable("minecraft", config={{"bridge_token_id": ..., '
                        f'"bridge_token_secret": ...}}), server.connectBridge(token_id=..., token_secret=...) '
                        f'or server.createBridgeToken().')
                self._bridge = _bridge.newClient(self.getBridgeUrl(), credentials)
            return self._bridge

    def connectBridge(self, url: str = None, *, token_id: str = None, token_secret: str = None, **options) -> BridgeClient:
        '''
        Sets the bridge URL and/or token for this server and returns the new client.

        Args:
            url: HungerBridge URL; keeps the current one when None.
            token_id, token_secret: A new token (both, or neither to keep the current one).
            **options: BridgeClient options, e.g. timeout=(5, 30), min_interval=0.2.

        Example:
            server.connectBridge('http://10.0.0.5:1913', token_id='bot', token_secret='9f2c...')
        '''
        new = _credentials(token_id, token_secret, 'token_id/token_secret')
        with self._bridge_lock:
            if url:
                self._bridge_url = url.rstrip('/')
            if new is not None:
                self._credentials = new
            self.closeBridge()
            if options:
                credentials = self._configuredCredentials()
                if credentials is None:
                    raise BridgeNotConfiguredError(f'{self.name} has no HungerBridge token; pass token_id and token_secret')
                self._bridge = _bridge.newClient(self.getBridgeUrl(), credentials, **options)
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
            client.close()

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
        token = redeemPickup(url)
        return self.connectBridge(token_id=token.token_id, token_secret=token.token_secret)

    def createBridgeToken(self, token_id: str = 'calagoapi', policy: str = 'admin', expiry: int = None,
                          timeout: float = 30, url: str = None) -> Credentials:
        '''
        Creates a HungerBridge token through the server console and connects the bridge with it.

        Runs `hb token create <token_id> <policy> [expiry]` over the daemon console (the
        command is console-only), reads the pickup URL it prints, redeems it, and returns
        the token so you can store it (e.g. as the `bridge_token_id`/`bridge_token_secret`
        config).

        Args:
            token_id: Id of the new token.
            policy: Policy from HungerBridge's policies.yaml ('admin' needs to exist there).
            expiry: Lifetime in seconds; None uses the policy default.
            timeout: Seconds to wait for the pickup URL.
            url: Bridge URL to use for this server (see getBridgeUrl()).

        Returns:
            hungerbridge.Credentials (token_id, token_secret).

        Raises:
            MinecraftError: No pickup URL appeared (bridge not installed, unknown policy, ...).

        Example:
            token = server.createBridgeToken(url='http://10.0.0.5:1913')
            save_somewhere(token.token_id, token.token_secret)
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
        return self.redeemBridgePickup(pickup).credentials


    # commands and console (HungerBridge)
    def sendCommand(self, command: str, *, show_console: bool = False) -> str:
        '''
        Runs a console command through HungerBridge and returns its output
        (HungerBridgePy runCommand()).

        The command runs with console permissions on the server thread (Folia: the global
        region). Its output is captured directly and is not printed to the server console
        unless show_console is True.

        Example:
            print(server.sendCommand('list'))
            server.sendCommand('save-all', show_console=True)
        '''
        return self.bridge.runCommand(command, show_console=show_console)

    def sendCommands(self, commands: list, *, show_console: bool = False) -> list:
        '''Runs several commands in order. Returns their outputs.'''
        return [self.sendCommand(command, show_console=show_console) for command in commands]

    def sendPanelCommand(self, command: str) -> None:
        '''
        Sends a command through the panel instead of HungerBridge (Server.sendCommand).

        Works without HungerBridge, returns no output. Use it when the bridge is not
        installed or not running.
        '''
        return Server.sendCommand(self, command)

    def streamConsole(self, history: int = 0, timeout: float = None, *, reconnect: bool = None):
        '''
        Yields console lines live from HungerBridge's log stream, e.g.
        "[12:00:05] [Server thread/INFO]: Steve joined the game".

        Lines are plain text in HungerBridge's format on every loader. For the structured
        events (level, thread, logger, message) use server.bridge.streamLogs().

        Args:
            history: Replay this many recent lines first (True: everything the bridge keeps).
            timeout: Stop when nothing is logged for this many seconds. None streams forever.
            reconnect: Reconnect (replaying exactly what was missed) when the stream drops.
                None uses the `stream_reconnect` config (default True).

        Example:
            for line in server.streamConsole(history=20):
                if 'joined the game' in line:
                    server.say('Welcome!')
        '''
        if reconnect is None:
            reconnect = settings()['stream_reconnect']
        events = self.bridge.streamLogs(history or None, timeout=timeout, reconnect=reconnect)
        return (event.line for event in events)

    def onConsoleLine(self, callback, history: int = 0, *, reconnect: bool = None) -> Stream:
        '''
        Calls `callback(line)` for every console line, in a background thread.

        Returns the HungerBridgePy Stream; call `.disconnect()` on it to stop.

        Example:
            stream = server.onConsoleLine(print, history=10)
            ...
            stream.disconnect()
        '''
        if reconnect is None:
            reconnect = settings()['stream_reconnect']
        stream = self.bridge.openStream(on_event=lambda event: callback(event.line),
                                        on_history=lambda events: [callback(event.line) for event in events])
        return stream.connect(history or None, reconnect=reconnect)


    # chat and moderation (commands through HungerBridge)
    def say(self, message: str) -> str:
        '''Broadcasts a chat message as the server.'''
        return self.sendCommand(f'say {message}')

    def tellraw(self, target: str, component) -> str:
        '''
        Sends a JSON text component.

        Example:
            server.tellraw('@a', {'text': 'Hello', 'color': 'gold'})
        '''
        if not isinstance(component, str):
            component = json.dumps(component, ensure_ascii=False)
        return self.sendCommand(f'tellraw {target} {component}')

    def kick(self, player: str, reason: str = None) -> str:
        '''Kicks a player.'''
        return self.sendCommand(f'kick {player} {reason}' if reason else f'kick {player}')

    def ban(self, player: str, reason: str = None) -> str:
        '''Bans a player.'''
        return self.sendCommand(f'ban {player} {reason}' if reason else f'ban {player}')

    def pardon(self, player: str) -> str:
        '''Unbans a player.'''
        return self.sendCommand(f'pardon {player}')

    def op(self, player: str) -> str:
        '''Gives a player operator status.'''
        return self.sendCommand(f'op {player}')

    def deop(self, player: str) -> str:
        '''Removes operator status from a player.'''
        return self.sendCommand(f'deop {player}')

    def whitelistAdd(self, player: str) -> str:
        '''Adds a player to the whitelist.'''
        return self.sendCommand(f'whitelist add {player}')

    def whitelistRemove(self, player: str) -> str:
        '''Removes a player from the whitelist.'''
        return self.sendCommand(f'whitelist remove {player}')

    def saveAll(self) -> str:
        '''Saves every world.'''
        return self.sendCommand('save-all')


    # installing HungerBridge (Modrinth through HungerBridgePy + panel files)
    def installBridge(self, minecraft_version: str, loader: str, *, version: str = None,
                      replace: bool = True) -> BridgeRelease:
        '''
        Downloads the HungerBridge jar for a Minecraft version and loader from Modrinth into
        /plugins (paper, purpur, folia) or /mods (fabric). Restart the server afterwards.

        Nothing is detected: pass what the server runs. The release is chosen from Modrinth's
        version metadata (loaders, game versions) by HungerBridgePy's findRelease().

        Args:
            minecraft_version: e.g. '1.21.11' or '26.3'.
            loader: 'paper', 'purpur', 'folia' or 'fabric'.
            version: A HungerBridge version number to pin (e.g. '5-alpha.1'); None: the newest
                compatible release.
            replace: Delete other HungerBridge*.jar files in that directory first.

        Returns:
            The installed hungerbridge.BridgeRelease (version_number, filename, url, sha512, ...).

        Raises:
            ValueError: A missing argument, or a loader/version HungerBridge is not published for.
            hungerbridge.HungerBridgeNotFound: No compatible release exists.

        Example:
            server.installBridge(minecraft_version='1.21.11', loader='paper')
            server.restart()
            server.waitForBridge()
        '''
        release = findRelease(minecraft_version=minecraft_version, loader=loader, version=version)
        if replace:
            try:
                old = [f.getName() for f in self.files.listFiles(release.directory)
                       if f.getName() != release.filename and f.getName().lower().startswith('hungerbridge')
                       and f.getName().lower().endswith('.jar')]
            except NotFoundError:
                old = []
            if old:
                self.files.deleteFiles(release.directory, old)
        self.files.pullFile(release.url, release.directory, name=release.filename)
        return release


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
