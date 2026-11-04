'''Tests for helpers that do not need the fake panel.'''
import pytest

from calagoapi import Page, convert, formatBytes, formatDuration, triggers, actions, variable
from calagoapi.api.client import clean, segment
from calagoapi.api.files import FilesAPI
from calagoapi.files import splitPath, joinPath
from calagoapi.utils.model import Model, idOf


def test_page():
    page = Page([1, 2], total=5, page=1, per_page=2)
    assert len(page) == 2 and page.getPageCount() == 3 and page.hasNextPage()
    doubled = page.map(lambda x: x * 2)
    assert list(doubled) == [2, 4] and doubled.getTotal() == 5


def test_id_of():
    assert idOf('abc') == 'abc'
    assert idOf(Model(None, {'uuid': 'u1'})) == 'u1'
    assert idOf(None) is None


def test_clean_drops_none():
    assert clean({'a': 1, 'b': None, 'c': False}) == {'a': 1, 'c': False}


def test_segment_encodes_slashes():
    assert segment('logs/wings.log') == 'logs%2Fwings.log'


def test_file_list_uses_api_page_limit():
    class Client:
        def __init__(self):
            self.calls = []

        def get(self, path, params):
            self.calls.append(params.copy())
            start = (params['page'] - 1) * params['per_page']
            data = list(range(start, min(start + params['per_page'], 101)))
            return {'entries': {
                'data': data,
                'total': 101,
                'page': params['page'],
                'per_page': params['per_page'],
            }}

    client = Client()
    _, entries = FilesAPI(client).list('server-id')

    assert len(entries) == 101
    assert [call['per_page'] for call in client.calls] == [100, 100]


def test_paths():
    assert splitPath('/plugins/config.yml') == ('/plugins', 'config.yml')
    assert splitPath('server.jar') == ('/', 'server.jar')
    assert joinPath('/plugins/', 'a.jar') == '/plugins/a.jar'


def test_convert():
    assert convert.byte(2048, 'mib', 'gib') == 2.0
    assert convert.time(90_000, 'ms', 'min') == 1.5
    assert formatBytes(1536) == '1.5 KiB'
    assert formatDuration(3_900_000) == '1h 5m'
    with pytest.raises(ValueError):
        convert.byte(1, 'b', 'parsecs')


def test_builders_accept_variable_names():
    assert triggers.consoleLine('x', output_into='line')['output_into'] == {'variable': 'line'}
    assert triggers.consoleLine('x', output_into=variable('line'))['output_into'] == {'variable': 'line'}
    assert actions.matchRegex('a', '(.)', ['x', None])['output_into'] == [{'variable': 'x'}, None]
    assert actions.renameFiles('/', [('a', 'b')])['files'] == [{'from': 'a', 'to': 'b'}]
