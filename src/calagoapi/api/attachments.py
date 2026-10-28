# Internal Calagopus AttachmentsAPI (server mounts and devices)
class AttachmentsAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, suffix=''):
        return f'/api/client/servers/{server_id}{suffix}'

    # mounts
    def mounts(self, server_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, '/mounts'), 'mounts', {'search': search}, page, per_page)

    def attachMount(self, server_id, mount_uuid):
        return self.client.post(self._path(server_id, '/mounts'), json={'mount_uuid': mount_uuid})

    def detachMount(self, server_id, mount_uuid):
        return self.client.delete(self._path(server_id, f'/mounts/{mount_uuid}'))

    # devices
    def devices(self, server_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id, '/devices'), 'devices', {'search': search}, page, per_page)

    def attachDevice(self, server_id, device_uuid):
        return self.client.post(self._path(server_id, '/devices'), json={'device_uuid': device_uuid})

    def detachDevice(self, server_id, device_uuid):
        return self.client.delete(self._path(server_id, f'/devices/{device_uuid}'))
