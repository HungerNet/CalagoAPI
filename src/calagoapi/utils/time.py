import time
from datetime import datetime


def waitForState(server, state: str, timeout: int = 60, interval: int = 2) -> bool:
    '''
    Blocks until the server reaches a power state.

    Args:
        server: A server object.
        state: One of 'running', 'offline', 'starting', 'stopping'.
        timeout: Maximum seconds to wait.
        interval: Seconds between checks.

    Returns:
        True if the state was reached, False if the timeout expired.

    Example:
        server.start()
        waitForState(server, 'running', timeout=120)
    '''
    deadline = time.monotonic() + timeout
    while True:
        if server.getPowerState() == state:
            return True
        if time.monotonic() >= deadline:
            return False
        time.sleep(interval)


def waitForOnline(server, timeout: int = 60, interval: int = 2) -> bool:
    '''
    Pauses the script until the server is online.

    Returns:
        True once the server is running, False if the timeout expired.

    Example:
        server.restart()
        if waitForOnline(server, timeout=180):
            server.sendCommand('say Back online!')
    '''
    return waitForState(server, 'running', timeout, interval)


def waitForOffline(server, timeout: int = 60, interval: int = 2) -> bool:
    '''
    Pauses the script until the server is fully offline.

    Returns:
        True once the server is offline, False if the timeout expired.

    Example:
        server.stop()
        waitForOffline(server)
        server.files.deleteFiles('/', ['world'])
    '''
    return waitForState(server, 'offline', timeout, interval)


def secsUntil(target: datetime) -> int:
    '''Returns the seconds until the target time.'''
    return int((target - datetime.now()).total_seconds())


def minsUntil(target: datetime) -> int:
    '''Returns the minutes until the target time.'''
    return secsUntil(target) // 60
