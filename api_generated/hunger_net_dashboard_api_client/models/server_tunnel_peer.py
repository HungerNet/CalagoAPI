from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_tunnel_port import ServerTunnelPort


T = TypeVar("T", bound="ServerTunnelPeer")


@_attrs_define
class ServerTunnelPeer:
    """
    Attributes:
        server_uuid (UUID):
        server_name (str):
        name (str):
        alias (str):
        ports (list[ServerTunnelPort]):
        created (datetime.datetime):
        address (None | str | Unset):
    """

    server_uuid: UUID
    server_name: str
    name: str
    alias: str
    ports: list[ServerTunnelPort]
    created: datetime.datetime
    address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_uuid = str(self.server_uuid)

        server_name = self.server_name

        name = self.name

        alias = self.alias

        ports = []
        for ports_item_data in self.ports:
            ports_item = ports_item_data.to_dict()
            ports.append(ports_item)

        created = self.created.isoformat()

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_uuid": server_uuid,
                "server_name": server_name,
                "name": name,
                "alias": alias,
                "ports": ports,
                "created": created,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_tunnel_port import ServerTunnelPort  # noqa: PLC0415

        d = dict(src_dict)
        server_uuid = UUID(d.pop("server_uuid"))

        server_name = d.pop("server_name")

        name = d.pop("name")

        alias = d.pop("alias")

        ports = []
        _ports = d.pop("ports")
        for ports_item_data in _ports:
            ports_item = ServerTunnelPort.from_dict(ports_item_data)

            ports.append(ports_item)

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        server_tunnel_peer = cls(
            server_uuid=server_uuid,
            server_name=server_name,
            name=name,
            alias=alias,
            ports=ports,
            created=created,
            address=address,
        )

        server_tunnel_peer.additional_properties = d
        return server_tunnel_peer

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
