from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compression_level import CompressionLevel
from ..models.mass_transfer_allocation_mode import MassTransferAllocationMode
from ..models.transfer_archive_format import TransferArchiveFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_selector_type_0 import ServerSelectorType0
    from ..models.server_selector_type_1 import ServerSelectorType1


T = TypeVar("T", bound="PostApiAdminNodesNodeServersTransferBody")


@_attrs_define
class PostApiAdminNodesNodeServersTransferBody:
    """
    Attributes:
        servers (ServerSelectorType0 | ServerSelectorType1):
        node_uuid (UUID):
        allocation_mode (MassTransferAllocationMode):
        transfer_backups (bool):
        delete_source_backups (bool):
        archive_format (TransferArchiveFormat):
        multiplex_channels (int):
        compression_level (CompressionLevel | None | Unset):
    """

    servers: ServerSelectorType0 | ServerSelectorType1
    node_uuid: UUID
    allocation_mode: MassTransferAllocationMode
    transfer_backups: bool
    delete_source_backups: bool
    archive_format: TransferArchiveFormat
    multiplex_channels: int
    compression_level: CompressionLevel | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_selector_type_0 import ServerSelectorType0  # noqa: PLC0415

        servers: dict[str, Any]
        if isinstance(self.servers, ServerSelectorType0):
            servers = self.servers.to_dict()
        else:
            servers = self.servers.to_dict()

        node_uuid = str(self.node_uuid)

        allocation_mode = self.allocation_mode.value

        transfer_backups = self.transfer_backups

        delete_source_backups = self.delete_source_backups

        archive_format = self.archive_format.value

        multiplex_channels = self.multiplex_channels

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
                "servers": servers,
                "node_uuid": node_uuid,
                "allocation_mode": allocation_mode,
                "transfer_backups": transfer_backups,
                "delete_source_backups": delete_source_backups,
                "archive_format": archive_format,
                "multiplex_channels": multiplex_channels,
            }
        )
        if compression_level is not UNSET:
            field_dict["compression_level"] = compression_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_selector_type_0 import ServerSelectorType0  # noqa: PLC0415
        from ..models.server_selector_type_1 import ServerSelectorType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_servers(data: object) -> ServerSelectorType0 | ServerSelectorType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_server_selector_type_0 = ServerSelectorType0.from_dict(data)

                return componentsschemas_server_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_server_selector_type_1 = ServerSelectorType1.from_dict(data)

            return componentsschemas_server_selector_type_1

        servers = _parse_servers(d.pop("servers"))

        node_uuid = UUID(d.pop("node_uuid"))

        allocation_mode = MassTransferAllocationMode(d.pop("allocation_mode"))

        transfer_backups = d.pop("transfer_backups")

        delete_source_backups = d.pop("delete_source_backups")

        archive_format = TransferArchiveFormat(d.pop("archive_format"))

        multiplex_channels = d.pop("multiplex_channels")

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

        post_api_admin_nodes_node_servers_transfer_body = cls(
            servers=servers,
            node_uuid=node_uuid,
            allocation_mode=allocation_mode,
            transfer_backups=transfer_backups,
            delete_source_backups=delete_source_backups,
            archive_format=archive_format,
            multiplex_channels=multiplex_channels,
            compression_level=compression_level,
        )

        post_api_admin_nodes_node_servers_transfer_body.additional_properties = d
        return post_api_admin_nodes_node_servers_transfer_body

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
