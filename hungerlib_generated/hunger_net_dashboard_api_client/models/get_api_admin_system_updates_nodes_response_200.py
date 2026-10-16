from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_updates_nodes_response_200_outdated_nodes import (
        GetApiAdminSystemUpdatesNodesResponse200OutdatedNodes,
    )


T = TypeVar("T", bound="GetApiAdminSystemUpdatesNodesResponse200")


@_attrs_define
class GetApiAdminSystemUpdatesNodesResponse200:
    """
    Attributes:
        outdated_nodes (GetApiAdminSystemUpdatesNodesResponse200OutdatedNodes):
        failed_nodes (int):
    """

    outdated_nodes: GetApiAdminSystemUpdatesNodesResponse200OutdatedNodes
    failed_nodes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outdated_nodes = self.outdated_nodes.to_dict()

        failed_nodes = self.failed_nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outdated_nodes": outdated_nodes,
                "failed_nodes": failed_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_updates_nodes_response_200_outdated_nodes import (
            GetApiAdminSystemUpdatesNodesResponse200OutdatedNodes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        outdated_nodes = GetApiAdminSystemUpdatesNodesResponse200OutdatedNodes.from_dict(d.pop("outdated_nodes"))

        failed_nodes = d.pop("failed_nodes")

        get_api_admin_system_updates_nodes_response_200 = cls(
            outdated_nodes=outdated_nodes,
            failed_nodes=failed_nodes,
        )

        get_api_admin_system_updates_nodes_response_200.additional_properties = d
        return get_api_admin_system_updates_nodes_response_200

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
