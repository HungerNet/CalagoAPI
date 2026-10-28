'''
Helpers that build schedule triggers, conditions and actions.

Calagopus schedules are made of:
- triggers: what starts the schedule (a cron expression, a crash, a console line, ...)
- a condition: checked before running (server must be online, file must exist, ...)
- steps: ordered actions (send a command, wait, create a backup, ...)

These helpers return plain dicts, so you can also write the JSON yourself.
Durations and timeouts are in milliseconds. Text parameters accept either a
string or `variable('name')` to reuse a value captured by an earlier step.

Example:
    from calagoapi import triggers, conditions, actions

    server.schedules.createSchedule(
        'Nightly restart',
        triggers=[triggers.cron('0 0 4 * * *')],
        condition=conditions.serverState('running'),
        steps=[
            actions.sendCommand('say Restarting in 1 minute'),
            actions.sleep(60_000),
            actions.createBackup('nightly'),
            actions.sendPower('restart'),
        ],
    )
'''
from types import SimpleNamespace

from calagoapi.utils.model import idOf


def variable(name: str) -> dict:
    '''
    References a schedule variable, for use in any text parameter.

    Example:
        actions.waitForConsoleLine('joined the game', output_into=variable('line'))
        actions.sendCommand(variable('line'))
    '''
    return {'variable': name}


def _var(value):
    # output_into accepts a variable name or variable('name')
    return variable(value) if isinstance(value, str) else value


# triggers
def _cron(schedule: str) -> dict:
    '''
    Runs on a cron schedule. Calagopus cron expressions have 6 fields, starting with seconds.

    Example:
        triggers.cron('0 */30 * * * *')  # every 30 minutes
    '''
    return {'type': 'cron', 'schedule': schedule}

def _powerAction(action: str) -> dict:
    '''Runs when a power action (start, stop, restart, kill) is sent to the server.'''
    return {'type': 'power_action', 'action': action}

def _serverState(state: str) -> dict:
    '''Runs when the server enters a state: offline, starting, stopping, running.'''
    return {'type': 'server_state', 'state': state}

def _backupStatus(status: str) -> dict:
    '''Runs when a backup is starting, finished or failed.'''
    return {'type': 'backup_status', 'status': status}

def _databaseBackupStatus(status: str) -> dict:
    '''Runs when a database backup is starting, finished or failed.'''
    return {'type': 'database_backup_status', 'status': status}

def _scheduleCompletion(schedule, successful: bool = True) -> dict:
    '''Runs after another schedule completes (successfully or not).'''
    return {'type': 'schedule_completion', 'schedule': idOf(schedule), 'successful': successful}

def _resourceUsage(metric: str, comparator: str, value: float, for_seconds: int = None) -> dict:
    '''
    Runs when resource usage crosses a threshold.

    Args:
        metric: cpu, memory or disk.
        comparator: smaller_than, smaller_than_or_equals, equal, greater_than, greater_than_or_equals.
        value: Threshold.
        for_seconds: How long the threshold must hold.

    Example:
        triggers.resourceUsage('memory', 'greater_than', 95, for_seconds=60)
    '''
    trigger = {'type': 'resource_usage', 'metric': metric, 'comparator': comparator, 'value': value}
    if for_seconds is not None:
        trigger['for_seconds'] = for_seconds
    return trigger

def _consoleLine(contains: str, case_insensitive: bool = False, output_into: str = None) -> dict:
    '''Runs when a console line contains the given text. output_into stores the line in a variable.'''
    return {'type': 'console_line', 'contains': contains, 'case_insensitive': case_insensitive, 'output_into': _var(output_into)}

def _crash() -> dict:
    '''Runs when the server crashes.'''
    return {'type': 'crash'}


triggers = SimpleNamespace(
    cron=_cron,
    powerAction=_powerAction,
    serverState=_serverState,
    backupStatus=_backupStatus,
    databaseBackupStatus=_databaseBackupStatus,
    scheduleCompletion=_scheduleCompletion,
    resourceUsage=_resourceUsage,
    consoleLine=_consoleLine,
    crash=_crash,
)


# conditions
def _none() -> dict:
    '''No condition, the schedule always runs.'''
    return {'type': 'none'}

def _all(*conditions) -> dict:
    '''All conditions must match.'''
    return {'type': 'and', 'conditions': list(conditions)}

def _any(*conditions) -> dict:
    '''At least one condition must match.'''
    return {'type': 'or', 'conditions': list(conditions)}

def _negate(condition: dict) -> dict:
    '''Inverts a condition.'''
    return {'type': 'not', 'condition': condition}

