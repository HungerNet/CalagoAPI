from .client import Client
from .servers import ServersAPI
from .files import FilesAPI
from .backups import BackupsAPI
from .databases import DatabasesAPI
from .schedules import SchedulesAPI
from .network import NetworkAPI
from .users import UsersAPI
from .attachments import AttachmentsAPI
from .versions import VersionsAPI
from .account import AccountAPI
from .auth import AuthAPI
from .public import PublicAPI
from .admin import AdminAPI, ResourceAPI


class API:
    '''
    Bundle of every internal API module, available as `panel.api`.

    These modules are the only place CalagoAPI talks HTTP. You normally
    never need them, but they are handy for calls the high-level objects
    do not wrap yet.

    Example:
        panel.api.servers.resources(server_id)
        panel.api.client.get('/api/client/permissions')
    '''
    def __init__(self, client: Client):
        self.client = client
        self.servers = ServersAPI(client)
        self.files = FilesAPI(client)
        self.backups = BackupsAPI(client)
        self.databases = DatabasesAPI(client)
        self.schedules = SchedulesAPI(client)
        self.network = NetworkAPI(client)
        self.users = UsersAPI(client)
        self.attachments = AttachmentsAPI(client)
        self.versions = VersionsAPI(client)
        self.account = AccountAPI(client)
        self.auth = AuthAPI(client)
        self.public = PublicAPI(client)
        self.admin = AdminAPI(client)


__all__ = [
    'API',
    'Client',
    'ServersAPI',
    'FilesAPI',
    'BackupsAPI',
    'DatabasesAPI',
    'SchedulesAPI',
    'NetworkAPI',
    'UsersAPI',
    'AttachmentsAPI',
    'VersionsAPI',
    'AccountAPI',
    'AuthAPI',
    'PublicAPI',
    'AdminAPI',
    'ResourceAPI',
]
