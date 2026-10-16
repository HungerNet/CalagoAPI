from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminNodesCapacitiesResponse200AllocatedAdditionalProperty")


@_attrs_define
class GetApiAdminNodesCapacitiesResponse200AllocatedAdditionalProperty:
    """
    Attributes:
        servers (int):
        cpu (int):
        memory (int):
        memory_overhead (int):
        disk (int):
    """

    servers: int
    cpu: int
    memory: int
    memory_overhead: int
    disk: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        servers = self.servers

        cpu = self.cpu

        memory = self.memory

        memory_overhead = self.memory_overhead

        disk = self.disk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "servers": servers,
                "cpu": cpu,
                "memory": memory,
                "memory_overhead": memory_overhead,
                "disk": disk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        servers = d.pop("servers")

        cpu = d.pop("cpu")

        memory = d.pop("memory")

        memory_overhead = d.pop("memory_overhead")

        disk = d.pop("disk")

        get_api_admin_nodes_capacities_response_200_allocated_additional_property = cls(
            servers=servers,
            cpu=cpu,
            memory=memory,
            memory_overhead=memory_overhead,
            disk=disk,
        )

        get_api_admin_nodes_capacities_response_200_allocated_additional_property.additional_properties = d
        return get_api_admin_nodes_capacities_response_200_allocated_additional_property

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
