from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tundra_peer_drop_metrics import TundraPeerDropMetrics
    from ..models.tundra_peer_flow_metrics import TundraPeerFlowMetrics
    from ..models.tundra_peer_path_metrics import TundraPeerPathMetrics
    from ..models.tundra_peer_relay_metrics import TundraPeerRelayMetrics


T = TypeVar("T", bound="TundraPeerMetrics")


@_attrs_define
class TundraPeerMetrics:
    """
    Attributes:
        uuid (UUID):
        name (str):
        role (str):
        remote_addr (str):
        established_secs (int):
        path (TundraPeerPathMetrics):
        relay (TundraPeerRelayMetrics):
        flows (TundraPeerFlowMetrics):
        drops (TundraPeerDropMetrics):
    """

    uuid: UUID
    name: str
    role: str
    remote_addr: str
    established_secs: int
    path: TundraPeerPathMetrics
    relay: TundraPeerRelayMetrics
    flows: TundraPeerFlowMetrics
    drops: TundraPeerDropMetrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        role = self.role

        remote_addr = self.remote_addr

        established_secs = self.established_secs

        path = self.path.to_dict()

        relay = self.relay.to_dict()

        flows = self.flows.to_dict()

        drops = self.drops.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "role": role,
                "remote_addr": remote_addr,
                "established_secs": established_secs,
                "path": path,
                "relay": relay,
                "flows": flows,
                "drops": drops,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tundra_peer_drop_metrics import TundraPeerDropMetrics  # noqa: PLC0415
        from ..models.tundra_peer_flow_metrics import TundraPeerFlowMetrics  # noqa: PLC0415
        from ..models.tundra_peer_path_metrics import TundraPeerPathMetrics  # noqa: PLC0415
        from ..models.tundra_peer_relay_metrics import TundraPeerRelayMetrics  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        role = d.pop("role")

        remote_addr = d.pop("remote_addr")

        established_secs = d.pop("established_secs")

        path = TundraPeerPathMetrics.from_dict(d.pop("path"))

        relay = TundraPeerRelayMetrics.from_dict(d.pop("relay"))

        flows = TundraPeerFlowMetrics.from_dict(d.pop("flows"))

        drops = TundraPeerDropMetrics.from_dict(d.pop("drops"))

        tundra_peer_metrics = cls(
            uuid=uuid,
            name=name,
            role=role,
            remote_addr=remote_addr,
            established_secs=established_secs,
            path=path,
            relay=relay,
            flows=flows,
            drops=drops,
        )

        tundra_peer_metrics.additional_properties = d
        return tundra_peer_metrics

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
