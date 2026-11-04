'''
Tests for the extension system (calagoapi.extensions).

Every test uses its own ExtensionRegistry and throwaway target classes, so nothing
leaks into the real CalagoAPI classes or into other tests.
'''
import asyncio
import os
import sys
import textwrap
import threading
import time
import warnings

import pytest

from calagoapi import MinecraftServer
from calagoapi.aio.panel import AsyncWrapper
from calagoapi.extensions import (
    Alias,
    CircularDependencyError,
    ConfigurationError,
    Dependency,
    DependencyError,
    Extension,
    ExtensionConflictError,
    ExtensionDefinitionError,
    ExtensionDeprecationWarning,
    ExtensionError,
    ExtensionLoadError,
    ExtensionMetadata,
    ExtensionNamespace,
    ExtensionNotEnabledError,
    ExtensionNotFoundError,
    ExtensionRegistry,
    class_extension,
    method,
    migrated_to,
    property_extension,
)


@pytest.fixture
def registry():
    registry = ExtensionRegistry()
    registry._entry_points = {}  # ignore whatever is installed in this environment
    yield registry
    registry._reset_for_tests()


def makeTarget():
    class Base:
        def __init__(self, name='obj'):
            self.name = name
            self.data = {}

        def existing(self):
            return 'built-in'

    class Target(Base):
        pass

    return Base, Target


def makeExtension(extension_id, members=(), **attributes):
    attributes.setdefault('metadata', ExtensionMetadata(author='tests', version='1.0.0', schema=1))
    return type(f'{extension_id.title()}Extension', (Extension,),
                {'extension_id': extension_id, 'members': list(members), **attributes})


# basics
def test_direct_mode_adds_members_to_existing_and_future_objects(registry):
    Base, Target = makeTarget()
    existing = Target('early')

    @method(Target)
    def greet(self, greeting='hello'):
        return f'{greeting} {self.name}'

    @property_extension(Target)
    def shout(self):
        return self.name.upper()

    @class_extension(Target, 'tools')
    class Tools:
        def __init__(self, owner):
            self.owner = owner

        def count(self):
            return len(self.owner.name)

    registry.register(makeExtension('greeter', [greet, shout, Tools]))
    extension = registry.enable('greeter')

    later = Target('late')
    for obj in (existing, later):
        assert obj.greet() == f'hello {obj.name}'
        assert obj.shout == obj.name.upper()
        assert obj.tools.owner is obj
        assert obj.tools.count() == len(obj.name)
        assert obj.tools is obj.tools
    assert existing.tools is not later.tools
    assert not hasattr(Base('x'), 'greet')
    assert extension.mode == 'direct'
    assert dict(extension.config) == {}
    # decorated objects stay normal Python
    assert greet(existing, 'hi') == 'hi early'


def test_enable_is_idempotent_and_accepts_aliases(registry):
    _, Target = makeTarget()

    @method(Target)
    def ping(self):
        return 'pong'

    registry.register(makeExtension('pinger', [ping], aliases=['old_pinger']))
    first = registry.enable('pinger')
    assert registry.enable('pinger') is first
    assert registry.enable('old_pinger') is first
    assert registry.enable('pinger', config={}) is first
    assert registry.enable('pinger', mode='direct') is first
    assert registry.is_enabled('old_pinger') and registry.is_enabled('pinger')
    assert registry.get('old_pinger') is first
    assert registry.enabled() == [first]
    assert Target().ping() == 'pong'


def test_extension_get_and_not_enabled(registry):
    Ext = registry.register(makeExtension('lonely'))
    with pytest.raises(ExtensionNotEnabledError):
        Ext.get()
    with pytest.raises(ExtensionNotEnabledError):
        registry.get('lonely')
    instance = registry.enable('lonely')
    assert Ext.get() is instance
    assert registry.is_enabled('lonely')


def test_extension_without_members_is_valid(registry):
    calls = []
    Ext = makeExtension('hooks_only', on_enable=lambda self: calls.append(self.extension_id))
    registry.register(Ext)
    registry.enable('hooks_only')
    assert calls == ['hooks_only']


