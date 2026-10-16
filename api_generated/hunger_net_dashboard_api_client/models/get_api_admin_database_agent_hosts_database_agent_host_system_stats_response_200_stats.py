from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_cpu import (
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsCpu,
    )
    from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_disk import (
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsDisk,
    )
    from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_memory import (
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsMemory,
    )
    from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_network import (
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsNetwork,
    )


T = TypeVar("T", bound="GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200Stats")


@_attrs_define
class GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200Stats:
    """
    Attributes:
        cpu (GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsCpu):
        network (GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsNetwork):
        memory (GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsMemory):
        disk (GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsDisk):
    """

    cpu: GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsCpu
    network: GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsNetwork
    memory: GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsMemory
    disk: GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsDisk
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu.to_dict()

        network = self.network.to_dict()

        memory = self.memory.to_dict()

        disk = self.disk.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu": cpu,
                "network": network,
                "memory": memory,
                "disk": disk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_cpu import (
            GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsCpu,  # noqa: PLC0415
        )
        from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_disk import (
            GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsDisk,  # noqa: PLC0415
        )
        from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_memory import (
            GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsMemory,  # noqa: PLC0415
        )
        from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_network import (
            GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsNetwork,  # noqa: PLC0415
        )

        d = dict(src_dict)
        cpu = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsCpu.from_dict(d.pop("cpu"))

        network = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsNetwork.from_dict(
            d.pop("network")
        )

        memory = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsMemory.from_dict(
            d.pop("memory")
        )

        disk = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsDisk.from_dict(d.pop("disk"))

        get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats = cls(
            cpu=cpu,
            network=network,
            memory=memory,
            disk=disk,
        )

        get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats.additional_properties = d
        return get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats

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
