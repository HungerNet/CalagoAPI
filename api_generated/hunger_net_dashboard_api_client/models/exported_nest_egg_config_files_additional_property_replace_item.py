from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportedNestEggConfigFilesAdditionalPropertyReplaceItem")


@_attrs_define
class ExportedNestEggConfigFilesAdditionalPropertyReplaceItem:
    """
    Attributes:
        match (str):
        replace_with (Any):
        insert_new (bool | Unset):
        update_existing (bool | Unset):
        if_value (None | str | Unset):
    """

    match: str
    replace_with: Any
    insert_new: bool | Unset = UNSET
    update_existing: bool | Unset = UNSET
    if_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match = self.match

        replace_with = self.replace_with

        insert_new = self.insert_new

        update_existing = self.update_existing

        if_value: None | str | Unset
        if isinstance(self.if_value, Unset):
            if_value = UNSET
        else:
            if_value = self.if_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "match": match,
                "replace_with": replace_with,
            }
        )
        if insert_new is not UNSET:
            field_dict["insert_new"] = insert_new
        if update_existing is not UNSET:
            field_dict["update_existing"] = update_existing
        if if_value is not UNSET:
            field_dict["if_value"] = if_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match = d.pop("match")

        replace_with = d.pop("replace_with")

        insert_new = d.pop("insert_new", UNSET)

        update_existing = d.pop("update_existing", UNSET)

        def _parse_if_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        if_value = _parse_if_value(d.pop("if_value", UNSET))

        exported_nest_egg_config_files_additional_property_replace_item = cls(
            match=match,
            replace_with=replace_with,
            insert_new=insert_new,
            update_existing=update_existing,
            if_value=if_value,
        )

        exported_nest_egg_config_files_additional_property_replace_item.additional_properties = d
        return exported_nest_egg_config_files_additional_property_replace_item

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
