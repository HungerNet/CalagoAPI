from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_health_nodes_response_200_desync_nodes import (
        GetApiAdminSystemHealthNodesResponse200DesyncNodes,
    )


T = TypeVar("T", bound="GetApiAdminSystemHealthNodesResponse200")


@_attrs_define
class GetApiAdminSystemHealthNodesResponse200:
    """
    Attributes:
        desync_nodes (GetApiAdminSystemHealthNodesResponse200DesyncNodes):
        failed_nodes (int):
    """

    desync_nodes: GetApiAdminSystemHealthNodesResponse200DesyncNodes
    failed_nodes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desync_nodes = self.desync_nodes.to_dict()

        failed_nodes = self.failed_nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "desync_nodes": desync_nodes,
                "failed_nodes": failed_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_health_nodes_response_200_desync_nodes import (
            GetApiAdminSystemHealthNodesResponse200DesyncNodes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        desync_nodes = GetApiAdminSystemHealthNodesResponse200DesyncNodes.from_dict(d.pop("desync_nodes"))

        failed_nodes = d.pop("failed_nodes")

        get_api_admin_system_health_nodes_response_200 = cls(
            desync_nodes=desync_nodes,
            failed_nodes=failed_nodes,
        )

        get_api_admin_system_health_nodes_response_200.additional_properties = d
        return get_api_admin_system_health_nodes_response_200

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
