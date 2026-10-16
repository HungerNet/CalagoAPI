from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EggAssignment")


@_attrs_define
class EggAssignment:
    """
    Attributes:
        affected_types (list[str]):
        egg (UUID):
    """

    affected_types: list[str]
    egg: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_types = self.affected_types

        egg = str(self.egg)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "affected_types": affected_types,
                "egg": egg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_types = cast(list[str], d.pop("affected_types"))

        egg = UUID(d.pop("egg"))

        egg_assignment = cls(
            affected_types=affected_types,
            egg=egg,
        )

        egg_assignment.additional_properties = d
        return egg_assignment

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
