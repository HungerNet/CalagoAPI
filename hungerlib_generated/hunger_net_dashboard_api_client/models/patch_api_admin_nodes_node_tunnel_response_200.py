from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_node_tunnel import AdminNodeTunnel


T = TypeVar("T", bound="PatchApiAdminNodesNodeTunnelResponse200")


@_attrs_define
class PatchApiAdminNodesNodeTunnelResponse200:
    """
    Attributes:
        tunnel (AdminNodeTunnel):
    """

    tunnel: AdminNodeTunnel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tunnel = self.tunnel.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tunnel": tunnel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_node_tunnel import AdminNodeTunnel  # noqa: PLC0415

        d = dict(src_dict)
        tunnel = AdminNodeTunnel.from_dict(d.pop("tunnel"))

        patch_api_admin_nodes_node_tunnel_response_200 = cls(
            tunnel=tunnel,
        )

        patch_api_admin_nodes_node_tunnel_response_200.additional_properties = d
        return patch_api_admin_nodes_node_tunnel_response_200

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
