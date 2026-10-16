from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminNodesNodeAllocationsBody")


@_attrs_define
class PostApiAdminNodesNodeAllocationsBody:
    """
    Attributes:
        ip (str):
        ports (list[int]):
        ip_alias (None | str | Unset):
    """

    ip: str
    ports: list[int]
    ip_alias: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        ports = self.ports

        ip_alias: None | str | Unset
        if isinstance(self.ip_alias, Unset):
            ip_alias = UNSET
        else:
            ip_alias = self.ip_alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip": ip,
                "ports": ports,
            }
        )
        if ip_alias is not UNSET:
            field_dict["ip_alias"] = ip_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ip = d.pop("ip")

        ports = cast(list[int], d.pop("ports"))

        def _parse_ip_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_alias = _parse_ip_alias(d.pop("ip_alias", UNSET))

        post_api_admin_nodes_node_allocations_body = cls(
            ip=ip,
            ports=ports,
            ip_alias=ip_alias,
        )

        post_api_admin_nodes_node_allocations_body.additional_properties = d
        return post_api_admin_nodes_node_allocations_body

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