# configuration
def test_config_defaults_are_merged_and_frozen(registry):
    Ext = registry.register(makeExtension('configured', default_config={'mc_version': 'latest', 'retries': 3, 'tags': []}))
    extension = registry.enable('configured', config={'mc_version': '1.21.11'})
    assert dict(extension.config) == {'mc_version': '1.21.11', 'retries': 3, 'tags': []}
    with pytest.raises(TypeError):
        extension.config['retries'] = 5
    extension.config['tags'].append('x')
    assert Ext.default_config['tags'] == []  # defaults are copied, never shared


def test_reenable_with_different_config_fails(registry):
    registry.register(makeExtension('bridge', default_config={'mc_version': 'latest'}))
    registry.enable('bridge', config={'mc_version': '1.20.4'})
    registry.enable('bridge', config={'mc_version': '1.20.4'})  # same config: fine
    registry.enable('bridge')  # no opinion: fine
    with pytest.raises(ConfigurationError) as error:
        registry.enable('bridge', config={'mc_version': '1.21.1'})
    assert '1.20.4' in str(error.value) and '1.21.1' in str(error.value)
    with pytest.raises(ConfigurationError, match='namespace'):
        registry.enable('bridge', mode='namespace')


def test_reenable_equal_to_defaults_is_fine(registry):
    registry.register(makeExtension('defaults', default_config={'a': 1}))
    registry.enable('defaults')
    registry.enable('defaults', config={'a': 1})


def test_unknown_config_keys(registry):
    registry.register(makeExtension('strict', default_config={'port': 1913}))
    with pytest.raises(ConfigurationError, match='prot.*Known keys: port'):
        registry.enable('strict', config={'prot': 1})
    assert not registry.is_enabled('strict')

    registry.register(makeExtension('loose', default_config={}, allow_unknown_config=True))
    assert registry.enable('loose', config={'anything': 1}).config['anything'] == 1


def test_validate_config(registry):
    def validate(self, config):
        if config['port'] <= 0:
            raise ValueError('port must be positive')
        config['port'] = int(config['port'])
        return config

    registry.register(makeExtension('validated', default_config={'port': 1913}, validate_config=validate))
    with pytest.raises(ConfigurationError, match='port must be positive'):
        registry.enable('validated', config={'port': -1})
    assert registry.enable('validated', config={'port': 25565.0}).config['port'] == 25565


def test_invalid_mode_and_config_types(registry):
    registry.register(makeExtension('typed'))
    with pytest.raises(ConfigurationError):
        registry.enable('typed', mode='sideways')
    with pytest.raises(ConfigurationError):
        registry.enable('typed', config=['not', 'a', 'dict'])


# namespace mode
def test_namespace_mode(registry):
    Base, Target = makeTarget()

    @method(Base)
    def players(self):
        return ['Steve', self.name]

    @method(Target)
    def status(self):
        return f'{self.name} ok'

    @property_extension(Target)
    def label(self):
        return f'<{self.name}>'

    @class_extension(Target, 'bridge_client')
    class Client:
        def __init__(self, owner):
            self.owner = owner

    registry.register(makeExtension('bridge', [players, status, label, Client], default_mode='namespace',
                                    namespace='hb'))
    extension = registry.enable('bridge')
    obj = Target('srv')

    assert isinstance(obj.hb, ExtensionNamespace)
    assert obj.hb is obj.hb
    assert obj.hb.players() == ['Steve', 'srv']
    assert obj.hb.status() == 'srv ok'
    assert obj.hb.label == '<srv>'
    assert dir(obj.hb) == ['label', 'players', 'status']
    assert not hasattr(obj, 'players') and not hasattr(obj, 'status')
    # services are reached at their own name in both modes
    assert obj.bridge_client.owner is obj
    # base-class members are visible on base objects, subclass members are not
    assert Base('b').hb.players() == ['Steve', 'b']
    with pytest.raises(AttributeError, match="has no member 'status'"):
        Base('b').hb.status()
    with pytest.raises(AttributeError):
        obj.hb.label = 'x'
    assert extension.namespace == 'hb'
    namespaced = [r for r in registry.registrations(owner='bridge') if r.namespace]
    assert {r.name for r in namespaced} == {'players', 'status', 'label'}


