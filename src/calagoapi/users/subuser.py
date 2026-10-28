from calagoapi.utils.model import Model, idOf


class Subuser(Model):
    '''
    A user who has been given access to a server.

    Args:
        server: The server.
        data: Raw subuser data from Calagopus.

    Example:
        subuser = server.users.addSubuser('friend@example.com', ['control.console', 'control.start'])
        subuser.addPermissions(['file.read'])
        print(subuser.getUsername(), subuser.getPermissions())
    '''
    def __init__(self, server, data: dict):
        super().__init__(server.panel, data)
        self.server = server

    def __repr__(self):
        return f'<Subuser {self.getUsername()!r}>'

    def getUUID(self) -> str:
        '''Returns the user's UUID.'''
        return (self.data.get('user') or {}).get('uuid')

    def getUser(self) -> dict:
        '''Returns the raw user info (uuid, username, avatar, totp_enabled).'''
        return self.data.get('user', {})

    def getUsername(self) -> str:
        '''Returns the username.'''
        return self.getUser().get('username')

    def getAvatar(self) -> str:
        '''Returns the avatar URL, if any.'''
        return self.getUser().get('avatar')

    def getPermissions(self) -> list:
        '''Returns the granted permissions, e.g. ["control.console", "file.read"].'''
        return self.data.get('permissions', [])

    def getIgnoredFiles(self) -> list:
        '''Returns the file patterns hidden from this user.'''
        return self.data.get('ignored_files', [])

    def hasPermission(self, permission: str) -> bool:
        '''Returns True if the subuser has the permission.'''
        return permission in self.getPermissions()

    def hasTwoFactor(self) -> bool:
        '''Returns True if the user has two-factor authentication enabled.'''
        return bool(self.getUser().get('totp_enabled'))

    def setPermissions(self, permissions: list) -> 'Subuser':
        '''Replaces the subuser's permissions.'''
        self.panel.api.users.update(self.server.server_id, self.getUUID(), permissions=permissions)
        return self._update({'permissions': list(permissions)})

    def addPermissions(self, permissions: list) -> 'Subuser':
        '''Grants additional permissions.'''
        current = self.getPermissions()
        return self.setPermissions(current + [p for p in permissions if p not in current])

    def removePermissions(self, permissions: list) -> 'Subuser':
        '''Revokes permissions.'''
        return self.setPermissions([p for p in self.getPermissions() if p not in permissions])

    def setIgnoredFiles(self, ignored_files: list) -> 'Subuser':
        '''Sets file patterns the subuser cannot see.'''
        self.panel.api.users.update(self.server.server_id, self.getUUID(), ignored_files=ignored_files)
        return self._update({'ignored_files': list(ignored_files)})

    def delete(self) -> None:
        '''Removes the subuser from the server.'''
        return self.panel.api.users.delete(self.server.server_id, self.getUUID())


class SubuserManager:
    '''
    Subuser management for one server, available as `server.users`.

    Use `panel.account.getPermissions()` to list every permission that exists.

    Example:
        server.users.addSubuser('friend@example.com', ['control.console'])
        for subuser in server.users.getSubusers():
            print(subuser.getUsername())
    '''
    def __init__(self, server):
        self.server = server
        self.api = server.panel.api.users

    def getSubusers(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists the server's subusers as a Page of Subuser objects.'''
        return self.api.list(self.server.server_id, search, page, per_page).map(lambda data: Subuser(self.server, data))

    def getSubuser(self, uuid_or_username: str) -> Subuser:
        '''Returns a subuser by user UUID or username, or None.'''
        for subuser in self.getSubusers():
            if uuid_or_username in (subuser.getUUID(), subuser.getUsername()):
                return subuser
        return None

    def addSubuser(self, email: str, permissions: list, ignored_files: list = None) -> Subuser:
        '''
        Invites a user to the server.

        Args:
            email: Email of the user. An account is created if needed.
            permissions: Permissions to grant.
            ignored_files: File patterns to hide from the user.
        '''
        return Subuser(self.server, self.api.create(self.server.server_id, email, permissions, ignored_files))

    def createSubuser(self, email: str, permissions: list, ignored_files: list = None) -> Subuser:
        '''Alias of addSubuser().'''
        return self.addSubuser(email, permissions, ignored_files)

    def updateSubuser(self, subuser, permissions: list = None, ignored_files: list = None) -> None:
        '''Changes a subuser's permissions and/or ignored files.'''
        return self.api.update(self.server.server_id, idOf(subuser), permissions, ignored_files)

    def deleteSubuser(self, subuser) -> None:
        '''Removes a subuser from the server.'''
        return self.api.delete(self.server.server_id, idOf(subuser))
