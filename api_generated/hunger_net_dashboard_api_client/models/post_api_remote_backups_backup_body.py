from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_remote_backups_backup_body_parts_item import PostApiRemoteBackupsBackupBodyPartsItem


T = TypeVar("T", bound="PostApiRemoteBackupsBackupBody")


@_attrs_define
class PostApiRemoteBackupsBackupBody:
    """
    Attributes:
        checksum (str):
        checksum_type (str):
        size (int):
        files (int):
        successful (bool):
        browsable (bool):
        streaming (bool):
        parts (list[PostApiRemoteBackupsBackupBodyPartsItem]):
    """

    checksum: str
    checksum_type: str
    size: int
    files: int
    successful: bool
    browsable: bool
    streaming: bool
    parts: list[PostApiRemoteBackupsBackupBodyPartsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksum = self.checksum

        checksum_type = self.checksum_type

        size = self.size

        files = self.files

        successful = self.successful

        browsable = self.browsable

        streaming = self.streaming

        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()
            parts.append(parts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checksum": checksum,
                "checksum_type": checksum_type,
                "size": size,
                "files": files,
                "successful": successful,
                "browsable": browsable,
                "streaming": streaming,
                "parts": parts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_remote_backups_backup_body_parts_item import PostApiRemoteBackupsBackupBodyPartsItem  # noqa: PLC0415

        d = dict(src_dict)
        checksum = d.pop("checksum")

        checksum_type = d.pop("checksum_type")

        size = d.pop("size")

        files = d.pop("files")

        successful = d.pop("successful")

        browsable = d.pop("browsable")

        streaming = d.pop("streaming")

        parts = []
        _parts = d.pop("parts")
        for parts_item_data in _parts:
            parts_item = PostApiRemoteBackupsBackupBodyPartsItem.from_dict(parts_item_data)

            parts.append(parts_item)

        post_api_remote_backups_backup_body = cls(
            checksum=checksum,
            checksum_type=checksum_type,
            size=size,
            files=files,
            successful=successful,
            browsable=browsable,
            streaming=streaming,
            parts=parts,
        )

        post_api_remote_backups_backup_body.additional_properties = d
        return post_api_remote_backups_backup_body

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
