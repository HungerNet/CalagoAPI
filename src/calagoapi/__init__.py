'''
CalagoAPI: a Python SDK for the Calagopus panel.

The core package is game-agnostic. Game-specific features ship as separate
extension packages (see `calagoapi.extensions`).

Example:
    from calagoapi import Panel

    with Panel(url='https://panel.example.com', api_key='...') as panel:
        for server in panel.servers.getServers():
            print(f'{server.name}: {server.getStatus()}')
'''
from importlib.metadata import version as _pkg_version, PackageNotFoundError

# package version
try:
    __version__ = _pkg_version('calagoapi')
except PackageNotFoundError:
    __version__ = '0.0.0'

# modules
from .panel import Panel
from .aio import AsyncPanel, AsyncConsole
from .console import Console, ConsoleEvent
from .servers import Server, AdminServer, ServerGroup
from .files import File
from .backups import Backup, BackupGroup
from .databases import Database, DatabaseInstance, InstanceDatabase, InstanceUser, DatabaseExplorer
from .schedules import Schedule, ScheduleStep, triggers, conditions, actions, variable
from .schedules import backups as backup_selectors
from .users import Subuser, User, Activity
from .network import Allocation, Subdomain
from .nodes import Node
from .account import ApiKey, SshKey, SecurityKey, Session, OAuthLink, CommandSnippet
from .admin import (
    Location,
    Nest,
    Egg,
    EggVariable,
    Mount,
    Device,
    Role,
    Announcement,
    OAuthProvider,
    DatabaseHost,
    DatabaseAgentHost,
    DatabaseAgentTemplate,
    BackupConfiguration,
    BackupPolicy,
    EggRepository,
    EggConfiguration,
    SubdomainDomain,
)

from . import extensions

from .utils import (
    Page,
    convert,
    formatBytes,
    formatDuration,
    waitForState,
    waitForOnline,
    waitForOffline,
    secsUntil,
    minsUntil,
    CalagoAPIError,
    BadRequestError,
    AuthenticationError,
    PermissionDeniedError,
    NotFoundError,
    ConflictError,
    RateLimitError,
    ServerError,
    PanelConnectionError,
    ConsoleError,
    InvalidActionError,
    WaitTimeoutError,
)


__all__ = [
    '__version__',

    # core
    'Panel',
    'AsyncPanel',
    'Console',
    'AsyncConsole',
    'ConsoleEvent',
    'Server',
    'AdminServer',
    'ServerGroup',
    'Page',

    # server features
    'File',
    'Backup',
    'BackupGroup',
    'Database',
    'DatabaseInstance',
    'InstanceDatabase',
    'InstanceUser',
    'DatabaseExplorer',
    'Schedule',
    'ScheduleStep',
    'Subuser',
    'Allocation',
    'Subdomain',
    'Activity',

    # schedule builders
    'triggers',
    'conditions',
    'actions',
    'backup_selectors',
    'variable',

    # account
    'ApiKey',
    'SshKey',
    'SecurityKey',
    'Session',
    'OAuthLink',
    'CommandSnippet',

    # admin
    'User',
    'Node',
    'Location',
    'Nest',
    'Egg',
    'EggVariable',
    'Mount',
    'Device',
    'Role',
    'Announcement',
    'OAuthProvider',
    'DatabaseHost',
    'DatabaseAgentHost',
    'DatabaseAgentTemplate',
    'BackupConfiguration',
    'BackupPolicy',
    'EggRepository',
    'EggConfiguration',
    'SubdomainDomain',

    # utilities
    'convert',
    'formatBytes',
    'formatDuration',
    'waitForState',
    'waitForOnline',
    'waitForOffline',
    'secsUntil',
    'minsUntil',

    # exceptions
    'CalagoAPIError',
    'BadRequestError',
    'AuthenticationError',
    'PermissionDeniedError',
    'NotFoundError',
    'ConflictError',
    'RateLimitError',
    'ServerError',
    'PanelConnectionError',
    'ConsoleError',
    'InvalidActionError',
    'WaitTimeoutError',

    # extension system
    'extensions',
]
