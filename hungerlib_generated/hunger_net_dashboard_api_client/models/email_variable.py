from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_variable_default_translations import EmailVariableDefaultTranslations
    from ..models.email_variable_value_translations import EmailVariableValueTranslations


T = TypeVar("T", bound="EmailVariable")


@_attrs_define
class EmailVariable:
    """
    Attributes:
        name (str):
        system (bool):
        default_translations (EmailVariableDefaultTranslations):
        value_translations (EmailVariableValueTranslations):
        template_identifier (None | str | Unset):
        default_value (None | str | Unset):
        value (None | str | Unset):
    """

    name: str
    system: bool
    default_translations: EmailVariableDefaultTranslations
    value_translations: EmailVariableValueTranslations
    template_identifier: None | str | Unset = UNSET
    default_value: None | str | Unset = UNSET
    value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        system = self.system

        default_translations = self.default_translations.to_dict()

        value_translations = self.value_translations.to_dict()

        template_identifier: None | str | Unset
        if isinstance(self.template_identifier, Unset):
            template_identifier = UNSET
        else:
            template_identifier = self.template_identifier

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "system": system,
                "default_translations": default_translations,
                "value_translations": value_translations,
            }
        )
        if template_identifier is not UNSET:
            field_dict["template_identifier"] = template_identifier
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_variable_default_translations import EmailVariableDefaultTranslations  # noqa: PLC0415
        from ..models.email_variable_value_translations import EmailVariableValueTranslations  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        system = d.pop("system")

        default_translations = EmailVariableDefaultTranslations.from_dict(d.pop("default_translations"))

        value_translations = EmailVariableValueTranslations.from_dict(d.pop("value_translations"))

        def _parse_template_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_identifier = _parse_template_identifier(d.pop("template_identifier", UNSET))

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        email_variable = cls(
            name=name,
            system=system,
            default_translations=default_translations,
            value_translations=value_translations,
            template_identifier=template_identifier,
            default_value=default_value,
            value=value,
        )

        email_variable.additional_properties = d
        return email_variable

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
