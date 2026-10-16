from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TundraPeerDropMetrics")


@_attrs_define
class TundraPeerDropMetrics:
    """
    Attributes:
        send_buffer_full (int):
        unknown_flow (int):
        frag_timeout (int):
        frag_limit (int):
        oversize (int):
        malformed (int):
    """

    send_buffer_full: int
    unknown_flow: int
    frag_timeout: int
    frag_limit: int
    oversize: int
    malformed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        send_buffer_full = self.send_buffer_full

        unknown_flow = self.unknown_flow

        frag_timeout = self.frag_timeout

        frag_limit = self.frag_limit

        oversize = self.oversize

        malformed = self.malformed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "send_buffer_full": send_buffer_full,
                "unknown_flow": unknown_flow,
                "frag_timeout": frag_timeout,
                "frag_limit": frag_limit,
                "oversize": oversize,
                "malformed": malformed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        send_buffer_full = d.pop("send_buffer_full")

        unknown_flow = d.pop("unknown_flow")

        frag_timeout = d.pop("frag_timeout")

        frag_limit = d.pop("frag_limit")

        oversize = d.pop("oversize")

        malformed = d.pop("malformed")

        tundra_peer_drop_metrics = cls(
            send_buffer_full=send_buffer_full,
            unknown_flow=unknown_flow,
            frag_timeout=frag_timeout,
            frag_limit=frag_limit,
            oversize=oversize,
            malformed=malformed,
        )

        tundra_peer_drop_metrics.additional_properties = d
        return tundra_peer_drop_metrics

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
