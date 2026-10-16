from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tunnel_protocol import TunnelProtocol

T = TypeVar("T", bound="CreateServerTunnelPortOptions")


@_attrs_define
class CreateServerTunnelPortOptions:
    """
    Attributes:
        port (int):
        protocols (list[TunnelProtocol]):
    """

    port: int
    protocols: list[TunnelProtocol]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        protocols = []
        for protocols_item_data in self.protocols:
            protocols_item = protocols_item_data.value
            protocols.append(protocols_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
                "protocols": protocols,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        port = d.pop("port")

        protocols = []
        _protocols = d.pop("protocols")
        for protocols_item_data in _protocols:
            protocols_item = TunnelProtocol(protocols_item_data)

            protocols.append(protocols_item)

        create_server_tunnel_port_options = cls(
            port=port,
            protocols=protocols,
        )

        create_server_tunnel_port_options.additional_properties = d
        return create_server_tunnel_port_options

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
