from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiClientServersGroupsBody")


@_attrs_define
class PostApiClientServersGroupsBody:
    """
    Attributes:
        name (str):
        server_order (list[UUID]):
    """

    name: str
    server_order: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        server_order = []
        for server_order_item_data in self.server_order:
            server_order_item = str(server_order_item_data)
            server_order.append(server_order_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "server_order": server_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        server_order = []
        _server_order = d.pop("server_order")
        for server_order_item_data in _server_order:
            server_order_item = UUID(server_order_item_data)

            server_order.append(server_order_item)

        post_api_client_servers_groups_body = cls(
            name=name,
            server_order=server_order,
        )

        post_api_client_servers_groups_body.additional_properties = d
        return post_api_client_servers_groups_body

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
