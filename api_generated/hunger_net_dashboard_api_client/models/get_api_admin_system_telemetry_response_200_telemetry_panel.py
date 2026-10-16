from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_container_type import AppContainerType

T = TypeVar("T", bound="GetApiAdminSystemTelemetryResponse200TelemetryPanel")


@_attrs_define
class GetApiAdminSystemTelemetryResponse200TelemetryPanel:
    """
    Attributes:
        version (str):
        container_type (AppContainerType):
        database_version (str):
        cache_version (str):
        architecture (str):
        kernel_version (str):
    """

    version: str
    container_type: AppContainerType
    database_version: str
    cache_version: str
    architecture: str
    kernel_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        container_type = self.container_type.value

        database_version = self.database_version

        cache_version = self.cache_version

        architecture = self.architecture

        kernel_version = self.kernel_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "container_type": container_type,
                "database_version": database_version,
                "cache_version": cache_version,
                "architecture": architecture,
                "kernel_version": kernel_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        container_type = AppContainerType(d.pop("container_type"))

        database_version = d.pop("database_version")

        cache_version = d.pop("cache_version")

        architecture = d.pop("architecture")

        kernel_version = d.pop("kernel_version")

        get_api_admin_system_telemetry_response_200_telemetry_panel = cls(
            version=version,
            container_type=container_type,
            database_version=database_version,
            cache_version=cache_version,
            architecture=architecture,
            kernel_version=kernel_version,
        )

        get_api_admin_system_telemetry_response_200_telemetry_panel.additional_properties = d
        return get_api_admin_system_telemetry_response_200_telemetry_panel

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