def _conditionServerState(state: str) -> dict:
    '''The server must be in a state: offline, starting, stopping, running.'''
    return {'type': 'server_state', 'state': state}

def _uptime(comparator: str, value: int) -> dict:
    '''Compares the server uptime (milliseconds).'''
    return {'type': 'uptime', 'comparator': comparator, 'value': value}

def _conditionResourceUsage(metric: str, comparator: str, value: float) -> dict:
    '''Compares current cpu, memory or disk usage.'''
    return {'type': 'resource_usage', 'metric': metric, 'comparator': comparator, 'value': value}

def _fileExists(file: str) -> dict:
    '''A file must exist on the server.'''
    return {'type': 'file_exists', 'file': file}

def _variableExists(name: str) -> dict:
    '''A schedule variable must be set.'''
    return {'type': 'variable_exists', 'variable': variable(name)}

def _variableEquals(name: str, value) -> dict:
    '''A schedule variable must equal a value.'''
    return {'type': 'variable_equals', 'variable': variable(name), 'equals': value}

def _variableContains(name: str, value) -> dict:
    '''A schedule variable must contain a value.'''
    return {'type': 'variable_contains', 'variable': variable(name), 'contains': value}

def _variableStartsWith(name: str, value) -> dict:
    '''A schedule variable must start with a value.'''
    return {'type': 'variable_starts_with', 'variable': variable(name), 'starts_with': value}

def _variableEndsWith(name: str, value) -> dict:
    '''A schedule variable must end with a value.'''
    return {'type': 'variable_ends_with', 'variable': variable(name), 'ends_with': value}


conditions = SimpleNamespace(
    none=_none,
    all=_all,
    any=_any,
    negate=_negate,
    serverState=_conditionServerState,
    uptime=_uptime,
    resourceUsage=_conditionResourceUsage,
    fileExists=_fileExists,
    variableExists=_variableExists,
    variableEquals=_variableEquals,
    variableContains=_variableContains,
    variableStartsWith=_variableStartsWith,
    variableEndsWith=_variableEndsWith,
)


# backup selectors for backup actions
def _latestBackup(group=None) -> dict:
    '''Selects the newest backup, optionally inside a backup group.'''
    return {'mode': 'latest', 'backup_group_uuid': idOf(group)}

def _oldestBackup(group=None) -> dict:
    '''Selects the oldest backup, optionally inside a backup group.'''
    return {'mode': 'oldest', 'backup_group_uuid': idOf(group)}

def _backupById(backup) -> dict:
    '''Selects a backup by UUID.'''
    return {'mode': 'uuid', 'uuid': idOf(backup)}

def _backupByName(name, group=None, oldest: bool = False) -> dict:
    '''Selects a backup by name (newest match unless oldest=True).'''
    return {'mode': 'name', 'name': name, 'backup_group_uuid': idOf(group), 'oldest': oldest}


backups = SimpleNamespace(
    latest=_latestBackup,
    oldest=_oldestBackup,
    byId=_backupById,
    byName=_backupByName,
)


# actions
def _sleep(duration: int) -> dict:
    '''Waits `duration` milliseconds.'''
    return {'type': 'sleep', 'duration': duration}

def _ensure(condition: dict) -> dict:
    '''Stops the schedule unless the condition matches.'''
    return {'type': 'ensure', 'condition': condition}

def _if(condition: dict) -> dict:
    '''Starts a conditional block. Close it with actions.endIf().'''
    return {'type': 'if', 'condition': condition}

def _elseIf(condition: dict) -> dict:
    '''Adds an else-if branch to a conditional block.'''
    return {'type': 'else_if', 'condition': condition}

def _else() -> dict:
    '''Adds an else branch to a conditional block.'''
    return {'type': 'else'}

def _endIf() -> dict:
    '''Ends a conditional block.'''
    return {'type': 'end_if'}

def _exit(successful: bool = True) -> dict:
    '''Stops the schedule.'''
    return {'type': 'exit', 'successful': successful}

def _waitForState(state: str, timeout: int = 60_000, ignore_failure: bool = False) -> dict:
    '''Waits until the server reaches a state (timeout in milliseconds).'''
    return {'type': 'wait_for_state', 'state': state, 'timeout': timeout, 'ignore_failure': ignore_failure}

def _format(format: str, output_into: str) -> dict:
    '''Formats text into a variable. Use {variable} placeholders.'''
    return {'type': 'format', 'format': format, 'output_into': _var(output_into)}

def _matchRegex(input, regex: str, output_into: list) -> dict:
    '''Runs a regex on `input` and stores capture groups into variables (names or None).'''
    return {'type': 'match_regex', 'input': input, 'regex': regex, 'output_into': [_var(v) for v in output_into]}

