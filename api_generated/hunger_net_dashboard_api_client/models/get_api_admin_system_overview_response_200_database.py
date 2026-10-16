from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminSystemOverviewResponse200Database")


@_attrs_define
class GetApiAdminSystemOverviewResponse200Database:
    """
    Attributes:
        version (str):
        size_bytes (int):
        total_read_connections (int):
        idle_read_connections (int):
        total_write_connections (int):
        idle_write_connections (int):
    """

    version: str
    size_bytes: int
    total_read_connections: int
    idle_read_connections: int
    total_write_connections: int
    idle_write_connections: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        size_bytes = self.size_bytes

        total_read_connections = self.total_read_connections

        idle_read_connections = self.idle_read_connections

        total_write_connections = self.total_write_connections

        idle_write_connections = self.idle_write_connections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "size_bytes": size_bytes,
                "total_read_connections": total_read_connections,
                "idle_read_connections": idle_read_connections,
                "total_write_connections": total_write_connections,
                "idle_write_connections": idle_write_connections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        size_bytes = d.pop("size_bytes")

        total_read_connections = d.pop("total_read_connections")

        idle_read_connections = d.pop("idle_read_connections")

        total_write_connections = d.pop("total_write_connections")

        idle_write_connections = d.pop("idle_write_connections")

        get_api_admin_system_overview_response_200_database = cls(
            version=version,
            size_bytes=size_bytes,
            total_read_connections=total_read_connections,
            idle_read_connections=idle_read_connections,
            total_write_connections=total_write_connections,
            idle_write_connections=idle_write_connections,
        )

        get_api_admin_system_overview_response_200_database.additional_properties = d
        return get_api_admin_system_overview_response_200_database

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
