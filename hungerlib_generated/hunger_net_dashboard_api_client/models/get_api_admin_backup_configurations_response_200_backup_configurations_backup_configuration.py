from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_disk import BackupDisk
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_configs import BackupConfigs


T = TypeVar("T", bound="GetApiAdminBackupConfigurationsResponse200BackupConfigurationsBackupConfiguration")


@_attrs_define
class GetApiAdminBackupConfigurationsResponse200BackupConfigurationsBackupConfiguration:
    """
    Attributes:
        uuid (UUID):
        name (str):
        maintenance_enabled (bool):
        shared (bool):
        backup_disk (BackupDisk):
        backup_configs (BackupConfigs):
        created (datetime.datetime):
        description (None | str | Unset):
    """

    uuid: UUID
    name: str
    maintenance_enabled: bool
    shared: bool
    backup_disk: BackupDisk
    backup_configs: BackupConfigs
    created: datetime.datetime
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        maintenance_enabled = self.maintenance_enabled

        shared = self.shared

        backup_disk = self.backup_disk.value

        backup_configs = self.backup_configs.to_dict()

        created = self.created.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "maintenance_enabled": maintenance_enabled,
                "shared": shared,
                "backup_disk": backup_disk,
                "backup_configs": backup_configs,
                "created": created,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_configs import BackupConfigs  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        maintenance_enabled = d.pop("maintenance_enabled")

        shared = d.pop("shared")

        backup_disk = BackupDisk(d.pop("backup_disk"))

        backup_configs = BackupConfigs.from_dict(d.pop("backup_configs"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        get_api_admin_backup_configurations_response_200_backup_configurations_backup_configuration = cls(
            uuid=uuid,
            name=name,
            maintenance_enabled=maintenance_enabled,
            shared=shared,
            backup_disk=backup_disk,
            backup_configs=backup_configs,
            created=created,
            description=description,
        )

        get_api_admin_backup_configurations_response_200_backup_configurations_backup_configuration.additional_properties = d
        return get_api_admin_backup_configurations_response_200_backup_configurations_backup_configuration

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
