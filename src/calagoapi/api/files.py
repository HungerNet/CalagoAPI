import requests

from calagoapi.utils.model import Page
from calagoapi.utils.exceptions import PanelConnectionError


# Internal Calagopus FilesAPI
class FilesAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, action):
        return f'/api/client/servers/{server_id}/files/{action}'

    # browsing
    def list(self, server_id, directory='/', sort=None, page=None, per_page=None):
        params = {'directory': directory, 'sort': sort}
        if page is not None:
            params.update(page=page, per_page=per_page or 100)
            result = self.client.get(self._path(server_id, 'list'), params=params)
            entries = result['entries']
            return result, Page(entries['data'], entries['total'], entries['page'], entries['per_page'])

        items = []
        current = 1
        while True:
            params.update(page=current, per_page=per_page or 500)
            result = self.client.get(self._path(server_id, 'list'), params=params)
            entries = result['entries']
            items.extend(entries['data'])
            if not entries['data'] or len(items) >= entries['total']:
                return result, Page(items, entries['total'], 1, len(items))
            current += 1

    def stat(self, server_id, files, root='/'):
        return self.client.post(self._path(server_id, 'stat'), json={'root': root, 'files': files})['entries']

    def search(self, server_id, root='/', path_filter=None, size_filter=None, content_filter=None, match_context=None):
        return self.client.post(self._path(server_id, 'search'), json={
            'root': root,
            'path_filter': path_filter,
            'size_filter': size_filter,
            'content_filter': content_filter,
            'match_context': match_context,
        })

    def directorySizes(self, server_id, directory='/', depth=None):
        return self.client.get(
            self._path(server_id, 'directory-sizes'),
            params={'directory': directory, 'depth': depth}
        )['directory_sizes']

    def largestDirectories(self, server_id, directory='/'):
        return self.client.get(
            self._path(server_id, 'largest-directories'),
            params={'directory': directory}
        )['largest_directories']

    def fingerprint(self, server_id, file, algorithm=None):
        return self.client.get(
            self._path(server_id, 'fingerprint'),
            params={'file': file, 'algorithm': algorithm}
        )['fingerprint']

    # reading and writing
    def contents(self, server_id, file):
        return self.client.get(self._path(server_id, 'contents'), params={'file': file})

    def lines(self, server_id, file, start_line=None, end_line=None):
        return self.client.get(
            self._path(server_id, 'lines'),
            params={'file': file, 'start_line': start_line, 'end_line': end_line}
        )

    def write(self, server_id, file, content):
        return self.client.postText(self._path(server_id, 'write'), content, params={'file': file})

    def revisions(self, server_id, file):
        return self.client.get(self._path(server_id, 'revisions'), params={'file': file})['revisions']

    def revision(self, server_id, file, revision_id):
        return self.client.get(self._path(server_id, f'revisions/{revision_id}'), params={'file': file})

    # transfer
    def downloadUrl(self, server_id, files=None, root='/', directory=None, archive_format=None):
        params = {'root': root, 'directory': directory, 'archive_format': archive_format}
        if files is not None:
            params['files'] = files
        return self.client.get(self._path(server_id, 'download'), params=params)['url']

    def uploadUrl(self, server_id):
        return self.client.get(self._path(server_id, 'upload'))['url']

    def upload(self, server_id, directory, files):
        '''`files` is a list of (name, data) tuples'''
        url = self.uploadUrl(server_id)
        payload = [('files', (name, data)) for name, data in files]
        try:
            r = requests.post(
                url,
                params={'directory': directory},
                files=payload,
                verify=self.client.session.verify,
                timeout=max(self.client.timeout, 300),
            )
        except requests.RequestException as e:
            raise PanelConnectionError(f'Upload failed: {e}') from e
        if r.status_code >= 400:
            self.client.raiseError(r)
        return self.client.parse(r)

    def fetch(self, url, stream=False):
        '''Downloads a signed URL returned by the panel'''
        try:
            r = requests.get(url, verify=self.client.session.verify, timeout=max(self.client.timeout, 300), stream=stream)
        except requests.RequestException as e:
            raise PanelConnectionError(f'Download failed: {e}') from e
        if r.status_code >= 400:
            self.client.raiseError(r)
        return r

    def pull(self, server_id, url, root='/', name=None, use_header=None, foreground=None):
        return self.client.post(self._path(server_id, 'pull'), json={
            'url': url,
            'root': root,
            'name': name,
            'use_header': use_header,
            'foreground': foreground,
        })

    def queryPull(self, server_id, url):
        return self.client.post(self._path(server_id, 'pull/query'), json={'url': url})['query_result']

    # management
    def delete(self, server_id, root, files):
        return self.client.post(self._path(server_id, 'delete'), json={'root': root, 'files': files})

    def rename(self, server_id, root, files):
        '''`files` is a list of {'from': ..., 'to': ...}'''
        return self.client.put(self._path(server_id, 'rename'), json={'root': root, 'files': files})

    def copy(self, server_id, path, destination=None, overwrite=None, foreground=None):
        return self.client.post(self._path(server_id, 'copy'), json={
            'path': path,
            'destination': destination,
            'overwrite': overwrite,
            'foreground': foreground,
        })

    def copyMany(self, server_id, root, files, overwrite=None, foreground=None):
        return self.client.post(self._path(server_id, 'copy-many'), json={
            'root': root,
            'files': files,
            'overwrite': overwrite,
            'foreground': foreground,
        })

    def copyRemote(self, server_id, root, files, destination, destination_server, foreground=None):
        return self.client.post(self._path(server_id, 'copy-remote'), json={
            'root': root,
            'files': files,
            'destination': destination,
            'destination_server': destination_server,
            'foreground': foreground,
        })

    def copyRemoteMany(self, server_id, root, files, destination, destination_servers):
        return self.client.post(self._path(server_id, 'copy-remote-many'), json={
            'root': root,
            'files': files,
            'destination': destination,
            'destination_servers': destination_servers,
        })['results']

    def createDirectory(self, server_id, root, name):
        return self.client.post(self._path(server_id, 'create-directory'), json={'root': root, 'name': name})

    def createSymlink(self, server_id, root, link, target):
        return self.client.post(self._path(server_id, 'create-symlink'), json={'root': root, 'link': link, 'target': target})

    def compress(self, server_id, root, files, format='tar_gz', name=None, foreground=None):
        return self.client.post(self._path(server_id, 'compress'), json={
            'root': root,
            'files': files,
            'format': format,
            'name': name,
            'foreground': foreground,
        })

    def decompress(self, server_id, root, file, foreground=None):
        return self.client.post(self._path(server_id, 'decompress'), json={
            'root': root,
            'file': file,
            'foreground': foreground,
        })

    def chmod(self, server_id, root, files):
        '''`files` is a list of {'file': ..., 'mode': ..., 'recursive': ...}'''
        return self.client.put(self._path(server_id, 'chmod'), json={'root': root, 'files': files})

    def sqliteQuery(self, server_id, file, query, rows=None, read_only=None):
        return self.client.post(self._path(server_id, 'sqlite-query'), json={
            'file': file,
            'query': query,
            'rows': rows,
            'read_only': read_only,
        })['results']

    def cancelOperation(self, server_id, operation_id):
        return self.client.delete(self._path(server_id, f'operations/{operation_id}'))
