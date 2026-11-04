project = {
    'permissions': ['server.read', 'file.read'],
    'state_changes': [],
    'failure_checks': ['panel connection', 'permission error', 'operation timeout'],
    'secret_storage': 'environment variable or managed secret store',
}
print(project)