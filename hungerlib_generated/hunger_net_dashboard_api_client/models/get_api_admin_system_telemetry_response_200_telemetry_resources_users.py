from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_users_languages import (
        GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsersLanguages,
    )


T = TypeVar("T", bound="GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsers")


@_attrs_define
class GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsers:
    """
    Attributes:
        total (int):
        languages (GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsersLanguages):
    """

    total: int
    languages: GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsersLanguages
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        languages = self.languages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "languages": languages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_telemetry_response_200_telemetry_resources_users_languages import (
            GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsersLanguages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total = d.pop("total")

        languages = GetApiAdminSystemTelemetryResponse200TelemetryResourcesUsersLanguages.from_dict(d.pop("languages"))

        get_api_admin_system_telemetry_response_200_telemetry_resources_users = cls(
            total=total,
            languages=languages,
        )

        get_api_admin_system_telemetry_response_200_telemetry_resources_users.additional_properties = d
        return get_api_admin_system_telemetry_response_200_telemetry_resources_users

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