def test_user_can_override_mode(registry):
    _, Target = makeTarget()

    @method(Target)
    def installVersion(self, build):
        return f'installed {build}'

    registry.register(makeExtension('version_changer', [installVersion]))
    registry.enable('version_changer', mode='namespace')
    obj = Target()
    assert obj.version_changer.installVersion('b1') == 'installed b1'
    assert not hasattr(obj, 'installVersion')


def test_namespace_property_setter(registry):
    _, Target = makeTarget()

    def getMotd(self):
        return self.data.get('motd')

    def setMotd(self, value):
        self.data['motd'] = value

    motd = property_extension(Target, name='motd')(property(getMotd, setMotd))
    registry.register(makeExtension('motd', [motd], default_mode='namespace'))
    registry.enable('motd')
    obj = Target()
    obj.motd.motd = 'Welcome'
    assert obj.motd.motd == 'Welcome'


# conflicts
def test_conflict_with_builtin_method(registry):
    Base, Target = makeTarget()

    @method(Target)
    def existing(self):
        return 'mine'

    registry.register(makeExtension('rude', [existing]))
    with pytest.raises(ExtensionConflictError) as error:
        registry.enable('rude')
    e = error.value
    assert (e.extension, e.target, e.member) == ('rude', Target, 'existing')
    assert e.owner == __name__
    assert 'Base already defines' in str(e)
    assert Target('x').existing() == 'built-in'
    assert not registry.is_enabled('rude')


def test_conflict_with_real_calagoapi_class(registry):
    @method(MinecraftServer)
    def say(self, message):
        return message

    registry.register(makeExtension('loud', [say]))
    with pytest.raises(ExtensionConflictError) as error:
        registry.enable('loud')
    assert error.value.owner == 'calagoapi'
    assert error.value.target is MinecraftServer


def test_conflict_with_instance_attribute(registry):
    _, Target = makeTarget()

    @property_extension(Target)
    def data(self):
        return 'shadowed'

    registry.register(makeExtension('shadow', [data]))
    with pytest.raises(ExtensionConflictError, match=r'instance attribute self\.data'):
        registry.enable('shadow')


def test_conflict_with_subclass_member(registry):
    class Base:
        pass

    class Sub(Base):
        def ping(self):
            return 'sub'

    @method(Base)
    def ping(self):
        return 'ext'

    registry.register(makeExtension('pinger', [ping]))
    with pytest.raises(ExtensionConflictError, match='subclass Sub already defines'):
        registry.enable('pinger')


def test_conflict_between_extensions_names_both_owners(registry):
    _, Target = makeTarget()

    @method(Target, name='installVersion')
    def first(self):
        return 1

    @method(Target, name='installVersion')
    def second(self):
        return 2

    registry.register(makeExtension('first_ext', [first]))
    registry.register(makeExtension('second_ext', [second]))
    registry.enable('first_ext')
    with pytest.raises(ExtensionConflictError) as error:
        registry.enable('second_ext')
    e = error.value
    assert (e.extension, e.owner, e.target, e.member) == ('second_ext', 'first_ext', Target, 'installVersion')
    assert "already provided by extension 'first_ext'" in str(e)
    assert Target().installVersion() == 1


def test_conflict_across_base_and_subclass(registry):
    Base, Target = makeTarget()

    @method(Target, name='stats')
    def onSub(self):
        return 'sub'

    @method(Base, name='stats')
    def onBase(self):
        return 'base'

    registry.register(makeExtension('sub_ext', [onSub]))
    registry.register(makeExtension('base_ext', [onBase]))
    registry.enable('sub_ext')
    with pytest.raises(ExtensionConflictError, match="already provided by extension 'sub_ext'"):
        registry.enable('base_ext')


def test_same_extension_may_specialise_on_subclass(registry):
    Base, Target = makeTarget()

    @method(Base, name='kind')
    def baseKind(self):
        return 'base'

    @method(Target, name='kind')
    def targetKind(self):
        return 'target'

    registry.register(makeExtension('kinds', [baseKind, targetKind]))
    registry.enable('kinds')
    assert Base().kind() == 'base' and Target().kind() == 'target'


def test_conflict_with_async_wrapper_names(registry):
    _, Target = makeTarget()

    @method(Target)
    def target(self):
        return 'nope'

    registry.register(makeExtension('wrapper_clash', [target]))
    with pytest.raises(ExtensionConflictError, match='async wrappers'):
        registry.enable('wrapper_clash')


