from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminSystemEmailTemplatesResponse200EmailTemplatesItem")


@_attrs_define
class GetApiAdminSystemEmailTemplatesResponse200EmailTemplatesItem:
    """
    Attributes:
        identifier (str):
        available_variables (list[str]):
    """

    identifier: str
    available_variables: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        available_variables = self.available_variables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "available_variables": available_variables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        available_variables = cast(list[str], d.pop("available_variables"))

        get_api_admin_system_email_templates_response_200_email_templates_item = cls(
            identifier=identifier,
            available_variables=available_variables,
        )

        get_api_admin_system_email_templates_response_200_email_templates_item.additional_properties = d
        return get_api_admin_system_email_templates_response_200_email_templates_item

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
