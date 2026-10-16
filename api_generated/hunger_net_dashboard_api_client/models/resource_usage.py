from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_usage_state import ResourceUsageState

if TYPE_CHECKING:
    from ..models.resource_usage_network import ResourceUsageNetwork


T = TypeVar("T", bound="ResourceUsage")


@_attrs_define
class ResourceUsage:
    """
    Attributes:
        memory_bytes (int):
        memory_limit_bytes (int):
        disk_bytes (int):
        state (ResourceUsageState):
        network (ResourceUsageNetwork):
        cpu_absolute (float):
        cpu_limit_absolute (int):
        uptime (int):
    """

    memory_bytes: int
    memory_limit_bytes: int
    disk_bytes: int
    state: ResourceUsageState
    network: ResourceUsageNetwork
    cpu_absolute: float
    cpu_limit_absolute: int
    uptime: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory_bytes = self.memory_bytes

        memory_limit_bytes = self.memory_limit_bytes

        disk_bytes = self.disk_bytes

        state = self.state.value

        network = self.network.to_dict()

        cpu_absolute = self.cpu_absolute

        cpu_limit_absolute = self.cpu_limit_absolute

        uptime = self.uptime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memory_bytes": memory_bytes,
                "memory_limit_bytes": memory_limit_bytes,
                "disk_bytes": disk_bytes,
                "state": state,
                "network": network,
                "cpu_absolute": cpu_absolute,
                "cpu_limit_absolute": cpu_limit_absolute,
                "uptime": uptime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_usage_network import ResourceUsageNetwork  # noqa: PLC0415

        d = dict(src_dict)
        memory_bytes = d.pop("memory_bytes")

        memory_limit_bytes = d.pop("memory_limit_bytes")

        disk_bytes = d.pop("disk_bytes")

        state = ResourceUsageState(d.pop("state"))

        network = ResourceUsageNetwork.from_dict(d.pop("network"))

        cpu_absolute = d.pop("cpu_absolute")

        cpu_limit_absolute = d.pop("cpu_limit_absolute")

        uptime = d.pop("uptime")

        resource_usage = cls(
            memory_bytes=memory_bytes,
            memory_limit_bytes=memory_limit_bytes,
            disk_bytes=disk_bytes,
            state=state,
            network=network,
            cpu_absolute=cpu_absolute,
            cpu_limit_absolute=cpu_limit_absolute,
            uptime=uptime,
        )

        resource_usage.additional_properties = d
        return resource_usage

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
