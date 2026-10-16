from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_locations_location_database_hosts_response_200_database_hosts import (
        GetApiAdminLocationsLocationDatabaseHostsResponse200DatabaseHosts,
    )


T = TypeVar("T", bound="GetApiAdminLocationsLocationDatabaseHostsResponse200")


@_attrs_define
class GetApiAdminLocationsLocationDatabaseHostsResponse200:
    """
    Attributes:
        database_hosts (GetApiAdminLocationsLocationDatabaseHostsResponse200DatabaseHosts):
    """

    database_hosts: GetApiAdminLocationsLocationDatabaseHostsResponse200DatabaseHosts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_hosts = self.database_hosts.to_dict()

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
        from ..models.get_api_admin_locations_location_database_hosts_response_200_database_hosts import (
            GetApiAdminLocationsLocationDatabaseHostsResponse200DatabaseHosts,  # noqa: PLC0415
        )

        d = dict(src_dict)
        database_hosts = GetApiAdminLocationsLocationDatabaseHostsResponse200DatabaseHosts.from_dict(
            d.pop("database_hosts")
        )

        get_api_admin_locations_location_database_hosts_response_200 = cls(
            database_hosts=database_hosts,
        )

        get_api_admin_locations_location_database_hosts_response_200.additional_properties = d
        return get_api_admin_locations_location_database_hosts_response_200

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
