from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiRemoteBackupsBackupRestoreBody")


@_attrs_define
class PostApiRemoteBackupsBackupRestoreBody:
    """
    Attributes:
        successful (bool):
        server_uuid (None | Unset | UUID):
    """

    successful: bool
    server_uuid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        successful = self.successful

        server_uuid: None | str | Unset
        if isinstance(self.server_uuid, Unset):
            server_uuid = UNSET
        elif isinstance(self.server_uuid, UUID):
            server_uuid = str(self.server_uuid)
        else:
            server_uuid = self.server_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "successful": successful,
            }
        )
        if server_uuid is not UNSET:
            field_dict["server_uuid"] = server_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        successful = d.pop("successful")

        def _parse_server_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                server_uuid_type_0 = UUID(data)

                return server_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        server_uuid = _parse_server_uuid(d.pop("server_uuid", UNSET))

        post_api_remote_backups_backup_restore_body = cls(
            successful=successful,
            server_uuid=server_uuid,
        )

        post_api_remote_backups_backup_restore_body.additional_properties = d
        return post_api_remote_backups_backup_restore_body

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