def test_conflict_is_atomic(registry):
    _, Target = makeTarget()

    @method(Target)
    def fine(self):
        return 'fine'

    @method(Target)
    def existing(self):
        return 'clash'

    registry.register(makeExtension('half', [fine, existing]))
    with pytest.raises(ExtensionConflictError):
        registry.enable('half')
    assert not hasattr(Target, 'fine')
    assert registry.registrations() == []


def test_namespace_name_conflicts(registry):
    _, Target = makeTarget()

    @method(Target)
    def go(self):
        return 'go'

    registry.register(makeExtension('existing', [go], default_mode='namespace'))
    with pytest.raises(ExtensionConflictError, match="namespace 'existing'"):
        registry.enable('existing')


# ids and aliases
def test_duplicate_ids_and_aliases(registry):
    registry.register(makeExtension('alpha', aliases=['old_alpha']))
    same = registry._classes['alpha']
    registry.register(same)  # registering the same class again is fine

    with pytest.raises(ExtensionConflictError, match='Two extensions use the id'):
        registry.register(makeExtension('alpha'))
    with pytest.raises(ExtensionConflictError, match='already used by extension'):
        registry.register(makeExtension('beta', aliases=['old_alpha']))
    with pytest.raises(ExtensionConflictError, match='is the id of another'):
        registry.register(makeExtension('gamma', aliases=['alpha']))
    with pytest.raises(ExtensionConflictError, match='already an alias'):
        registry.register(makeExtension('old_alpha'))


def test_deprecated_alias_warns_at_the_caller(registry):
    registry.register(makeExtension('minecraft_version_manager',
                                    aliases=['version_changer', Alias('vc', deprecated=True, message='Renamed in 2.0.')]))
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        registry.enable('version_changer')
        assert not caught
        registry.enable('vc')
    assert len(caught) == 1
    warning = caught[0]
    assert issubclass(warning.category, ExtensionDeprecationWarning)
    assert "'vc' is deprecated, use 'minecraft_version_manager'" in str(warning.message)
    assert 'Renamed in 2.0.' in str(warning.message)
    assert warning.filename == __file__


def test_not_found_message(registry):
    registry.register(makeExtension('hungerbridge_tools'))
    with pytest.raises(ExtensionNotFoundError) as error:
        registry.enable('hungerbridge_tool')
    message = str(error.value)
    assert "Extension 'hungerbridge_tool' is not installed" in message
    assert "Did you mean: 'hungerbridge_tools'" in message
    assert isinstance(error.value, LookupError)

    with pytest.raises(ExtensionNotFoundError, match='pip install calagoapi-hungerbridge'):
        registry.enable('hungerbridge')


# dependencies
def test_dependencies_are_enabled_first(registry):
    order = []
    registry.register(makeExtension('base_dep', on_enable=lambda self: order.append('base_dep')))
    registry.register(makeExtension('middle', dependencies=['base_dep'], on_enable=lambda self: order.append('middle')))
    registry.register(makeExtension('top', dependencies=['middle', Dependency('missing', optional=True)],
                                    on_enable=lambda self: order.append('top')))
    registry.enable('top')
    assert order == ['base_dep', 'middle', 'top']
    assert registry.get('middle').enabled_by == 'top'
    assert registry.get('top').enabled_by is None
    registry.enable('top')
    assert order == ['base_dep', 'middle', 'top']


def test_missing_dependency(registry):
    registry.register(makeExtension('needs_vc', dependencies=['version_changer']))
    with pytest.raises(DependencyError) as error:
        registry.enable('needs_vc')
    assert "'needs_vc' requires 'version_changer', which is not installed" in str(error.value)
    assert 'pip install calagoapi-version-changer' in str(error.value)
    assert not registry.is_enabled('needs_vc')


def test_circular_dependencies(registry):
    registry.register(makeExtension('chicken', dependencies=['egg']))
    registry.register(makeExtension('egg', dependencies=['chicken']))
    registry.register(makeExtension('narcissus', dependencies=['narcissus']))
    with pytest.raises(CircularDependencyError) as error:
        registry.enable('chicken')
    assert error.value.cycle == ['chicken', 'egg', 'chicken']
    assert 'chicken -> egg -> chicken' in str(error.value)
    with pytest.raises(CircularDependencyError):
        registry.enable('narcissus')
    assert registry.enabled() == []


