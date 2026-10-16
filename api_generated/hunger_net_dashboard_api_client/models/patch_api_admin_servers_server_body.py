from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_auto_start_behavior import ServerAutoStartBehavior
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_api_server_limits import AdminApiServerLimits
    from ..models.api_server_feature_limits import ApiServerFeatureLimits
    from ..models.patch_api_admin_servers_server_body_auto_kill_type_1 import (
        PatchApiAdminServersServerBodyAutoKillType1,
    )
    from ..models.patch_api_admin_servers_server_body_labels_type_0 import PatchApiAdminServersServerBodyLabelsType0


T = TypeVar("T", bound="PatchApiAdminServersServerBody")


@_attrs_define
class PatchApiAdminServersServerBody:
    """
    Attributes:
        owner_uuid (None | Unset | UUID):
        egg_uuid (None | Unset | UUID):
        backup_configuration_uuid (None | Unset | UUID):
        suspended (bool | None | Unset):
        external_id (None | str | Unset):
        name (None | str | Unset):
        description (None | str | Unset):
        limits (AdminApiServerLimits | None | Unset):
        pinned_cpus (list[int] | None | Unset):
        startup (None | str | Unset):
        image (None | str | Unset):
        labels (None | PatchApiAdminServersServerBodyLabelsType0 | Unset):
        auto_kill (None | PatchApiAdminServersServerBodyAutoKillType1 | Unset):
        auto_start_behavior (None | ServerAutoStartBehavior | Unset):
        timezone (None | str | Unset):
        hugepages_passthrough_enabled (bool | None | Unset):
        kvm_passthrough_enabled (bool | None | Unset):
        feature_limits (ApiServerFeatureLimits | None | Unset):
    """

    owner_uuid: None | Unset | UUID = UNSET
    egg_uuid: None | Unset | UUID = UNSET
    backup_configuration_uuid: None | Unset | UUID = UNSET
    suspended: bool | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    limits: AdminApiServerLimits | None | Unset = UNSET
    pinned_cpus: list[int] | None | Unset = UNSET
    startup: None | str | Unset = UNSET
    image: None | str | Unset = UNSET
    labels: None | PatchApiAdminServersServerBodyLabelsType0 | Unset = UNSET
    auto_kill: None | PatchApiAdminServersServerBodyAutoKillType1 | Unset = UNSET
    auto_start_behavior: None | ServerAutoStartBehavior | Unset = UNSET
    timezone: None | str | Unset = UNSET
    hugepages_passthrough_enabled: bool | None | Unset = UNSET
    kvm_passthrough_enabled: bool | None | Unset = UNSET
    feature_limits: ApiServerFeatureLimits | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.admin_api_server_limits import AdminApiServerLimits  # noqa: PLC0415
        from ..models.api_server_feature_limits import ApiServerFeatureLimits  # noqa: PLC0415
        from ..models.patch_api_admin_servers_server_body_auto_kill_type_1 import (
            PatchApiAdminServersServerBodyAutoKillType1,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_servers_server_body_labels_type_0 import PatchApiAdminServersServerBodyLabelsType0  # noqa: PLC0415

        owner_uuid: None | str | Unset
        if isinstance(self.owner_uuid, Unset):
            owner_uuid = UNSET
        elif isinstance(self.owner_uuid, UUID):
            owner_uuid = str(self.owner_uuid)
        else:
            owner_uuid = self.owner_uuid

        egg_uuid: None | str | Unset
        if isinstance(self.egg_uuid, Unset):
            egg_uuid = UNSET
        elif isinstance(self.egg_uuid, UUID):
            egg_uuid = str(self.egg_uuid)
        else:
            egg_uuid = self.egg_uuid

        backup_configuration_uuid: None | str | Unset
        if isinstance(self.backup_configuration_uuid, Unset):
            backup_configuration_uuid = UNSET
        elif isinstance(self.backup_configuration_uuid, UUID):
            backup_configuration_uuid = str(self.backup_configuration_uuid)
        else:
            backup_configuration_uuid = self.backup_configuration_uuid

        suspended: bool | None | Unset
        if isinstance(self.suspended, Unset):
            suspended = UNSET
        else:
            suspended = self.suspended

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        limits: dict[str, Any] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, AdminApiServerLimits):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

        pinned_cpus: list[int] | None | Unset
        if isinstance(self.pinned_cpus, Unset):
            pinned_cpus = UNSET
        elif isinstance(self.pinned_cpus, list):
            pinned_cpus = self.pinned_cpus

        else:
            pinned_cpus = self.pinned_cpus

        startup: None | str | Unset
        if isinstance(self.startup, Unset):
            startup = UNSET
        else:
            startup = self.startup

        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        labels: dict[str, Any] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, PatchApiAdminServersServerBodyLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        auto_kill: dict[str, Any] | None | Unset
        if isinstance(self.auto_kill, Unset):
            auto_kill = UNSET
        elif isinstance(self.auto_kill, PatchApiAdminServersServerBodyAutoKillType1):
            auto_kill = self.auto_kill.to_dict()
        else:
            auto_kill = self.auto_kill

        auto_start_behavior: None | str | Unset
        if isinstance(self.auto_start_behavior, Unset):
            auto_start_behavior = UNSET
        elif isinstance(self.auto_start_behavior, ServerAutoStartBehavior):
            auto_start_behavior = self.auto_start_behavior.value
        else:
            auto_start_behavior = self.auto_start_behavior

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        hugepages_passthrough_enabled: bool | None | Unset
        if isinstance(self.hugepages_passthrough_enabled, Unset):
            hugepages_passthrough_enabled = UNSET
        else:
            hugepages_passthrough_enabled = self.hugepages_passthrough_enabled

        kvm_passthrough_enabled: bool | None | Unset
        if isinstance(self.kvm_passthrough_enabled, Unset):
            kvm_passthrough_enabled = UNSET
        else:
            kvm_passthrough_enabled = self.kvm_passthrough_enabled

        feature_limits: dict[str, Any] | None | Unset
        if isinstance(self.feature_limits, Unset):
            feature_limits = UNSET
        elif isinstance(self.feature_limits, ApiServerFeatureLimits):
            feature_limits = self.feature_limits.to_dict()
        else:
            feature_limits = self.feature_limits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_uuid is not UNSET:
            field_dict["owner_uuid"] = owner_uuid
        if egg_uuid is not UNSET:
            field_dict["egg_uuid"] = egg_uuid
        if backup_configuration_uuid is not UNSET:
            field_dict["backup_configuration_uuid"] = backup_configuration_uuid
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if limits is not UNSET:
            field_dict["limits"] = limits
        if pinned_cpus is not UNSET:
            field_dict["pinned_cpus"] = pinned_cpus
        if startup is not UNSET:
            field_dict["startup"] = startup
        if image is not UNSET:
            field_dict["image"] = image
        if labels is not UNSET:
            field_dict["labels"] = labels
        if auto_kill is not UNSET:
            field_dict["auto_kill"] = auto_kill
        if auto_start_behavior is not UNSET:
            field_dict["auto_start_behavior"] = auto_start_behavior
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if hugepages_passthrough_enabled is not UNSET:
            field_dict["hugepages_passthrough_enabled"] = hugepages_passthrough_enabled
        if kvm_passthrough_enabled is not UNSET:
            field_dict["kvm_passthrough_enabled"] = kvm_passthrough_enabled
        if feature_limits is not UNSET:
            field_dict["feature_limits"] = feature_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_api_server_limits import AdminApiServerLimits  # noqa: PLC0415
        from ..models.api_server_feature_limits import ApiServerFeatureLimits  # noqa: PLC0415
        from ..models.patch_api_admin_servers_server_body_auto_kill_type_1 import (
            PatchApiAdminServersServerBodyAutoKillType1,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_servers_server_body_labels_type_0 import PatchApiAdminServersServerBodyLabelsType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_owner_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_uuid_type_0 = UUID(data)

                return owner_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_uuid = _parse_owner_uuid(d.pop("owner_uuid", UNSET))

        def _parse_egg_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                egg_uuid_type_0 = UUID(data)

                return egg_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        egg_uuid = _parse_egg_uuid(d.pop("egg_uuid", UNSET))

        def _parse_backup_configuration_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_configuration_uuid_type_0 = UUID(data)

                return backup_configuration_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_configuration_uuid = _parse_backup_configuration_uuid(d.pop("backup_configuration_uuid", UNSET))

        def _parse_suspended(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        suspended = _parse_suspended(d.pop("suspended", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_limits(data: object) -> AdminApiServerLimits | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limits_type_1 = AdminApiServerLimits.from_dict(data)

                return limits_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AdminApiServerLimits | None | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        def _parse_pinned_cpus(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pinned_cpus_type_0 = cast(list[int], data)

                return pinned_cpus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        pinned_cpus = _parse_pinned_cpus(d.pop("pinned_cpus", UNSET))

        def _parse_startup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        startup = _parse_startup(d.pop("startup", UNSET))

        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_labels(data: object) -> None | PatchApiAdminServersServerBodyLabelsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = PatchApiAdminServersServerBodyLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminServersServerBodyLabelsType0 | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_auto_kill(data: object) -> None | PatchApiAdminServersServerBodyAutoKillType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auto_kill_type_1 = PatchApiAdminServersServerBodyAutoKillType1.from_dict(data)

                return auto_kill_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminServersServerBodyAutoKillType1 | Unset, data)

        auto_kill = _parse_auto_kill(d.pop("auto_kill", UNSET))

        def _parse_auto_start_behavior(data: object) -> None | ServerAutoStartBehavior | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auto_start_behavior_type_1 = ServerAutoStartBehavior(data)

                return auto_start_behavior_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerAutoStartBehavior | Unset, data)

        auto_start_behavior = _parse_auto_start_behavior(d.pop("auto_start_behavior", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_hugepages_passthrough_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hugepages_passthrough_enabled = _parse_hugepages_passthrough_enabled(
            d.pop("hugepages_passthrough_enabled", UNSET)
        )

        def _parse_kvm_passthrough_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        kvm_passthrough_enabled = _parse_kvm_passthrough_enabled(d.pop("kvm_passthrough_enabled", UNSET))

        def _parse_feature_limits(data: object) -> ApiServerFeatureLimits | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feature_limits_type_1 = ApiServerFeatureLimits.from_dict(data)

                return feature_limits_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiServerFeatureLimits | None | Unset, data)

        feature_limits = _parse_feature_limits(d.pop("feature_limits", UNSET))

        patch_api_admin_servers_server_body = cls(
            owner_uuid=owner_uuid,
            egg_uuid=egg_uuid,
            backup_configuration_uuid=backup_configuration_uuid,
            suspended=suspended,
            external_id=external_id,
            name=name,
            description=description,
            limits=limits,
            pinned_cpus=pinned_cpus,
            startup=startup,
            image=image,
            labels=labels,
            auto_kill=auto_kill,
            auto_start_behavior=auto_start_behavior,
            timezone=timezone,
            hugepages_passthrough_enabled=hugepages_passthrough_enabled,
            kvm_passthrough_enabled=kvm_passthrough_enabled,
            feature_limits=feature_limits,
        )

        patch_api_admin_servers_server_body.additional_properties = d
        return patch_api_admin_servers_server_body

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
