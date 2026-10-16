from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProvidersAdditionalProperty"
)


@_attrs_define
class GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProvidersAdditionalProperty:
    """
    Attributes:
        name (str):
        link (str):
    """

    name: str
    link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        link = self.link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        link = d.pop("link")

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers_additional_property = cls(
            name=name,
            link=link,
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers_additional_property.additional_properties = d
        return get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers_additional_property

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
