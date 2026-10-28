from types import SimpleNamespace


TIME_UNITS = {
    'ns': 1e-9,
    'us': 1e-6,
    'ms': 1e-3,
    's': 1,
    'min': 60,
    'h': 3600,
    'day': 86400,
}

BYTE_UNITS = {
    # decimal
    'b': 1,
    'kb': 1_000,
    'mb': 1_000_000,
    'gb': 1_000_000_000,
    'tb': 1_000_000_000_000,

    # binary
    'kib': 1024,
    'mib': 1024**2,
    'gib': 1024**3,
    'tib': 1024**4,
}


def _convert(value, src, dst, units, rounding=None):
    if src not in units or dst not in units:
        raise ValueError(f'Unknown unit, expected one of: {", ".join(units)}')
    result = float(value) * units[src] / units[dst]
    return round(result, rounding) if rounding is not None else result


def _time(value, src, dst, rounding=None):
    '''
    Converts a duration between units.

    Args:
        value: The number to convert.
        src: Source unit: ns, us, ms, s, min, h, day.
        dst: Target unit.
        rounding: Optional number of decimal places.

    Example:
        convert.time(90_000, 'ms', 'min')  # 1.5
    '''
    return _convert(value, src, dst, TIME_UNITS, rounding)


def _byte(value, src, dst, rounding=None):
    '''
    Converts a size between units.

    Args:
        value: The number to convert.
        src: Source unit: b, kb, mb, gb, tb, kib, mib, gib, tib.
        dst: Target unit.
        rounding: Optional number of decimal places.

    Example:
        convert.byte(server.resources()['memory_bytes'], 'b', 'gib', 2)
    '''
    return _convert(value, src, dst, BYTE_UNITS, rounding)


def formatBytes(value, rounding: int = 2) -> str:
    '''
    Formats a byte count as a human readable string using binary units.

    Example:
        formatBytes(1536)  # '1.5 KiB'
    '''
    if value is None:
        return None
    value = float(value)
    for unit in ('B', 'KiB', 'MiB', 'GiB', 'TiB'):
        if abs(value) < 1024 or unit == 'TiB':
            return f'{round(value, rounding):g} {unit}'
        value /= 1024


def formatDuration(milliseconds) -> str:
    '''
    Formats a duration in milliseconds the same way HungerLib formats uptime.

    Example:
        formatDuration(3_900_000)  # '1h 5m'
    '''
    if milliseconds is None:
        return None
    seconds = int(milliseconds) // 1000
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if days > 0:
        return f'{days}d {hours}h'
    if hours > 0:
        return f'{hours}h {minutes}m'
    if minutes > 0:
        return f'{minutes}m {secs}s'
    return f'{secs}s'


convert = SimpleNamespace(
    time=_time,
    byte=_byte,
    formatBytes=formatBytes,
    formatDuration=formatDuration,
)
