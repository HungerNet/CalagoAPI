from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_database_instance_database import ServerDatabaseInstanceDatabase


T = TypeVar("T", bound="GetApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesResponse200")


@_attrs_define
class GetApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesResponse200:
    """
    Attributes:
        databases (list[ServerDatabaseInstanceDatabase]):
    """

    databases: list[ServerDatabaseInstanceDatabase]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        databases = []
        for databases_item_data in self.databases:
            databases_item = databases_item_data.to_dict()
            databases.append(databases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "databases": databases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_database_instance_database import ServerDatabaseInstanceDatabase  # noqa: PLC0415

        d = dict(src_dict)
        databases = []
        _databases = d.pop("databases")
        for databases_item_data in _databases:
            databases_item = ServerDatabaseInstanceDatabase.from_dict(databases_item_data)

            databases.append(databases_item)

        get_api_client_servers_server_databases_instances_database_instance_databases_response_200 = cls(
            databases=databases,
        )

        get_api_client_servers_server_databases_instances_database_instance_databases_response_200.additional_properties = d
        return get_api_client_servers_server_databases_instances_database_instance_databases_response_200

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
