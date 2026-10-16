from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200_container_type import (
    GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200ContainerType,
)

if TYPE_CHECKING:
    from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200_cpu import (
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Cpu,
    )
    from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200_instances import (
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Instances,
    )
    from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200_memory import (
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Memory,
    )


T = TypeVar("T", bound="GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200")


@_attrs_define
class GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200:
    """
    Attributes:
        version (str):
        local_time (datetime.datetime):
        container_type (GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200ContainerType):
        cpu (GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Cpu):
        memory (GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Memory):
        instances (GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Instances):
        architecture (str):
        kernel_version (str):
    """

    version: str
    local_time: datetime.datetime
    container_type: GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200ContainerType
    cpu: GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Cpu
    memory: GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Memory
    instances: GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Instances
    architecture: str
    kernel_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        local_time = self.local_time.isoformat()

        container_type = self.container_type.value

        cpu = self.cpu.to_dict()

        memory = self.memory.to_dict()

        instances = self.instances.to_dict()

        architecture = self.architecture

        kernel_version = self.kernel_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "local_time": local_time,
                "container_type": container_type,
                "cpu": cpu,
                "memory": memory,
                "instances": instances,
                "architecture": architecture,
                "kernel_version": kernel_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200_cpu import (
            GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Cpu,  # noqa: PLC0415
        )
        from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200_instances import (
            GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Instances,  # noqa: PLC0415
        )
        from ..models.get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200_memory import (
            GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Memory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        version = d.pop("version")

        local_time = datetime.datetime.fromisoformat(d.pop("local_time"))

        container_type = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200ContainerType(
            d.pop("container_type")
        )

        cpu = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Cpu.from_dict(d.pop("cpu"))

        memory = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Memory.from_dict(
            d.pop("memory")
        )

        instances = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200Instances.from_dict(
            d.pop("instances")
        )

        architecture = d.pop("architecture")

        kernel_version = d.pop("kernel_version")

        get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200 = cls(
            version=version,
            local_time=local_time,
            container_type=container_type,
            cpu=cpu,
            memory=memory,
            instances=instances,
            architecture=architecture,
            kernel_version=kernel_version,
        )

        get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200.additional_properties = d
        return get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200

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