def test_dependency_config_conflict_explains_order(registry):
    registry.register(makeExtension('vc', default_config={'auto_backup': False}))
    registry.register(makeExtension('hb', dependencies=['vc']))
    registry.enable('hb')
    with pytest.raises(ConfigurationError, match="dependency of 'hb'.*enable 'vc' before 'hb'"):
        registry.enable('vc', config={'auto_backup': True})


def test_dependency_errors_are_wrapped(registry):
    _, Target = makeTarget()

    @method(Target)
    def existing(self):
        pass

    registry.register(makeExtension('broken_dep', [existing]))
    registry.register(makeExtension('uses_broken', dependencies=['broken_dep']))
    with pytest.raises(DependencyError, match="could not enable its dependency 'broken_dep'"):
        registry.enable('uses_broken')


# lifecycle
def test_on_enable_runs_after_install_and_failure_rolls_back(registry):
    _, Target = makeTarget()
    seen = []

    @method(Target)
    def hello(self):
        return 'hello'

    def onEnable(self):
        seen.append(Target().hello())
        raise RuntimeError('database unreachable')

    registry.register(makeExtension('fragile', [hello], on_enable=onEnable))
    with pytest.raises(ExtensionError, match='on_enable.*database unreachable'):
        registry.enable('fragile')
    assert seen == ['hello']
    assert not hasattr(Target, 'hello')
    assert not registry.is_enabled('fragile')
    assert registry.registrations() == []


# migration handover
def test_migrated_builtin_is_handed_over(registry):
    class Server:
        @migrated_to('version_changer', 'calagoapi-version-changer')
        def installVersion(self, build):
            return f'legacy {build}'

    with pytest.warns(ExtensionDeprecationWarning, match='pip install calagoapi-version-changer'):
        assert Server().installVersion('b') == 'legacy b'
    legacy = Server.__dict__['installVersion']

    @method(Server, name='installVersion')
    def stolen(self, build):
        return 'stolen'

    @method(Server, name='installVersion')
    def modern(self, build):
        return f'modern {build}'

    registry.register(makeExtension('thief', [stolen]))
    with pytest.raises(ExtensionConflictError):
        registry.enable('thief')

    registry.register(makeExtension('minecraft_version_manager', [modern], aliases=['version_changer']))
    registry.enable('version_changer')
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        assert Server().installVersion('b') == 'modern b'
    registration = registry.registrations(owner='version_changer')[0]
    assert registration.replaced is legacy

    registry._reset_for_tests()
    assert Server.__dict__['installVersion'] is legacy


# ownership and introspection
def test_ownership_introspection(registry):
    Base, Target = makeTarget()

    @method(Base)
    def alpha(self):
        pass

    @class_extension(Target)
    class Beta:
        def __init__(self, owner):
            pass

    registry.register(makeExtension('owned', [alpha, Beta]))
    registry.enable('owned')
    assert registry.owner_of(Target, 'alpha') == 'owned'
    assert registry.owner_of(Target, 'beta') == 'owned'
    assert registry.owner_of(Target, 'existing') is None
    kinds = {(r.target, r.name, r.kind) for r in registry.registrations(owner='owned')}
    assert kinds == {(Base, 'alpha', 'method'), (Target, 'beta', 'service')}
    assert registry.registrations(target=Target)[0].name == 'beta'
    text = registry.describe()
    assert 'owned 1.0.0 by tests [direct]' in text and 'Base.alpha (method' in text
    assert repr(Target.__dict__['beta']).startswith("<service 'beta'")


def test_member_belongs_to_one_extension(registry):
    _, Target = makeTarget()

    @method(Target)
    def shared(self):
        pass

    registry.register(makeExtension('owner_a', [shared]))
    registry.register(makeExtension('owner_b', [shared]))
    registry.enable('owner_a')
    with pytest.raises(ExtensionDefinitionError, match="already belongs to extension 'owner_a'"):
        registry.enable('owner_b')


