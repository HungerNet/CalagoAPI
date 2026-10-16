from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_tunnel import ServerTunnel
    from ..models.server_tunnel_peer import ServerTunnelPeer
    from ..models.server_tunnel_port import ServerTunnelPort


T = TypeVar("T", bound="GetApiClientServersServerTunnelResponse200")


@_attrs_define
class GetApiClientServersServerTunnelResponse200:
    """
    Attributes:
        supported (bool):
        ports (list[ServerTunnelPort]):
        allocation_ports (list[int]):
        outgoing (list[ServerTunnelPeer]):
        incoming (list[ServerTunnelPeer]):
        tunnel (None | ServerTunnel | Unset):
    """

    supported: bool
    ports: list[ServerTunnelPort]
    allocation_ports: list[int]
    outgoing: list[ServerTunnelPeer]
    incoming: list[ServerTunnelPeer]
    tunnel: None | ServerTunnel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_tunnel import ServerTunnel  # noqa: PLC0415

        supported = self.supported

        ports = []
        for ports_item_data in self.ports:
            ports_item = ports_item_data.to_dict()
            ports.append(ports_item)

        allocation_ports = self.allocation_ports

        outgoing = []
        for outgoing_item_data in self.outgoing:
            outgoing_item = outgoing_item_data.to_dict()
            outgoing.append(outgoing_item)

        incoming = []
        for incoming_item_data in self.incoming:
            incoming_item = incoming_item_data.to_dict()
            incoming.append(incoming_item)

        tunnel: dict[str, Any] | None | Unset
        if isinstance(self.tunnel, Unset):
            tunnel = UNSET
        elif isinstance(self.tunnel, ServerTunnel):
            tunnel = self.tunnel.to_dict()
        else:
            tunnel = self.tunnel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supported": supported,
                "ports": ports,
                "allocation_ports": allocation_ports,
                "outgoing": outgoing,
                "incoming": incoming,
            }
        )
        if tunnel is not UNSET:
            field_dict["tunnel"] = tunnel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_tunnel import ServerTunnel  # noqa: PLC0415
        from ..models.server_tunnel_peer import ServerTunnelPeer  # noqa: PLC0415
        from ..models.server_tunnel_port import ServerTunnelPort  # noqa: PLC0415

        d = dict(src_dict)
        supported = d.pop("supported")

        ports = []
        _ports = d.pop("ports")
        for ports_item_data in _ports:
            ports_item = ServerTunnelPort.from_dict(ports_item_data)

            ports.append(ports_item)

        allocation_ports = cast(list[int], d.pop("allocation_ports"))

        outgoing = []
        _outgoing = d.pop("outgoing")
        for outgoing_item_data in _outgoing:
            outgoing_item = ServerTunnelPeer.from_dict(outgoing_item_data)

            outgoing.append(outgoing_item)

        incoming = []
        _incoming = d.pop("incoming")
        for incoming_item_data in _incoming:
            incoming_item = ServerTunnelPeer.from_dict(incoming_item_data)

            incoming.append(incoming_item)

        def _parse_tunnel(data: object) -> None | ServerTunnel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tunnel_type_1 = ServerTunnel.from_dict(data)

                return tunnel_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerTunnel | Unset, data)

        tunnel = _parse_tunnel(d.pop("tunnel", UNSET))

        get_api_client_servers_server_tunnel_response_200 = cls(
            supported=supported,
            ports=ports,
            allocation_ports=allocation_ports,
            outgoing=outgoing,
            incoming=incoming,
            tunnel=tunnel,
        )

        get_api_client_servers_server_tunnel_response_200.additional_properties = d
        return get_api_client_servers_server_tunnel_response_200

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
