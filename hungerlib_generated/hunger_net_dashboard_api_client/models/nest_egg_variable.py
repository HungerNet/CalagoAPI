from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nest_egg_variable_description_translations import NestEggVariableDescriptionTranslations
    from ..models.nest_egg_variable_name_translations import NestEggVariableNameTranslations


T = TypeVar("T", bound="NestEggVariable")


@_attrs_define
class NestEggVariable:
    """
    Attributes:
        uuid (UUID):
        name (str):
        name_translations (NestEggVariableNameTranslations):
        description_translations (NestEggVariableDescriptionTranslations):
        order (int):
        env_variable (str):
        user_viewable (bool):
        user_editable (bool):
        is_secret (bool):
        rules (list[str]):
        created (datetime.datetime):
        description (None | str | Unset):
        default_value (None | str | Unset):
    """

    uuid: UUID
    name: str
    name_translations: NestEggVariableNameTranslations
    description_translations: NestEggVariableDescriptionTranslations
    order: int
    env_variable: str
    user_viewable: bool
    user_editable: bool
    is_secret: bool
    rules: list[str]
    created: datetime.datetime
    description: None | str | Unset = UNSET
    default_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        name_translations = self.name_translations.to_dict()

        description_translations = self.description_translations.to_dict()

        order = self.order

        env_variable = self.env_variable

        user_viewable = self.user_viewable

        user_editable = self.user_editable

        is_secret = self.is_secret

        rules = self.rules

        created = self.created.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "name_translations": name_translations,
                "description_translations": description_translations,
                "order": order,
                "env_variable": env_variable,
                "user_viewable": user_viewable,
                "user_editable": user_editable,
                "is_secret": is_secret,
                "rules": rules,
                "created": created,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["default_value"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nest_egg_variable_description_translations import NestEggVariableDescriptionTranslations  # noqa: PLC0415
        from ..models.nest_egg_variable_name_translations import NestEggVariableNameTranslations  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        name_translations = NestEggVariableNameTranslations.from_dict(d.pop("name_translations"))

        description_translations = NestEggVariableDescriptionTranslations.from_dict(d.pop("description_translations"))

        order = d.pop("order")

        env_variable = d.pop("env_variable")

        user_viewable = d.pop("user_viewable")

        user_editable = d.pop("user_editable")

        is_secret = d.pop("is_secret")

        rules = cast(list[str], d.pop("rules"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        nest_egg_variable = cls(
            uuid=uuid,
            name=name,
            name_translations=name_translations,
            description_translations=description_translations,
            order=order,
            env_variable=env_variable,
            user_viewable=user_viewable,
            user_editable=user_editable,
            is_secret=is_secret,
            rules=rules,
            created=created,
            description=description,
            default_value=default_value,
        )

        nest_egg_variable.additional_properties = d
        return nest_egg_variable

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
