from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_container_type import AppContainerType

if TYPE_CHECKING:
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item_instances import (
        GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemInstances,
    )
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item_memory import (
        GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemMemory,
    )


T = TypeVar("T", bound="GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItem")


@_attrs_define
class GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItem:
    """
    Attributes:
        version (str):
        container_type (AppContainerType):
        memory (GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemMemory):
        instances (GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemInstances):
        architecture (str):
        kernel_version (str):
    """

    version: str
    container_type: AppContainerType
    memory: GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemMemory
    instances: GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemInstances
    architecture: str
    kernel_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        container_type = self.container_type.value

        memory = self.memory.to_dict()

        instances = self.instances.to_dict()

        architecture = self.architecture

        kernel_version = self.kernel_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "container_type": container_type,
                "memory": memory,
                "instances": instances,
                "architecture": architecture,
                "kernel_version": kernel_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item_instances import (
            GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemInstances,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item_memory import (
            GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemMemory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        version = d.pop("version")

        container_type = AppContainerType(d.pop("container_type"))

        memory = GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemMemory.from_dict(d.pop("memory"))

        instances = GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemInstances.from_dict(
            d.pop("instances")
        )

        architecture = d.pop("architecture")

        kernel_version = d.pop("kernel_version")

        get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item = cls(
            version=version,
            container_type=container_type,
            memory=memory,
            instances=instances,
            architecture=architecture,
            kernel_version=kernel_version,
        )

        get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item.additional_properties = d
        return get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item

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
