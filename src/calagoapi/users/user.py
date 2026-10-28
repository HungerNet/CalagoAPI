from calagoapi.utils.model import Model, idOf
from calagoapi.users.activity import Activity


class User(Model):
    '''
    A panel user, as seen by an administrator.

    Returned by `panel.admin.users`. Requires an admin API key.

    Example:
        user = panel.admin.users.getUser('...')
        if user.isSuspended():
            user.unsuspend()
        user.setPassword('a-new-password')
    '''
    def _api(self):
        return self.panel.api.admin.users

    # getters
    def getUsername(self) -> str:
        '''Returns the username.'''
        return self.data.get('username')

    def getEmail(self) -> str:
        '''Returns the email address.'''
        return self.data.get('email')

    def getName(self) -> str:
        '''Returns "First Last", or the username if no name is set.'''
        name = ' '.join(filter(None, [self.data.get('name_first'), self.data.get('name_last')]))
        return name or self.getUsername()

    def getFirstName(self) -> str:
        '''Returns the first name.'''
        return self.data.get('name_first')

    def getLastName(self) -> str:
        '''Returns the last name.'''
        return self.data.get('name_last')

    def getExternalId(self) -> str:
        '''Returns the external id used by billing systems, if set.'''
        return self.data.get('external_id')

    def getRole(self) -> dict:
        '''Returns the assigned role, or None.'''
        return self.data.get('role')

    def getLanguage(self) -> str:
        '''Returns the preferred language code.'''
        return self.data.get('language')

    def getAvatar(self) -> str:
        '''Returns the avatar URL, if any.'''
        return self.data.get('avatar')

    def getTwoFactorMethods(self) -> list:
        '''Returns enabled two-factor methods: totp, security_key, email.'''
        return self.data.get('two_factor_methods', [])

    # state checks
    def isAdmin(self) -> bool:
        '''Returns True for root administrators.'''
        return bool(self.data.get('admin'))

    def isSuspended(self) -> bool:
        '''Returns True if the user is suspended.'''
        return bool(self.data.get('suspended'))

    def isFrozen(self) -> bool:
        '''Returns True if the account is frozen (read-only).'''
        return bool(self.data.get('frozen'))

    def isEmailVerified(self) -> bool:
        '''Returns True if the email address is verified.'''
        return bool(self.data.get('email_verified'))

    def hasTwoFactor(self) -> bool:
        '''Returns True if any two-factor method is enabled.'''
        return bool(self.getTwoFactorMethods() or self.data.get('totp_enabled'))

    def hasPassword(self) -> bool:
        '''Returns True if the user has a password (OAuth-only users do not).'''
        return bool(self.data.get('has_password'))

    # actions
    def refresh(self) -> 'User':
        '''Re-fetches the user.'''
        self.data = self._api().get(self.getUUID())
        return self

    def update(self, **fields) -> 'User':
        '''
        Updates the user.

        Accepted fields: username, email, name_first, name_last, password, admin,
        frozen, suspended, language, role_uuid, external_id.

        Example:
            user.update(email='new@example.com', language='de')
        '''
        if 'role' in fields:
            fields['role_uuid'] = idOf(fields.pop('role'))
        self._api().update(self.getUUID(), **fields)
        return self._update({k: v for k, v in fields.items() if k != 'password'})

    def setPassword(self, password: str) -> 'User':
        '''Sets a new password.'''
        return self.update(password=password)

    def setEmail(self, email: str) -> 'User':
        '''Changes the email address.'''
        return self.update(email=email)

    def setUsername(self, username: str) -> 'User':
        '''Changes the username.'''
        return self.update(username=username)

    def setAdmin(self, admin: bool) -> 'User':
        '''Grants or revokes root admin.'''
        return self.update(admin=admin)

    def setRole(self, role) -> 'User':
        '''Assigns a role (Role object or UUID).'''
        return self.update(role=role)

    def suspend(self) -> 'User':
        '''Suspends the user.'''
        return self.update(suspended=True)

    def unsuspend(self) -> 'User':
        '''Lifts a suspension.'''
        return self.update(suspended=False)

    def freeze(self) -> 'User':
        '''Freezes the account.'''
        return self.update(frozen=True)

    def unfreeze(self) -> 'User':
        '''Unfreezes the account.'''
        return self.update(frozen=False)

    def disableTwoFactor(self) -> None:
        '''Removes every two-factor method from the account.'''
        return self.panel.api.admin.userDisableTwoFactor(self.getUUID())

    def sendPasswordReset(self) -> None:
        '''Emails the user a password reset link.'''
        return self.panel.api.admin.userSendPasswordReset(self.getUUID())

    def verifyEmail(self) -> None:
        '''Marks the email address as verified.'''
        return self.panel.api.admin.userVerifyEmail(self.getUUID())

    def getServers(self, owned: bool = None, search: str = None, page: int = None, per_page: int = None):
        '''
        Returns servers the user can access.

        Args:
            owned: True for owned servers only, False for subuser access only.
        '''
        from calagoapi.servers.admin import AdminServer
        return self.panel.api.admin.userServers(self.getUUID(), owned, search, page, per_page).map(
            lambda data: AdminServer(self.panel, data)
        )

    def getActivity(self, search: str = None, page: int = None, per_page: int = 50):
        '''Returns the user's activity log (first page by default).'''
        return self.panel.api.admin.userActivity(self.getUUID(), search, page or 1, per_page).map(
            lambda data: Activity(self.panel, data)
        )

    def getOAuthLinks(self, page: int = None, per_page: int = None):
        '''Returns linked OAuth accounts.'''
        return self.panel.api.admin.userOauthLinks(self.getUUID()).list(page=page, per_page=per_page)

    def getOAuthLink(self, oauth_link_id: str) -> dict:
        '''Returns one linked OAuth identity.'''
        return self.panel.api.admin.userOauthLinks(self.getUUID()).get(oauth_link_id)

    def linkOAuth(self, oauth_provider, identifier: str) -> dict:
        '''Links an OAuth identity to the user.'''
        return self.panel.api.admin.userOauthLinks(self.getUUID()).create(
            oauth_provider_uuid=idOf(oauth_provider), identifier=identifier
        )

    def unlinkOAuth(self, oauth_link_id: str) -> None:
        '''Removes a linked OAuth identity.'''
        return self.panel.api.admin.userOauthLinks(self.getUUID()).delete(oauth_link_id)

    def delete(self) -> None:
        '''Deletes the user.'''
        return self._api().delete(self.getUUID())


