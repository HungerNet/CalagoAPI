from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TundraNodeMetrics")


@_attrs_define
class TundraNodeMetrics:
    """
    Attributes:
        uptime_secs (int):
        epoch (int):
        remote_link (str):
        frontends (int):
        snapshots_applied (int):
        local_flows_open (int):
        local_drops (int):
        frozen_flows (int):
        peers_connected (int):
    """

    uptime_secs: int
    epoch: int
    remote_link: str
    frontends: int
    snapshots_applied: int
    local_flows_open: int
    local_drops: int
    frozen_flows: int
    peers_connected: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uptime_secs = self.uptime_secs

        epoch = self.epoch

        remote_link = self.remote_link

        frontends = self.frontends

        snapshots_applied = self.snapshots_applied

        local_flows_open = self.local_flows_open

        local_drops = self.local_drops

        frozen_flows = self.frozen_flows

        peers_connected = self.peers_connected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uptime_secs": uptime_secs,
                "epoch": epoch,
                "remote_link": remote_link,
                "frontends": frontends,
                "snapshots_applied": snapshots_applied,
                "local_flows_open": local_flows_open,
                "local_drops": local_drops,
                "frozen_flows": frozen_flows,
                "peers_connected": peers_connected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uptime_secs = d.pop("uptime_secs")

        epoch = d.pop("epoch")

        remote_link = d.pop("remote_link")

        frontends = d.pop("frontends")

        snapshots_applied = d.pop("snapshots_applied")

        local_flows_open = d.pop("local_flows_open")

        local_drops = d.pop("local_drops")

        frozen_flows = d.pop("frozen_flows")

        peers_connected = d.pop("peers_connected")

        tundra_node_metrics = cls(
            uptime_secs=uptime_secs,
            epoch=epoch,
            remote_link=remote_link,
            frontends=frontends,
            snapshots_applied=snapshots_applied,
            local_flows_open=local_flows_open,
            local_drops=local_drops,
            frozen_flows=frozen_flows,
            peers_connected=peers_connected,
        )

        tundra_node_metrics.additional_properties = d
        return tundra_node_metrics

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
