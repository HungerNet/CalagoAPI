from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mount import Mount


T = TypeVar("T", bound="GetApiAdminNodesNodeMountsResponse200MountsAdminNodeMount")


@_attrs_define
class GetApiAdminNodesNodeMountsResponse200MountsAdminNodeMount:
    """
    Attributes:
        mount (Mount):
        created (datetime.datetime):
    """

    mount: Mount
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount = self.mount.to_dict()

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mount": mount,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mount import Mount  # noqa: PLC0415

        d = dict(src_dict)
        mount = Mount.from_dict(d.pop("mount"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        get_api_admin_nodes_node_mounts_response_200_mounts_admin_node_mount = cls(
            mount=mount,
            created=created,
        )

        get_api_admin_nodes_node_mounts_response_200_mounts_admin_node_mount.additional_properties = d
        return get_api_admin_nodes_node_mounts_response_200_mounts_admin_node_mount

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
