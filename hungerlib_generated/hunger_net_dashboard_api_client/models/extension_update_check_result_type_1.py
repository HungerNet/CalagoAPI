from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.extension_update_check_result_type_1_type import ExtensionUpdateCheckResultType1Type

T = TypeVar("T", bound="ExtensionUpdateCheckResultType1")


@_attrs_define
class ExtensionUpdateCheckResultType1:
    """
    Attributes:
        version (str):
        latest_version (str):
        changes (list[str]):
        type_ (ExtensionUpdateCheckResultType1Type):
    """

    version: str
    latest_version: str
    changes: list[str]
    type_: ExtensionUpdateCheckResultType1Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        latest_version = self.latest_version

        changes = self.changes

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "latest_version": latest_version,
                "changes": changes,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        latest_version = d.pop("latest_version")

        changes = cast(list[str], d.pop("changes"))

        type_ = ExtensionUpdateCheckResultType1Type(d.pop("type"))

        extension_update_check_result_type_1 = cls(
            version=version,
            latest_version=latest_version,
            changes=changes,
            type_=type_,
        )

        extension_update_check_result_type_1.additional_properties = d
        return extension_update_check_result_type_1

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
