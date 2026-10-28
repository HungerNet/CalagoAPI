from calagoapi.utils.model import Model, idOf


class AdminResource(Model):
    '''
    Base class for objects managed through the admin API.

    Every admin object supports `refresh()`, `update(**fields)` and `delete()`.
    Objects Calagopus can copy also have `duplicate()`. The accepted fields
    of `update()` are the fields Calagopus returns for the object.

    Args:
        panel: The Panel.
        data: Raw data from Calagopus.
        resource: Internal API collection, only needed for nested objects (eggs, variables).
    '''
    collection = None

    def __init__(self, panel, data: dict = None, resource=None):
        super().__init__(panel, data)
        self.resource = resource

    def _api(self):
        return self.resource or getattr(self.panel.api.admin, self.collection)

    def getName(self) -> str:
        '''Returns the name.'''
        return self.data.get('name')

    def getDescription(self) -> str:
        '''Returns the description.'''
        return self.data.get('description')

    def refresh(self):
        '''Re-fetches the object from the panel.'''
        self.data = self._api().get(self.getUUID())
        return self

    def update(self, **fields):
        '''
        Updates the object. Only the given fields change.

        Example:
            location.update(name='Frankfurt', description='DE-1')
        '''
        self._api().update(self.getUUID(), **fields)
        return self._update(fields)

    def rename(self, name: str):
        '''Renames the object.'''
        return self.update(name=name)

    def setName(self, name: str):
        '''Alias of rename().'''
        return self.update(name=name)

    def setDescription(self, description: str):
        '''Changes the description.'''
        return self.update(description=description)

    def _duplicate(self, **fields):
        # only exposed as duplicate() by objects whose collection supports it
        return self.__class__(self.panel, self._api().duplicate(self.getUUID(), **fields), self.resource)

    def delete(self, **options) -> None:
        '''Deletes the object.'''
        return self._api().delete(self.getUUID(), **options)


class AdminManager:
    '''Base class for admin managers like `panel.admin.locations`.'''
    model = AdminResource

    def __init__(self, panel, resource=None):
        self.panel = panel
        self.admin = panel.api.admin
        # nested collections (eggs of a nest, ...) pass their own resource
        self.resource = resource
        self.api = resource or getattr(panel.api.admin, self.model.collection)

    def _wrap(self, data):
        return self.model(self.panel, data, self.resource)

    def _list(self, search=None, page=None, per_page=None, **params):
        return self.api.list(search, page, per_page, **params).map(self._wrap)

    def _get(self, resource_id):
        return self._wrap(self.api.get(idOf(resource_id)))

    def _find(self, name):
        for item in self._list(search=name):
            if name in (item.getUUID(), item.getName()):
                return item
        return None

    def _create(self, **fields):
        return self._wrap(self.api.create(**fields))

    def _delete(self, resource_id, **options):
        return self.api.delete(idOf(resource_id), **options)
