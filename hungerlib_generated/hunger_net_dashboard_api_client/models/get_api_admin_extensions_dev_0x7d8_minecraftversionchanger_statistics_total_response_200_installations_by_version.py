from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByVersion"
)


@_attrs_define
class GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByVersion:
    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200_installations_by_version = cls()

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200_installations_by_version.additional_properties = d
        return get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200_installations_by_version

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
