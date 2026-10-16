from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_matches_blocks_item_matches_item import ContentMatchesBlocksItemMatchesItem


T = TypeVar("T", bound="ContentMatchesBlocksItem")


@_attrs_define
class ContentMatchesBlocksItem:
    """
    Attributes:
        start_line (int):
        end_line (int):
        content (str):
        matches (list[ContentMatchesBlocksItemMatchesItem]):
    """

    start_line: int
    end_line: int
    content: str
    matches: list[ContentMatchesBlocksItemMatchesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_line = self.start_line

        end_line = self.end_line

        content = self.content

        matches = []
        for matches_item_data in self.matches:
            matches_item = matches_item_data.to_dict()
            matches.append(matches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_line": start_line,
                "end_line": end_line,
                "content": content,
                "matches": matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_matches_blocks_item_matches_item import ContentMatchesBlocksItemMatchesItem  # noqa: PLC0415

        d = dict(src_dict)
        start_line = d.pop("start_line")

        end_line = d.pop("end_line")

        content = d.pop("content")

        matches = []
        _matches = d.pop("matches")
        for matches_item_data in _matches:
            matches_item = ContentMatchesBlocksItemMatchesItem.from_dict(matches_item_data)

            matches.append(matches_item)

        content_matches_blocks_item = cls(
            start_line=start_line,
            end_line=end_line,
            content=content,
            matches=matches,
        )

        content_matches_blocks_item.additional_properties = d
        return content_matches_blocks_item

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
