'''
Example 9: configuration, lifecycle hooks and introspection.

Run it:
    python examples/extensions/09_configuration_and_lifecycle.py

Covers:
    - default_config + the user's config
    - validate_config() to check and normalize values
    - on_enable() to run setup once
    - re-enabling: same config is fine, different config is an error
    - secret_config to keep tokens out of diagnostics
    - registry.describe() / owner_of() to see who added what
'''
from calagoapi import MinecraftServer
from calagoapi.extensions import (
    ConfigurationError,
    Extension,
    ExtensionMetadata,
    enable,
    get_extension,
    method,
    register,
    registry,
)


@method(MinecraftServer)
def notifyUrl(self) -> str:
    config = NotifierExtension.get().config      # the effective, read-only config
    return f'{config["webhook"]}?server={self.server_id}'


class NotifierExtension(Extension):
    extension_id = 'notifier'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    default_config = {
        'webhook': 'https://hooks.example.com/default',
        'retries': 3,
        'api_token': None,
    }
    secret_config = ('api_token',)               # shown as *** in describe() and errors

    def validate_config(self, config):
        # Runs before anything is installed. Raise ConfigurationError for bad values;
        # return the (possibly normalized) config.
        if not config['webhook'].startswith('https://'):
            raise ConfigurationError('notifier: webhook must use https://')
        config['retries'] = int(config['retries'])
        return config

    def on_enable(self):
        # Runs once, after every member is installed. Raising here undoes the enable.
        print(f'  on_enable: notifier ready (mode={self.mode}, retries={self.config["retries"]})')


register(NotifierExtension)

# Unknown keys are rejected, which catches typos:
try:
    enable('notifier', config={'webhok': 'https://x'})
except ConfigurationError as e:
    print('ConfigurationError:', e)

# validate_config() rejects bad values:
try:
    enable('notifier', config={'webhook': 'http://insecure'})
except ConfigurationError as e:
    print('ConfigurationError:', e)

# User values override the defaults; the rest keep their default.
extension = enable('notifier', config={'webhook': 'https://hooks.example.com/mc', 'retries': '5', 'api_token': 's3cret'})
print(dict(extension.config))

# Same config again: fine. No config: fine ("just make sure it is enabled").
enable('notifier', config={'webhook': 'https://hooks.example.com/mc', 'retries': '5', 'api_token': 's3cret'})
enable('notifier')

# A different config: refused instead of silently reconfiguring.
try:
    enable('notifier', config={'webhook': 'https://hooks.example.com/other'})
except ConfigurationError as e:
    print('ConfigurationError:', e)

print(get_extension('notifier') is extension)                      # True
print('owner of MinecraftServer.notifyUrl:', registry.owner_of(MinecraftServer, 'notifyUrl'))
print(registry.describe())                                          # api_token shows as ***
