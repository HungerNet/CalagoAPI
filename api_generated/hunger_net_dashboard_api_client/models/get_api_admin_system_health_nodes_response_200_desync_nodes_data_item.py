from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node import Node


T = TypeVar("T", bound="GetApiAdminSystemHealthNodesResponse200DesyncNodesDataItem")


@_attrs_define
class GetApiAdminSystemHealthNodesResponse200DesyncNodesDataItem:
    """
    Attributes:
        local_time (datetime.datetime):
        panel_local_time (datetime.datetime):
        node (Node):
    """

    local_time: datetime.datetime
    panel_local_time: datetime.datetime
    node: Node
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_time = self.local_time.isoformat()

        panel_local_time = self.panel_local_time.isoformat()

        node = self.node.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "local_time": local_time,
                "panel_local_time": panel_local_time,
                "node": node,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node import Node  # noqa: PLC0415

        d = dict(src_dict)
        local_time = datetime.datetime.fromisoformat(d.pop("local_time"))

        panel_local_time = datetime.datetime.fromisoformat(d.pop("panel_local_time"))

        node = Node.from_dict(d.pop("node"))

        get_api_admin_system_health_nodes_response_200_desync_nodes_data_item = cls(
            local_time=local_time,
            panel_local_time=panel_local_time,
            node=node,
        )

        get_api_admin_system_health_nodes_response_200_desync_nodes_data_item.additional_properties = d
        return get_api_admin_system_health_nodes_response_200_desync_nodes_data_item

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
