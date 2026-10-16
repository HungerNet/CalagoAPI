from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_retention import BackupRetention


T = TypeVar("T", bound="PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody")


@_attrs_define
class PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        backup_configuration_uuid (None | Unset | UUID):
        enabled (bool | None | Unset):
        cron (None | str | Unset):  Example: 0 0 0 * * *.
        retention (BackupRetention | Unset):
        parallelism (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    backup_configuration_uuid: None | Unset | UUID = UNSET
    enabled: bool | None | Unset = UNSET
    cron: None | str | Unset = UNSET
    retention: BackupRetention | Unset = UNSET
    parallelism: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        backup_configuration_uuid: None | str | Unset
        if isinstance(self.backup_configuration_uuid, Unset):
            backup_configuration_uuid = UNSET
        elif isinstance(self.backup_configuration_uuid, UUID):
            backup_configuration_uuid = str(self.backup_configuration_uuid)
        else:
            backup_configuration_uuid = self.backup_configuration_uuid

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        cron: None | str | Unset
        if isinstance(self.cron, Unset):
            cron = UNSET
        else:
            cron = self.cron

        retention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.to_dict()

        parallelism: int | None | Unset
        if isinstance(self.parallelism, Unset):
            parallelism = UNSET
        else:
            parallelism = self.parallelism

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if backup_configuration_uuid is not UNSET:
            field_dict["backup_configuration_uuid"] = backup_configuration_uuid
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if cron is not UNSET:
            field_dict["cron"] = cron
        if retention is not UNSET:
            field_dict["retention"] = retention
        if parallelism is not UNSET:
            field_dict["parallelism"] = parallelism

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_retention import BackupRetention  # noqa: PLC0415

        d = dict(src_dict)

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

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_cron(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cron = _parse_cron(d.pop("cron", UNSET))

        _retention = d.pop("retention", UNSET)
        retention: BackupRetention | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = BackupRetention.from_dict(_retention)

        def _parse_parallelism(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parallelism = _parse_parallelism(d.pop("parallelism", UNSET))

        patch_api_admin_system_backup_policies_system_backup_policy_body = cls(
            name=name,
            description=description,
            backup_configuration_uuid=backup_configuration_uuid,
            enabled=enabled,
            cron=cron,
            retention=retention,
            parallelism=parallelism,
        )

        patch_api_admin_system_backup_policies_system_backup_policy_body.additional_properties = d
        return patch_api_admin_system_backup_policies_system_backup_policy_body

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
