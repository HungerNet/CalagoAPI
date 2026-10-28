from calagoapi.utils.model import Model


class ApiKey(Model):
    '''
    An API key of the current account.

    The secret key is only known right after creation (`getKey()`).

    Example:
        api_key = panel.account.createApiKey('backup-bot', server_permissions=['backup.*'])
        print(api_key.getKey())  # store it now, it is never shown again
    '''
    def __init__(self, panel, data: dict, key: str = None):
        super().__init__(panel, data)
        self.key = key

    def getName(self) -> str:
        '''Returns the key name.'''
        return self.data.get('name')

    def getKey(self) -> str:
        '''Returns the full secret key. Only available right after creation or recreate().'''
        return self.key

    def getKeyStart(self) -> str:
        '''Returns the first characters of the key, for identification.'''
        return self.data.get('key_start')

    def getAllowedIPs(self) -> list:
        '''Returns the IPs allowed to use the key. Empty means all.'''
        return self.data.get('allowed_ips', [])

    def getUserPermissions(self) -> list:
        '''Returns the account permissions of the key.'''
        return self.data.get('user_permissions', [])

    def getAdminPermissions(self) -> list:
        '''Returns the admin permissions of the key.'''
        return self.data.get('admin_permissions', [])

    def getServerPermissions(self) -> list:
        '''Returns the server permissions of the key.'''
        return self.data.get('server_permissions', [])

    def getLastUsed(self) -> str:
        '''Returns when the key was last used.'''
        return self.data.get('last_used')

    def getExpires(self) -> str:
        '''Returns when the key expires, or None.'''
        return self.data.get('expires')

    def isEnabled(self) -> bool:
        '''Returns True if the key is enabled.'''
        return bool(self.data.get('enabled'))

    def update(self, **fields) -> 'ApiKey':
        '''
        Changes the key. Fields: name, enabled, allowed_ips, user_permissions,
        admin_permissions, server_permissions, expires.
        '''
        allowed_ips = fields.pop('allowed_ips', self.getAllowedIPs())
        self.panel.api.account.updateApiKey(self.getUUID(), allowed_ips, **fields)
        return self._update({'allowed_ips': allowed_ips, **fields})

    def rename(self, name: str) -> 'ApiKey':
        '''Renames the key.'''
        return self.update(name=name)

    def enable(self) -> 'ApiKey':
        '''Enables the key.'''
        return self.update(enabled=True)

    def disable(self) -> 'ApiKey':
        '''Disables the key.'''
        return self.update(enabled=False)

    def recreate(self) -> str:
        '''Generates a new secret for the key and returns it.'''
        self.key = self.panel.api.account.recreateApiKey(self.getUUID())
        return self.key

    def duplicate(self, name: str) -> 'ApiKey':
        '''Creates a copy with the same permissions. The copy holds its new secret.'''
        result = self.panel.api.account.duplicateApiKey(self.getUUID(), name)
        return ApiKey(self.panel, result['api_key'], result.get('key'))

    def delete(self) -> None:
        '''Deletes the key.'''
        return self.panel.api.account.deleteApiKey(self.getUUID())


class SshKey(Model):
    '''An SSH public key used for SFTP login.'''
    def getName(self) -> str:
        '''Returns the key name.'''
        return self.data.get('name')

    def getFingerprint(self) -> str:
        '''Returns the key fingerprint.'''
        return self.data.get('fingerprint')

    def rename(self, name: str) -> 'SshKey':
        '''Renames the key.'''
        self.panel.api.account.updateSshKey(self.getUUID(), name)
        return self._update({'name': name})

    def delete(self) -> None:
        '''Deletes the key.'''
        return self.panel.api.account.deleteSshKey(self.getUUID())


class SecurityKey(Model):
    '''A WebAuthn security key / passkey.'''
    def getName(self) -> str:
        '''Returns the key name.'''
        return self.data.get('name')

    def getCredentialId(self) -> str:
        '''Returns the WebAuthn credential id.'''
        return self.data.get('credential_id')

    def getLastUsed(self) -> str:
        '''Returns when the key was last used.'''
        return self.data.get('last_used')

    def rename(self, name: str) -> 'SecurityKey':
        '''Renames the key.'''
        self.panel.api.account.updateSecurityKey(self.getUUID(), name)
        return self._update({'name': name})

    def delete(self, password: str = None) -> None:
        '''Deletes the key.'''
        return self.panel.api.account.deleteSecurityKey(self.getUUID(), password)


class Session(Model):
    '''A logged-in browser session.'''
    def __repr__(self):
        return f'<Session {self.getIP()!r}>'

    def getIP(self) -> str:
        '''Returns the IP address.'''
        return self.data.get('ip')

    def getUserAgent(self) -> str:
        '''Returns the browser user agent.'''
        return self.data.get('user_agent')

    def getLastUsed(self) -> str:
        '''Returns when the session was last used.'''
        return self.data.get('last_used')

    def isCurrent(self) -> bool:
        '''Returns True for the session making this request.'''
        return bool(self.data.get('is_using'))

    def delete(self) -> None:
        '''Logs the session out.'''
        return self.panel.api.account.deleteSession(self.getUUID())


class OAuthLink(Model):
    '''An external account (Discord, GitHub, ...) linked for login.'''
    def __repr__(self):
        return f'<OAuthLink {self.getIdentifier()!r}>'

    def getProvider(self) -> dict:
        '''Returns the OAuth provider.'''
        return self.data.get('oauth_provider')

    def getIdentifier(self) -> str:
        '''Returns the external account id.'''
        return self.data.get('identifier')

    def getLastUsed(self) -> str:
        '''Returns when the link was last used to log in.'''
        return self.data.get('last_used')

    def delete(self) -> None:
        '''Unlinks the account.'''
        return self.panel.api.account.deleteOauthLink(self.getUUID())


class CommandSnippet(Model):
    '''
    A saved console command, shown on matching servers.

    Example:
        snippet = panel.account.createCommandSnippet('Day', 'time set day')
    '''
    def getName(self) -> str:
        '''Returns the snippet name.'''
        return self.data.get('name')

    def getCommand(self) -> str:
        '''Returns the command.'''
        return self.data.get('command')

    def getEggs(self) -> list:
        '''Returns the eggs the snippet applies to. Empty means all.'''
        return self.data.get('eggs', [])

    def update(self, name: str = None, command: str = None, eggs: list = None) -> 'CommandSnippet':
        '''Changes the snippet.'''
        name = name or self.getName()
        self.panel.api.account.updateCommandSnippet(self.getUUID(), name, command, eggs)
        return self._update({'name': name, 'command': command, 'eggs': eggs})

    def duplicate(self, name: str) -> 'CommandSnippet':
        '''Copies the snippet.'''
        return CommandSnippet(self.panel, self.panel.api.account.duplicateCommandSnippet(self.getUUID(), name))

    def runOn(self, server) -> None:
        '''Sends the command to a server.'''
        return server.sendCommand(self.getCommand())

    def delete(self) -> None:
        '''Deletes the snippet.'''
        return self.panel.api.account.deleteCommandSnippet(self.getUUID())
