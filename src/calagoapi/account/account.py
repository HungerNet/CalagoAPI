import os

from calagoapi.account.models import ApiKey, SshKey, SecurityKey, Session, OAuthLink, CommandSnippet
from calagoapi.users.activity import Activity
from calagoapi.utils.model import idOf


class Account:
    '''
    The account that owns the API key, available as `panel.account`.

    Example:
        print(panel.account.getUsername(), panel.account.getEmail())
        panel.account.addSshKey('laptop', open('~/.ssh/id_ed25519.pub').read())
        for session in panel.account.getSessions():
            print(session.getIP(), session.getUserAgent())
    '''
    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.account
        self.data = None

    def __repr__(self):
        return f'<Account {self.getUsername()!r}>' if self.data else '<Account>'

    # profile
    def getUser(self) -> dict:
        '''Returns the account details (cached, see refresh()).'''
        if self.data is None:
            self.refresh()
        return self.data

    def refresh(self) -> dict:
        '''Re-fetches the account details.'''
        self.data = self.api.get()
        return self.data

    def getUUID(self) -> str:
        '''Returns the user UUID.'''
        return self.getUser().get('uuid')

    def getUsername(self) -> str:
        '''Returns the username.'''
        return self.getUser().get('username')

    def getEmail(self) -> str:
        '''Returns the email address.'''
        return self.getUser().get('email')

    def getName(self) -> str:
        '''Returns "First Last", or the username if no name is set.'''
        user = self.getUser()
        return ' '.join(filter(None, [user.get('name_first'), user.get('name_last')])) or user.get('username')

    def getLanguage(self) -> str:
        '''Returns the language code.'''
        return self.getUser().get('language')

    def getRole(self) -> dict:
        '''Returns the account role, or None.'''
        return self.getUser().get('role')

    def getTwoFactorMethods(self) -> list:
        '''Returns enabled two-factor methods: totp, security_key, email.'''
        return self.getUser().get('two_factor_methods', [])

    def isAdmin(self) -> bool:
        '''Returns True for root administrators.'''
        return bool(self.getUser().get('admin'))

    def hasTwoFactor(self) -> bool:
        '''Returns True if any two-factor method is enabled.'''
        return bool(self.getTwoFactorMethods())

    def isEmailVerified(self) -> bool:
        '''Returns True if the email address is verified.'''
        return bool(self.getUser().get('email_verified'))

    def update(self, username: str = None, name_first: str = None, name_last: str = None, language: str = None) -> None:
        '''Changes profile fields. Only the given fields change.'''
        self.api.update(username, name_first, name_last, language)
        self.data = None

    def setUsername(self, username: str) -> None:
        '''Changes the username.'''
        return self.update(username=username)

    def setName(self, name_first: str, name_last: str = None) -> None:
        '''Changes the first and last name.'''
        return self.update(name_first=name_first, name_last=name_last)

    def setLanguage(self, language: str) -> None:
        '''Changes the language, e.g. "en" or "de".'''
        return self.update(language=language)

    def changeEmail(self, email: str, password: str) -> dict:
        '''Starts an email change. The new address must be verified.'''
        return self.api.changeEmail(email, password)

    def resendVerificationEmail(self) -> dict:
        '''Sends the verification email again.'''
        return self.api.resendVerification()

    def changePassword(self, password: str, new_password: str) -> None:
        '''Changes the password.'''
        return self.api.changePassword(password, new_password)

    def setPasswordLogin(self, enabled: bool, password: str) -> None:
        '''Allows or forbids logging in with a password (for OAuth/passkey-only accounts).'''
        return self.api.setPasswordLogin(not enabled, password)

    def setAvatar(self, image, content_type: str = 'image/png') -> str:
        '''
        Uploads a new avatar.

        Args:
            image: Local file path or image bytes.

        Returns:
            The avatar URL.
        '''
        if isinstance(image, (str, os.PathLike)):
            with open(image, 'rb') as f:
                image = f.read()
        return self.api.setAvatar(image, content_type)

    def removeAvatar(self) -> None:
        '''Removes the avatar.'''
        return self.api.deleteAvatar()

    def getSettings(self) -> dict:
        '''Returns personal UI settings.'''
        return self.api.settings()

    def updateSettings(self, settings: dict) -> None:
        '''Saves personal UI settings.'''
        return self.api.updateSettings(settings)

    def getPermissions(self) -> dict:
        '''
        Returns every permission that exists, grouped into user, admin and server permissions.

        Useful when creating API keys, roles or subusers.
        '''
        return self.api.permissions()

    def getActivity(self, search: str = None, page: int = 1, per_page: int = 50):
        '''Returns the account activity log.'''
        return self.api.activity(search, page, per_page).map(lambda data: Activity(self.panel, data))

    def logout(self) -> None:
        '''Ends the current session.'''
        return self.api.logout()

    # two factor
    def getTwoFactorSetup(self) -> dict:
        '''Returns the TOTP secret and otpauth:// URL for setting up an authenticator app.'''
        return self.api.twoFactorSetup()

    def enableTwoFactor(self, code: str, password: str) -> list:
        '''Enables TOTP two-factor. Returns recovery codes.'''
        return self.api.enableTwoFactor(code, password)

    def disableTwoFactor(self, code: str, password: str) -> None:
        '''Disables TOTP two-factor.'''
        return self.api.disableTwoFactor(code, password)

    def enableEmailTwoFactor(self, password: str) -> list:
        '''Enables email two-factor. Returns recovery codes.'''
        return self.api.enableEmailTwoFactor(password)

    def disableEmailTwoFactor(self, password: str) -> None:
        '''Disables email two-factor.'''
        return self.api.disableEmailTwoFactor(password)

    # api keys
    def getApiKeys(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists the account's API keys.'''
        return self.api.apiKeys(search, page, per_page).map(lambda data: ApiKey(self.panel, data))

    def getApiKey(self, identifier: str) -> ApiKey:
        '''Returns an API key by its identifier (the start of the key).'''
        return ApiKey(self.panel, self.api.apiKeyByIdentifier(identifier))

    def createApiKey(self, name: str, user_permissions: list = None, server_permissions: list = None,
                     admin_permissions: list = None, allowed_ips: list = None, expires: str = None) -> ApiKey:
        '''
        Creates an API key.

        Args:
            name: Key name.
            user_permissions: Account permissions.
            server_permissions: Server permissions, e.g. ['control.*', 'file.read'].
            admin_permissions: Admin permissions.
            allowed_ips: Restrict usage to these IPs/CIDRs.
            expires: ISO-8601 expiry time.

        Returns:
            The ApiKey. Call `getKey()` to read the secret, it is shown only once.
        '''
        result = self.api.createApiKey(name, allowed_ips, user_permissions, admin_permissions, server_permissions, expires=expires)
        return ApiKey(self.panel, result['api_key'], result.get('key'))

    def deleteApiKey(self, api_key) -> None:
        '''Deletes an API key.'''
        return self.api.deleteApiKey(idOf(api_key))

    # ssh keys
    def getSshKeys(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists SSH keys.'''
        return self.api.sshKeys(search, page, per_page).map(lambda data: SshKey(self.panel, data))

    def addSshKey(self, name: str, public_key: str) -> SshKey:
        '''Adds an SSH public key for SFTP.'''
        return SshKey(self.panel, self.api.createSshKey(name, public_key))

    def importSshKeys(self, provider: str, username: str) -> list:
        '''
        Imports public keys from github, gitlab or launchpad.

        Example:
            panel.account.importSshKeys('github', 'octocat')
        '''
        return [SshKey(self.panel, data) for data in self.api.importSshKeys(provider, username)]

    def deleteSshKey(self, ssh_key) -> None:
        '''Deletes an SSH key.'''
        return self.api.deleteSshKey(idOf(ssh_key))

    # security keys
    def getSecurityKeys(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists security keys / passkeys.'''
        return self.api.securityKeys(search, page, per_page).map(lambda data: SecurityKey(self.panel, data))

    def startSecurityKeyRegistration(self, name: str, password: str, allow_usernameless_login: bool = None) -> dict:
        '''
        Starts registering a security key.

        Returns:
            dict with the pending `security_key` and WebAuthn `options` to pass to the authenticator.
            Finish with `finishSecurityKeyRegistration()`.
        '''
        return self.api.createSecurityKey(name, password, allow_usernameless_login)

    def finishSecurityKeyRegistration(self, security_key, public_key_credential: dict) -> str:
        '''Completes a security key registration with the authenticator's response.'''
        key_id = security_key.get('uuid') if isinstance(security_key, dict) else idOf(security_key)
        return self.api.challengeSecurityKey(key_id, public_key_credential)

    def deleteSecurityKey(self, security_key, password: str = None) -> None:
        '''Deletes a security key.'''
        return self.api.deleteSecurityKey(idOf(security_key), password)

    # sessions
    def getSessions(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists active browser sessions.'''
        return self.api.sessions(search, page, per_page).map(lambda data: Session(self.panel, data))

    def logoutOtherSessions(self) -> int:
        '''Logs out every other session. Returns how many were removed.'''
        return self.api.deleteOtherSessions()

    # oauth
    def getOAuthLinks(self, page: int = None, per_page: int = None):
        '''Lists linked external accounts.'''
        return self.api.oauthLinks(page, per_page).map(lambda data: OAuthLink(self.panel, data))

    def getOAuthLink(self, oauth_link_id: str) -> OAuthLink:
        '''Returns one linked external account.'''
        return OAuthLink(self.panel, self.api.oauthLink(oauth_link_id))

    def unlinkOAuth(self, oauth_link) -> None:
        '''Removes a linked external account.'''
        return self.api.deleteOauthLink(idOf(oauth_link))

    # command snippets
    def getCommandSnippets(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists saved command snippets.'''
        return self.api.commandSnippets(search, page, per_page).map(lambda data: CommandSnippet(self.panel, data))

    def createCommandSnippet(self, name: str, command: str, eggs: list = None) -> CommandSnippet:
        '''
        Saves a console command.

        Args:
            eggs: Eggs (UUIDs) the snippet is shown for. All when empty.
        '''
        return CommandSnippet(self.panel, self.api.createCommandSnippet(name, command, [idOf(e) for e in eggs or []]))

    def deleteCommandSnippet(self, snippet) -> None:
        '''Deletes a command snippet.'''
        return self.api.deleteCommandSnippet(idOf(snippet))
