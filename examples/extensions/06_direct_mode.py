'''
Example 6: direct mode.

Run it:
    python examples/extensions/06_direct_mode.py

In direct mode (the default) methods and properties appear directly on the
object: `server.deployRelease(...)`, `server.deployedRelease`. It feels like
CalagoAPI always had them.

The trade-off: the names share the object's namespace with CalagoAPI and every
other extension, so a name that is already taken is an ExtensionConflictError.
'''
from calagoapi import Panel, Server
from calagoapi.extensions import (
    Extension,
    ExtensionConflictError,
    ExtensionMetadata,
    enable,
    method,
    propertyExtension,
    register,
)


@method(Server)
def deployRelease(self, release: str) -> str:
    # A stand-in for a real deployment: remember what was deployed.
    self.data['release'] = release
    return f'deploying {release} to {self.getName()}'


@propertyExtension(Server)
def deployedRelease(self) -> str:
    return self.data.get('release', 'unknown')


class DeployExtension(Extension):
    extension_id = 'deploy'
    metadata = ExtensionMetadata(author='you', version='1.0.0', schema=1)
    default_mode = 'direct'          # the default, written out for clarity
    members = [deployRelease, deployedRelease]


register(DeployExtension)
enable('deploy')

panel = Panel(url='https://panel.example.com', api_key='not-a-real-key')
server = Server(panel, 'abc123', data={'uuid': 'abc123', 'name': 'Survival'})

print(server.deployRelease('v2.4.1'))      # directly on the server
print(server.deployedRelease)              # v2.4.1


# Direct mode never replaces anything. A second extension that also wants
# `deployRelease` on Server is rejected, with both owners named:
@method(Server, name='deployRelease')
def otherDeploy(self, release):
    return 'other'


class OtherExtension(Extension):
    extension_id = 'other_deploy'
    members = [otherDeploy]


register(OtherExtension)
try:
    enable('other_deploy')
except ExtensionConflictError as e:
    print(f'ExtensionConflictError: {e}')
    print(f'  extension: {e.extension} | owner: {e.owner} | target: {e.target.__name__} | member: {e.member}')

# The same is true for CalagoAPI's own members (start, stop, files, console, ...).
# Users who hit a conflict can often enable the extension in namespace mode
# instead (see 07_namespace_mode.py).
