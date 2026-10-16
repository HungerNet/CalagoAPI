from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.streamable_archive_format import StreamableArchiveFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminNodesNodeBackupsBackupExportBody")


@_attrs_define
class PostApiAdminNodesNodeBackupsBackupExportBody:
    """
    Attributes:
        server_uuid (UUID):
        path (str):
        archive_format (StreamableArchiveFormat | Unset):
        foreground (bool | Unset):
    """

    server_uuid: UUID
    path: str
    archive_format: StreamableArchiveFormat | Unset = UNSET
    foreground: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_uuid = str(self.server_uuid)

        path = self.path

        archive_format: str | Unset = UNSET
        if not isinstance(self.archive_format, Unset):
            archive_format = self.archive_format.value

        foreground = self.foreground

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_uuid": server_uuid,
                "path": path,
            }
        )
        if archive_format is not UNSET:
            field_dict["archive_format"] = archive_format
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_uuid = UUID(d.pop("server_uuid"))

        path = d.pop("path")

        _archive_format = d.pop("archive_format", UNSET)
        archive_format: StreamableArchiveFormat | Unset
        if isinstance(_archive_format, Unset):
            archive_format = UNSET
        else:
            archive_format = StreamableArchiveFormat(_archive_format)

        foreground = d.pop("foreground", UNSET)

        post_api_admin_nodes_node_backups_backup_export_body = cls(
            server_uuid=server_uuid,
            path=path,
            archive_format=archive_format,
            foreground=foreground,
        )

        post_api_admin_nodes_node_backups_backup_export_body.additional_properties = d
        return post_api_admin_nodes_node_backups_backup_export_body

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
