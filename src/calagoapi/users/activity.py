from calagoapi.utils.model import Model


class Activity(Model):
    '''
    One entry of an activity log (server, account or panel-wide).

    Example:
        for entry in server.getActivity(page=1, per_page=10):
            print(entry.getCreated(), entry.getUsername(), entry.getEvent())
    '''
    def __repr__(self):
        return f'<Activity {self.getEvent()!r} by {self.getUsername()!r}>'

    def getEvent(self) -> str:
        '''Returns the event name, e.g. "server:power.start".'''
        return self.data.get('event')

    def getUser(self) -> dict:
        '''Returns the user who caused the event, or None for system events.'''
        return self.data.get('user')

    def getUsername(self) -> str:
        '''Returns the username who caused the event, or None.'''
        return (self.data.get('user') or {}).get('username')

    def getImpersonator(self) -> dict:
        '''Returns the admin who acted on behalf of the user, if any.'''
        return self.data.get('impersonator')

    def getIP(self) -> str:
        '''Returns the IP address the event came from.'''
        return self.data.get('ip')

    def getData(self) -> dict:
        '''Returns event specific details.'''
        return self.data.get('data')

    def isApi(self) -> bool:
        '''Returns True if the event was caused through the API.'''
        return bool(self.data.get('is_api'))

    def isSchedule(self) -> bool:
        '''Returns True if the event was caused by a schedule.'''
        return bool(self.data.get('is_schedule'))
