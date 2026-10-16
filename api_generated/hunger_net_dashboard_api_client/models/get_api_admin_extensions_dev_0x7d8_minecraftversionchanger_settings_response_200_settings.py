from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egg_assignment import EggAssignment
    from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_response_200_settings_mcjars_type_order_type_0 import (
        GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0,
    )


T = TypeVar("T", bound="GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200Settings")


@_attrs_define
class GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200Settings:
    """
    Attributes:
        mcjars_url (str):
        mcjars_icon_base_url (str):
        mcjars_icon_file_extension (str):
        type_egg_assignments (list[EggAssignment]):
        collect_installation_statistics (bool):
        mcjars_api_key (None | str | Unset):
        mcjars_type_order
            (GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0 | None |
            Unset):
    """

    mcjars_url: str
    mcjars_icon_base_url: str
    mcjars_icon_file_extension: str
    type_egg_assignments: list[EggAssignment]
    collect_installation_statistics: bool
    mcjars_api_key: None | str | Unset = UNSET
    mcjars_type_order: (
        GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_response_200_settings_mcjars_type_order_type_0 import (
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0,  # noqa: PLC0415
        )

        mcjars_url = self.mcjars_url

        mcjars_icon_base_url = self.mcjars_icon_base_url

        mcjars_icon_file_extension = self.mcjars_icon_file_extension

        type_egg_assignments = []
        for type_egg_assignments_item_data in self.type_egg_assignments:
            type_egg_assignments_item = type_egg_assignments_item_data.to_dict()
            type_egg_assignments.append(type_egg_assignments_item)

        collect_installation_statistics = self.collect_installation_statistics

        mcjars_api_key: None | str | Unset
        if isinstance(self.mcjars_api_key, Unset):
            mcjars_api_key = UNSET
        else:
            mcjars_api_key = self.mcjars_api_key

        mcjars_type_order: dict[str, Any] | None | Unset
        if isinstance(self.mcjars_type_order, Unset):
            mcjars_type_order = UNSET
        elif isinstance(
            self.mcjars_type_order,
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0,
        ):
            mcjars_type_order = self.mcjars_type_order.to_dict()
        else:
            mcjars_type_order = self.mcjars_type_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mcjars_url": mcjars_url,
                "mcjars_icon_base_url": mcjars_icon_base_url,
                "mcjars_icon_file_extension": mcjars_icon_file_extension,
                "type_egg_assignments": type_egg_assignments,
                "collect_installation_statistics": collect_installation_statistics,
            }
        )
        if mcjars_api_key is not UNSET:
            field_dict["mcjars_api_key"] = mcjars_api_key
        if mcjars_type_order is not UNSET:
            field_dict["mcjars_type_order"] = mcjars_type_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egg_assignment import EggAssignment  # noqa: PLC0415
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_response_200_settings_mcjars_type_order_type_0 import (
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        mcjars_url = d.pop("mcjars_url")

        mcjars_icon_base_url = d.pop("mcjars_icon_base_url")

        mcjars_icon_file_extension = d.pop("mcjars_icon_file_extension")

        type_egg_assignments = []
        _type_egg_assignments = d.pop("type_egg_assignments")
        for type_egg_assignments_item_data in _type_egg_assignments:
            type_egg_assignments_item = EggAssignment.from_dict(type_egg_assignments_item_data)

            type_egg_assignments.append(type_egg_assignments_item)

        collect_installation_statistics = d.pop("collect_installation_statistics")

        def _parse_mcjars_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcjars_api_key = _parse_mcjars_api_key(d.pop("mcjars_api_key", UNSET))

        def _parse_mcjars_type_order(
            data: object,
        ) -> (
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcjars_type_order_type_0 = GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0.from_dict(
                    data
                )

                return mcjars_type_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsResponse200SettingsMcjarsTypeOrderType0
                | None
                | Unset,
                data,
            )

        mcjars_type_order = _parse_mcjars_type_order(d.pop("mcjars_type_order", UNSET))

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_response_200_settings = cls(
            mcjars_url=mcjars_url,
            mcjars_icon_base_url=mcjars_icon_base_url,
            mcjars_icon_file_extension=mcjars_icon_file_extension,
            type_egg_assignments=type_egg_assignments,
            collect_installation_statistics=collect_installation_statistics,
            mcjars_api_key=mcjars_api_key,
            mcjars_type_order=mcjars_type_order,
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_response_200_settings.additional_properties = d
        return get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_response_200_settings

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
