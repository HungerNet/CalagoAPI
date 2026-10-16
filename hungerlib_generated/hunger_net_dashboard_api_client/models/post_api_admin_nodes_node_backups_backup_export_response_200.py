from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.directory_entry import DirectoryEntry


T = TypeVar("T", bound="PostApiAdminNodesNodeBackupsBackupExportResponse200")


@_attrs_define
class PostApiAdminNodesNodeBackupsBackupExportResponse200:
    """
    Attributes:
        entry (DirectoryEntry):
    """

    entry: DirectoryEntry
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.directory_entry import DirectoryEntry  # noqa: PLC0415

        d = dict(src_dict)
        entry = DirectoryEntry.from_dict(d.pop("entry"))

        post_api_admin_nodes_node_backups_backup_export_response_200 = cls(
            entry=entry,
        )

        post_api_admin_nodes_node_backups_backup_export_response_200.additional_properties = d
        return post_api_admin_nodes_node_backups_backup_export_response_200

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
