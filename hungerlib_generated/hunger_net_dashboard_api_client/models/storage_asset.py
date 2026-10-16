from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StorageAsset")


@_attrs_define
class StorageAsset:
    """
    Attributes:
        name (str):
        url (str):
        size (int):
        is_directory (bool):
        created (datetime.datetime):
    """

    name: str
    url: str
    size: int
    is_directory: bool
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        size = self.size

        is_directory = self.is_directory

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
                "size": size,
                "is_directory": is_directory,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        size = d.pop("size")

        is_directory = d.pop("is_directory")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        storage_asset = cls(
            name=name,
            url=url,
            size=size,
            is_directory=is_directory,
            created=created,
        )

        storage_asset.additional_properties = d
        return storage_asset

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
