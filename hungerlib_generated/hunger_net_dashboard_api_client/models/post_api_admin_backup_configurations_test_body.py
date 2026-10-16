from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_disk import BackupDisk

if TYPE_CHECKING:
    from ..models.backup_configs import BackupConfigs


T = TypeVar("T", bound="PostApiAdminBackupConfigurationsTestBody")


@_attrs_define
class PostApiAdminBackupConfigurationsTestBody:
    """
    Attributes:
        node_uuid (UUID):
        backup_disk (BackupDisk):
        backup_configs (BackupConfigs):
    """

    node_uuid: UUID
    backup_disk: BackupDisk
    backup_configs: BackupConfigs
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_uuid = str(self.node_uuid)

        backup_disk = self.backup_disk.value

        backup_configs = self.backup_configs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_uuid": node_uuid,
                "backup_disk": backup_disk,
                "backup_configs": backup_configs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_configs import BackupConfigs  # noqa: PLC0415

        d = dict(src_dict)
        node_uuid = UUID(d.pop("node_uuid"))

        backup_disk = BackupDisk(d.pop("backup_disk"))

        backup_configs = BackupConfigs.from_dict(d.pop("backup_configs"))

        post_api_admin_backup_configurations_test_body = cls(
            node_uuid=node_uuid,
            backup_disk=backup_disk,
            backup_configs=backup_configs,
        )

        post_api_admin_backup_configurations_test_body.additional_properties = d
        return post_api_admin_backup_configurations_test_body

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
