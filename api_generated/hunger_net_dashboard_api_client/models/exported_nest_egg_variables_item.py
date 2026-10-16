from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exported_nest_egg_variables_item_description_translations import (
        ExportedNestEggVariablesItemDescriptionTranslations,
    )
    from ..models.exported_nest_egg_variables_item_name_translations import ExportedNestEggVariablesItemNameTranslations


T = TypeVar("T", bound="ExportedNestEggVariablesItem")


@_attrs_define
class ExportedNestEggVariablesItem:
    """
    Attributes:
        name (str):
        env_variable (str):
        user_viewable (bool):
        user_editable (bool):
        name_translations (ExportedNestEggVariablesItemNameTranslations | Unset):
        description (None | str | Unset):
        description_translations (ExportedNestEggVariablesItemDescriptionTranslations | Unset):
        order (int | Unset):
        default_value (None | str | Unset):
        secret (bool | Unset):
        rules (list[str] | Unset):
    """

    name: str
    env_variable: str
    user_viewable: bool
    user_editable: bool
    name_translations: ExportedNestEggVariablesItemNameTranslations | Unset = UNSET
    description: None | str | Unset = UNSET
    description_translations: ExportedNestEggVariablesItemDescriptionTranslations | Unset = UNSET
    order: int | Unset = UNSET
    default_value: None | str | Unset = UNSET
    secret: bool | Unset = UNSET
    rules: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        env_variable = self.env_variable

        user_viewable = self.user_viewable

        user_editable = self.user_editable

        name_translations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_translations, Unset):
            name_translations = self.name_translations.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        description_translations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description_translations, Unset):
            description_translations = self.description_translations.to_dict()

        order = self.order

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        secret = self.secret

        rules: list[str] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "env_variable": env_variable,
                "user_viewable": user_viewable,
                "user_editable": user_editable,
            }
        )
        if name_translations is not UNSET:
            field_dict["name_translations"] = name_translations
        if description is not UNSET:
            field_dict["description"] = description
        if description_translations is not UNSET:
            field_dict["description_translations"] = description_translations
        if order is not UNSET:
            field_dict["order"] = order
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if secret is not UNSET:
            field_dict["secret"] = secret
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exported_nest_egg_variables_item_description_translations import (
            ExportedNestEggVariablesItemDescriptionTranslations,  # noqa: PLC0415
        )
        from ..models.exported_nest_egg_variables_item_name_translations import (
            ExportedNestEggVariablesItemNameTranslations,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        env_variable = d.pop("env_variable")

        user_viewable = d.pop("user_viewable")

        user_editable = d.pop("user_editable")

        _name_translations = d.pop("name_translations", UNSET)
        name_translations: ExportedNestEggVariablesItemNameTranslations | Unset
        if isinstance(_name_translations, Unset):
            name_translations = UNSET
        else:
            name_translations = ExportedNestEggVariablesItemNameTranslations.from_dict(_name_translations)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _description_translations = d.pop("description_translations", UNSET)
        description_translations: ExportedNestEggVariablesItemDescriptionTranslations | Unset
        if isinstance(_description_translations, Unset):
            description_translations = UNSET
        else:
            description_translations = ExportedNestEggVariablesItemDescriptionTranslations.from_dict(
                _description_translations
            )

        order = d.pop("order", UNSET)

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        secret = d.pop("secret", UNSET)

        rules = cast(list[str], d.pop("rules", UNSET))

        exported_nest_egg_variables_item = cls(
            name=name,
            env_variable=env_variable,
            user_viewable=user_viewable,
            user_editable=user_editable,
            name_translations=name_translations,
            description=description,
            description_translations=description_translations,
            order=order,
            default_value=default_value,
            secret=secret,
            rules=rules,
        )

        exported_nest_egg_variables_item.additional_properties = d
        return exported_nest_egg_variables_item

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
