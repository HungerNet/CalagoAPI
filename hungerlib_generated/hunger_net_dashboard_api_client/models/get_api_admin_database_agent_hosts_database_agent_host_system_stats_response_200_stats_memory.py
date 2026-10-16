from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsMemory")


@_attrs_define
class GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsMemory:
    """
    Attributes:
        used (int):
        used_process (int):
        total (int):
    """

    used: int
    used_process: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used = self.used

        used_process = self.used_process

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used": used,
                "used_process": used_process,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used = d.pop("used")

        used_process = d.pop("used_process")

        total = d.pop("total")

        get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_memory = cls(
            used=used,
            used_process=used_process,
            total=total,
        )

        get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_memory.additional_properties = d
        return get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_memory

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
