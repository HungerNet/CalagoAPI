from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteApiClientServersServerBackupsGroupsBackupGroupBody")


@_attrs_define
class DeleteApiClientServersServerBackupsGroupsBackupGroupBody:
    """
    Attributes:
        lock_backups (bool | Unset):
    """

    lock_backups: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lock_backups = self.lock_backups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lock_backups is not UNSET:
            field_dict["lock_backups"] = lock_backups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lock_backups = d.pop("lock_backups", UNSET)

        delete_api_client_servers_server_backups_groups_backup_group_body = cls(
            lock_backups=lock_backups,
        )

        delete_api_client_servers_server_backups_groups_backup_group_body.additional_properties = d
        return delete_api_client_servers_server_backups_groups_backup_group_body

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
