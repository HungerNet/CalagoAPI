'''
calagoapi-server-notes: an example of a packaged extension.

    from calagoapi.extensions import enable

    enable('server_notes', config={'path': 'notes.json'})
    server.notes.add('Upgrade to 1.21.11 on Friday')
    print(server.notes.list())
    print(server.lastNote)
'''
import json
import os
import threading

from calagoapi import GenericServer
from calagoapi.extensions import (
    ConfigurationError,
    Extension,
    ExtensionMetadata,
    class_extension,
    property_extension,
)

_lock = threading.Lock()


def _load(path):
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)


@class_extension(GenericServer, 'notes')
class ServerNotes:
    '''Notes about one server, stored in a local JSON file. Available as `server.notes`.'''
    def __init__(self, server):
        self.server = server

    @property
    def _path(self):
        return ServerNotesExtension.get().config['path']

    def add(self, text: str) -> None:
        '''Adds a note.'''
        with _lock:
            notes = _load(self._path)
            notes.setdefault(self.server.server_id, []).append(text)
            with open(self._path, 'w', encoding='utf-8') as f:
                json.dump(notes, f, indent=2)

    def list(self) -> list:
        '''Returns every note of this server, oldest first.'''
        return _load(self._path).get(self.server.server_id, [])


@property_extension(GenericServer)
def lastNote(self):
    '''The newest note, or None.'''
    # Use the service through the attribute here: services are never moved by the
    # mode, so `self.notes` exists in direct and namespace mode alike.
    notes = self.notes.list()
    return notes[-1] if notes else None


class ServerNotesExtension(Extension):
    extension_id = 'server_notes'
    metadata = ExtensionMetadata(
        author='you',
        version='1.0.0',
        schema=1,
        description='Keep notes on servers',
        package='calagoapi-server-notes',
    )
    default_mode = 'direct'
    default_config = {'path': 'calagoapi-notes.json'}

    def validate_config(self, config):
        if not str(config['path']).endswith('.json'):
            raise ConfigurationError('server_notes: path must be a .json file')
        return config
