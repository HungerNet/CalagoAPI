from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_default_order_response_200_mcjars_type_order import (
        GetApiAdminExtensionsDev0X7D8MinecraftversionchangerDefaultOrderResponse200McjarsTypeOrder,
    )


T = TypeVar("T", bound="GetApiAdminExtensionsDev0X7D8MinecraftversionchangerDefaultOrderResponse200")


@_attrs_define
class GetApiAdminExtensionsDev0X7D8MinecraftversionchangerDefaultOrderResponse200:
    """
    Attributes:
        mcjars_type_order (GetApiAdminExtensionsDev0X7D8MinecraftversionchangerDefaultOrderResponse200McjarsTypeOrder):
    """

    mcjars_type_order: GetApiAdminExtensionsDev0X7D8MinecraftversionchangerDefaultOrderResponse200McjarsTypeOrder
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mcjars_type_order = self.mcjars_type_order.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mcjars_type_order": mcjars_type_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_default_order_response_200_mcjars_type_order import (
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerDefaultOrderResponse200McjarsTypeOrder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        mcjars_type_order = (
            GetApiAdminExtensionsDev0X7D8MinecraftversionchangerDefaultOrderResponse200McjarsTypeOrder.from_dict(
                d.pop("mcjars_type_order")
            )
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_default_order_response_200 = cls(
            mcjars_type_order=mcjars_type_order,
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_default_order_response_200.additional_properties = d
        return get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_default_order_response_200

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
