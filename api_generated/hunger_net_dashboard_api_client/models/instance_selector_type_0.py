from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.instance_selector_type_0_type import InstanceSelectorType0Type

T = TypeVar("T", bound="InstanceSelectorType0")


@_attrs_define
class InstanceSelectorType0:
    """
    Attributes:
        uuids (list[UUID]):
        type_ (InstanceSelectorType0Type):
    """

    uuids: list[UUID]
    type_: InstanceSelectorType0Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuids = []
        for uuids_item_data in self.uuids:
            uuids_item = str(uuids_item_data)
            uuids.append(uuids_item)

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuids": uuids,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuids = []
        _uuids = d.pop("uuids")
        for uuids_item_data in _uuids:
            uuids_item = UUID(uuids_item_data)

            uuids.append(uuids_item)

        type_ = InstanceSelectorType0Type(d.pop("type"))

        instance_selector_type_0 = cls(
            uuids=uuids,
            type_=type_,
        )

        instance_selector_type_0.additional_properties = d
        return instance_selector_type_0

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
