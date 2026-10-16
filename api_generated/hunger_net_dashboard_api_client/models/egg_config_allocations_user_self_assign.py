from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EggConfigAllocationsUserSelfAssign")


@_attrs_define
class EggConfigAllocationsUserSelfAssign:
    """
    Attributes:
        enabled (bool):
        require_primary_allocation (bool):
        start_port (int):
        end_port (int):
    """

    enabled: bool
    require_primary_allocation: bool
    start_port: int
    end_port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        require_primary_allocation = self.require_primary_allocation

        start_port = self.start_port

        end_port = self.end_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "require_primary_allocation": require_primary_allocation,
                "start_port": start_port,
                "end_port": end_port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        require_primary_allocation = d.pop("require_primary_allocation")

        start_port = d.pop("start_port")

        end_port = d.pop("end_port")

        egg_config_allocations_user_self_assign = cls(
            enabled=enabled,
            require_primary_allocation=require_primary_allocation,
            start_port=start_port,
            end_port=end_port,
        )

        egg_config_allocations_user_self_assign.additional_properties = d
        return egg_config_allocations_user_self_assign

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
