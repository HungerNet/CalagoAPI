from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TundraPeerPathMetrics")


@_attrs_define
class TundraPeerPathMetrics:
    """
    Attributes:
        rtt_ms (float):
        current_mtu (int):
        lost_packets (int):
        congestion_events (int):
    """

    rtt_ms: float
    current_mtu: int
    lost_packets: int
    congestion_events: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rtt_ms = self.rtt_ms

        current_mtu = self.current_mtu

        lost_packets = self.lost_packets

        congestion_events = self.congestion_events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rtt_ms": rtt_ms,
                "current_mtu": current_mtu,
                "lost_packets": lost_packets,
                "congestion_events": congestion_events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rtt_ms = d.pop("rtt_ms")

        current_mtu = d.pop("current_mtu")

        lost_packets = d.pop("lost_packets")

        congestion_events = d.pop("congestion_events")

        tundra_peer_path_metrics = cls(
            rtt_ms=rtt_ms,
            current_mtu=current_mtu,
            lost_packets=lost_packets,
            congestion_events=congestion_events,
        )

        tundra_peer_path_metrics.additional_properties = d
        return tundra_peer_path_metrics

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
