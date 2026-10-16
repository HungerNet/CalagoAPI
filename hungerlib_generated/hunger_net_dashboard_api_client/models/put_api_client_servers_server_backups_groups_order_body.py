from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApiClientServersServerBackupsGroupsOrderBody")


@_attrs_define
class PutApiClientServersServerBackupsGroupsOrderBody:
    """
    Attributes:
        backup_group_order (list[UUID]):
    """

    backup_group_order: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_group_order = []
        for backup_group_order_item_data in self.backup_group_order:
            backup_group_order_item = str(backup_group_order_item_data)
            backup_group_order.append(backup_group_order_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backup_group_order": backup_group_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_group_order = []
        _backup_group_order = d.pop("backup_group_order")
        for backup_group_order_item_data in _backup_group_order:
            backup_group_order_item = UUID(backup_group_order_item_data)

            backup_group_order.append(backup_group_order_item)

        put_api_client_servers_server_backups_groups_order_body = cls(
            backup_group_order=backup_group_order,
        )

        put_api_client_servers_server_backups_groups_order_body.additional_properties = d
        return put_api_client_servers_server_backups_groups_order_body

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
