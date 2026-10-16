from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200_installations_by_type import (
        GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByType,
    )
    from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200_installations_by_version import (
        GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByVersion,
    )


T = TypeVar("T", bound="GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200")


@_attrs_define
class GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200:
    """
    Attributes:
        total_installations (int):
        installations_by_type
            (GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByType):
        installations_by_version
            (GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByVersion):
    """

    total_installations: int
    installations_by_type: (
        GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByType
    )
    installations_by_version: (
        GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByVersion
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_installations = self.total_installations

        installations_by_type = self.installations_by_type.to_dict()

        installations_by_version = self.installations_by_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_installations": total_installations,
                "installations_by_type": installations_by_type,
                "installations_by_version": installations_by_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200_installations_by_type import (
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByType,  # noqa: PLC0415
        )
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200_installations_by_version import (
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByVersion,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total_installations = d.pop("total_installations")

        installations_by_type = (
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByType.from_dict(
                d.pop("installations_by_type")
            )
        )

        installations_by_version = GetApiAdminExtensionsDev0X7D8MinecraftversionchangerStatisticsTotalResponse200InstallationsByVersion.from_dict(
            d.pop("installations_by_version")
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200 = cls(
            total_installations=total_installations,
            installations_by_type=installations_by_type,
            installations_by_version=installations_by_version,
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200.additional_properties = d
        return get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_statistics_total_response_200

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
