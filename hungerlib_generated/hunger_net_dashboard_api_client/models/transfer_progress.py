from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransferProgress")


@_attrs_define
class TransferProgress:
    """
    Attributes:
        archive_bytes_processed (int):
        network_bytes_processed (int):
        bytes_total (int):
        files_processed (int):
    """

    archive_bytes_processed: int
    network_bytes_processed: int
    bytes_total: int
    files_processed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archive_bytes_processed = self.archive_bytes_processed

        network_bytes_processed = self.network_bytes_processed

        bytes_total = self.bytes_total

        files_processed = self.files_processed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archive_bytes_processed": archive_bytes_processed,
                "network_bytes_processed": network_bytes_processed,
                "bytes_total": bytes_total,
                "files_processed": files_processed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archive_bytes_processed = d.pop("archive_bytes_processed")

        network_bytes_processed = d.pop("network_bytes_processed")

        bytes_total = d.pop("bytes_total")

        files_processed = d.pop("files_processed")

        transfer_progress = cls(
            archive_bytes_processed=archive_bytes_processed,
            network_bytes_processed=network_bytes_processed,
            bytes_total=bytes_total,
            files_processed=files_processed,
        )

        transfer_progress.additional_properties = d
        return transfer_progress

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
