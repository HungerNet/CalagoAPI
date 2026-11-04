'''
calagoapi-version-changer: the Calagopus Minecraft Version Changer for CalagoAPI.

You do not need to import this package. Install it and enable it by id:

    from calagoapi.extensions import enable
    enable('version_changer')
'''
from importlib.metadata import version as _pkg_version, PackageNotFoundError

try:
    __version__ = _pkg_version('calagoapi-version-changer')
except PackageNotFoundError:
    __version__ = '0.0.0'
