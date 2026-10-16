from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiClientServersGroupsServerGroupBody")


@_attrs_define
class PatchApiClientServersGroupsServerGroupBody:
    """
    Attributes:
        name (str):
        server_order (list[UUID] | None | Unset):
    """

    name: str
    server_order: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        server_order: list[str] | None | Unset
        if isinstance(self.server_order, Unset):
            server_order = UNSET
        elif isinstance(self.server_order, list):
            server_order = []
            for server_order_type_0_item_data in self.server_order:
                server_order_type_0_item = str(server_order_type_0_item_data)
                server_order.append(server_order_type_0_item)

        else:
            server_order = self.server_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if server_order is not UNSET:
            field_dict["server_order"] = server_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_server_order(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                server_order_type_0 = []
                _server_order_type_0 = data
                for server_order_type_0_item_data in _server_order_type_0:
                    server_order_type_0_item = UUID(server_order_type_0_item_data)

                    server_order_type_0.append(server_order_type_0_item)

                return server_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        server_order = _parse_server_order(d.pop("server_order", UNSET))

        patch_api_client_servers_groups_server_group_body = cls(
            name=name,
            server_order=server_order,
        )

        patch_api_client_servers_groups_server_group_body.additional_properties = d
        return patch_api_client_servers_groups_server_group_body

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
