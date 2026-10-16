from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TundraPeerRelayMetrics")


@_attrs_define
class TundraPeerRelayMetrics:
    """
    Attributes:
        stream_bytes_in (int):
        stream_bytes_out (int):
        datagram_bytes_in (int):
        datagram_bytes_out (int):
        streams_open (int):
        streams_total (int):
    """

    stream_bytes_in: int
    stream_bytes_out: int
    datagram_bytes_in: int
    datagram_bytes_out: int
    streams_open: int
    streams_total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stream_bytes_in = self.stream_bytes_in

        stream_bytes_out = self.stream_bytes_out

        datagram_bytes_in = self.datagram_bytes_in

        datagram_bytes_out = self.datagram_bytes_out

        streams_open = self.streams_open

        streams_total = self.streams_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stream_bytes_in": stream_bytes_in,
                "stream_bytes_out": stream_bytes_out,
                "datagram_bytes_in": datagram_bytes_in,
                "datagram_bytes_out": datagram_bytes_out,
                "streams_open": streams_open,
                "streams_total": streams_total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stream_bytes_in = d.pop("stream_bytes_in")

        stream_bytes_out = d.pop("stream_bytes_out")

        datagram_bytes_in = d.pop("datagram_bytes_in")

        datagram_bytes_out = d.pop("datagram_bytes_out")

        streams_open = d.pop("streams_open")

        streams_total = d.pop("streams_total")

        tundra_peer_relay_metrics = cls(
            stream_bytes_in=stream_bytes_in,
            stream_bytes_out=stream_bytes_out,
            datagram_bytes_in=datagram_bytes_in,
            datagram_bytes_out=datagram_bytes_out,
            streams_open=streams_open,
            streams_total=streams_total,
        )

        tundra_peer_relay_metrics.additional_properties = d
        return tundra_peer_relay_metrics

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
