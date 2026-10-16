from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_power_action import ServerPowerAction

if TYPE_CHECKING:
    from ..models.server_selector_type_0 import ServerSelectorType0
    from ..models.server_selector_type_1 import ServerSelectorType1


T = TypeVar("T", bound="PostApiAdminNodesNodeServersPowerBody")


@_attrs_define
class PostApiAdminNodesNodeServersPowerBody:
    """
    Attributes:
        servers (ServerSelectorType0 | ServerSelectorType1):
        action (ServerPowerAction):
    """

    servers: ServerSelectorType0 | ServerSelectorType1
    action: ServerPowerAction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_selector_type_0 import ServerSelectorType0  # noqa: PLC0415

        servers: dict[str, Any]
        if isinstance(self.servers, ServerSelectorType0):
            servers = self.servers.to_dict()
        else:
            servers = self.servers.to_dict()

        action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "servers": servers,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_selector_type_0 import ServerSelectorType0  # noqa: PLC0415
        from ..models.server_selector_type_1 import ServerSelectorType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_servers(data: object) -> ServerSelectorType0 | ServerSelectorType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_server_selector_type_0 = ServerSelectorType0.from_dict(data)

                return componentsschemas_server_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_server_selector_type_1 = ServerSelectorType1.from_dict(data)

            return componentsschemas_server_selector_type_1

        servers = _parse_servers(d.pop("servers"))

        action = ServerPowerAction(d.pop("action"))

        post_api_admin_nodes_node_servers_power_body = cls(
            servers=servers,
            action=action,
        )

        post_api_admin_nodes_node_servers_power_body.additional_properties = d
        return post_api_admin_nodes_node_servers_power_body

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
