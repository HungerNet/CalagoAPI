'''Reading and editing server.properties text, keeping comments and order.'''


def formatValue(value) -> str:
    '''Booleans become true/false, everything else str().'''
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return str(value)


def parse(text: str) -> dict:
    '''
    Returns {key: value} for a server.properties file (values are strings).

    Example:
        parse('motd=Hello\\n# comment\\nmax-players=20')   # {'motd': 'Hello', 'max-players': '20'}
    '''
    properties = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(('#', '!')) or '=' not in line:
            continue
        key, value = line.split('=', 1)
        properties[key.strip()] = value.strip()
    return properties


def update(text: str, values: dict) -> str:
    '''
    Returns the file text with `values` changed in place; new keys are appended.

    Example:
        update('motd=Old\\n', {'motd': 'New', 'pvp': False})   # 'motd=New\\npvp=false\\n'
    '''
    pending = {key: formatValue(value) for key, value in values.items()}
    lines = []
    for line in text.splitlines():
        key = line.split('=', 1)[0].strip()
        if '=' in line and not line.lstrip().startswith(('#', '!')) and key in pending:
            line = f'{key}={pending.pop(key)}'
        lines.append(line)
    lines.extend(f'{key}={value}' for key, value in pending.items())
    return '\n'.join(lines) + '\n'
