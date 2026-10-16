from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_backups_disks import (
        GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackupsDisks,
    )


T = TypeVar("T", bound="GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackups")


@_attrs_define
class GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackups:
    """
    Attributes:
        total (int):
        disks (GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackupsDisks):
    """

    total: int
    disks: GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackupsDisks
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        disks = self.disks.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "disks": disks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_backups_disks import (
            GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackupsDisks,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total = d.pop("total")

        disks = GetApiAdminSystemTelemetryResponse200TelemetryResourcesBackupsDisks.from_dict(d.pop("disks"))

        get_api_admin_system_telemetry_response_200_telemetry_resources_backups = cls(
            total=total,
            disks=disks,
        )

        get_api_admin_system_telemetry_response_200_telemetry_resources_backups.additional_properties = d
        return get_api_admin_system_telemetry_response_200_telemetry_resources_backups

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
