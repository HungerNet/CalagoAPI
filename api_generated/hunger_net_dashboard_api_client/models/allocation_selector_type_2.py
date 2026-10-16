from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.allocation_selector_type_2_type import AllocationSelectorType2Type

if TYPE_CHECKING:
    from ..models.allocation_filter import AllocationFilter


T = TypeVar("T", bound="AllocationSelectorType2")


@_attrs_define
class AllocationSelectorType2:
    """
    Attributes:
        filter_ (AllocationFilter):
        type_ (AllocationSelectorType2Type):
    """

    filter_: AllocationFilter
    type_: AllocationSelectorType2Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_filter import AllocationFilter  # noqa: PLC0415

        d = dict(src_dict)
        filter_ = AllocationFilter.from_dict(d.pop("filter"))

        type_ = AllocationSelectorType2Type(d.pop("type"))

        allocation_selector_type_2 = cls(
            filter_=filter_,
            type_=type_,
        )

        allocation_selector_type_2.additional_properties = d
        return allocation_selector_type_2

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
