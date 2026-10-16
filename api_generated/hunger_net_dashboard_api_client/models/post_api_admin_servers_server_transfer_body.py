from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compression_level import CompressionLevel
from ..models.transfer_archive_format import TransferArchiveFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminServersServerTransferBody")


@_attrs_define
class PostApiAdminServersServerTransferBody:
    """
    Attributes:
        node_uuid (UUID):
        allocation_uuids (list[UUID]):
        backups (list[UUID]):
        delete_source_backups (bool):
        archive_format (TransferArchiveFormat):
        multiplex_channels (int):
        allocation_uuid (None | Unset | UUID):
        compression_level (CompressionLevel | None | Unset):
    """

    node_uuid: UUID
    allocation_uuids: list[UUID]
    backups: list[UUID]
    delete_source_backups: bool
    archive_format: TransferArchiveFormat
    multiplex_channels: int
    allocation_uuid: None | Unset | UUID = UNSET
    compression_level: CompressionLevel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_uuid = str(self.node_uuid)

        allocation_uuids = []
        for allocation_uuids_item_data in self.allocation_uuids:
            allocation_uuids_item = str(allocation_uuids_item_data)
            allocation_uuids.append(allocation_uuids_item)

        backups = []
        for backups_item_data in self.backups:
            backups_item = str(backups_item_data)
            backups.append(backups_item)

        delete_source_backups = self.delete_source_backups

        archive_format = self.archive_format.value

        multiplex_channels = self.multiplex_channels

        allocation_uuid: None | str | Unset
        if isinstance(self.allocation_uuid, Unset):
            allocation_uuid = UNSET
        elif isinstance(self.allocation_uuid, UUID):
            allocation_uuid = str(self.allocation_uuid)
        else:
            allocation_uuid = self.allocation_uuid

        compression_level: None | str | Unset
        if isinstance(self.compression_level, Unset):
            compression_level = UNSET
        elif isinstance(self.compression_level, CompressionLevel):
            compression_level = self.compression_level.value
        else:
            compression_level = self.compression_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_uuid": node_uuid,
                "allocation_uuids": allocation_uuids,
                "backups": backups,
                "delete_source_backups": delete_source_backups,
                "archive_format": archive_format,
                "multiplex_channels": multiplex_channels,
            }
        )
        if allocation_uuid is not UNSET:
            field_dict["allocation_uuid"] = allocation_uuid
        if compression_level is not UNSET:
            field_dict["compression_level"] = compression_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_uuid = UUID(d.pop("node_uuid"))

        allocation_uuids = []
        _allocation_uuids = d.pop("allocation_uuids")
        for allocation_uuids_item_data in _allocation_uuids:
            allocation_uuids_item = UUID(allocation_uuids_item_data)

            allocation_uuids.append(allocation_uuids_item)

        backups = []
        _backups = d.pop("backups")
        for backups_item_data in _backups:
            backups_item = UUID(backups_item_data)

            backups.append(backups_item)

        delete_source_backups = d.pop("delete_source_backups")

        archive_format = TransferArchiveFormat(d.pop("archive_format"))

        multiplex_channels = d.pop("multiplex_channels")

        def _parse_allocation_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                allocation_uuid_type_0 = UUID(data)

                return allocation_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        allocation_uuid = _parse_allocation_uuid(d.pop("allocation_uuid", UNSET))

        def _parse_compression_level(data: object) -> CompressionLevel | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compression_level_type_1 = CompressionLevel(data)

                return compression_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompressionLevel | None | Unset, data)

        compression_level = _parse_compression_level(d.pop("compression_level", UNSET))

        post_api_admin_servers_server_transfer_body = cls(
            node_uuid=node_uuid,
            allocation_uuids=allocation_uuids,
            backups=backups,
            delete_source_backups=delete_source_backups,
            archive_format=archive_format,
            multiplex_channels=multiplex_channels,
            allocation_uuid=allocation_uuid,
            compression_level=compression_level,
        )

        post_api_admin_servers_server_transfer_body.additional_properties = d
        return post_api_admin_servers_server_transfer_body

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
