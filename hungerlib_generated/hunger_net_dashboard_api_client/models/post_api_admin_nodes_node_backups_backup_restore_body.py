from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminNodesNodeBackupsBackupRestoreBody")


@_attrs_define
class PostApiAdminNodesNodeBackupsBackupRestoreBody:
    """
    Attributes:
        server_uuid (UUID):
        truncate_directory (bool | Unset):
        restore_startup (bool | Unset):
    """

    server_uuid: UUID
    truncate_directory: bool | Unset = UNSET
    restore_startup: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_uuid = str(self.server_uuid)

        truncate_directory = self.truncate_directory

        restore_startup = self.restore_startup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_uuid": server_uuid,
            }
        )
        if truncate_directory is not UNSET:
            field_dict["truncate_directory"] = truncate_directory
        if restore_startup is not UNSET:
            field_dict["restore_startup"] = restore_startup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_uuid = UUID(d.pop("server_uuid"))

        truncate_directory = d.pop("truncate_directory", UNSET)

        restore_startup = d.pop("restore_startup", UNSET)

        post_api_admin_nodes_node_backups_backup_restore_body = cls(
            server_uuid=server_uuid,
            truncate_directory=truncate_directory,
            restore_startup=restore_startup,
        )

        post_api_admin_nodes_node_backups_backup_restore_body.additional_properties = d
        return post_api_admin_nodes_node_backups_backup_restore_body

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
