# Internal Calagopus SchedulesAPI
class SchedulesAPI:
    def __init__(self, client):
        self.client = client

    def _path(self, server_id, suffix=''):
        return f'/api/client/servers/{server_id}/schedules{suffix}'

    # schedules
    def list(self, server_id, search=None, page=None, per_page=None):
        return self.client.list(self._path(server_id), 'schedules', {'search': search}, page, per_page)

    def get(self, server_id, schedule_id):
        return self.client.get(self._path(server_id, f'/{schedule_id}'))['schedule']

    def create(self, server_id, name, triggers, condition, enabled=True):
        return self.client.post(self._path(server_id), json={
            'name': name,
            'enabled': enabled,
            'triggers': triggers,
            'condition': condition,
        })['schedule']

    def update(self, server_id, schedule_id, name=None, enabled=None, triggers=None, condition=None):
        return self.client.patch(self._path(server_id, f'/{schedule_id}'), json={
            'name': name,
            'enabled': enabled,
            'triggers': triggers,
            'condition': condition,
        })

    def delete(self, server_id, schedule_id):
        return self.client.delete(self._path(server_id, f'/{schedule_id}'))

    def duplicate(self, server_id, schedule_id, name):
        return self.client.post(self._path(server_id, f'/{schedule_id}/duplicate'), json={'name': name})['schedule']

    def trigger(self, server_id, schedule_id, skip_condition=None):
        return self.client.post(self._path(server_id, f'/{schedule_id}/trigger'), json={'skip_condition': skip_condition})

    def abort(self, server_id, schedule_id):
        return self.client.post(self._path(server_id, f'/{schedule_id}/abort'))

    def status(self, server_id, schedule_id):
        return self.client.get(self._path(server_id, f'/{schedule_id}/status'))['status']

    def export(self, server_id, schedule_id):
        return self.client.get(self._path(server_id, f'/{schedule_id}/export'))

    def importSchedule(self, server_id, data):
        return self.client.post(self._path(server_id, '/import'), json=data)['schedule']

    # steps
    def steps(self, server_id, schedule_id):
        return self.client.get(self._path(server_id, f'/{schedule_id}/steps'))['schedule_steps']

    def createStep(self, server_id, schedule_id, action, order):
        return self.client.post(
            self._path(server_id, f'/{schedule_id}/steps'),
            json={'action': action, 'order': order}
        )['schedule_step']

    def updateStep(self, server_id, schedule_id, step_id, action=None, order=None):
        return self.client.patch(
            self._path(server_id, f'/{schedule_id}/steps/{step_id}'),
            json={'action': action, 'order': order}
        )

    def deleteStep(self, server_id, schedule_id, step_id):
        return self.client.delete(self._path(server_id, f'/{schedule_id}/steps/{step_id}'))

    def duplicateStep(self, server_id, schedule_id, step_id):
        return self.client.post(self._path(server_id, f'/{schedule_id}/steps/{step_id}/duplicate'))['schedule_step']

    def orderSteps(self, server_id, schedule_id, step_order):
        return self.client.put(
            self._path(server_id, f'/{schedule_id}/steps/order'),
            json={'schedule_step_order': step_order}
        )
