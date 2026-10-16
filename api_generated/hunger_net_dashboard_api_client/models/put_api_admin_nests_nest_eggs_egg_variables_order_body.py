from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApiAdminNestsNestEggsEggVariablesOrderBody")


@_attrs_define
class PutApiAdminNestsNestEggsEggVariablesOrderBody:
    """
    Attributes:
        variable_order (list[UUID]):
    """

    variable_order: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variable_order = []
        for variable_order_item_data in self.variable_order:
            variable_order_item = str(variable_order_item_data)
            variable_order.append(variable_order_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variable_order": variable_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        variable_order = []
        _variable_order = d.pop("variable_order")
        for variable_order_item_data in _variable_order:
            variable_order_item = UUID(variable_order_item_data)

            variable_order.append(variable_order_item)

        put_api_admin_nests_nest_eggs_egg_variables_order_body = cls(
            variable_order=variable_order,
        )

        put_api_admin_nests_nest_eggs_egg_variables_order_body.additional_properties = d
        return put_api_admin_nests_nest_eggs_egg_variables_order_body

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
