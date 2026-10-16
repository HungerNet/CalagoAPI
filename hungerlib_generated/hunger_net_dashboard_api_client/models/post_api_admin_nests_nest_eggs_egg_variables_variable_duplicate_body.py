from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAdminNestsNestEggsEggVariablesVariableDuplicateBody")


@_attrs_define
class PostApiAdminNestsNestEggsEggVariablesVariableDuplicateBody:
    """
    Attributes:
        name (str):
        env_variable (str):
    """

    name: str
    env_variable: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        env_variable = self.env_variable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "env_variable": env_variable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        env_variable = d.pop("env_variable")

        post_api_admin_nests_nest_eggs_egg_variables_variable_duplicate_body = cls(
            name=name,
            env_variable=env_variable,
        )

        post_api_admin_nests_nest_eggs_egg_variables_variable_duplicate_body.additional_properties = d
        return post_api_admin_nests_nest_eggs_egg_variables_variable_duplicate_body

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
