from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.directory_entry import DirectoryEntry


T = TypeVar("T", bound="PostApiClientServersServerFilesCopyManyResponse200")


@_attrs_define
class PostApiClientServersServerFilesCopyManyResponse200:
    """
    Attributes:
        copied (int):
        skipped (list[DirectoryEntry]):
    """

    copied: int
    skipped: list[DirectoryEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        copied = self.copied

        skipped = []
        for skipped_item_data in self.skipped:
            skipped_item = skipped_item_data.to_dict()
            skipped.append(skipped_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "copied": copied,
                "skipped": skipped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.directory_entry import DirectoryEntry  # noqa: PLC0415

        d = dict(src_dict)
        copied = d.pop("copied")

        skipped = []
        _skipped = d.pop("skipped")
        for skipped_item_data in _skipped:
            skipped_item = DirectoryEntry.from_dict(skipped_item_data)

            skipped.append(skipped_item)

        post_api_client_servers_server_files_copy_many_response_200 = cls(
            copied=copied,
            skipped=skipped,
        )

        post_api_client_servers_server_files_copy_many_response_200.additional_properties = d
        return post_api_client_servers_server_files_copy_many_response_200

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
