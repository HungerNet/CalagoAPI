'''
Shared setup for the Minecraft examples: reads the connection from environment variables.

    CALAGOPUS_URL       panel URL, e.g. https://panel.example.com
    CALAGOPUS_API_KEY   client API key
    MC_SERVER           server UUID or short id
    HB_URL              HungerBridge URL, e.g. http://10.0.0.5:1913 (optional)
    HB_TOKEN            HungerBridge token "tokenId:secret" (optional for 01_connect.py)

Without CALAGOPUS_URL the examples only print how to run them, so they are safe to
execute anywhere. The calagoapi-minecraft test suite calls each example's main()
against a fake panel and a fake HungerBridge instead.
'''
import os


def settings():
    '''Returns the connection settings, or None (after printing help) when not configured.'''
    url = os.environ.get('CALAGOPUS_URL')
    if not url:
        print(__doc__)
        return None
    return {
        'url': url,
        'api_key': os.environ['CALAGOPUS_API_KEY'],
        'server_id': os.environ['MC_SERVER'],
        'bridge_url': os.environ.get('HB_URL'),
        'bridge_token': os.environ.get('HB_TOKEN'),
    }
