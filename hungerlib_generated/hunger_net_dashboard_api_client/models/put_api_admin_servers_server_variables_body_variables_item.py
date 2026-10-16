from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApiAdminServersServerVariablesBodyVariablesItem")


@_attrs_define
class PutApiAdminServersServerVariablesBodyVariablesItem:
    """
    Attributes:
        env_variable (str):
        value (str):
    """

    env_variable: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_variable = self.env_variable

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "env_variable": env_variable,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        env_variable = d.pop("env_variable")

        value = d.pop("value")

        put_api_admin_servers_server_variables_body_variables_item = cls(
            env_variable=env_variable,
            value=value,
        )

        put_api_admin_servers_server_variables_body_variables_item.additional_properties = d
        return put_api_admin_servers_server_variables_body_variables_item

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
