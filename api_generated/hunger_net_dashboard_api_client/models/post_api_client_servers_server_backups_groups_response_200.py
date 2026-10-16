from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_backup_group import ServerBackupGroup


T = TypeVar("T", bound="PostApiClientServersServerBackupsGroupsResponse200")


@_attrs_define
class PostApiClientServersServerBackupsGroupsResponse200:
    """
    Attributes:
        backup_group (ServerBackupGroup):
    """

    backup_group: ServerBackupGroup
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_group = self.backup_group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backup_group": backup_group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_backup_group import ServerBackupGroup  # noqa: PLC0415

        d = dict(src_dict)
        backup_group = ServerBackupGroup.from_dict(d.pop("backup_group"))

        post_api_client_servers_server_backups_groups_response_200 = cls(
            backup_group=backup_group,
        )

        post_api_client_servers_server_backups_groups_response_200.additional_properties = d
        return post_api_client_servers_server_backups_groups_response_200

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
