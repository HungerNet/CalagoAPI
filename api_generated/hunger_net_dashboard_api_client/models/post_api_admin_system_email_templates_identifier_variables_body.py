from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_admin_system_email_templates_identifier_variables_body_value_translations import (
        PostApiAdminSystemEmailTemplatesIdentifierVariablesBodyValueTranslations,
    )


T = TypeVar("T", bound="PostApiAdminSystemEmailTemplatesIdentifierVariablesBody")


@_attrs_define
class PostApiAdminSystemEmailTemplatesIdentifierVariablesBody:
    """
    Attributes:
        name (str):
        value (str):
        value_translations (PostApiAdminSystemEmailTemplatesIdentifierVariablesBodyValueTranslations | Unset):
    """

    name: str
    value: str
    value_translations: PostApiAdminSystemEmailTemplatesIdentifierVariablesBodyValueTranslations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        value_translations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_translations, Unset):
            value_translations = self.value_translations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if value_translations is not UNSET:
            field_dict["value_translations"] = value_translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_admin_system_email_templates_identifier_variables_body_value_translations import (
            PostApiAdminSystemEmailTemplatesIdentifierVariablesBodyValueTranslations,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        _value_translations = d.pop("value_translations", UNSET)
        value_translations: PostApiAdminSystemEmailTemplatesIdentifierVariablesBodyValueTranslations | Unset
        if isinstance(_value_translations, Unset):
            value_translations = UNSET
        else:
            value_translations = PostApiAdminSystemEmailTemplatesIdentifierVariablesBodyValueTranslations.from_dict(
                _value_translations
            )

        post_api_admin_system_email_templates_identifier_variables_body = cls(
            name=name,
            value=value,
            value_translations=value_translations,
        )

        post_api_admin_system_email_templates_identifier_variables_body.additional_properties = d
        return post_api_admin_system_email_templates_identifier_variables_body

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
