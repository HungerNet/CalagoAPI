from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nest_egg_variable import NestEggVariable


T = TypeVar("T", bound="GetApiAdminNestsNestEggsEggVariablesResponse200")


@_attrs_define
class GetApiAdminNestsNestEggsEggVariablesResponse200:
    """
    Attributes:
        variables (list[NestEggVariable]):
    """

    variables: list[NestEggVariable]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variables": variables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nest_egg_variable import NestEggVariable  # noqa: PLC0415

        d = dict(src_dict)
        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = NestEggVariable.from_dict(variables_item_data)

            variables.append(variables_item)

        get_api_admin_nests_nest_eggs_egg_variables_response_200 = cls(
            variables=variables,
        )

        get_api_admin_nests_nest_eggs_egg_variables_response_200.additional_properties = d
        return get_api_admin_nests_nest_eggs_egg_variables_response_200

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
