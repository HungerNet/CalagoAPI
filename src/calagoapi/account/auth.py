class Auth:
    '''
    Public authentication endpoints, available as `panel.auth`.

    These do not need an API key. They are useful for account tooling such as
    registration bots or password reset helpers.

    Example:
        panel.auth.forgotPassword('user@example.com')
        for provider in panel.auth.getOAuthProviders():
            print(provider['name'], panel.auth.getOAuthLoginUrl(provider))
    '''
    def __init__(self, panel):
        self.panel = panel
        self.api = panel.api.auth

    def login(self, user: str, password: str, captcha: str = None) -> dict:
        '''
        Logs in with a username/email and password.

        Returns:
            dict with `type` 'completed', or 'two_factor_required' together with
            a `token` for `completeTwoFactor()`.
        '''
        return self.api.login(user, password, captcha)

    def completeTwoFactor(self, code: str, confirmation_token: str, method: str = None) -> dict:
        '''Finishes a login that requires two-factor authentication.'''
        return self.api.checkpoint(code, confirmation_token, method)

    def sendTwoFactorEmail(self, confirmation_token: str) -> None:
        '''Sends the email two-factor code for a pending login.'''
        return self.api.checkpointEmail(confirmation_token)

    def register(self, username: str, email: str, password: str, name_first: str = None, name_last: str = None,
                 language: str = None, captcha: str = None) -> dict:
        '''Registers a new account (if registration is enabled on the panel).'''
        return self.api.register(username, email, password, name_first, name_last, language, captcha)

    def verifyEmail(self, token: str) -> dict:
        '''Verifies an email address with the token from the verification email.'''
        return self.api.verifyEmail(token)

    def forgotPassword(self, email: str, captcha: str = None) -> None:
        '''Sends a password reset email.'''
        return self.api.forgotPassword(email, captcha)

    def resetPassword(self, token: str, new_password: str) -> None:
        '''Sets a new password using the token from the reset email.'''
        return self.api.resetPassword(token, new_password)

    def getOAuthProviders(self) -> list:
        '''Returns the OAuth providers users can log in with.'''
        return self.api.oauthProviders()

    def getOAuthLoginUrl(self, provider) -> str:
        '''Returns the URL that starts an OAuth login with a provider (dict or UUID).'''
        provider_id = provider.get('uuid') if isinstance(provider, dict) else provider
        return self.api.oauthRedirectUrl(provider_id)

    def getSecurityKeyOptions(self, user: str = None) -> dict:
        '''
        Starts a passkey login.

        Args:
            user: Username for a username-first login. Omit for discoverable (usernameless) passkeys.
        '''
        return self.api.securityKeyOptions(user, discoverable=user is None)

    def loginWithSecurityKey(self, uuid: str, public_key_credential: dict, discoverable: bool = False) -> dict:
        '''Completes a passkey login with the authenticator's response.'''
        return self.api.securityKeyLogin(uuid, public_key_credential, discoverable)
