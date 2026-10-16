from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EggConfigAllocationsDeploymentPrimaryType1")


@_attrs_define
class EggConfigAllocationsDeploymentPrimaryType1:
    """
    Attributes:
        start_port (int):
        end_port (int):
        assign_to_variable (None | str | Unset):
    """

    start_port: int
    end_port: int
    assign_to_variable: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_port = self.start_port

        end_port = self.end_port

        assign_to_variable: None | str | Unset
        if isinstance(self.assign_to_variable, Unset):
            assign_to_variable = UNSET
        else:
            assign_to_variable = self.assign_to_variable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_port": start_port,
                "end_port": end_port,
            }
        )
        if assign_to_variable is not UNSET:
            field_dict["assign_to_variable"] = assign_to_variable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_port = d.pop("start_port")

        end_port = d.pop("end_port")

        def _parse_assign_to_variable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to_variable = _parse_assign_to_variable(d.pop("assign_to_variable", UNSET))

        egg_config_allocations_deployment_primary_type_1 = cls(
            start_port=start_port,
            end_port=end_port,
            assign_to_variable=assign_to_variable,
        )

        egg_config_allocations_deployment_primary_type_1.additional_properties = d
        return egg_config_allocations_deployment_primary_type_1

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
