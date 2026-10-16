from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_client_servers_server_databases_instances_database_instance_resources_response_200_resources_state import (
    GetApiClientServersServerDatabasesInstancesDatabaseInstanceResourcesResponse200ResourcesState,
)

T = TypeVar("T", bound="GetApiClientServersServerDatabasesInstancesDatabaseInstanceResourcesResponse200Resources")


@_attrs_define
class GetApiClientServersServerDatabasesInstancesDatabaseInstanceResourcesResponse200Resources:
    """
    Attributes:
        memory_bytes (int):
        memory_limit_bytes (int):
        disk_bytes (int):
        state (GetApiClientServersServerDatabasesInstancesDatabaseInstanceResourcesResponse200ResourcesState):
        cpu_absolute (float):
        uptime (int):
    """

    memory_bytes: int
    memory_limit_bytes: int
    disk_bytes: int
    state: GetApiClientServersServerDatabasesInstancesDatabaseInstanceResourcesResponse200ResourcesState
    cpu_absolute: float
    uptime: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory_bytes = self.memory_bytes

        memory_limit_bytes = self.memory_limit_bytes

        disk_bytes = self.disk_bytes

        state = self.state.value

        cpu_absolute = self.cpu_absolute

        uptime = self.uptime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memory_bytes": memory_bytes,
                "memory_limit_bytes": memory_limit_bytes,
                "disk_bytes": disk_bytes,
                "state": state,
                "cpu_absolute": cpu_absolute,
                "uptime": uptime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memory_bytes = d.pop("memory_bytes")

        memory_limit_bytes = d.pop("memory_limit_bytes")

        disk_bytes = d.pop("disk_bytes")

        state = GetApiClientServersServerDatabasesInstancesDatabaseInstanceResourcesResponse200ResourcesState(
            d.pop("state")
        )

        cpu_absolute = d.pop("cpu_absolute")

        uptime = d.pop("uptime")

        get_api_client_servers_server_databases_instances_database_instance_resources_response_200_resources = cls(
            memory_bytes=memory_bytes,
            memory_limit_bytes=memory_limit_bytes,
            disk_bytes=disk_bytes,
            state=state,
            cpu_absolute=cpu_absolute,
            uptime=uptime,
        )

        get_api_client_servers_server_databases_instances_database_instance_resources_response_200_resources.additional_properties = d
        return get_api_client_servers_server_databases_instances_database_instance_resources_response_200_resources

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
