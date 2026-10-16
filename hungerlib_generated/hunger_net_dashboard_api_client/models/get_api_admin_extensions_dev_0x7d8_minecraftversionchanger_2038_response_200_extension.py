from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_changelogs import (
        GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionChangelogs,
    )
    from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_product import (
        GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProduct,
    )
    from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers import (
        GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProviders,
    )


T = TypeVar("T", bound="GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200Extension")


@_attrs_define
class GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200Extension:
    """
    Attributes:
        product (GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProduct):
        providers (GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProviders):
        changelogs (GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionChangelogs):
    """

    product: GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProduct
    providers: GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProviders
    changelogs: GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionChangelogs
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product = self.product.to_dict()

        providers = self.providers.to_dict()

        changelogs = self.changelogs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product": product,
                "providers": providers,
                "changelogs": changelogs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_changelogs import (
            GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionChangelogs,  # noqa: PLC0415
        )
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_product import (
            GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProduct,  # noqa: PLC0415
        )
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_providers import (
            GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProviders,  # noqa: PLC0415
        )

        d = dict(src_dict)
        product = GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProduct.from_dict(
            d.pop("product")
        )

        providers = GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionProviders.from_dict(
            d.pop("providers")
        )

        changelogs = GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionChangelogs.from_dict(
            d.pop("changelogs")
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension = cls(
            product=product,
            providers=providers,
            changelogs=changelogs,
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension.additional_properties = d
        return get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension

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