def _waitForConsoleLine(contains, timeout: int = 60_000, case_insensitive: bool = False, output_into: str = None, ignore_failure: bool = False) -> dict:
    '''Waits for a console line containing text (timeout in milliseconds).'''
    return {
        'type': 'wait_for_console_line',
        'contains': contains,
        'timeout': timeout,
        'case_insensitive': case_insensitive,
        'output_into': _var(output_into),
        'ignore_failure': ignore_failure,
    }

def _sendPower(action: str, ignore_failure: bool = False) -> dict:
    '''Sends a power action: start, stop, restart or kill.'''
    return {'type': 'send_power', 'action': action, 'ignore_failure': ignore_failure}

def _sendCommand(command, ignore_failure: bool = False) -> dict:
    '''Sends a console command.'''
    return {'type': 'send_command', 'command': command, 'ignore_failure': ignore_failure}

def _createBackup(name=None, ignored_files: list = None, group=None, foreground: bool = False, output_into: str = None, ignore_failure: bool = False) -> dict:
    '''Creates a backup. `foreground=True` waits for it to finish before the next step.'''
    return {
        'type': 'create_backup',
        'name': name,
        'ignored_files': ignored_files or [],
        'backup_group_uuid': idOf(group),
        'foreground': foreground,
        'output_into': _var(output_into),
        'ignore_failure': ignore_failure,
    }

def _restoreBackup(backup: dict = None, truncate_directory: bool = False, restore_startup: bool = False, ignore_failure: bool = False) -> dict:
    '''Restores a backup. `backup` is a selector from `backups.*`, defaults to the latest.'''
    return {
        'type': 'restore_backup',
        'backup': backup or _latestBackup(),
        'truncate_directory': truncate_directory,
        'restore_startup': restore_startup,
        'ignore_failure': ignore_failure,
    }

def _deleteBackup(backup: dict = None, ignore_failure: bool = False) -> dict:
    '''Deletes a backup. `backup` is a selector from `backups.*`, defaults to the oldest.'''
    return {'type': 'delete_backup', 'backup': backup or _oldestBackup(), 'ignore_failure': ignore_failure}

def _moveBackup(backup: dict, group, ignore_failure: bool = False) -> dict:
    '''Moves a backup into a backup group.'''
    return {'type': 'move_backup', 'backup': backup, 'backup_group_uuid': idOf(group), 'ignore_failure': ignore_failure}

def _createDatabaseBackup(database_instance, name=None, group=None, foreground: bool = False, output_into: str = None, ignore_failure: bool = False) -> dict:
    '''Creates a backup of a database instance.'''
    return {
        'type': 'create_database_backup',
        'database_instance_uuid': idOf(database_instance),
        'name': name,
        'backup_group_uuid': idOf(group),
        'foreground': foreground,
        'output_into': _var(output_into),
        'ignore_failure': ignore_failure,
    }

def _deleteDatabaseBackup(backup: dict, database_instance=None, ignore_failure: bool = False) -> dict:
    '''Deletes a database backup.'''
    return {'type': 'delete_database_backup', 'backup': backup, 'database_instance_uuid': idOf(database_instance), 'ignore_failure': ignore_failure}

def _moveDatabaseBackup(backup: dict, group, database_instance=None, ignore_failure: bool = False) -> dict:
    '''Moves a database backup into a backup group.'''
    return {
        'type': 'move_database_backup',
        'backup': backup,
        'backup_group_uuid': idOf(group),
        'database_instance_uuid': idOf(database_instance),
        'ignore_failure': ignore_failure,
    }

def _restoreDatabaseBackup(backup: dict, database_instance=None, source_database_instance=None, ignore_failure: bool = False) -> dict:
    '''Restores a database backup.'''
    return {
        'type': 'restore_database_backup',
        'backup': backup,
        'database_instance_uuid': idOf(database_instance),
        'source_database_instance_uuid': idOf(source_database_instance),
        'ignore_failure': ignore_failure,
    }

def _createDirectory(root, name, ignore_failure: bool = False) -> dict:
    '''Creates a directory.'''
    return {'type': 'create_directory', 'root': root, 'name': name, 'ignore_failure': ignore_failure}

def _writeFile(file, content, append: bool = False, ignore_failure: bool = False) -> dict:
    '''Writes (or appends) text to a file.'''
    return {'type': 'write_file', 'file': file, 'content': content, 'append': append, 'ignore_failure': ignore_failure}

def _copyFile(file, destination, foreground: bool = False, ignore_failure: bool = False) -> dict:
    '''Copies a file.'''
    return {'type': 'copy_file', 'file': file, 'destination': destination, 'foreground': foreground, 'ignore_failure': ignore_failure}

