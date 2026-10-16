from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.email_variable import EmailVariable


T = TypeVar("T", bound="GetApiAdminSystemEmailTemplatesIdentifierVariablesResponse200")


@_attrs_define
class GetApiAdminSystemEmailTemplatesIdentifierVariablesResponse200:
    """
    Attributes:
        email_variables (list[EmailVariable]):
    """

    email_variables: list[EmailVariable]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_variables = []
        for email_variables_item_data in self.email_variables:
            email_variables_item = email_variables_item_data.to_dict()
            email_variables.append(email_variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_variables": email_variables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_variable import EmailVariable  # noqa: PLC0415

        d = dict(src_dict)
        email_variables = []
        _email_variables = d.pop("email_variables")
        for email_variables_item_data in _email_variables:
            email_variables_item = EmailVariable.from_dict(email_variables_item_data)

            email_variables.append(email_variables_item)

        get_api_admin_system_email_templates_identifier_variables_response_200 = cls(
            email_variables=email_variables,
        )

        get_api_admin_system_email_templates_identifier_variables_response_200.additional_properties = d
        return get_api_admin_system_email_templates_identifier_variables_response_200

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
