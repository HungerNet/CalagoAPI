from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminStatsBackupsResponse200Week")


@_attrs_define
class GetApiAdminStatsBackupsResponse200Week:
    """
    Attributes:
        total (int):
        successful (int):
        successful_bytes (int):
        failed (int):
        deleted (int):
        deleted_bytes (int):
    """

    total: int
    successful: int
    successful_bytes: int
    failed: int
    deleted: int
    deleted_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        successful = self.successful

        successful_bytes = self.successful_bytes

        failed = self.failed

        deleted = self.deleted

        deleted_bytes = self.deleted_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "successful": successful,
                "successful_bytes": successful_bytes,
                "failed": failed,
                "deleted": deleted,
                "deleted_bytes": deleted_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        successful = d.pop("successful")

        successful_bytes = d.pop("successful_bytes")

        failed = d.pop("failed")

        deleted = d.pop("deleted")

        deleted_bytes = d.pop("deleted_bytes")

        get_api_admin_stats_backups_response_200_week = cls(
            total=total,
            successful=successful,
            successful_bytes=successful_bytes,
            failed=failed,
            deleted=deleted,
            deleted_bytes=deleted_bytes,
        )

        get_api_admin_stats_backups_response_200_week.additional_properties = d
        return get_api_admin_stats_backups_response_200_week

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
