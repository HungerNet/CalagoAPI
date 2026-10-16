from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceUsageNetwork")


@_attrs_define
class ResourceUsageNetwork:
    """
    Attributes:
        rx_bytes (int):
        rx_packets (int):
        tx_bytes (int):
        tx_packets (int):
    """

    rx_bytes: int
    rx_packets: int
    tx_bytes: int
    tx_packets: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rx_bytes = self.rx_bytes

        rx_packets = self.rx_packets

        tx_bytes = self.tx_bytes

        tx_packets = self.tx_packets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rx_bytes": rx_bytes,
                "rx_packets": rx_packets,
                "tx_bytes": tx_bytes,
                "tx_packets": tx_packets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rx_bytes = d.pop("rx_bytes")

        rx_packets = d.pop("rx_packets")

        tx_bytes = d.pop("tx_bytes")

        tx_packets = d.pop("tx_packets")

        resource_usage_network = cls(
            rx_bytes=rx_bytes,
            rx_packets=rx_packets,
            tx_bytes=tx_bytes,
            tx_packets=tx_packets,
        )

        resource_usage_network.additional_properties = d
        return resource_usage_network

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
