from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.archive_format import ArchiveFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiClientServersServerBackupsBackupQueryResponse200")


@_attrs_define
class GetApiClientServersServerBackupsBackupQueryResponse200:
    """
    Attributes:
        archive_format (ArchiveFormat | None | Unset):
        size (int | None | Unset):
    """

    archive_format: ArchiveFormat | None | Unset = UNSET
    size: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archive_format: None | str | Unset
        if isinstance(self.archive_format, Unset):
            archive_format = UNSET
        elif isinstance(self.archive_format, ArchiveFormat):
            archive_format = self.archive_format.value
        else:
            archive_format = self.archive_format

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archive_format is not UNSET:
            field_dict["archive_format"] = archive_format
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_archive_format(data: object) -> ArchiveFormat | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archive_format_type_1 = ArchiveFormat(data)

                return archive_format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArchiveFormat | None | Unset, data)

        archive_format = _parse_archive_format(d.pop("archive_format", UNSET))

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        get_api_client_servers_server_backups_backup_query_response_200 = cls(
            archive_format=archive_format,
            size=size,
        )

        get_api_client_servers_server_backups_backup_query_response_200.additional_properties = d
        return get_api_client_servers_server_backups_backup_query_response_200

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
