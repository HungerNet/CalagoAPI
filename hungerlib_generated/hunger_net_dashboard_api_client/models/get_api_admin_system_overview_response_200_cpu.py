from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminSystemOverviewResponse200Cpu")


@_attrs_define
class GetApiAdminSystemOverviewResponse200Cpu:
    """
    Attributes:
        name (str):
        brand (str):
        vendor_id (str):
        frequency_mhz (int):
        cpu_count (int):
    """

    name: str
    brand: str
    vendor_id: str
    frequency_mhz: int
    cpu_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        brand = self.brand

        vendor_id = self.vendor_id

        frequency_mhz = self.frequency_mhz

        cpu_count = self.cpu_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "brand": brand,
                "vendor_id": vendor_id,
                "frequency_mhz": frequency_mhz,
                "cpu_count": cpu_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        brand = d.pop("brand")

        vendor_id = d.pop("vendor_id")

        frequency_mhz = d.pop("frequency_mhz")

        cpu_count = d.pop("cpu_count")

        get_api_admin_system_overview_response_200_cpu = cls(
            name=name,
            brand=brand,
            vendor_id=vendor_id,
            frequency_mhz=frequency_mhz,
            cpu_count=cpu_count,
        )

        get_api_admin_system_overview_response_200_cpu.additional_properties = d
        return get_api_admin_system_overview_response_200_cpu

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
