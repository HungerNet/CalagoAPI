from importlib import metadata as importlib_metadata


# entry point group extension packages publish under
ENTRY_POINT_GROUP = 'calagoapi'

# first-party extension ids -> PyPI package, for "pip install ..." hints
FIRST_PARTY = {
    'version_changer': 'calagoapi-version-changer',
    'hungerbridge': 'calagoapi-hungerbridge',
}


def entryPoints(group: str = ENTRY_POINT_GROUP) -> list:
    '''
    Lists the entry points of a group without importing anything.

    Works with the Python 3.9 dict API and the 3.10+ selectable API.
    '''
    eps = importlib_metadata.entry_points()
    if hasattr(eps, 'select'):
        return list(eps.select(group=group))
    return list(eps.get(group, []))


def distributionName(entry_point) -> str:
    '''Returns the distribution that publishes an entry point, or None if unknown (Python 3.9)'''
    dist = getattr(entry_point, 'dist', None)
    return getattr(dist, 'name', None) or (dist.metadata['Name'] if dist is not None else None)


def describeEntryPoint(entry_point) -> str:
    dist = distributionName(entry_point)
    where = f' from {dist}' if dist else ''
    return f'entry point {entry_point.name!r} ({entry_point.value}){where}'