# definitions
@pytest.mark.parametrize('attributes, message', [
    ({'extension_id': 'Bad-Id'}, 'extension_id must be'),
    ({'default_mode': 'sideways'}, 'default_mode'),
    ({'metadata': ExtensionMetadata(schema=99)}, 'schema 99'),
    ({'metadata': {'author': 'me'}}, 'ExtensionMetadata'),
    ({'aliases': [42]}, 'aliases'),
    ({'namespace': '_private'}, 'namespace'),
    ({'default_config': ['x']}, 'default_config'),
])
def test_invalid_extension_classes(registry, attributes, message):
    attributes = dict(attributes)
    extension_id = attributes.pop('extension_id', 'invalid')
    with pytest.raises(ExtensionDefinitionError, match=message):
        registry.register(makeExtension(extension_id, **attributes))


def test_invalid_members():
    _, Target = makeTarget()
    with pytest.raises(ExtensionDefinitionError, match='Use @method\\(TargetClass\\)'):
        method(lambda self: None)
    with pytest.raises(ExtensionDefinitionError, match='dunder'):
        method(Target, name='__init__')(lambda self: None)
    with pytest.raises(ExtensionDefinitionError, match='@class_extension'):
        method(Target)(type('NotAFunction', (), {}))
    with pytest.raises(ExtensionDefinitionError):
        class_extension(Target)(lambda self: None)


def test_members_list_must_contain_decorated_objects(registry):
    registry.register(makeExtension('sloppy', [lambda self: None]))
    with pytest.raises(ExtensionDefinitionError, match='not decorated'):
        registry.enable('sloppy')


def test_slotted_targets_cannot_get_services(registry):
    class Slotted:
        __slots__ = ('x',)

    @class_extension(Slotted, 'svc')
    class Service:
        def __init__(self, owner):
            pass

    registry.register(makeExtension('slots', [Service]))
    with pytest.raises(ExtensionDefinitionError, match='__slots__'):
        registry.enable('slots')


