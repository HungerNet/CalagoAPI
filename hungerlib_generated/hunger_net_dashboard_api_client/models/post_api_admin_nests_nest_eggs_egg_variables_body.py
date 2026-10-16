from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_admin_nests_nest_eggs_egg_variables_body_description_translations import (
        PostApiAdminNestsNestEggsEggVariablesBodyDescriptionTranslations,
    )
    from ..models.post_api_admin_nests_nest_eggs_egg_variables_body_name_translations import (
        PostApiAdminNestsNestEggsEggVariablesBodyNameTranslations,
    )


T = TypeVar("T", bound="PostApiAdminNestsNestEggsEggVariablesBody")


@_attrs_define
class PostApiAdminNestsNestEggsEggVariablesBody:
    """
    Attributes:
        name (str):
        name_translations (PostApiAdminNestsNestEggsEggVariablesBodyNameTranslations):
        description_translations (PostApiAdminNestsNestEggsEggVariablesBodyDescriptionTranslations):
        order (int):
        env_variable (str):
        user_viewable (bool):
        user_editable (bool):
        secret (bool):
        rules (list[str]):
        description (None | str | Unset):
        default_value (None | str | Unset):
    """

    name: str
    name_translations: PostApiAdminNestsNestEggsEggVariablesBodyNameTranslations
    description_translations: PostApiAdminNestsNestEggsEggVariablesBodyDescriptionTranslations
    order: int
    env_variable: str
    user_viewable: bool
    user_editable: bool
    secret: bool
    rules: list[str]
    description: None | str | Unset = UNSET
    default_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        name_translations = self.name_translations.to_dict()

        description_translations = self.description_translations.to_dict()

        order = self.order

        env_variable = self.env_variable

        user_viewable = self.user_viewable

        user_editable = self.user_editable

        secret = self.secret

        rules = self.rules

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
                "name": name,
                "name_translations": name_translations,
                "description_translations": description_translations,
                "order": order,
                "env_variable": env_variable,
                "user_viewable": user_viewable,
                "user_editable": user_editable,
                "secret": secret,
                "rules": rules,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["default_value"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_admin_nests_nest_eggs_egg_variables_body_description_translations import (
            PostApiAdminNestsNestEggsEggVariablesBodyDescriptionTranslations,  # noqa: PLC0415
        )
        from ..models.post_api_admin_nests_nest_eggs_egg_variables_body_name_translations import (
            PostApiAdminNestsNestEggsEggVariablesBodyNameTranslations,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        name_translations = PostApiAdminNestsNestEggsEggVariablesBodyNameTranslations.from_dict(
            d.pop("name_translations")
        )

        description_translations = PostApiAdminNestsNestEggsEggVariablesBodyDescriptionTranslations.from_dict(
            d.pop("description_translations")
        )

        order = d.pop("order")

        env_variable = d.pop("env_variable")

        user_viewable = d.pop("user_viewable")

        user_editable = d.pop("user_editable")

        secret = d.pop("secret")

        rules = cast(list[str], d.pop("rules"))

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

        post_api_admin_nests_nest_eggs_egg_variables_body = cls(
            name=name,
            name_translations=name_translations,
            description_translations=description_translations,
            order=order,
            env_variable=env_variable,
            user_viewable=user_viewable,
            user_editable=user_editable,
            secret=secret,
            rules=rules,
            description=description,
            default_value=default_value,
        )

        post_api_admin_nests_nest_eggs_egg_variables_body.additional_properties = d
        return post_api_admin_nests_nest_eggs_egg_variables_body

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
