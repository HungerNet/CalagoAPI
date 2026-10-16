from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DirectorySizes")


@_attrs_define
class DirectorySizes:
    """
    Attributes:
        name (str):
        size (int):
        size_physical (int):
        files_size (int):
        inaccessible_size (int):
        other_size (int):
        other_count (int):
        truncated (bool):
        children (list[DirectorySizes]):
    """

    name: str
    size: int
    size_physical: int
    files_size: int
    inaccessible_size: int
    other_size: int
    other_count: int
    truncated: bool
    children: list[DirectorySizes]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        size = self.size

        size_physical = self.size_physical

        files_size = self.files_size

        inaccessible_size = self.inaccessible_size

        other_size = self.other_size

        other_count = self.other_count

        truncated = self.truncated

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "size": size,
                "size_physical": size_physical,
                "files_size": files_size,
                "inaccessible_size": inaccessible_size,
                "other_size": other_size,
                "other_count": other_count,
                "truncated": truncated,
                "children": children,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        size = d.pop("size")

        size_physical = d.pop("size_physical")

        files_size = d.pop("files_size")

        inaccessible_size = d.pop("inaccessible_size")

        other_size = d.pop("other_size")

        other_count = d.pop("other_count")

        truncated = d.pop("truncated")

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = DirectorySizes.from_dict(children_item_data)

            children.append(children_item)

        directory_sizes = cls(
            name=name,
            size=size,
            size_physical=size_physical,
            files_size=files_size,
            inaccessible_size=inaccessible_size,
            other_size=other_size,
            other_count=other_count,
            truncated=truncated,
            children=children,
        )

        directory_sizes.additional_properties = d
        return directory_sizes

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
