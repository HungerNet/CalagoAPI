# Account and authentication

## Your account

`panel.account` is the user that owns the API key.

```python
account = panel.account
print(account.getUsername(), account.getEmail(), account.getName())
account.isAdmin()
account.hasTwoFactor()
account.isEmailVerified()

account.setName('Steve', 'Miner')
account.setLanguage('de')
account.changePassword('old', 'new')
account.changeEmail('new@example.com', password='...')
account.setAvatar('avatar.png')
account.removeAvatar()

account.getActivity(page=1, per_page=20)
account.getSettings()
account.updateSettings({...})
account.refresh()
```

### Permissions

```python
permissions = panel.account.getPermissions()
permissions['server_permissions']    # every server permission, e.g. for subusers and API keys
permissions['admin_permissions']
permissions['user_permissions']
```

## API keys

The secret is only returned once, right after creation.

```python
key = panel.account.createApiKey(
    'backup-bot',
    server_permissions=['backup.*', 'control.console'],
    allowed_ips=['203.0.113.10/32'],
    expires='2027-01-01T00:00:00Z',
)
print(key.getKey())    # store it now

for key in panel.account.getApiKeys():
    print(key.getName(), key.getKeyStart(), key.getLastUsed(), key.isEnabled())

key.disable()
key.update(server_permissions=['backup.read'])
new_secret = key.recreate()
key.duplicate('backup-bot-2')
key.delete()
```

## SSH keys

```python
panel.account.addSshKey('laptop', 'ssh-ed25519 AAAA... me@laptop')
panel.account.importSshKeys('github', 'octocat')     # github, gitlab or launchpad
for key in panel.account.getSshKeys():
    print(key.getName(), key.getFingerprint())
```

## Security keys (passkeys)

Registration needs a WebAuthn-capable client, so CalagoAPI exposes both halves:

```python
pending = panel.account.startSecurityKeyRegistration('YubiKey', password='...')
# pass pending['options'] to your authenticator, then:
panel.account.finishSecurityKeyRegistration(pending['security_key'], credential)

panel.account.getSecurityKeys()
```

## Two-factor authentication

```python
setup = panel.account.getTwoFactorSetup()      # {'secret': ..., 'otp_url': ...}
codes = panel.account.enableTwoFactor('123456', password='...')
panel.account.disableTwoFactor('123456', password='...')

panel.account.enableEmailTwoFactor(password='...')
```

## Sessions and OAuth links

```python
for session in panel.account.getSessions():
    print(session.getIP(), session.getUserAgent(), session.isCurrent())
panel.account.logoutOtherSessions()

for link in panel.account.getOAuthLinks():
    print(link.getProvider()['name'], link.getIdentifier())
```

## Command snippets

Saved console commands shown on matching servers.

```python
snippet = panel.account.createCommandSnippet('Day', 'time set day')
snippet.runOn(server)
panel.account.getCommandSnippets()
panel.servers.getCommandSnippets(egg)      # snippets for one egg
```

## Public endpoints

`panel.auth` wraps endpoints that work without an API key.

```python
panel.auth.forgotPassword('user@example.com')
panel.auth.resetPassword(token, 'new-password')
panel.auth.verifyEmail(token)
panel.auth.register('steve', 'steve@example.com', 'password')

for provider in panel.auth.getOAuthProviders():
    print(provider['name'], panel.auth.getOAuthLoginUrl(provider))

result = panel.auth.login('steve', 'password')
if result['type'] == 'two_factor_required':
    panel.auth.completeTwoFactor('123456', result['token'])
```

Panel information:

```python
panel.getSettings()['app']['name']
panel.getLanguages()
panel.getAnnouncements()
```
