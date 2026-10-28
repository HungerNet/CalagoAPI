import json

from calagoapi.servers.generic import GenericServer
from calagoapi.utils.model import idOf
from calagoapi.utils.exceptions import NotFoundError


class MinecraftServer(GenericServer):
    '''
    A Minecraft server.

    Adds Minecraft helpers on top of GenericServer: console shortcuts,
    server.properties editing, EULA handling and the Calagopus Minecraft
    Version Changer (install any Paper, Purpur, Fabric, Forge, ... build).

    Args:
        panel: The Panel the server lives on.
        server_id: Server UUID (or short id).
        name: Optional display name.
        server_domain: Optional address players use, overrides getAddress().
        server_port: Optional port players use.
        data: Optional server data, if already fetched.

    Example:
        server = panel.servers.getMinecraftServer('abc123')
        server.say('Restarting in 5 minutes!')
        server.setProperty('max-players', 50)

        build = server.getBuilds('PAPER', '1.21.1')[0]
        server.installVersion(build)
    '''
    def __init__(self, panel, server_id: str = None, name: str = None, server_domain: str = None,
                 server_port: int = None, data: dict = None):
        super().__init__(panel, server_id, name, data)

        # Minecraft-specific fields
        self.server_domain = server_domain
        self.server_port = server_port

    def getAddress(self) -> str:
        '''Returns server_domain:server_port if set, otherwise the primary allocation address.'''
        if self.server_domain:
            return f'{self.server_domain}:{self.server_port or 25565}'
        return super().getAddress()


    # console helpers
    def say(self, message: str) -> None:
        '''Broadcasts a chat message as the server.'''
        return self.sendCommand(f'say {message}')

    def broadcast(self, message: str) -> None:
        '''Alias of say().'''
        return self.say(message)

    def tellraw(self, target: str, component) -> None:
        '''
        Sends a JSON text component.

        Example:
            server.tellraw('@a', {'text': 'Hello', 'color': 'gold'})
        '''
        if not isinstance(component, str):
            component = json.dumps(component)
        return self.sendCommand(f'tellraw {target} {component}')

    def kick(self, player: str, reason: str = None) -> None:
        '''Kicks a player.'''
        return self.sendCommand(f'kick {player} {reason}' if reason else f'kick {player}')

    def ban(self, player: str, reason: str = None) -> None:
        '''Bans a player.'''
        return self.sendCommand(f'ban {player} {reason}' if reason else f'ban {player}')

    def pardon(self, player: str) -> None:
        '''Unbans a player.'''
        return self.sendCommand(f'pardon {player}')

    def op(self, player: str) -> None:
        '''Gives a player operator status.'''
        return self.sendCommand(f'op {player}')

    def deop(self, player: str) -> None:
        '''Removes operator status from a player.'''
        return self.sendCommand(f'deop {player}')

    def whitelistAdd(self, player: str) -> None:
        '''Adds a player to the whitelist.'''
        return self.sendCommand(f'whitelist add {player}')

    def whitelistRemove(self, player: str) -> None:
        '''Removes a player from the whitelist.'''
        return self.sendCommand(f'whitelist remove {player}')

    def saveAll(self) -> None:
        '''Saves every world.'''
        return self.sendCommand('save-all')


    # server.properties
    def getProperties(self) -> dict:
        '''
        Reads server.properties.

        Returns:
            dict of property name -> string value.

        Example:
            server.getProperties()['max-players']
        '''
        properties = {}
        for line in self.files.readFile('/server.properties').splitlines():
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            properties[key.strip()] = value.strip()
        return properties

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
            server.setProperties({'motd': 'Welcome!', 'max-players': 100})
        '''
        values = {k: _propertyValue(v) for k, v in values.items()}
        lines = []
        for line in self.files.readFile('/server.properties').splitlines():
            key = line.split('=', 1)[0].strip()
            if '=' in line and not line.lstrip().startswith('#') and key in values:
                line = f'{key}={values.pop(key)}'
            lines.append(line)
        lines.extend(f'{k}={v}' for k, v in values.items())
        return self.files.writeFile('/server.properties', '\n'.join(lines) + '\n')

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


    # version changer
    def getInstalledVersion(self) -> dict:
        '''Returns the installed build (type, version, build), or None if unknown.'''
        return self.panel.api.versions.installed(self.server_id)

    def getVersionTypes(self) -> dict:
        '''Returns the available server types (PAPER, PURPUR, FABRIC, VANILLA, ...).'''
        return self.panel.api.versions.types(self.server_id)

    def getVersions(self, type: str, search: str = None, page: int = None, per_page: int = None):
        '''
        Returns the Minecraft versions available for a server type.

        Example:
            server.getVersions('PAPER', page=1, per_page=10)
        '''
        return self.panel.api.versions.versions(self.server_id, type, search, page, per_page)

    def getBuilds(self, type: str, version: str, search: str = None, page: int = None, per_page: int = None):
        '''Returns the builds of a version, newest first.'''
        return self.panel.api.versions.builds(self.server_id, type, version, search, page, per_page)

    def installVersion(self, build, truncate_directory: bool = False, accept_eula: bool = True) -> None:
        '''
        Installs a server build.

        Args:
            build: Build dict from getBuilds() or build UUID.
            truncate_directory: Delete every file first.
            accept_eula: Accept the Minecraft EULA.

        Example:
            latest = server.getBuilds('PAPER', '1.21.1', page=1, per_page=1)[0]
            server.installVersion(latest)
        '''
        build_id = build.get('uuid') if isinstance(build, dict) else idOf(build)
        return self.panel.api.versions.install(self.server_id, build_id, truncate_directory, accept_eula)


def _propertyValue(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return str(value)
