from calagoapi.schedules.schedule import Schedule
from calagoapi.schedules.builders import conditions as _conditions
from calagoapi.utils.model import idOf


class ScheduleManager:
    '''
    Schedule management for one server, available as `server.schedules`.

    See `calagoapi.triggers`, `calagoapi.conditions` and `calagoapi.actions`
    for building schedules without writing JSON by hand.

    Args:
        server: The server to manage schedules for.

    Example:
        from calagoapi import triggers, actions

        server.schedules.createSchedule(
            'Hourly announcement',
            triggers=[triggers.cron('0 0 * * * *')],
            steps=[actions.sendCommand('say Thanks for playing!')],
        )
    '''
    def __init__(self, server):
        self.server = server
        self.api = server.panel.api.schedules

    @property
    def server_id(self):
        return self.server.server_id

    def _wrap(self, data):
        return Schedule(self.server, data)

    def getSchedules(self, search: str = None, page: int = None, per_page: int = None):
        '''Lists the server's schedules as a Page of Schedule objects.'''
        return self.api.list(self.server_id, search, page, per_page).map(self._wrap)

    def getSchedule(self, schedule_id_or_name: str) -> Schedule:
        '''
        Returns a schedule by UUID or by name.

        Example:
            server.schedules.getSchedule('Nightly restart')
        '''
        for schedule in self.getSchedules():
            if schedule_id_or_name in (schedule.getUUID(), schedule.getName()):
                return schedule
        return None

    def createSchedule(self, name: str, triggers: list = None, condition: dict = None, steps: list = None, enabled: bool = True) -> Schedule:
        '''
        Creates a schedule.

        Args:
            name: Schedule name.
            triggers: List of triggers from `calagoapi.triggers`.
            condition: Condition from `calagoapi.conditions`. Defaults to none.
            steps: List of actions from `calagoapi.actions`, run in order.
            enabled: Whether the schedule is active.

        Returns:
            The new Schedule.
        '''
        condition = condition or _conditions.none()
        if steps:
            return self.importSchedule({
                'name': name,
                'enabled': enabled,
                'triggers': triggers or [],
                'condition': condition,
                'steps': [{'action': action, 'order': order} for order, action in enumerate(steps, start=1)],
            })
        return self._wrap(self.api.create(self.server_id, name, triggers or [], condition, enabled))

    def importSchedule(self, data: dict) -> Schedule:
        '''Imports a schedule exported with `schedule.export()`.'''
        return self._wrap(self.api.importSchedule(self.server_id, data))

    def exportSchedule(self, schedule_id: str) -> dict:
        '''Exports a schedule as a dict.'''
        return self.api.export(self.server_id, idOf(schedule_id))

    def updateSchedule(self, schedule_id: str, name: str = None, enabled: bool = None, triggers: list = None, condition: dict = None) -> None:
        '''Updates a schedule. Only the given fields change.'''
        return self.api.update(self.server_id, idOf(schedule_id), name, enabled, triggers, condition)

    def deleteSchedule(self, schedule_id: str) -> None:
        '''Deletes a schedule.'''
        return self.api.delete(self.server_id, idOf(schedule_id))

    def runSchedule(self, schedule_id: str, skip_condition: bool = False) -> None:
        '''Runs a schedule now.'''
        return self.api.trigger(self.server_id, idOf(schedule_id), skip_condition)

    def abortSchedule(self, schedule_id: str) -> None:
        '''Stops a running schedule.'''
        return self.api.abort(self.server_id, idOf(schedule_id))

    def enableSchedule(self, schedule_id: str) -> None:
        '''Enables a schedule.'''
        return self.api.update(self.server_id, idOf(schedule_id), enabled=True)

    def disableSchedule(self, schedule_id: str) -> None:
        '''Disables a schedule.'''
        return self.api.update(self.server_id, idOf(schedule_id), enabled=False)
