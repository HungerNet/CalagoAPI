from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminNodesNodeSystemStatsResponse200StatsCpu")


@_attrs_define
class GetApiAdminNodesNodeSystemStatsResponse200StatsCpu:
    """
    Attributes:
        used (float):
        threads (int):
        model (str):
    """

    used: float
    threads: int
    model: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used = self.used

        threads = self.threads

        model = self.model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used": used,
                "threads": threads,
                "model": model,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used = d.pop("used")

        threads = d.pop("threads")

        model = d.pop("model")

        get_api_admin_nodes_node_system_stats_response_200_stats_cpu = cls(
            used=used,
            threads=threads,
            model=model,
        )

        get_api_admin_nodes_node_system_stats_response_200_stats_cpu.additional_properties = d
        return get_api_admin_nodes_node_system_stats_response_200_stats_cpu

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
