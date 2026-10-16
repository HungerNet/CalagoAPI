from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_email_templates_response_200_email_templates_item import (
        GetApiAdminSystemEmailTemplatesResponse200EmailTemplatesItem,
    )


T = TypeVar("T", bound="GetApiAdminSystemEmailTemplatesResponse200")


@_attrs_define
class GetApiAdminSystemEmailTemplatesResponse200:
    """
    Attributes:
        email_templates (list[GetApiAdminSystemEmailTemplatesResponse200EmailTemplatesItem]):
    """

    email_templates: list[GetApiAdminSystemEmailTemplatesResponse200EmailTemplatesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_templates = []
        for email_templates_item_data in self.email_templates:
            email_templates_item = email_templates_item_data.to_dict()
            email_templates.append(email_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_templates": email_templates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_email_templates_response_200_email_templates_item import (
            GetApiAdminSystemEmailTemplatesResponse200EmailTemplatesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        email_templates = []
        _email_templates = d.pop("email_templates")
        for email_templates_item_data in _email_templates:
            email_templates_item = GetApiAdminSystemEmailTemplatesResponse200EmailTemplatesItem.from_dict(
                email_templates_item_data
            )

            email_templates.append(email_templates_item)

        get_api_admin_system_email_templates_response_200 = cls(
            email_templates=email_templates,
        )

        get_api_admin_system_email_templates_response_200.additional_properties = d
        return get_api_admin_system_email_templates_response_200

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
