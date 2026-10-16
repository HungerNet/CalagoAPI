from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiAdminSystemEmailTemplatesIdentifierResponse200EmailTemplate")


@_attrs_define
class GetApiAdminSystemEmailTemplatesIdentifierResponse200EmailTemplate:
    """
    Attributes:
        available_variables (list[str]):
        default_enabled (bool):
        enabled (bool):
        default_subject (str):
        default_content (str):
        subject (None | str | Unset):
        content (None | str | Unset):
    """

    available_variables: list[str]
    default_enabled: bool
    enabled: bool
    default_subject: str
    default_content: str
    subject: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_variables = self.available_variables

        default_enabled = self.default_enabled

        enabled = self.enabled

        default_subject = self.default_subject

        default_content = self.default_content

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_variables": available_variables,
                "default_enabled": default_enabled,
                "enabled": enabled,
                "default_subject": default_subject,
                "default_content": default_content,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_variables = cast(list[str], d.pop("available_variables"))

        default_enabled = d.pop("default_enabled")

        enabled = d.pop("enabled")

        default_subject = d.pop("default_subject")

        default_content = d.pop("default_content")

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        get_api_admin_system_email_templates_identifier_response_200_email_template = cls(
            available_variables=available_variables,
            default_enabled=default_enabled,
            enabled=enabled,
            default_subject=default_subject,
            default_content=default_content,
            subject=subject,
            content=content,
        )

        get_api_admin_system_email_templates_identifier_response_200_email_template.additional_properties = d
        return get_api_admin_system_email_templates_identifier_response_200_email_template

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
