from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColumnDefinition")


@_attrs_define
class ColumnDefinition:
    """
    Attributes:
        name (str):
        type_ (str):
        nullable (bool | Unset):
        primary_key (bool | Unset):
        auto_increment (bool | Unset):
    """

    name: str
    type_: str
    nullable: bool | Unset = UNSET
    primary_key: bool | Unset = UNSET
    auto_increment: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        nullable = self.nullable

        primary_key = self.primary_key

        auto_increment = self.auto_increment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if nullable is not UNSET:
            field_dict["nullable"] = nullable
        if primary_key is not UNSET:
            field_dict["primary_key"] = primary_key
        if auto_increment is not UNSET:
            field_dict["auto_increment"] = auto_increment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        nullable = d.pop("nullable", UNSET)

        primary_key = d.pop("primary_key", UNSET)

        auto_increment = d.pop("auto_increment", UNSET)

        column_definition = cls(
            name=name,
            type_=type_,
            nullable=nullable,
            primary_key=primary_key,
            auto_increment=auto_increment,
        )

        column_definition.additional_properties = d
        return column_definition

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
