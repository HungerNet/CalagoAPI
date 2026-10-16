from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_matches_blocks_item import ContentMatchesBlocksItem


T = TypeVar("T", bound="ContentMatches")


@_attrs_define
class ContentMatches:
    """
    Attributes:
        file (str):
        truncated (bool):
        blocks (list[ContentMatchesBlocksItem]):
    """

    file: str
    truncated: bool
    blocks: list[ContentMatchesBlocksItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        truncated = self.truncated

        blocks = []
        for blocks_item_data in self.blocks:
            blocks_item = blocks_item_data.to_dict()
            blocks.append(blocks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "truncated": truncated,
                "blocks": blocks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_matches_blocks_item import ContentMatchesBlocksItem  # noqa: PLC0415

        d = dict(src_dict)
        file = d.pop("file")

        truncated = d.pop("truncated")

        blocks = []
        _blocks = d.pop("blocks")
        for blocks_item_data in _blocks:
            blocks_item = ContentMatchesBlocksItem.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        content_matches = cls(
            file=file,
            truncated=truncated,
            blocks=blocks,
        )

        content_matches.additional_properties = d
        return content_matches

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
