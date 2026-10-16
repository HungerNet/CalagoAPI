from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_admin_nests_nest_eggs_egg_variables_variable_body_description_translations_type_0 import (
        PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0,
    )
    from ..models.patch_api_admin_nests_nest_eggs_egg_variables_variable_body_name_translations_type_0 import (
        PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0,
    )


T = TypeVar("T", bound="PatchApiAdminNestsNestEggsEggVariablesVariableBody")


@_attrs_define
class PatchApiAdminNestsNestEggsEggVariablesVariableBody:
    """
    Attributes:
        name (None | str | Unset):
        name_translations (None | PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0 | Unset):
        description (None | str | Unset):
        description_translations (None | PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0
            | Unset):
        order (int | None | Unset):
        env_variable (None | str | Unset):
        default_value (None | str | Unset):
        user_viewable (bool | None | Unset):
        user_editable (bool | None | Unset):
        secret (bool | None | Unset):
        rules (list[str] | None | Unset):
    """

    name: None | str | Unset = UNSET
    name_translations: None | PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0 | Unset = UNSET
    description: None | str | Unset = UNSET
    description_translations: (
        None | PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0 | Unset
    ) = UNSET
    order: int | None | Unset = UNSET
    env_variable: None | str | Unset = UNSET
    default_value: None | str | Unset = UNSET
    user_viewable: bool | None | Unset = UNSET
    user_editable: bool | None | Unset = UNSET
    secret: bool | None | Unset = UNSET
    rules: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_api_admin_nests_nest_eggs_egg_variables_variable_body_description_translations_type_0 import (
            PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_variables_variable_body_name_translations_type_0 import (
            PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0,  # noqa: PLC0415
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        name_translations: dict[str, Any] | None | Unset
        if isinstance(self.name_translations, Unset):
            name_translations = UNSET
        elif isinstance(
            self.name_translations, PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0
        ):
            name_translations = self.name_translations.to_dict()
        else:
            name_translations = self.name_translations

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        description_translations: dict[str, Any] | None | Unset
        if isinstance(self.description_translations, Unset):
            description_translations = UNSET
        elif isinstance(
            self.description_translations,
            PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0,
        ):
            description_translations = self.description_translations.to_dict()
        else:
            description_translations = self.description_translations

        order: int | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        env_variable: None | str | Unset
        if isinstance(self.env_variable, Unset):
            env_variable = UNSET
        else:
            env_variable = self.env_variable

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        user_viewable: bool | None | Unset
        if isinstance(self.user_viewable, Unset):
            user_viewable = UNSET
        else:
            user_viewable = self.user_viewable

        user_editable: bool | None | Unset
        if isinstance(self.user_editable, Unset):
            user_editable = UNSET
        else:
            user_editable = self.user_editable

        secret: bool | None | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        else:
            secret = self.secret

        rules: list[str] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, list):
            rules = self.rules

        else:
            rules = self.rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if name_translations is not UNSET:
            field_dict["name_translations"] = name_translations
        if description is not UNSET:
            field_dict["description"] = description
        if description_translations is not UNSET:
            field_dict["description_translations"] = description_translations
        if order is not UNSET:
            field_dict["order"] = order
        if env_variable is not UNSET:
            field_dict["env_variable"] = env_variable
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if user_viewable is not UNSET:
            field_dict["user_viewable"] = user_viewable
        if user_editable is not UNSET:
            field_dict["user_editable"] = user_editable
        if secret is not UNSET:
            field_dict["secret"] = secret
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_api_admin_nests_nest_eggs_egg_variables_variable_body_description_translations_type_0 import (
            PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_variables_variable_body_name_translations_type_0 import (
            PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_name_translations(
            data: object,
        ) -> None | PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_translations_type_0 = (
                    PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0.from_dict(data)
                )

                return name_translations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminNestsNestEggsEggVariablesVariableBodyNameTranslationsType0 | Unset, data)

        name_translations = _parse_name_translations(d.pop("name_translations", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_description_translations(
            data: object,
        ) -> None | PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                description_translations_type_0 = (
                    PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0.from_dict(data)
                )

                return description_translations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PatchApiAdminNestsNestEggsEggVariablesVariableBodyDescriptionTranslationsType0 | Unset, data
            )

        description_translations = _parse_description_translations(d.pop("description_translations", UNSET))

        def _parse_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))

        def _parse_env_variable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        env_variable = _parse_env_variable(d.pop("env_variable", UNSET))

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        def _parse_user_viewable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_viewable = _parse_user_viewable(d.pop("user_viewable", UNSET))

        def _parse_user_editable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_editable = _parse_user_editable(d.pop("user_editable", UNSET))

        def _parse_secret(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        secret = _parse_secret(d.pop("secret", UNSET))

        def _parse_rules(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_type_0 = cast(list[str], data)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))

        patch_api_admin_nests_nest_eggs_egg_variables_variable_body = cls(
            name=name,
            name_translations=name_translations,
            description=description,
            description_translations=description_translations,
            order=order,
            env_variable=env_variable,
            default_value=default_value,
            user_viewable=user_viewable,
            user_editable=user_editable,
            secret=secret,
            rules=rules,
        )

        patch_api_admin_nests_nest_eggs_egg_variables_variable_body.additional_properties = d
        return patch_api_admin_nests_nest_eggs_egg_variables_variable_body

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
