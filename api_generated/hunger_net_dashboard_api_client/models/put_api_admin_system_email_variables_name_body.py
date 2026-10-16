from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_admin_system_email_variables_name_body_value_translations_type_0 import (
        PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0,
    )


T = TypeVar("T", bound="PutApiAdminSystemEmailVariablesNameBody")


@_attrs_define
class PutApiAdminSystemEmailVariablesNameBody:
    """
    Attributes:
        value (None | str | Unset):
        value_translations (None | PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0 | Unset):
    """

    value: None | str | Unset = UNSET
    value_translations: None | PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.put_api_admin_system_email_variables_name_body_value_translations_type_0 import (
            PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0,  # noqa: PLC0415
        )

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        value_translations: dict[str, Any] | None | Unset
        if isinstance(self.value_translations, Unset):
            value_translations = UNSET
        elif isinstance(self.value_translations, PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0):
            value_translations = self.value_translations.to_dict()
        else:
            value_translations = self.value_translations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if value_translations is not UNSET:
            field_dict["value_translations"] = value_translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_admin_system_email_variables_name_body_value_translations_type_0 import (
            PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_value_translations(
            data: object,
        ) -> None | PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_translations_type_0 = PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0.from_dict(
                    data
                )

                return value_translations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PutApiAdminSystemEmailVariablesNameBodyValueTranslationsType0 | Unset, data)

        value_translations = _parse_value_translations(d.pop("value_translations", UNSET))

        put_api_admin_system_email_variables_name_body = cls(
            value=value,
            value_translations=value_translations,
        )

        put_api_admin_system_email_variables_name_body.additional_properties = d
        return put_api_admin_system_email_variables_name_body

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
