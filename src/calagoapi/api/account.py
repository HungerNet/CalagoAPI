from calagoapi.api.client import segment


# Internal Calagopus AccountAPI
class AccountAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, suffix=''):
        return f'/api/client/account{suffix}'

    # profile
    def get(self):
        return self.client.get(self._path())['user']

    def update(self, username=None, name_first=None, name_last=None, language=None):
        return self.client.patch(self._path(), json={
            'username': username,
            'name_first': name_first,
            'name_last': name_last,
            'language': language,
        })

    def permissions(self):
        return self.client.get('/api/client/permissions')

    def activity(self, search=None, page=None, per_page=None):
        return self.client.list(self._path('/activity'), 'activities', {'search': search}, page, per_page)

    def settings(self):
        return self.client.get(self._path('/settings'))['settings']

    def updateSettings(self, settings):
        return self.client.patch(self._path('/settings'), json={'settings': settings})

    def setAvatar(self, content, content_type='image/png'):
        return self.client.request(
            'PUT', self._path('/avatar'), data=content, headers={'Content-Type': content_type}
        )['avatar']

    def deleteAvatar(self):
        return self.client.delete(self._path('/avatar'))

    def logout(self):
        return self.client.post(self._path('/logout'))

    # email and password
    def changeEmail(self, email, password):
        return self.client.put(self._path('/email'), json={'email': email, 'password': password})

    def resendVerification(self):
        return self.client.post(self._path('/email/resend-verification'))

    def changePassword(self, password, new_password):
        return self.client.put(self._path('/password'), json={'password': password, 'new_password': new_password})

    def setPasswordLogin(self, disabled, password):
        return self.client.put(self._path('/password-login'), json={'disabled': disabled, 'password': password})

    # two factor
    def twoFactorSetup(self):
        return self.client.get(self._path('/two-factor'))

    def enableTwoFactor(self, code, password):
        return self.client.post(self._path('/two-factor'), json={'code': code, 'password': password})['recovery_codes']

    def disableTwoFactor(self, code, password):
        return self.client.delete(self._path('/two-factor'), json={'code': code, 'password': password})

    def enableEmailTwoFactor(self, password):
        return self.client.post(self._path('/two-factor/email'), json={'password': password})['recovery_codes']

    def disableEmailTwoFactor(self, password):
        return self.client.delete(self._path('/two-factor/email'), json={'password': password})

    # api keys
    def apiKeys(self, search=None, page=None, per_page=None):
        return self.client.list(self._path('/api-keys'), 'api_keys', {'search': search}, page, per_page)

    def apiKeyByIdentifier(self, identifier):
        return self.client.get(self._path(f'/api-keys/identifier/{segment(identifier)}'))['api_key']

    def createApiKey(self, name, allowed_ips=None, user_permissions=None, admin_permissions=None, server_permissions=None, enabled=None, expires=None):
        return self.client.post(self._path('/api-keys'), json={
            'name': name,
            'allowed_ips': allowed_ips or [],
            'user_permissions': user_permissions or [],
            'admin_permissions': admin_permissions or [],
            'server_permissions': server_permissions or [],
            'enabled': enabled,
            'expires': expires,
        })

    def updateApiKey(self, api_key_id, allowed_ips, name=None, enabled=None, user_permissions=None, admin_permissions=None, server_permissions=None, expires=None):
        return self.client.patch(self._path(f'/api-keys/{api_key_id}'), json={
            'allowed_ips': allowed_ips,
            'name': name,
            'enabled': enabled,
            'user_permissions': user_permissions,
            'admin_permissions': admin_permissions,
            'server_permissions': server_permissions,
            'expires': expires,
        })

    def deleteApiKey(self, api_key_id):
        return self.client.delete(self._path(f'/api-keys/{api_key_id}'))

    def duplicateApiKey(self, api_key_id, name):
        return self.client.post(self._path(f'/api-keys/{api_key_id}/duplicate'), json={'name': name})

    def recreateApiKey(self, api_key_id):
        return self.client.post(self._path(f'/api-keys/{api_key_id}/recreate'))['key']

    # ssh keys
    def sshKeys(self, search=None, page=None, per_page=None):
        return self.client.list(self._path('/ssh-keys'), 'ssh_keys', {'search': search}, page, per_page)

    def createSshKey(self, name, public_key):
        return self.client.post(self._path('/ssh-keys'), json={'name': name, 'public_key': public_key})['ssh_key']

    def importSshKeys(self, provider, username):
        return self.client.post(self._path('/ssh-keys/import'), json={'provider': provider, 'username': username})['ssh_keys']

    def updateSshKey(self, ssh_key_id, name):
        return self.client.patch(self._path(f'/ssh-keys/{ssh_key_id}'), json={'name': name})

    def deleteSshKey(self, ssh_key_id):
        return self.client.delete(self._path(f'/ssh-keys/{ssh_key_id}'))

    # security keys
    def securityKeys(self, search=None, page=None, per_page=None):
        return self.client.list(self._path('/security-keys'), 'security_keys', {'search': search}, page, per_page)

    def createSecurityKey(self, name, password, allow_usernameless_login=None):
        return self.client.post(self._path('/security-keys'), json={
            'name': name,
            'password': password,
            'allow_usernameless_login': allow_usernameless_login,
        })

    def challengeSecurityKey(self, security_key_id, public_key_credential):
        return self.client.post(
            self._path(f'/security-keys/{security_key_id}/challenge'),
            json={'public_key_credential': public_key_credential}
        )['credential_id']

    def updateSecurityKey(self, security_key_id, name):
        return self.client.patch(self._path(f'/security-keys/{security_key_id}'), json={'name': name})

    def deleteSecurityKey(self, security_key_id, password=None):
        return self.client.delete(self._path(f'/security-keys/{security_key_id}'), json={'password': password})

    # sessions
    def sessions(self, search=None, page=None, per_page=None):
        return self.client.list(self._path('/sessions'), 'sessions', {'search': search}, page, per_page)

    def deleteSession(self, session_id):
        return self.client.delete(self._path(f'/sessions/{session_id}'))

    def deleteOtherSessions(self):
        return self.client.delete(self._path('/sessions'))['deleted']

    # oauth links
    def oauthLinks(self, page=None, per_page=None):
        return self.client.list(self._path('/oauth-links'), 'oauth_links', None, page, per_page)

    def oauthLink(self, oauth_link_id):
        return self.client.get(self._path(f'/oauth-links/{oauth_link_id}'))['oauth_link']

    def deleteOauthLink(self, oauth_link_id):
        return self.client.delete(self._path(f'/oauth-links/{oauth_link_id}'))

    # command snippets
    def commandSnippets(self, search=None, page=None, per_page=None):
        return self.client.list(self._path('/command-snippets'), 'command_snippets', {'search': search}, page, per_page)

    def createCommandSnippet(self, name, command, eggs=None):
        return self.client.post(self._path('/command-snippets'), json={
            'name': name,
            'command': command,
            'eggs': eggs or [],
        })['command_snippet']

    def updateCommandSnippet(self, snippet_id, name, command=None, eggs=None):
        return self.client.patch(self._path(f'/command-snippets/{snippet_id}'), json={
            'name': name,
            'command': command,
            'eggs': eggs,
        })

    def deleteCommandSnippet(self, snippet_id):
        return self.client.delete(self._path(f'/command-snippets/{snippet_id}'))

    def duplicateCommandSnippet(self, snippet_id, name):
        return self.client.post(self._path(f'/command-snippets/{snippet_id}/duplicate'), json={'name': name})['command_snippet']
