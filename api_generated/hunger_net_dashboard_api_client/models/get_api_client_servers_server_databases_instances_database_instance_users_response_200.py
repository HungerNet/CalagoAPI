from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_database_instance_user import ServerDatabaseInstanceUser


T = TypeVar("T", bound="GetApiClientServersServerDatabasesInstancesDatabaseInstanceUsersResponse200")


@_attrs_define
class GetApiClientServersServerDatabasesInstancesDatabaseInstanceUsersResponse200:
    """
    Attributes:
        users (list[ServerDatabaseInstanceUser]):
    """

    users: list[ServerDatabaseInstanceUser]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_database_instance_user import ServerDatabaseInstanceUser  # noqa: PLC0415

        d = dict(src_dict)
        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = ServerDatabaseInstanceUser.from_dict(users_item_data)

            users.append(users_item)

        get_api_client_servers_server_databases_instances_database_instance_users_response_200 = cls(
            users=users,
        )

        get_api_client_servers_server_databases_instances_database_instance_users_response_200.additional_properties = d
        return get_api_client_servers_server_databases_instances_database_instance_users_response_200

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
