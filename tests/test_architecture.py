'''
Architecture rules for the core package (see PLAN.md, "Dependency architecture"):

- calagoapi is game-agnostic: no module imports HungerBridge, HungerBridgePy or a game
  extension, and no core source mentions a specific game.
- the only runtime dependencies are requests and websockets.
- calagoapi imports while game packages are unavailable.
'''
import ast
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE = os.path.join(ROOT, 'src', 'calagoapi')

FORBIDDEN_IMPORTS = ('hungerbridge', 'calagoapi_minecraft')
GAME_WORDS = re.compile(r'minecraft|hungerbridge|MinecraftServer', re.IGNORECASE)
# the first-party package table maps extension ids to PyPI names ("pip install ..." hints)
ALLOWED_GAME_WORDS = {os.path.join('extensions', 'discovery.py')}


def coreModules():
    for folder, _, files in os.walk(CORE):
        for name in files:
            if name.endswith('.py'):
                path = os.path.join(folder, name)
                yield os.path.relpath(path, CORE), path


def test_core_imports_no_game_packages():
    offenders = []
    for relative, path in coreModules():
        with open(path, encoding='utf-8') as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                names = [node.module]
            for name in names:
                if name.split('.')[0] in FORBIDDEN_IMPORTS:
                    offenders.append(f'{relative}: import {name}')
    assert not offenders, '\n'.join(offenders)


def test_core_source_is_game_agnostic():
    offenders = []
    for relative, path in coreModules():
        if relative in ALLOWED_GAME_WORDS:
            continue
        with open(path, encoding='utf-8') as f:
            for number, line in enumerate(f, 1):
                if GAME_WORDS.search(line):
                    offenders.append(f'{relative}:{number}: {line.strip()}')
    assert not offenders, 'Game-specific code or docs in core:\n' + '\n'.join(offenders)


def test_runtime_dependencies():
    with open(os.path.join(ROOT, 'pyproject.toml'), encoding='utf-8') as f:
        text = f.read()
    block = re.search(r'^dependencies = \[(.*?)\]', text, re.S | re.M).group(1)
    names = sorted(re.findall(r'"([A-Za-z0-9_.-]+)', block))
    assert names == ['requests', 'websockets'], names


def test_core_imports_without_game_packages():
    script = (
        'import sys\n'
        'sys.modules["hungerbridge"] = None\n'          # any import attempt raises ImportError
        'sys.modules["calagoapi_minecraft"] = None\n'
        'import calagoapi, calagoapi.aio, calagoapi.extensions\n'
        'assert calagoapi.Server.__module__ == "calagoapi.servers.server"\n'
        'assert not hasattr(calagoapi, "MinecraftServer")\n'
        'print("ok")\n'
    )
    env = dict(os.environ, PYTHONPATH=os.path.join(ROOT, 'src'))
    result = subprocess.run([sys.executable, '-c', script], capture_output=True, text=True, env=env, timeout=60)
    assert result.returncode == 0 and 'ok' in result.stdout, result.stderr


def test_subpackages_are_not_shadowed():
    import calagoapi
    import calagoapi.schedules
    import calagoapi.servers
    import calagoapi.utils
    assert calagoapi.servers is sys.modules['calagoapi.servers']
    assert calagoapi.utils is sys.modules['calagoapi.utils']
    assert calagoapi.schedules is sys.modules['calagoapi.schedules']
