from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaColumn")


@_attrs_define
class SchemaColumn:
    """
    Attributes:
        name (str):
        type_name (str):
        nullable (bool):
        primary_key (bool):
        auto_increment (bool):
        generated (bool):
        binary (bool):
        default (None | str | Unset):
        enum_values (list[str] | None | Unset):
        set_values (list[str] | None | Unset):
    """

    name: str
    type_name: str
    nullable: bool
    primary_key: bool
    auto_increment: bool
    generated: bool
    binary: bool
    default: None | str | Unset = UNSET
    enum_values: list[str] | None | Unset = UNSET
    set_values: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_name = self.type_name

        nullable = self.nullable

        primary_key = self.primary_key

        auto_increment = self.auto_increment

        generated = self.generated

        binary = self.binary

        default: None | str | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        enum_values: list[str] | None | Unset
        if isinstance(self.enum_values, Unset):
            enum_values = UNSET
        elif isinstance(self.enum_values, list):
            enum_values = self.enum_values

        else:
            enum_values = self.enum_values

        set_values: list[str] | None | Unset
        if isinstance(self.set_values, Unset):
            set_values = UNSET
        elif isinstance(self.set_values, list):
            set_values = self.set_values

        else:
            set_values = self.set_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type_name": type_name,
                "nullable": nullable,
                "primary_key": primary_key,
                "auto_increment": auto_increment,
                "generated": generated,
                "binary": binary,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if enum_values is not UNSET:
            field_dict["enum_values"] = enum_values
        if set_values is not UNSET:
            field_dict["set_values"] = set_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_name = d.pop("type_name")

        nullable = d.pop("nullable")

        primary_key = d.pop("primary_key")

        auto_increment = d.pop("auto_increment")

        generated = d.pop("generated")

        binary = d.pop("binary")

        def _parse_default(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_enum_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enum_values_type_0 = cast(list[str], data)

                return enum_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        enum_values = _parse_enum_values(d.pop("enum_values", UNSET))

        def _parse_set_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                set_values_type_0 = cast(list[str], data)

                return set_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        set_values = _parse_set_values(d.pop("set_values", UNSET))

        schema_column = cls(
            name=name,
            type_name=type_name,
            nullable=nullable,
            primary_key=primary_key,
            auto_increment=auto_increment,
            generated=generated,
            binary=binary,
            default=default,
            enum_values=enum_values,
            set_values=set_values,
        )

        schema_column.additional_properties = d
        return schema_column

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
