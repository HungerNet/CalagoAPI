from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_admin_nodes_node_system_overview_response_200_container_type import (
    GetApiAdminNodesNodeSystemOverviewResponse200ContainerType,
)

if TYPE_CHECKING:
    from ..models.get_api_admin_nodes_node_system_overview_response_200_cpu import (
        GetApiAdminNodesNodeSystemOverviewResponse200Cpu,
    )
    from ..models.get_api_admin_nodes_node_system_overview_response_200_memory import (
        GetApiAdminNodesNodeSystemOverviewResponse200Memory,
    )
    from ..models.get_api_admin_nodes_node_system_overview_response_200_servers import (
        GetApiAdminNodesNodeSystemOverviewResponse200Servers,
    )


T = TypeVar("T", bound="GetApiAdminNodesNodeSystemOverviewResponse200")


@_attrs_define
class GetApiAdminNodesNodeSystemOverviewResponse200:
    """
    Attributes:
        version (str):
        local_time (datetime.datetime):
        container_type (GetApiAdminNodesNodeSystemOverviewResponse200ContainerType):
        cpu (GetApiAdminNodesNodeSystemOverviewResponse200Cpu):
        memory (GetApiAdminNodesNodeSystemOverviewResponse200Memory):
        servers (GetApiAdminNodesNodeSystemOverviewResponse200Servers):
        architecture (str):
        kernel_version (str):
    """

    version: str
    local_time: datetime.datetime
    container_type: GetApiAdminNodesNodeSystemOverviewResponse200ContainerType
    cpu: GetApiAdminNodesNodeSystemOverviewResponse200Cpu
    memory: GetApiAdminNodesNodeSystemOverviewResponse200Memory
    servers: GetApiAdminNodesNodeSystemOverviewResponse200Servers
    architecture: str
    kernel_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        local_time = self.local_time.isoformat()

        container_type = self.container_type.value

        cpu = self.cpu.to_dict()

        memory = self.memory.to_dict()

        servers = self.servers.to_dict()

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
                "servers": servers,
                "architecture": architecture,
                "kernel_version": kernel_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_nodes_node_system_overview_response_200_cpu import (
            GetApiAdminNodesNodeSystemOverviewResponse200Cpu,  # noqa: PLC0415
        )
        from ..models.get_api_admin_nodes_node_system_overview_response_200_memory import (
            GetApiAdminNodesNodeSystemOverviewResponse200Memory,  # noqa: PLC0415
        )
        from ..models.get_api_admin_nodes_node_system_overview_response_200_servers import (
            GetApiAdminNodesNodeSystemOverviewResponse200Servers,  # noqa: PLC0415
        )

        d = dict(src_dict)
        version = d.pop("version")

        local_time = datetime.datetime.fromisoformat(d.pop("local_time"))

        container_type = GetApiAdminNodesNodeSystemOverviewResponse200ContainerType(d.pop("container_type"))

        cpu = GetApiAdminNodesNodeSystemOverviewResponse200Cpu.from_dict(d.pop("cpu"))

        memory = GetApiAdminNodesNodeSystemOverviewResponse200Memory.from_dict(d.pop("memory"))

        servers = GetApiAdminNodesNodeSystemOverviewResponse200Servers.from_dict(d.pop("servers"))

        architecture = d.pop("architecture")

        kernel_version = d.pop("kernel_version")

        get_api_admin_nodes_node_system_overview_response_200 = cls(
            version=version,
            local_time=local_time,
            container_type=container_type,
            cpu=cpu,
            memory=memory,
            servers=servers,
            architecture=architecture,
            kernel_version=kernel_version,
        )

        get_api_admin_nodes_node_system_overview_response_200.additional_properties = d
        return get_api_admin_nodes_node_system_overview_response_200

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
