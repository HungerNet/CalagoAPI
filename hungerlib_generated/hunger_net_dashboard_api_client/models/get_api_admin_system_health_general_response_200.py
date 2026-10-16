from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_health_general_response_200_migrations import (
        GetApiAdminSystemHealthGeneralResponse200Migrations,
    )
    from ..models.get_api_admin_system_health_general_response_200_ntp_offsets import (
        GetApiAdminSystemHealthGeneralResponse200NtpOffsets,
    )


T = TypeVar("T", bound="GetApiAdminSystemHealthGeneralResponse200")


@_attrs_define
class GetApiAdminSystemHealthGeneralResponse200:
    """
    Attributes:
        local_time (datetime.datetime):
        ntp_offsets (GetApiAdminSystemHealthGeneralResponse200NtpOffsets):
        migrations (GetApiAdminSystemHealthGeneralResponse200Migrations):
    """

    local_time: datetime.datetime
    ntp_offsets: GetApiAdminSystemHealthGeneralResponse200NtpOffsets
    migrations: GetApiAdminSystemHealthGeneralResponse200Migrations
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_time = self.local_time.isoformat()

        ntp_offsets = self.ntp_offsets.to_dict()

        migrations = self.migrations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "local_time": local_time,
                "ntp_offsets": ntp_offsets,
                "migrations": migrations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_health_general_response_200_migrations import (
            GetApiAdminSystemHealthGeneralResponse200Migrations,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_health_general_response_200_ntp_offsets import (
            GetApiAdminSystemHealthGeneralResponse200NtpOffsets,  # noqa: PLC0415
        )

        d = dict(src_dict)
        local_time = datetime.datetime.fromisoformat(d.pop("local_time"))

        ntp_offsets = GetApiAdminSystemHealthGeneralResponse200NtpOffsets.from_dict(d.pop("ntp_offsets"))

        migrations = GetApiAdminSystemHealthGeneralResponse200Migrations.from_dict(d.pop("migrations"))

        get_api_admin_system_health_general_response_200 = cls(
            local_time=local_time,
            ntp_offsets=ntp_offsets,
            migrations=migrations,
        )

        get_api_admin_system_health_general_response_200.additional_properties = d
        return get_api_admin_system_health_general_response_200

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
