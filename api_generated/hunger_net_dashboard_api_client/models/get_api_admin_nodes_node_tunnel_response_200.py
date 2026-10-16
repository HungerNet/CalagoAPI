from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_node_tunnel import AdminNodeTunnel
    from ..models.tundra_status import TundraStatus


T = TypeVar("T", bound="GetApiAdminNodesNodeTunnelResponse200")


@_attrs_define
class GetApiAdminNodesNodeTunnelResponse200:
    """
    Attributes:
        tunnel (AdminNodeTunnel | None | Unset):
        status (None | TundraStatus | Unset):
    """

    tunnel: AdminNodeTunnel | None | Unset = UNSET
    status: None | TundraStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.admin_node_tunnel import AdminNodeTunnel  # noqa: PLC0415
        from ..models.tundra_status import TundraStatus  # noqa: PLC0415

        tunnel: dict[str, Any] | None | Unset
        if isinstance(self.tunnel, Unset):
            tunnel = UNSET
        elif isinstance(self.tunnel, AdminNodeTunnel):
            tunnel = self.tunnel.to_dict()
        else:
            tunnel = self.tunnel

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TundraStatus):
            status = self.status.to_dict()
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tunnel is not UNSET:
            field_dict["tunnel"] = tunnel
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_node_tunnel import AdminNodeTunnel  # noqa: PLC0415
        from ..models.tundra_status import TundraStatus  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_tunnel(data: object) -> AdminNodeTunnel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tunnel_type_1 = AdminNodeTunnel.from_dict(data)

                return tunnel_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AdminNodeTunnel | None | Unset, data)

        tunnel = _parse_tunnel(d.pop("tunnel", UNSET))

        def _parse_status(data: object) -> None | TundraStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = TundraStatus.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TundraStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        get_api_admin_nodes_node_tunnel_response_200 = cls(
            tunnel=tunnel,
            status=status,
        )

        get_api_admin_nodes_node_tunnel_response_200.additional_properties = d
        return get_api_admin_nodes_node_tunnel_response_200

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
