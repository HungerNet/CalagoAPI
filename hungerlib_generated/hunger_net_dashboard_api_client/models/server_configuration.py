from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_configuration_auto_start_behavior import ServerConfigurationAutoStartBehavior
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_configuration_allocations import ServerConfigurationAllocations
    from ..models.server_configuration_auto_kill import ServerConfigurationAutoKill
    from ..models.server_configuration_build import ServerConfigurationBuild
    from ..models.server_configuration_container import ServerConfigurationContainer
    from ..models.server_configuration_devices_item import ServerConfigurationDevicesItem
    from ..models.server_configuration_egg import ServerConfigurationEgg
    from ..models.server_configuration_environment import ServerConfigurationEnvironment
    from ..models.server_configuration_features import ServerConfigurationFeatures
    from ..models.server_configuration_firewall_item import ServerConfigurationFirewallItem
    from ..models.server_configuration_labels import ServerConfigurationLabels
    from ..models.server_configuration_meta import ServerConfigurationMeta
    from ..models.server_configuration_mounts_item import ServerConfigurationMountsItem
    from ..models.server_configuration_schedules_item import ServerConfigurationSchedulesItem


T = TypeVar("T", bound="ServerConfiguration")


@_attrs_define
class ServerConfiguration:
    """
    Attributes:
        uuid (UUID):
        meta (ServerConfigurationMeta):
        suspended (bool):
        invocation (str):
        skip_egg_scripts (bool):
        environment (ServerConfigurationEnvironment):
        labels (ServerConfigurationLabels):
        backups (list[UUID]):
        schedules (list[ServerConfigurationSchedulesItem]):
        allocations (ServerConfigurationAllocations):
        build (ServerConfigurationBuild):
        mounts (list[ServerConfigurationMountsItem]):
        devices (list[ServerConfigurationDevicesItem]):
        firewall (list[ServerConfigurationFirewallItem]):
        egg (ServerConfigurationEgg):
        container (ServerConfigurationContainer):
        auto_kill (ServerConfigurationAutoKill):
        auto_start_behavior (ServerConfigurationAutoStartBehavior):
        features (ServerConfigurationFeatures):
        start_on_completion (bool | None | Unset):
        entrypoint (list[str] | None | Unset):
    """

    uuid: UUID
    meta: ServerConfigurationMeta
    suspended: bool
    invocation: str
    skip_egg_scripts: bool
    environment: ServerConfigurationEnvironment
    labels: ServerConfigurationLabels
    backups: list[UUID]
    schedules: list[ServerConfigurationSchedulesItem]
    allocations: ServerConfigurationAllocations
    build: ServerConfigurationBuild
    mounts: list[ServerConfigurationMountsItem]
    devices: list[ServerConfigurationDevicesItem]
    firewall: list[ServerConfigurationFirewallItem]
    egg: ServerConfigurationEgg
    container: ServerConfigurationContainer
    auto_kill: ServerConfigurationAutoKill
    auto_start_behavior: ServerConfigurationAutoStartBehavior
    features: ServerConfigurationFeatures
    start_on_completion: bool | None | Unset = UNSET
    entrypoint: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        meta = self.meta.to_dict()

        suspended = self.suspended

        invocation = self.invocation

        skip_egg_scripts = self.skip_egg_scripts

        environment = self.environment.to_dict()

        labels = self.labels.to_dict()

        backups = []
        for backups_item_data in self.backups:
            backups_item = str(backups_item_data)
            backups.append(backups_item)

        schedules = []
        for schedules_item_data in self.schedules:
            schedules_item = schedules_item_data.to_dict()
            schedules.append(schedules_item)

        allocations = self.allocations.to_dict()

        build = self.build.to_dict()

        mounts = []
        for mounts_item_data in self.mounts:
            mounts_item = mounts_item_data.to_dict()
            mounts.append(mounts_item)

        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()
            devices.append(devices_item)

        firewall = []
        for firewall_item_data in self.firewall:
            firewall_item = firewall_item_data.to_dict()
            firewall.append(firewall_item)

        egg = self.egg.to_dict()

        container = self.container.to_dict()

        auto_kill = self.auto_kill.to_dict()

        auto_start_behavior = self.auto_start_behavior.value

        features = self.features.to_dict()

        start_on_completion: bool | None | Unset
        if isinstance(self.start_on_completion, Unset):
            start_on_completion = UNSET
        else:
            start_on_completion = self.start_on_completion

        entrypoint: list[str] | None | Unset
        if isinstance(self.entrypoint, Unset):
            entrypoint = UNSET
        elif isinstance(self.entrypoint, list):
            entrypoint = self.entrypoint

        else:
            entrypoint = self.entrypoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "meta": meta,
                "suspended": suspended,
                "invocation": invocation,
                "skip_egg_scripts": skip_egg_scripts,
                "environment": environment,
                "labels": labels,
                "backups": backups,
                "schedules": schedules,
                "allocations": allocations,
                "build": build,
                "mounts": mounts,
                "devices": devices,
                "firewall": firewall,
                "egg": egg,
                "container": container,
                "auto_kill": auto_kill,
                "auto_start_behavior": auto_start_behavior,
                "features": features,
            }
        )
        if start_on_completion is not UNSET:
            field_dict["start_on_completion"] = start_on_completion
        if entrypoint is not UNSET:
            field_dict["entrypoint"] = entrypoint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_configuration_allocations import ServerConfigurationAllocations  # noqa: PLC0415
        from ..models.server_configuration_auto_kill import ServerConfigurationAutoKill  # noqa: PLC0415
        from ..models.server_configuration_build import ServerConfigurationBuild  # noqa: PLC0415
        from ..models.server_configuration_container import ServerConfigurationContainer  # noqa: PLC0415
        from ..models.server_configuration_devices_item import ServerConfigurationDevicesItem  # noqa: PLC0415
        from ..models.server_configuration_egg import ServerConfigurationEgg  # noqa: PLC0415
        from ..models.server_configuration_environment import ServerConfigurationEnvironment  # noqa: PLC0415
        from ..models.server_configuration_features import ServerConfigurationFeatures  # noqa: PLC0415
        from ..models.server_configuration_firewall_item import ServerConfigurationFirewallItem  # noqa: PLC0415
        from ..models.server_configuration_labels import ServerConfigurationLabels  # noqa: PLC0415
        from ..models.server_configuration_meta import ServerConfigurationMeta  # noqa: PLC0415
        from ..models.server_configuration_mounts_item import ServerConfigurationMountsItem  # noqa: PLC0415
        from ..models.server_configuration_schedules_item import ServerConfigurationSchedulesItem  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        meta = ServerConfigurationMeta.from_dict(d.pop("meta"))

        suspended = d.pop("suspended")

        invocation = d.pop("invocation")

        skip_egg_scripts = d.pop("skip_egg_scripts")

        environment = ServerConfigurationEnvironment.from_dict(d.pop("environment"))

        labels = ServerConfigurationLabels.from_dict(d.pop("labels"))

        backups = []
        _backups = d.pop("backups")
        for backups_item_data in _backups:
            backups_item = UUID(backups_item_data)

            backups.append(backups_item)

        schedules = []
        _schedules = d.pop("schedules")
        for schedules_item_data in _schedules:
            schedules_item = ServerConfigurationSchedulesItem.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        allocations = ServerConfigurationAllocations.from_dict(d.pop("allocations"))

        build = ServerConfigurationBuild.from_dict(d.pop("build"))

        mounts = []
        _mounts = d.pop("mounts")
        for mounts_item_data in _mounts:
            mounts_item = ServerConfigurationMountsItem.from_dict(mounts_item_data)

            mounts.append(mounts_item)

        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = ServerConfigurationDevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        firewall = []
        _firewall = d.pop("firewall")
        for firewall_item_data in _firewall:
            firewall_item = ServerConfigurationFirewallItem.from_dict(firewall_item_data)

            firewall.append(firewall_item)

        egg = ServerConfigurationEgg.from_dict(d.pop("egg"))

        container = ServerConfigurationContainer.from_dict(d.pop("container"))

        auto_kill = ServerConfigurationAutoKill.from_dict(d.pop("auto_kill"))

        auto_start_behavior = ServerConfigurationAutoStartBehavior(d.pop("auto_start_behavior"))

        features = ServerConfigurationFeatures.from_dict(d.pop("features"))

        def _parse_start_on_completion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        start_on_completion = _parse_start_on_completion(d.pop("start_on_completion", UNSET))

        def _parse_entrypoint(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entrypoint_type_0 = cast(list[str], data)

                return entrypoint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        entrypoint = _parse_entrypoint(d.pop("entrypoint", UNSET))

        server_configuration = cls(
            uuid=uuid,
            meta=meta,
            suspended=suspended,
            invocation=invocation,
            skip_egg_scripts=skip_egg_scripts,
            environment=environment,
            labels=labels,
            backups=backups,
            schedules=schedules,
            allocations=allocations,
            build=build,
            mounts=mounts,
            devices=devices,
            firewall=firewall,
            egg=egg,
            container=container,
            auto_kill=auto_kill,
            auto_start_behavior=auto_start_behavior,
            features=features,
            start_on_completion=start_on_completion,
            entrypoint=entrypoint,
        )

        server_configuration.additional_properties = d
        return server_configuration

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
