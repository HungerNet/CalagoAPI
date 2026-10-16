from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.constructed_extension import ConstructedExtension
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item import (
        GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItem,
    )
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_nodes_item import (
        GetApiAdminSystemTelemetryResponse200TelemetryNodesItem,
    )
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_panel import (
        GetApiAdminSystemTelemetryResponse200TelemetryPanel,
    )
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources import (
        GetApiAdminSystemTelemetryResponse200TelemetryResources,
    )


T = TypeVar("T", bound="GetApiAdminSystemTelemetryResponse200Telemetry")


@_attrs_define
class GetApiAdminSystemTelemetryResponse200Telemetry:
    """
    Attributes:
        uuid (UUID):
        panel (GetApiAdminSystemTelemetryResponse200TelemetryPanel):
        resources (GetApiAdminSystemTelemetryResponse200TelemetryResources):
        extensions (list[ConstructedExtension]):
        nodes (list[GetApiAdminSystemTelemetryResponse200TelemetryNodesItem]):
        database_agent_hosts (list[GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItem]):
    """

    uuid: UUID
    panel: GetApiAdminSystemTelemetryResponse200TelemetryPanel
    resources: GetApiAdminSystemTelemetryResponse200TelemetryResources
    extensions: list[ConstructedExtension]
    nodes: list[GetApiAdminSystemTelemetryResponse200TelemetryNodesItem]
    database_agent_hosts: list[GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        panel = self.panel.to_dict()

        resources = self.resources.to_dict()

        extensions = []
        for extensions_item_data in self.extensions:
            extensions_item = extensions_item_data.to_dict()
            extensions.append(extensions_item)

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        database_agent_hosts = []
        for database_agent_hosts_item_data in self.database_agent_hosts:
            database_agent_hosts_item = database_agent_hosts_item_data.to_dict()
            database_agent_hosts.append(database_agent_hosts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "panel": panel,
                "resources": resources,
                "extensions": extensions,
                "nodes": nodes,
                "database_agent_hosts": database_agent_hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constructed_extension import ConstructedExtension  # noqa: PLC0415
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item import (
            GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItem,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_nodes_item import (
            GetApiAdminSystemTelemetryResponse200TelemetryNodesItem,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_panel import (
            GetApiAdminSystemTelemetryResponse200TelemetryPanel,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources import (
            GetApiAdminSystemTelemetryResponse200TelemetryResources,  # noqa: PLC0415
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        panel = GetApiAdminSystemTelemetryResponse200TelemetryPanel.from_dict(d.pop("panel"))

        resources = GetApiAdminSystemTelemetryResponse200TelemetryResources.from_dict(d.pop("resources"))

        extensions = []
        _extensions = d.pop("extensions")
        for extensions_item_data in _extensions:
            extensions_item = ConstructedExtension.from_dict(extensions_item_data)

            extensions.append(extensions_item)

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = GetApiAdminSystemTelemetryResponse200TelemetryNodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        database_agent_hosts = []
        _database_agent_hosts = d.pop("database_agent_hosts")
        for database_agent_hosts_item_data in _database_agent_hosts:
            database_agent_hosts_item = GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItem.from_dict(
                database_agent_hosts_item_data
            )

            database_agent_hosts.append(database_agent_hosts_item)

        get_api_admin_system_telemetry_response_200_telemetry = cls(
            uuid=uuid,
            panel=panel,
            resources=resources,
            extensions=extensions,
            nodes=nodes,
            database_agent_hosts=database_agent_hosts,
        )

        get_api_admin_system_telemetry_response_200_telemetry.additional_properties = d
        return get_api_admin_system_telemetry_response_200_telemetry

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