class UserManager:
    '''
    Admin user management, available as `panel.admin.users`.

    Example:
        user = panel.admin.users.createUser('steve', 'steve@example.com', password='hunter2')
        for user in panel.admin.users.getUsers(search='steve'):
            print(user.getUsername(), user.isAdmin())
    '''
    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.admin.users

    def _wrap(self, data):
        return User(self.panel, data)

    def getUsers(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists users as a Page of User objects.'''
        return self.api.list(search, page, per_page).map(self._wrap)

    def getUser(self, user_id: str) -> User:
        '''Returns a user by UUID.'''
        return self._wrap(self.api.get(user_id))

    def getUserByExternalId(self, external_id: str) -> User:
        '''Returns a user by external id (as set by billing integrations).'''
        return self._wrap(self.panel.api.admin.userByExternalId(external_id))

    def getUserByUsername(self, username: str) -> User:
        '''Returns a user by exact username or email, or None.'''
        for user in self.getUsers(search=username):
            if username in (user.getUsername(), user.getEmail()):
                return user
        return None

    def createUser(self, username: str, email: str, password: str = None, admin: bool = False, language: str = 'en',
                   name_first: str = None, name_last: str = None, role=None, external_id: str = None,
                   send_email: bool = None, verify_email: bool = None) -> User:
        '''
        Creates a user.

        Args:
            username: Username.
            email: Email address.
            password: Password. Leave empty to let the user set one via email.
            admin: Make the user a root administrator.
            language: Language code.
            name_first: First name.
            name_last: Last name.
            role: Role object or UUID.
            external_id: Id from an external system.
            send_email: Send the welcome email.
            verify_email: Mark the email address as already verified.
        '''
        return self._wrap(self.api.create(
            username=username,
            email=email,
            password=password,
            admin=admin,
            language=language,
            name_first=name_first,
            name_last=name_last,
            role_uuid=idOf(role),
            external_id=external_id,
            send_email=send_email,
            verify_email=verify_email,
        ))

    def deleteUser(self, user) -> None:
        '''Deletes a user.'''
        return self.api.delete(idOf(user))
