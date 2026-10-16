from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.database_host import DatabaseHost


T = TypeVar("T", bound="GetApiClientServersServerDatabasesHostsResponse200")


@_attrs_define
class GetApiClientServersServerDatabasesHostsResponse200:
    """
    Attributes:
        database_hosts (list[DatabaseHost]):
    """

    database_hosts: list[DatabaseHost]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_hosts = []
        for database_hosts_item_data in self.database_hosts:
            database_hosts_item = database_hosts_item_data.to_dict()
            database_hosts.append(database_hosts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database_hosts": database_hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_host import DatabaseHost  # noqa: PLC0415

        d = dict(src_dict)
        database_hosts = []
        _database_hosts = d.pop("database_hosts")
        for database_hosts_item_data in _database_hosts:
            database_hosts_item = DatabaseHost.from_dict(database_hosts_item_data)

            database_hosts.append(database_hosts_item)

        get_api_client_servers_server_databases_hosts_response_200 = cls(
            database_hosts=database_hosts,
        )

        get_api_client_servers_server_databases_hosts_response_200.additional_properties = d
        return get_api_client_servers_server_databases_hosts_response_200

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
