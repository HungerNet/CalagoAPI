from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_server_group import UserServerGroup


T = TypeVar("T", bound="GetApiClientServersGroupsResponse200")


@_attrs_define
class GetApiClientServersGroupsResponse200:
    """
    Attributes:
        server_groups (list[UserServerGroup]):
    """

    server_groups: list[UserServerGroup]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_groups = []
        for server_groups_item_data in self.server_groups:
            server_groups_item = server_groups_item_data.to_dict()
            server_groups.append(server_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_groups": server_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_server_group import UserServerGroup  # noqa: PLC0415

        d = dict(src_dict)
        server_groups = []
        _server_groups = d.pop("server_groups")
        for server_groups_item_data in _server_groups:
            server_groups_item = UserServerGroup.from_dict(server_groups_item_data)

            server_groups.append(server_groups_item)

        get_api_client_servers_groups_response_200 = cls(
            server_groups=server_groups,
        )

        get_api_client_servers_groups_response_200.additional_properties = d
        return get_api_client_servers_groups_response_200

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
