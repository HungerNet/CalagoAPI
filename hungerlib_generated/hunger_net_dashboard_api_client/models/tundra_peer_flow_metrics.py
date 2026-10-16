from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TundraPeerFlowMetrics")


@_attrs_define
class TundraPeerFlowMetrics:
    """
    Attributes:
        open_ (int):
        opened_total (int):
        tcp_open (int):
    """

    open_: int
    opened_total: int
    tcp_open: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        opened_total = self.opened_total

        tcp_open = self.tcp_open

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open": open_,
                "opened_total": opened_total,
                "tcp_open": tcp_open,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_ = d.pop("open")

        opened_total = d.pop("opened_total")

        tcp_open = d.pop("tcp_open")

        tundra_peer_flow_metrics = cls(
            open_=open_,
            opened_total=opened_total,
            tcp_open=tcp_open,
        )

        tundra_peer_flow_metrics.additional_properties = d
        return tundra_peer_flow_metrics

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
