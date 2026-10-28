# CalagoAPI exceptions
class CalagoAPIError(Exception):
    '''
    Base class for every error raised by CalagoAPI.

    Catch this to handle any panel error in one place.

    Attributes:
        message: Human readable error message.
        status_code: HTTP status code returned by the panel, or None if the request never completed.
        errors: List of error strings returned by Calagopus (its `errors` array).
        response: The raw `requests.Response`, or None.

    Example:
        from calagoapi import Panel, CalagoAPIError

        try:
            panel.servers.getServer('does-not-exist')
        except CalagoAPIError as e:
            print(e.status_code, e.errors)
    '''
    def __init__(self, message, status_code=None, errors=None, response=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.errors = errors or []
        self.response = response


# HTTP errors
class BadRequestError(CalagoAPIError):
    '''The panel rejected the request (HTTP 400). Usually invalid parameters.'''

class AuthenticationError(CalagoAPIError):
    '''The API key is missing, invalid or expired (HTTP 401).'''

class PermissionDeniedError(CalagoAPIError):
    '''The API key is valid but lacks permission for this action (HTTP 403).'''

class NotFoundError(CalagoAPIError):
    '''The requested resource does not exist (HTTP 404).'''

class ConflictError(CalagoAPIError):
    '''The request conflicts with the current state, e.g. a server that is still installing (HTTP 409).'''

class RateLimitError(CalagoAPIError):
    '''
    Too many requests (HTTP 429).

    Attributes:
        retry_after: Seconds to wait before retrying, if the panel sent a Retry-After header.
    '''
    def __init__(self, message, status_code=None, errors=None, response=None, retry_after=None):
        super().__init__(message, status_code, errors, response)
        self.retry_after = retry_after

class ServerError(CalagoAPIError):
    '''The panel failed to handle the request (HTTP 5xx).'''

class PanelConnectionError(CalagoAPIError):
    '''The panel could not be reached (DNS failure, refused connection, timeout, ...).'''

class ConsoleError(CalagoAPIError):
    '''The live console websocket could not connect, authenticate or send a message.'''


# Usage errors
class InvalidActionError(CalagoAPIError, ValueError):
    '''An invalid value was passed to a method, e.g. an unknown power action.'''

class WaitTimeoutError(CalagoAPIError, TimeoutError):
    '''A wait helper gave up before the expected state was reached.'''
