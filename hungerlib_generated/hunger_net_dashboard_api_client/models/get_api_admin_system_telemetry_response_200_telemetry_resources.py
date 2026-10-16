from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_backups import (
        GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackups,
    )
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_servers import (
        GetApiAdminSystemTelemetryResponse200TelemetryResourcesServers,
    )
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_users import (
        GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsers,
    )


T = TypeVar("T", bound="GetApiAdminSystemTelemetryResponse200TelemetryResources")


@_attrs_define
class GetApiAdminSystemTelemetryResponse200TelemetryResources:
    """
    Attributes:
        users (GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsers):
        backups (GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackups):
        servers (GetApiAdminSystemTelemetryResponse200TelemetryResourcesServers):
    """

    users: GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsers
    backups: GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackups
    servers: GetApiAdminSystemTelemetryResponse200TelemetryResourcesServers
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = self.users.to_dict()

        backups = self.backups.to_dict()

        servers = self.servers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "backups": backups,
                "servers": servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_backups import (
            GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackups,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_servers import (
            GetApiAdminSystemTelemetryResponse200TelemetryResourcesServers,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_users import (
            GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsers,  # noqa: PLC0415
        )

        d = dict(src_dict)
        users = GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsers.from_dict(d.pop("users"))

        backups = GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackups.from_dict(d.pop("backups"))

        servers = GetApiAdminSystemTelemetryResponse200TelemetryResourcesServers.from_dict(d.pop("servers"))

        get_api_admin_system_telemetry_response_200_telemetry_resources = cls(
            users=users,
            backups=backups,
            servers=servers,
        )

        get_api_admin_system_telemetry_response_200_telemetry_resources.additional_properties = d
        return get_api_admin_system_telemetry_response_200_telemetry_resources

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
