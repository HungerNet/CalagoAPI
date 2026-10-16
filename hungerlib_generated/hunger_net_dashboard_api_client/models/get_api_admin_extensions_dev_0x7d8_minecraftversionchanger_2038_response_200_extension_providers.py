from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers_additional_property import (
        GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProvidersAdditionalProperty,
    )


T = TypeVar("T", bound="GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProviders")


@_attrs_define
class GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProviders:
    additional_properties: dict[
        str, GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProvidersAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers_additional_property import (
            GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProvidersAdditionalProperty,  # noqa: PLC0415
        )

        d = dict(src_dict)
        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProvidersAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers.additional_properties = additional_properties
        return get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProvidersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProvidersAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
