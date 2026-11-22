from calagoapi.utils.exceptions import CalagoAPIError


class MinecraftError(CalagoAPIError):
    '''
    A Minecraft feature could not be used, e.g. the bridge jar for a version does not exist.

    Errors returned by HungerBridge itself are raised unchanged as
    `hungerbridge.HungerBridgeError` subclasses (HungerBridgeAuthError, ...), and panel
    errors as the usual CalagoAPIError subclasses.
    '''


class BridgeNotConfiguredError(MinecraftError):
    '''
    A method needs HungerBridge, but no bridge token is configured for the server.

    Fix it with one of:

        enable('minecraft', config={'bridge_token': 'id:secret'})   # every server
        server.connectBridge(url, 'id:secret')                       # one server
        server.createBridgeToken()                                   # create one through the console
    '''
