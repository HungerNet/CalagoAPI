# Internal Calagopus AuthAPI (public, unauthenticated endpoints)
class AuthAPI:
    def __init__(self, client):
        self.client = client

    def login(self, user, password, captcha=None):
        return self.client.post('/api/auth/login', json={'user': user, 'password': password, 'captcha': captcha})

    def checkpoint(self, code, confirmation_token, method=None):
        return self.client.post('/api/auth/login/checkpoint', json={
            'code': code,
            'confirmation_token': confirmation_token,
            'method': method,
        })['user']

    def checkpointEmail(self, confirmation_token):
        return self.client.post('/api/auth/login/checkpoint/email', json={'confirmation_token': confirmation_token})

    def register(self, username, email, password, name_first=None, name_last=None, language=None, captcha=None):
        return self.client.post('/api/auth/register', json={
            'username': username,
            'email': email,
            'password': password,
            'name_first': name_first,
            'name_last': name_last,
            'language': language,
            'captcha': captcha,
        })['user']

    def verifyEmail(self, token):
        return self.client.post('/api/auth/email/verify', json={'token': token})

    def forgotPassword(self, email, captcha=None):
        return self.client.post('/api/auth/password/forgot', json={'email': email, 'captcha': captcha})

    def resetPassword(self, token, new_password):
        return self.client.post('/api/auth/password/reset', json={'token': token, 'new_password': new_password})

    def oauthProviders(self):
        return self.client.get('/api/auth/oauth')['oauth_providers']

    def oauthRedirectUrl(self, oauth_provider_id):
        return f'{self.client.url}/api/auth/oauth/redirect/{oauth_provider_id}'

    def securityKeyOptions(self, user=None, discoverable=False):
        if discoverable:
            return self.client.get('/api/auth/login/security-key/discoverable')
        return self.client.get('/api/auth/login/security-key', params={'user': user})

    def securityKeyLogin(self, uuid, public_key_credential, discoverable=False):
        path = '/api/auth/login/security-key/discoverable' if discoverable else '/api/auth/login/security-key'
        return self.client.post(path, json={'uuid': uuid, 'public_key_credential': public_key_credential})['user']
