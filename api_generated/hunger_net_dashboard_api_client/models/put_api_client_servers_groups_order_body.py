from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApiClientServersGroupsOrderBody")


@_attrs_define
class PutApiClientServersGroupsOrderBody:
    """
    Attributes:
        server_group_order (list[UUID]):
    """

    server_group_order: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_group_order = []
        for server_group_order_item_data in self.server_group_order:
            server_group_order_item = str(server_group_order_item_data)
            server_group_order.append(server_group_order_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_group_order": server_group_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_group_order = []
        _server_group_order = d.pop("server_group_order")
        for server_group_order_item_data in _server_group_order:
            server_group_order_item = UUID(server_group_order_item_data)

            server_group_order.append(server_group_order_item)

        put_api_client_servers_groups_order_body = cls(
            server_group_order=server_group_order,
        )

        put_api_client_servers_groups_order_body.additional_properties = d
        return put_api_client_servers_groups_order_body

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
