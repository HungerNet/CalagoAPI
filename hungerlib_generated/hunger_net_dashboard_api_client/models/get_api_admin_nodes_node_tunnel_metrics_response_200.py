from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tundra_node_metrics import TundraNodeMetrics
    from ..models.tundra_peer_metrics import TundraPeerMetrics


T = TypeVar("T", bound="GetApiAdminNodesNodeTunnelMetricsResponse200")


@_attrs_define
class GetApiAdminNodesNodeTunnelMetricsResponse200:
    """The mesh daemon reports considerably more than this - per-path congestion detail, UDP
    socket counters, restart handover state - and serde drops what is not declared here. The
    fields below are the ones the panel renders, so a daemon that stops sending one fails
    deserialization on the panel rather than the browser.

        Attributes:
            node (TundraNodeMetrics):
            peers (list[TundraPeerMetrics]):
    """

    node: TundraNodeMetrics
    peers: list[TundraPeerMetrics]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node.to_dict()

        peers = []
        for peers_item_data in self.peers:
            peers_item = peers_item_data.to_dict()
            peers.append(peers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node": node,
                "peers": peers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tundra_node_metrics import TundraNodeMetrics  # noqa: PLC0415
        from ..models.tundra_peer_metrics import TundraPeerMetrics  # noqa: PLC0415

        d = dict(src_dict)
        node = TundraNodeMetrics.from_dict(d.pop("node"))

        peers = []
        _peers = d.pop("peers")
        for peers_item_data in _peers:
            peers_item = TundraPeerMetrics.from_dict(peers_item_data)

            peers.append(peers_item)

        get_api_admin_nodes_node_tunnel_metrics_response_200 = cls(
            node=node,
            peers=peers,
        )

        get_api_admin_nodes_node_tunnel_metrics_response_200.additional_properties = d
        return get_api_admin_nodes_node_tunnel_metrics_response_200

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
