# 09 · Configuration and dependencies

This builds on [07](07-your-first-extension.md) (the `monitoring` extension) and
[08](08-services-and-namespaces.md).

## What you will build

An `alerts` extension that depends on `monitoring`, is configured with a threshold and a
webhook token, validates its configuration, and runs setup once when enabled.

## Step 1: configuration

```python
class AlertsExtension(Extension):
    extension_id = 'alerts'
    default_config = {'warn_percent': 90, 'webhook': None, 'token': None}
    secret_config = ('token',)           # shown as *** in describe() and in errors
```

Users override defaults with `enable('alerts', config={...})`. Unknown keys are rejected.
Inside members read the effective, read-only config with `AlertsExtension.get().config`.

## Step 2: validation and setup

```python
    def validateConfig(self, config):
        if not 1 <= config['warn_percent'] <= 100:
            raise ConfigurationError('alerts: warn_percent must be 1-100')
        if config['webhook'] and not config['webhook'].startswith('https://'):
            raise ConfigurationError('alerts: webhook must use https://')
        return config

    def onEnable(self):
        print(f'alerts at {self.config["warn_percent"]} %')
```

`validateConfig()` runs before anything is installed. `onEnable()` runs once after every
member is installed, and if it raises, the whole enable is rolled back.

## Step 3: depend on another extension

```python
    dependencies = ['monitoring']
```

`enable('alerts')` enables `monitoring` first, with its defaults. To configure
`monitoring` yourself, enable it **before** `alerts`. Enabling it afterwards with a
different config raises `ConfigurationError`.

## Complete program

`alerts.py` (with `monitoring.py` from tutorial 07 next to it):

```python
from calagoapi import Server
from calagoapi.extensions import ConfigurationError, Extension, ExtensionMetadata, method

from monitoring import getMemoryPercent


@method(Server)
def checkAlerts(self) -> list:
    '''Returns alert messages for this server (and would post them to the webhook).'''
    config = AlertsExtension.get().config
    percent = getMemoryPercent(self)
    if percent is not None and percent >= config['warn_percent']:
        return [f'{self.name} uses {percent} % of its memory']
    return []


class AlertsExtension(Extension):
    extension_id = 'alerts'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    dependencies = ['monitoring']
    default_config = {'warn_percent': 90, 'webhook': None, 'token': None}
    secret_config = ('token',)
    members = [checkAlerts]

    def validateConfig(self, config):
        if not 1 <= config['warn_percent'] <= 100:
            raise ConfigurationError('alerts: warn_percent must be 1-100')
        if config['webhook'] and not config['webhook'].startswith('https://'):
            raise ConfigurationError('alerts: webhook must use https://')
        return config

    def onEnable(self):
        print(f'alerts at {self.config["warn_percent"]} %')
```

`check.py`:

```python
from calagoapi import Panel
from calagoapi.extensions import enable, getExtension, register, registry

from alerts import AlertsExtension
from monitoring import MonitoringExtension

register(MonitoringExtension)
register(AlertsExtension)
enable('alerts', config={'warn_percent': 80, 'token': 's3cret'})

print(f'monitoring was enabled by: {getExtension("monitoring").enabled_by}')   # alerts
print(registry.describe())                                                  # token: ***

with Panel(url='https://panel.example.com', api_key='c7sp_...') as panel:
    for server in panel.servers.getServers():
        for alert in server.checkAlerts():
            print(f'ALERT {alert}')
```

## Renaming later: aliases

If you rename `alerts` to `server_alerts`, keep the old id working:

```python
from calagoapi.extensions import Alias

class ServerAlertsExtension(Extension):
    extension_id = 'server_alerts'
    aliases = [Alias('alerts', deprecated=True, message='Renamed in 2.0.')]
```

`enable('alerts')` then still works and warns (`ExtensionDeprecationWarning`). If the API
changed completely, an alias would be misleading. Let the old id fail with a clear
message instead, as CalagoAPI 2.0 does for `hungerbridge` → `minecraft`.

## How it works

- Dependencies are resolved depth-first. A missing dependency raises `DependencyError`
  (with a `pip install` hint for first-party ids); a cycle raises
  `CircularDependencyError` with its path; `Dependency('x', optional=True)` is skipped
  when `x` is not installed.
- The config is merged shallowly (`{**default_config, **user_config}`), validated, then
  frozen.
- Each `enable()` runs under one lock, so enabling from several threads is safe.

Runnable versions: [examples/extensions/05, 08, 09](../../../examples/extensions/README.md).

## Next

[10 · Packaging and publishing](10-packaging-and-publishing.md).
