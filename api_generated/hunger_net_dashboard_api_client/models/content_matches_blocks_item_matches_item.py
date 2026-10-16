from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ContentMatchesBlocksItemMatchesItem")


@_attrs_define
class ContentMatchesBlocksItemMatchesItem:
    """
    Attributes:
        start_byte (int):
        end_byte (int):
    """

    start_byte: int
    end_byte: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_byte = self.start_byte

        end_byte = self.end_byte

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_byte": start_byte,
                "end_byte": end_byte,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_byte = d.pop("start_byte")

        end_byte = d.pop("end_byte")

        content_matches_blocks_item_matches_item = cls(
            start_byte=start_byte,
            end_byte=end_byte,
        )

        content_matches_blocks_item_matches_item.additional_properties = d
        return content_matches_blocks_item_matches_item

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