def _deleteFiles(root, files: list, ignore_failure: bool = False) -> dict:
    '''Deletes files from a directory.'''
    return {'type': 'delete_files', 'root': root, 'files': files, 'ignore_failure': ignore_failure}

def _renameFiles(root, files: list, ignore_failure: bool = False) -> dict:
    '''Renames files. `files` is a list of {'from': ..., 'to': ...} or (from, to) tuples.'''
    files = [f if isinstance(f, dict) else {'from': f[0], 'to': f[1]} for f in files]
    return {'type': 'rename_files', 'root': root, 'files': files, 'ignore_failure': ignore_failure}

def _compressFiles(root, files: list, name, format: str = 'tar_gz', foreground: bool = False, ignore_failure: bool = False) -> dict:
    '''Compresses files into an archive.'''
    return {
        'type': 'compress_files',
        'root': root,
        'files': files,
        'name': name,
        'format': format,
        'foreground': foreground,
        'ignore_failure': ignore_failure,
    }

def _decompressFile(root, file, foreground: bool = False, ignore_failure: bool = False) -> dict:
    '''Extracts an archive.'''
    return {'type': 'decompress_file', 'root': root, 'file': file, 'foreground': foreground, 'ignore_failure': ignore_failure}

def _pullFile(url, root='/', file_name=None, use_header: bool = False, foreground: bool = False, ignore_failure: bool = False) -> dict:
    '''Downloads a file from a URL onto the server.'''
    return {
        'type': 'pull_file',
        'url': url,
        'root': root,
        'file_name': file_name,
        'use_header': use_header,
        'foreground': foreground,
        'ignore_failure': ignore_failure,
    }

def _updateStartupVariable(env_variable, value, ignore_failure: bool = False) -> dict:
    '''Changes a startup variable.'''
    return {'type': 'update_startup_variable', 'env_variable': env_variable, 'value': value, 'ignore_failure': ignore_failure}

def _updateStartupCommand(command, ignore_failure: bool = False) -> dict:
    '''Changes the startup command.'''
    return {'type': 'update_startup_command', 'command': command, 'ignore_failure': ignore_failure}

def _updateDockerImage(image, ignore_failure: bool = False) -> dict:
    '''Changes the docker image.'''
    return {'type': 'update_startup_docker_image', 'image': image, 'ignore_failure': ignore_failure}

def _httpRequest(url: str, method: str = 'post', body=None, headers: dict = None, timeout: int = 10_000,
                 ignore_error_status: bool = False, output_status_into: str = None, output_body_into: str = None,
                 ignore_failure: bool = False) -> dict:
    '''
    Sends an HTTP request, e.g. to a Discord webhook.

    Example:
        actions.httpRequest('https://discord.com/api/webhooks/...', body='{"content": "Restarting"}',
                            headers={'Content-Type': 'application/json'})
    '''
    return {
        'type': 'http_request',
        'url': url,
        'method': method,
        'body': body,
        'headers': [{'name': k, 'value': v} for k, v in (headers or {}).items()],
        'timeout': timeout,
        'ignore_error_status': ignore_error_status,
        'output_status_into': _var(output_status_into),
        'output_body_into': _var(output_body_into),
        'ignore_failure': ignore_failure,
    }


actions = SimpleNamespace(
    sleep=_sleep,
    ensure=_ensure,
    ifCondition=_if,
    elseIf=_elseIf,
    otherwise=_else,
    endIf=_endIf,
    exit=_exit,
    waitForState=_waitForState,
    format=_format,
    matchRegex=_matchRegex,
    waitForConsoleLine=_waitForConsoleLine,
    sendPower=_sendPower,
    sendCommand=_sendCommand,
    createBackup=_createBackup,
    restoreBackup=_restoreBackup,
    deleteBackup=_deleteBackup,
    moveBackup=_moveBackup,
    createDatabaseBackup=_createDatabaseBackup,
    deleteDatabaseBackup=_deleteDatabaseBackup,
    moveDatabaseBackup=_moveDatabaseBackup,
    restoreDatabaseBackup=_restoreDatabaseBackup,
    createDirectory=_createDirectory,
    writeFile=_writeFile,
    copyFile=_copyFile,
    deleteFiles=_deleteFiles,
    renameFiles=_renameFiles,
    compressFiles=_compressFiles,
    decompressFile=_decompressFile,
    pullFile=_pullFile,
    updateStartupVariable=_updateStartupVariable,
    updateStartupCommand=_updateStartupCommand,
    updateDockerImage=_updateDockerImage,
    httpRequest=_httpRequest,
)
