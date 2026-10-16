from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_disk import BackupDisk
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_configs import BackupConfigs


T = TypeVar("T", bound="PatchApiAdminBackupConfigurationsBackupConfigurationBody")


@_attrs_define
class PatchApiAdminBackupConfigurationsBackupConfigurationBody:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        maintenance_enabled (bool | None | Unset):
        shared (bool | None | Unset):
        backup_disk (BackupDisk | None | Unset):
        backup_configs (BackupConfigs | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    maintenance_enabled: bool | None | Unset = UNSET
    shared: bool | None | Unset = UNSET
    backup_disk: BackupDisk | None | Unset = UNSET
    backup_configs: BackupConfigs | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_configs import BackupConfigs  # noqa: PLC0415

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

        maintenance_enabled: bool | None | Unset
        if isinstance(self.maintenance_enabled, Unset):
            maintenance_enabled = UNSET
        else:
            maintenance_enabled = self.maintenance_enabled

        shared: bool | None | Unset
        if isinstance(self.shared, Unset):
            shared = UNSET
        else:
            shared = self.shared

        backup_disk: None | str | Unset
        if isinstance(self.backup_disk, Unset):
            backup_disk = UNSET
        elif isinstance(self.backup_disk, BackupDisk):
            backup_disk = self.backup_disk.value
        else:
            backup_disk = self.backup_disk

        backup_configs: dict[str, Any] | None | Unset
        if isinstance(self.backup_configs, Unset):
            backup_configs = UNSET
        elif isinstance(self.backup_configs, BackupConfigs):
            backup_configs = self.backup_configs.to_dict()
        else:
            backup_configs = self.backup_configs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if maintenance_enabled is not UNSET:
            field_dict["maintenance_enabled"] = maintenance_enabled
        if shared is not UNSET:
            field_dict["shared"] = shared
        if backup_disk is not UNSET:
            field_dict["backup_disk"] = backup_disk
        if backup_configs is not UNSET:
            field_dict["backup_configs"] = backup_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_configs import BackupConfigs  # noqa: PLC0415

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

        def _parse_maintenance_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        maintenance_enabled = _parse_maintenance_enabled(d.pop("maintenance_enabled", UNSET))

        def _parse_shared(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        shared = _parse_shared(d.pop("shared", UNSET))

        def _parse_backup_disk(data: object) -> BackupDisk | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_disk_type_1 = BackupDisk(data)

                return backup_disk_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupDisk | None | Unset, data)

        backup_disk = _parse_backup_disk(d.pop("backup_disk", UNSET))

        def _parse_backup_configs(data: object) -> BackupConfigs | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                backup_configs_type_1 = BackupConfigs.from_dict(data)

                return backup_configs_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupConfigs | None | Unset, data)

        backup_configs = _parse_backup_configs(d.pop("backup_configs", UNSET))

        patch_api_admin_backup_configurations_backup_configuration_body = cls(
            name=name,
            description=description,
            maintenance_enabled=maintenance_enabled,
            shared=shared,
            backup_disk=backup_disk,
            backup_configs=backup_configs,
        )

        patch_api_admin_backup_configurations_backup_configuration_body.additional_properties = d
        return patch_api_admin_backup_configurations_backup_configuration_body

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
