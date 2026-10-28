import math


def idOf(value):
    '''
    Returns the id of an object, or the value itself if it already is an id.

    Lets every method accept either an object or its UUID.

    Example:
        idOf(server)  # 'abc123...'
        idOf('abc123')  # 'abc123'
    '''
    if isinstance(value, Model):
        return getattr(value, 'server_id', None) or value.getUUID()
    return value


class Model:
    '''
    Base class for every object returned by the panel.

    Wraps the raw JSON returned by Calagopus and exposes it through getters.
    The raw data is always available through `.data`, `get()` or `toDict()`,
    so nothing the panel returns is ever hidden.

    Args:
        panel: The `Panel` this object belongs to.
        data: Raw data returned by the panel.

    Example:
        backup = server.getBackup('...')
        backup.getName()         # getter
        backup.get('checksum')   # raw access
        backup['bytes']          # raw access
        backup.toDict()          # copy of all data
    '''
    def __init__(self, panel, data: dict = None):
        self.panel = panel
        self.data = data or {}

    def __getitem__(self, key):
        return self.data[key]

    def __contains__(self, key):
        return key in self.data

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.getUUID() is not None and self.getUUID() == other.getUUID()

    def __hash__(self):
        return hash((self.__class__.__name__, self.getUUID()))

    def __repr__(self):
        label = self.data.get('name') or self.data.get('username') or self.getUUID()
        return f'<{self.__class__.__name__} {label!r}>'

    def get(self, key: str, default=None):
        '''
        Returns a raw field from the panel data.

        Args:
            key: Field name as returned by Calagopus.
            default: Value returned when the field is missing.

        Example:
            server.get('sftp_port')
        '''
        return self.data.get(key, default)

    def toDict(self) -> dict:
        '''Returns a copy of the raw panel data.'''
        return dict(self.data)

    def getUUID(self) -> str:
        '''Returns the object's UUID.'''
        return self.data.get('uuid')

    def getCreated(self) -> str:
        '''Returns when the object was created, as an ISO-8601 string.'''
        return self.data.get('created')

    def _update(self, data: dict):
        # merge local changes after a successful PATCH
        self.data.update({k: v for k, v in data.items() if v is not None})
        return self


class Page(list):
    '''
    A list of results, plus pagination info from the panel.

    Behaves exactly like a normal list, so you can loop over it, index it and
    call `len()` on it.

    Attributes:
        total: Total number of results on the panel (across all pages).
        page: The page number this list represents.
        per_page: Page size used for the request.

    Example:
        servers = panel.servers.getServers(page=1, per_page=25)
        print(f'Showing {len(servers)} of {servers.getTotal()}')
        if servers.hasNextPage():
            more = panel.servers.getServers(page=2, per_page=25)
    '''
    def __init__(self, items=None, total=None, page=1, per_page=None):
        super().__init__(items or [])
        self.total = len(self) if total is None else total
        self.page = page
        self.per_page = per_page or len(self)

    def __repr__(self):
        return f'<Page {self.page}/{self.getPageCount()} items={len(self)} total={self.total}>'

    def getTotal(self) -> int:
        '''Returns the total number of results across every page.'''
        return self.total

    def getPage(self) -> int:
        '''Returns the current page number.'''
        return self.page

    def getPerPage(self) -> int:
        '''Returns the page size.'''
        return self.per_page

    def getPageCount(self) -> int:
        '''Returns how many pages exist in total.'''
        if not self.per_page:
            return 1
        return max(1, math.ceil(self.total / self.per_page))

    def hasNextPage(self) -> bool:
        '''Returns True if there are more results after this page.'''
        return self.page < self.getPageCount()

    def map(self, func) -> 'Page':
        '''Returns a new Page with `func` applied to every item, keeping the pagination info.'''
        return Page([func(item) for item in self], self.total, self.page, self.per_page)
