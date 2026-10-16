from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_nodes_node_transfers_response_200_transfers import (
        GetApiAdminNodesNodeTransfersResponse200Transfers,
    )


T = TypeVar("T", bound="GetApiAdminNodesNodeTransfersResponse200")


@_attrs_define
class GetApiAdminNodesNodeTransfersResponse200:
    """
    Attributes:
        transfers (GetApiAdminNodesNodeTransfersResponse200Transfers):
    """

    transfers: GetApiAdminNodesNodeTransfersResponse200Transfers
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transfers = self.transfers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transfers": transfers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_nodes_node_transfers_response_200_transfers import (
            GetApiAdminNodesNodeTransfersResponse200Transfers,  # noqa: PLC0415
        )

        d = dict(src_dict)
        transfers = GetApiAdminNodesNodeTransfersResponse200Transfers.from_dict(d.pop("transfers"))

        get_api_admin_nodes_node_transfers_response_200 = cls(
            transfers=transfers,
        )

        get_api_admin_nodes_node_transfers_response_200.additional_properties = d
        return get_api_admin_nodes_node_transfers_response_200

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
