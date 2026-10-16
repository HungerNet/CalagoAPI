from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserServerGroup")


@_attrs_define
class UserServerGroup:
    """
    Attributes:
        uuid (UUID):
        name (str):
        order (int):
        server_order (list[UUID]):
        created (datetime.datetime):
    """

    uuid: UUID
    name: str
    order: int
    server_order: list[UUID]
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        order = self.order

        server_order = []
        for server_order_item_data in self.server_order:
            server_order_item = str(server_order_item_data)
            server_order.append(server_order_item)

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "order": order,
                "server_order": server_order,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        order = d.pop("order")

        server_order = []
        _server_order = d.pop("server_order")
        for server_order_item_data in _server_order:
            server_order_item = UUID(server_order_item_data)

            server_order.append(server_order_item)

        created = datetime.datetime.fromisoformat(d.pop("created"))

        user_server_group = cls(
            uuid=uuid,
            name=name,
            order=order,
            server_order=server_order,
            created=created,
        )

        user_server_group.additional_properties = d
        return user_server_group

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
