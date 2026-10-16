from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_extensions_response_200_extensions_item import (
        GetApiAdminExtensionsResponse200ExtensionsItem,
    )


T = TypeVar("T", bound="GetApiAdminExtensionsResponse200")


@_attrs_define
class GetApiAdminExtensionsResponse200:
    """
    Attributes:
        extensions (list[GetApiAdminExtensionsResponse200ExtensionsItem]):
        disabled (list[str]):
        pending_disabled (list[str]):
        management_disabled (bool):
    """

    extensions: list[GetApiAdminExtensionsResponse200ExtensionsItem]
    disabled: list[str]
    pending_disabled: list[str]
    management_disabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions = []
        for extensions_item_data in self.extensions:
            extensions_item = extensions_item_data.to_dict()
            extensions.append(extensions_item)

        disabled = self.disabled

        pending_disabled = self.pending_disabled

        management_disabled = self.management_disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extensions": extensions,
                "disabled": disabled,
                "pending_disabled": pending_disabled,
                "management_disabled": management_disabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_extensions_response_200_extensions_item import (
            GetApiAdminExtensionsResponse200ExtensionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        extensions = []
        _extensions = d.pop("extensions")
        for extensions_item_data in _extensions:
            extensions_item = GetApiAdminExtensionsResponse200ExtensionsItem.from_dict(extensions_item_data)

            extensions.append(extensions_item)

        disabled = cast(list[str], d.pop("disabled"))

        pending_disabled = cast(list[str], d.pop("pending_disabled"))

        management_disabled = d.pop("management_disabled")

        get_api_admin_extensions_response_200 = cls(
            extensions=extensions,
            disabled=disabled,
            pending_disabled=pending_disabled,
            management_disabled=management_disabled,
        )

        get_api_admin_extensions_response_200.additional_properties = d
        return get_api_admin_extensions_response_200

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