# threads and async
def test_concurrent_enable_and_service_creation(registry):
    _, Target = makeTarget()
    created = []

    @class_extension(Target, 'slow')
    class Slow:
        def __init__(self, owner):
            time.sleep(0.01)
            created.append(self)

    registry.register(makeExtension('slow_ext', [Slow]))
    results = []
    threads = [threading.Thread(target=lambda: results.append(registry.enable('slow_ext'))) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert len({id(r) for r in results}) == 1

    obj = Target()
    services = []
    threads = [threading.Thread(target=lambda: services.append(obj.slow)) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert len(created) == 1 and all(s is created[0] for s in services)


def test_async_wrapper_supports_extension_members(registry):
    _, Target = makeTarget()

    @method(Target)
    def syncHello(self):
        return f'sync {self.name}'

    @method(Target)
    async def asyncHello(self):
        await asyncio.sleep(0)
        return f'async {self.name}'

    @class_extension(Target, 'svc')
    class Service:
        def __init__(self, owner):
            self.owner = owner

        def players(self):
            return ['Steve']

    @method(Target, name='status')
    def nsStatus(self):
        return 'ok'

    registry.register(makeExtension('async_ext', [syncHello, asyncHello, Service]))
    registry.register(makeExtension('ns_ext', [nsStatus], default_mode='namespace', namespace='hb'))
    registry.enable('async_ext')
    registry.enable('ns_ext')

    async def main():
        wrapper = AsyncWrapper(Target('srv'))
        assert await wrapper.syncHello() == 'sync srv'
        assert await wrapper.asyncHello() == 'async srv'
        assert wrapper.svc is wrapper.svc
        assert await wrapper.svc.players() == ['Steve']
        assert await wrapper.hb.status() == 'ok'

    asyncio.run(main())


# discovery through real entry points
DIST_INFO = '''\
Metadata-Version: 2.1
Name: {name}
Version: 1.0.0
'''


def writeDistribution(root, name, entry_points):
    dist = os.path.join(root, f'{name}-1.0.0.dist-info')
    os.makedirs(dist)
    with open(os.path.join(dist, 'METADATA'), 'w') as f:
        f.write(DIST_INFO.format(name=name))
    with open(os.path.join(dist, 'entry_points.txt'), 'w') as f:
        f.write('[calagoapi]\n' + ''.join(f'{k} = {v}\n' for k, v in entry_points.items()))


@pytest.fixture
def site(tmp_path, monkeypatch):
    package = tmp_path / 'fake_calagoapi_ext'
    package.mkdir()
    (package / '__init__.py').write_text('')
    (package / 'targets.py').write_text(textwrap.dedent('''
        class Widget:
            def __init__(self, name):
                self.name = name
    '''))
    (package / 'members.py').write_text(textwrap.dedent('''
        from calagoapi.extensions import method
        from fake_calagoapi_ext.targets import Widget

        @method(Widget)
        def describe(self):
            return f'widget {self.name}'
    '''))
    (package / 'extension.py').write_text(textwrap.dedent('''
        from calagoapi.extensions import Extension, ExtensionMetadata, property_extension, Alias
        from fake_calagoapi_ext.targets import Widget
        from fake_calagoapi_ext.members import describe   # imported members are collected too

        @property_extension(Widget)
        def size(self):
            return len(self.name)

        class FakeExtension(Extension):
            extension_id = 'fake_ext'
            metadata = ExtensionMetadata(author='tests', version='1.0.0', schema=1)

        class RenamedExtension(Extension):
            extension_id = 'brand_new'
            aliases = [Alias('legacy_alias', deprecated=True)]
            members = []
    '''))
    (package / 'broken.py').write_text('raise ImportError("missing optional dependency")\n')
    writeDistribution(str(tmp_path), 'fake-calagoapi-ext', {
        'fake_ext': 'fake_calagoapi_ext.extension:FakeExtension',
        'old_entry_name': 'fake_calagoapi_ext.extension:RenamedExtension',
        'broken': 'fake_calagoapi_ext.broken:Nothing',
        'not_a_class': 'fake_calagoapi_ext.targets:Widget',
    })
    monkeypatch.syspath_prepend(str(tmp_path))
    yield tmp_path
    for name in list(sys.modules):
        if name.startswith('fake_calagoapi_ext'):
            del sys.modules[name]


def test_entry_point_discovery(site):
    registry = ExtensionRegistry()
    try:
        assert 'fake_calagoapi_ext.extension' not in sys.modules
        registry.enable('fake_ext')
        from fake_calagoapi_ext.targets import Widget
        widget = Widget('gear')
        assert widget.describe() == 'widget gear'
        assert widget.size == 4
        assert "entry point 'fake_ext'" in registry._origins['fake_ext']
        if sys.version_info >= (3, 10):  # 3.9 entry points do not know their distribution
            assert 'fake-calagoapi-ext' in registry._origins['fake_ext']

        # renamed ids are found through aliases declared inside the class
        with pytest.warns(ExtensionDeprecationWarning):
            assert registry.enable('legacy_alias').extension_id == 'brand_new'

        with pytest.raises(ExtensionLoadError, match="entry point 'broken'.*missing optional dependency"):
            registry.enable('broken')
        with pytest.raises(ExtensionLoadError, match='must point to a calagoapi.extensions.Extension'):
            registry.enable('not_a_class')
        with pytest.raises(ExtensionNotFoundError, match='Note: Could not load entry point'):
            registry.enable('nothing_here')
        assert {'brand_new', 'fake_ext'} <= set(registry.available())
    finally:
        registry._reset_for_tests()


def test_conflicting_entry_points(site):
    writeDistribution(str(site), 'other-ext', {'fake_ext': 'other_package.extension:OtherExtension'})
    registry = ExtensionRegistry()
    try:
        # the full scan for an alias skips the conflicting package instead of failing
        with pytest.warns(ExtensionDeprecationWarning):
            assert registry.enable('legacy_alias').extension_id == 'brand_new'
        for _ in range(2):
            with pytest.raises(ExtensionConflictError, match="Several installed packages provide the calagoapi extension 'fake_ext'"):
                registry.enable('fake_ext')
    finally:
        registry._reset_for_tests()


def test_global_api_is_exported():
    import calagoapi
    from calagoapi import extensions
    assert calagoapi.extensions is extensions
    assert isinstance(extensions.registry, ExtensionRegistry)
    for name in ('enable', 'register', 'get_extension', 'is_enabled', 'available', 'enabled_extensions'):
        assert callable(getattr(extensions, name))
    assert extensions.is_enabled('definitely_not_installed') is False
