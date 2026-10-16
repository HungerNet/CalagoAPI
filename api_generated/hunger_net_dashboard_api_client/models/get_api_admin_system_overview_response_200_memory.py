from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminSystemOverviewResponse200Memory")


@_attrs_define
class GetApiAdminSystemOverviewResponse200Memory:
    """
    Attributes:
        total_bytes (int):
        free_bytes (int):
        used_bytes (int):
        used_bytes_process (int):
    """

    total_bytes: int
    free_bytes: int
    used_bytes: int
    used_bytes_process: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_bytes = self.total_bytes

        free_bytes = self.free_bytes

        used_bytes = self.used_bytes

        used_bytes_process = self.used_bytes_process

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_bytes": total_bytes,
                "free_bytes": free_bytes,
                "used_bytes": used_bytes,
                "used_bytes_process": used_bytes_process,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_bytes = d.pop("total_bytes")

        free_bytes = d.pop("free_bytes")

        used_bytes = d.pop("used_bytes")

        used_bytes_process = d.pop("used_bytes_process")

        get_api_admin_system_overview_response_200_memory = cls(
            total_bytes=total_bytes,
            free_bytes=free_bytes,
            used_bytes=used_bytes,
            used_bytes_process=used_bytes_process,
        )

        get_api_admin_system_overview_response_200_memory.additional_properties = d
        return get_api_admin_system_overview_response_200_memory

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
