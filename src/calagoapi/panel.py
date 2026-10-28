import inspect

from calagoapi.api import API, Client
from calagoapi.servers import ServerManager
from calagoapi.account import Account, Auth
from calagoapi.admin import Admin
from calagoapi.utils.exceptions import CalagoAPIError, PanelConnectionError, ServerError


class Panel:
    '''
    A connection to a Calagopus panel. This is the entry point of CalagoAPI.

    Args:
        url: Panel URL, e.g. "https://panel.example.com".
        api_key: API key from Account -> API Keys.
        name: Optional label, handy when managing several panels.
        timeout: Request timeout in seconds.
        verify: Verify TLS certificates. Set to False for self-signed panels.
        max_retries: How often rate limited (429) requests, and GET requests that hit
            a connection error or 502/503/504, are retried. 0 disables retries.

    Attributes:
        servers: ServerManager, the servers the API key can access.
        account: Account, the user that owns the API key.
        admin: Admin, panel administration (requires admin permissions).
        auth: Auth, public login/registration endpoints.
        api: Internal API modules, for calls not wrapped by CalagoAPI.

    Example:
        from calagoapi import Panel

        panel = Panel(
            url='https://panel.example.com',
            api_key='...'
        )

        server = panel.servers.getServer('abc123')
        server.sendCommand('say Hello')
        server.restart()

        # or close the connections automatically
        with Panel(url='https://panel.example.com', api_key='...') as panel:
            print(panel.servers.getServers())
    '''
    def __init__(self, url: str, api_key: str, name: str = None, timeout: int = 10, verify: bool = True,
                 max_retries: int = 3):
        self.name = name or url
        self.url = url.rstrip('/')
        self.api_key = api_key

        # internal API layer
        self.client = Client(self.url, api_key, timeout=timeout, verify=verify, user_agent='CalagoAPI', max_retries=max_retries)
        self.api = API(self.client)

        # open live consoles, closed by close()
        self.consoles = set()

        # high-level managers
        self.servers = ServerManager(self)
        self.account = Account(self)
        self.admin = Admin(self)
        self.auth = Auth(self)

    def __repr__(self):
        return f'<Panel {self.name!r}>'

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def close(self) -> None:
        '''
        Closes the pooled HTTP connections and any open console connection.

        Called automatically when the Panel is used in a `with` block.
        '''
        for console in list(self.consoles):
            # async consoles are closed by AsyncPanel.close()
            if not inspect.iscoroutinefunction(console.close):
                console.close()
        self.client.close()

    def __str__(self):
        hidden = f'{self.api_key[:6]}...' if self.api_key else None
        return f'Panel name: {self.name}\nURL: {self.url}\nAPI key: {hidden}'

    # http core
    def get(self, path: str, params: dict = None):
        '''
        Sends a raw GET request and returns the decoded response.

        Example:
            panel.get('/api/client/permissions')
        '''
        return self.client.get(path, params=params)

    def post(self, path: str, json: dict = None, params: dict = None):
        '''Sends a raw POST request and returns the decoded response.'''
        return self.client.post(path, json=json, params=params)

    def put(self, path: str, json: dict = None, params: dict = None):
        '''Sends a raw PUT request and returns the decoded response.'''
        return self.client.put(path, json=json, params=params)

    def patch(self, path: str, json: dict = None, params: dict = None):
        '''Sends a raw PATCH request and returns the decoded response.'''
        return self.client.patch(path, json=json, params=params)

    def delete(self, path: str, json: dict = None, params: dict = None):
        '''Sends a raw DELETE request and returns the decoded response.'''
        return self.client.delete(path, json=json, params=params)

    # panel health
    def ping(self) -> bool:
        '''
        Returns True if the panel answers, without checking the API key.

        Example:
            if not panel.ping():
                print('Panel is down')
        '''
        try:
            self.client.request('GET', '/api/auth/oauth', raw=True)
            return True
        except (PanelConnectionError, ServerError):
            return False
        except CalagoAPIError:
            # any other HTTP error still means the panel answered
            return True

    def validateAPI(self) -> bool:
        '''Returns True if the API key is valid.'''
        try:
            self.api.account.get()
            return True
        except CalagoAPIError:
            return False

    def isAdmin(self) -> bool:
        '''Returns True if the API key belongs to a root administrator.'''
        return self.account.isAdmin()

    # public panel information
    def getSettings(self) -> dict:
        '''
        Returns the public panel settings (app name, captcha, enabled features, server time, ...).

        Example:
            print(panel.getSettings()['app']['name'])
        '''
        return self.api.public.settings()

    def getLanguages(self) -> list:
        '''Returns the languages the panel is translated into.'''
        return self.api.public.languages()

    def getAnnouncements(self) -> list:
        '''Returns the announcements currently shown to everyone.'''
        return self.api.public.announcements()
