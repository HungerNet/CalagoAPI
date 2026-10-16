from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.extension_update_check_result_type_2_type import ExtensionUpdateCheckResultType2Type

T = TypeVar("T", bound="ExtensionUpdateCheckResultType2")


@_attrs_define
class ExtensionUpdateCheckResultType2:
    """
    Attributes:
        error (str):
        type_ (ExtensionUpdateCheckResultType2Type):
    """

    error: str
    type_: ExtensionUpdateCheckResultType2Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        type_ = ExtensionUpdateCheckResultType2Type(d.pop("type"))

        extension_update_check_result_type_2 = cls(
            error=error,
            type_=type_,
        )

        extension_update_check_result_type_2.additional_properties = d
        return extension_update_check_result_type_2

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
