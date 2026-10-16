from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egg_assignment import EggAssignment
    from ..models.put_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_body_mcjars_type_order_type_0 import (
        PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0,
    )


T = TypeVar("T", bound="PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBody")


@_attrs_define
class PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBody:
    """
    Attributes:
        mcjars_url (None | str | Unset):
        mcjars_api_key (None | str | Unset):
        mcjars_icon_base_url (None | str | Unset):
        mcjars_icon_file_extension (None | str | Unset):
        mcjars_type_order (None | PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0 |
            Unset):
        type_egg_assignments (list[EggAssignment] | None | Unset):
        collect_installation_statistics (bool | None | Unset):
    """

    mcjars_url: None | str | Unset = UNSET
    mcjars_api_key: None | str | Unset = UNSET
    mcjars_icon_base_url: None | str | Unset = UNSET
    mcjars_icon_file_extension: None | str | Unset = UNSET
    mcjars_type_order: (
        None | PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0 | Unset
    ) = UNSET
    type_egg_assignments: list[EggAssignment] | None | Unset = UNSET
    collect_installation_statistics: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.put_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_body_mcjars_type_order_type_0 import (
            PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0,  # noqa: PLC0415
        )

        mcjars_url: None | str | Unset
        if isinstance(self.mcjars_url, Unset):
            mcjars_url = UNSET
        else:
            mcjars_url = self.mcjars_url

        mcjars_api_key: None | str | Unset
        if isinstance(self.mcjars_api_key, Unset):
            mcjars_api_key = UNSET
        else:
            mcjars_api_key = self.mcjars_api_key

        mcjars_icon_base_url: None | str | Unset
        if isinstance(self.mcjars_icon_base_url, Unset):
            mcjars_icon_base_url = UNSET
        else:
            mcjars_icon_base_url = self.mcjars_icon_base_url

        mcjars_icon_file_extension: None | str | Unset
        if isinstance(self.mcjars_icon_file_extension, Unset):
            mcjars_icon_file_extension = UNSET
        else:
            mcjars_icon_file_extension = self.mcjars_icon_file_extension

        mcjars_type_order: dict[str, Any] | None | Unset
        if isinstance(self.mcjars_type_order, Unset):
            mcjars_type_order = UNSET
        elif isinstance(
            self.mcjars_type_order, PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0
        ):
            mcjars_type_order = self.mcjars_type_order.to_dict()
        else:
            mcjars_type_order = self.mcjars_type_order

        type_egg_assignments: list[dict[str, Any]] | None | Unset
        if isinstance(self.type_egg_assignments, Unset):
            type_egg_assignments = UNSET
        elif isinstance(self.type_egg_assignments, list):
            type_egg_assignments = []
            for type_egg_assignments_type_0_item_data in self.type_egg_assignments:
                type_egg_assignments_type_0_item = type_egg_assignments_type_0_item_data.to_dict()
                type_egg_assignments.append(type_egg_assignments_type_0_item)

        else:
            type_egg_assignments = self.type_egg_assignments

        collect_installation_statistics: bool | None | Unset
        if isinstance(self.collect_installation_statistics, Unset):
            collect_installation_statistics = UNSET
        else:
            collect_installation_statistics = self.collect_installation_statistics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mcjars_url is not UNSET:
            field_dict["mcjars_url"] = mcjars_url
        if mcjars_api_key is not UNSET:
            field_dict["mcjars_api_key"] = mcjars_api_key
        if mcjars_icon_base_url is not UNSET:
            field_dict["mcjars_icon_base_url"] = mcjars_icon_base_url
        if mcjars_icon_file_extension is not UNSET:
            field_dict["mcjars_icon_file_extension"] = mcjars_icon_file_extension
        if mcjars_type_order is not UNSET:
            field_dict["mcjars_type_order"] = mcjars_type_order
        if type_egg_assignments is not UNSET:
            field_dict["type_egg_assignments"] = type_egg_assignments
        if collect_installation_statistics is not UNSET:
            field_dict["collect_installation_statistics"] = collect_installation_statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egg_assignment import EggAssignment  # noqa: PLC0415
        from ..models.put_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_body_mcjars_type_order_type_0 import (
            PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_mcjars_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcjars_url = _parse_mcjars_url(d.pop("mcjars_url", UNSET))

        def _parse_mcjars_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcjars_api_key = _parse_mcjars_api_key(d.pop("mcjars_api_key", UNSET))

        def _parse_mcjars_icon_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcjars_icon_base_url = _parse_mcjars_icon_base_url(d.pop("mcjars_icon_base_url", UNSET))

        def _parse_mcjars_icon_file_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcjars_icon_file_extension = _parse_mcjars_icon_file_extension(d.pop("mcjars_icon_file_extension", UNSET))

        def _parse_mcjars_type_order(
            data: object,
        ) -> None | PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcjars_type_order_type_0 = (
                    PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0.from_dict(data)
                )

                return mcjars_type_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PutApiAdminExtensionsDev0X7D8MinecraftversionchangerSettingsBodyMcjarsTypeOrderType0 | Unset,
                data,
            )

        mcjars_type_order = _parse_mcjars_type_order(d.pop("mcjars_type_order", UNSET))

        def _parse_type_egg_assignments(data: object) -> list[EggAssignment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                type_egg_assignments_type_0 = []
                _type_egg_assignments_type_0 = data
                for type_egg_assignments_type_0_item_data in _type_egg_assignments_type_0:
                    type_egg_assignments_type_0_item = EggAssignment.from_dict(type_egg_assignments_type_0_item_data)

                    type_egg_assignments_type_0.append(type_egg_assignments_type_0_item)

                return type_egg_assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EggAssignment] | None | Unset, data)

        type_egg_assignments = _parse_type_egg_assignments(d.pop("type_egg_assignments", UNSET))

        def _parse_collect_installation_statistics(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        collect_installation_statistics = _parse_collect_installation_statistics(
            d.pop("collect_installation_statistics", UNSET)
        )

        put_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_body = cls(
            mcjars_url=mcjars_url,
            mcjars_api_key=mcjars_api_key,
            mcjars_icon_base_url=mcjars_icon_base_url,
            mcjars_icon_file_extension=mcjars_icon_file_extension,
            mcjars_type_order=mcjars_type_order,
            type_egg_assignments=type_egg_assignments,
            collect_installation_statistics=collect_installation_statistics,
        )

        put_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_body.additional_properties = d
        return put_api_admin_extensions_dev_0x7d8_minecraftversionchanger_settings_body

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
