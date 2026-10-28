from calagoapi.utils.model import Model, idOf


class Schedule(Model):
    '''
    A server schedule.

    Args:
        server: The owning server.
        data: Raw schedule data from Calagopus.

    Example:
        schedule = server.schedules.getSchedule('Nightly restart')
        if not schedule.isEnabled():
            schedule.enable()
        schedule.run()
        print(schedule.getStatus())
    '''
    def __init__(self, server, data: dict):
        super().__init__(server.panel, data)
        self.server = server

    @property
    def schedule_id(self):
        return self.getUUID()

    def _api(self):
        return self.panel.api.schedules

    # getters
    def getName(self) -> str:
        '''Returns the schedule name.'''
        return self.data.get('name')

    def getTriggers(self) -> list:
        '''Returns the triggers that start this schedule.'''
        return self.data.get('triggers', [])

    def getCondition(self) -> dict:
        '''Returns the condition checked before running.'''
        return self.data.get('condition')

    def getLastRun(self) -> str:
        '''Returns when the schedule last ran, or None.'''
        return self.data.get('last_run')

    def getLastFailure(self) -> str:
        '''Returns when the schedule last failed, or None.'''
        return self.data.get('last_failure')

    def getStatus(self) -> dict:
        '''
        Returns the live run status.

        Returns:
            dict with `running` (bool), `step` (current step UUID) and `errors` (step UUID -> message).
        '''
        return self._api().status(self.server.server_id, self.schedule_id)

    # state checks
    def isEnabled(self) -> bool:
        '''Returns True if the schedule is enabled.'''
        return bool(self.data.get('enabled'))

    def isRunning(self) -> bool:
        '''Returns True if the schedule is currently executing.'''
        return bool(self.getStatus().get('running'))

    # actions
    def refresh(self) -> 'Schedule':
        '''Re-fetches the schedule from the panel.'''
        self.data = self._api().get(self.server.server_id, self.schedule_id)
        return self

    def update(self, name: str = None, enabled: bool = None, triggers: list = None, condition: dict = None) -> 'Schedule':
        '''
        Updates the schedule. Only the given fields change.

        Example:
            schedule.update(triggers=[triggers.cron('0 0 6 * * *')])
        '''
        self._api().update(self.server.server_id, self.schedule_id, name, enabled, triggers, condition)
        return self._update({'name': name, 'enabled': enabled, 'triggers': triggers, 'condition': condition})

    def rename(self, name: str) -> 'Schedule':
        '''Renames the schedule.'''
        return self.update(name=name)

    def setName(self, name: str) -> 'Schedule':
        '''Alias of rename().'''
        return self.update(name=name)

    def enable(self) -> 'Schedule':
        '''Enables the schedule.'''
        return self.update(enabled=True)

    def disable(self) -> 'Schedule':
        '''Disables the schedule.'''
        return self.update(enabled=False)

    def run(self, skip_condition: bool = False) -> None:
        '''
        Runs the schedule now.

        Args:
            skip_condition: Run even if the schedule's condition does not match.
        '''
        return self._api().trigger(self.server.server_id, self.schedule_id, skip_condition)

    def abort(self) -> None:
        '''Stops the schedule if it is currently running.'''
        return self._api().abort(self.server.server_id, self.schedule_id)

    def duplicate(self, name: str) -> 'Schedule':
        '''Copies the schedule, including its steps, under a new name.'''
        return Schedule(self.server, self._api().duplicate(self.server.server_id, self.schedule_id, name))

    def export(self) -> dict:
        '''
        Exports the schedule as a dict that can be imported on any server.

        Example:
            data = schedule.export()
            other_server.schedules.importSchedule(data)
        '''
        return self._api().export(self.server.server_id, self.schedule_id)

    def delete(self) -> None:
        '''Deletes the schedule.'''
        return self._api().delete(self.server.server_id, self.schedule_id)

    # steps
    def getSteps(self) -> list:
        '''Returns the steps in execution order.'''
        steps = self._api().steps(self.server.server_id, self.schedule_id)
        return sorted([ScheduleStep(self, data) for data in steps], key=lambda s: s.getOrder())

    def addStep(self, action: dict, order: int = None) -> 'ScheduleStep':
        '''
        Adds a step.

        Args:
            action: An action from `calagoapi.actions`.
            order: Position. Defaults to the end.

        Example:
            schedule.addStep(actions.sendCommand('say Hello'))
        '''
        if order is None:
            order = max([s.getOrder() for s in self.getSteps()], default=0) + 1
        return ScheduleStep(self, self._api().createStep(self.server.server_id, self.schedule_id, action, order))

    def setSteps(self, actions: list) -> list:
        '''Replaces every step with the given actions, in order.'''
        for step in self.getSteps():
            step.delete()
        return [self.addStep(action, order) for order, action in enumerate(actions, start=1)]

    def orderSteps(self, steps: list) -> None:
        '''Reorders steps. `steps` is a list of ScheduleStep objects or UUIDs.'''
        return self._api().orderSteps(self.server.server_id, self.schedule_id, [idOf(s) for s in steps])


class ScheduleStep(Model):
    '''
    One step (action) of a schedule.

    Example:
        for step in schedule.getSteps():
            print(step.getOrder(), step.getActionType())
    '''
    def __init__(self, schedule: Schedule, data: dict):
        super().__init__(schedule.panel, data)
        self.schedule = schedule
        self.server = schedule.server

    def _args(self):
        return self.server.server_id, self.schedule.schedule_id, self.getUUID()

    def __repr__(self):
        return f'<ScheduleStep {self.getOrder()} {self.getActionType()!r}>'

    def getAction(self) -> dict:
        '''Returns the action dict.'''
        return self.data.get('action', {})

    def getActionType(self) -> str:
        '''Returns the action type, e.g. "send_command".'''
        return self.getAction().get('type')

    def getOrder(self) -> int:
        '''Returns the position of the step.'''
        return self.data.get('order', 0)

    def getError(self) -> str:
        '''Returns the error from the last run of this step, or None.'''
        return self.data.get('error')

    def hasError(self) -> bool:
        '''Returns True if the step failed on its last run.'''
        return bool(self.data.get('error'))

    def update(self, action: dict = None, order: int = None) -> 'ScheduleStep':
        '''Changes the action and/or position of the step.'''
        self.panel.api.schedules.updateStep(*self._args(), action, order)
        return self._update({'action': action, 'order': order})

    def duplicate(self) -> 'ScheduleStep':
        '''Copies the step.'''
        return ScheduleStep(self.schedule, self.panel.api.schedules.duplicateStep(*self._args()))

    def delete(self) -> None:
        '''Deletes the step.'''
        return self.panel.api.schedules.deleteStep(*self._args())
