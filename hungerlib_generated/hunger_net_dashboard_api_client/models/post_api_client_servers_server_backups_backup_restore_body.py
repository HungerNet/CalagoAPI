from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerBackupsBackupRestoreBody")


@_attrs_define
class PostApiClientServersServerBackupsBackupRestoreBody:
    """
    Attributes:
        truncate_directory (bool | Unset):
        restore_startup (bool | Unset):
        database_instance_uuid (None | Unset | UUID):
    """

    truncate_directory: bool | Unset = UNSET
    restore_startup: bool | Unset = UNSET
    database_instance_uuid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        truncate_directory = self.truncate_directory

        restore_startup = self.restore_startup

        database_instance_uuid: None | str | Unset
        if isinstance(self.database_instance_uuid, Unset):
            database_instance_uuid = UNSET
        elif isinstance(self.database_instance_uuid, UUID):
            database_instance_uuid = str(self.database_instance_uuid)
        else:
            database_instance_uuid = self.database_instance_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if truncate_directory is not UNSET:
            field_dict["truncate_directory"] = truncate_directory
        if restore_startup is not UNSET:
            field_dict["restore_startup"] = restore_startup
        if database_instance_uuid is not UNSET:
            field_dict["database_instance_uuid"] = database_instance_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        truncate_directory = d.pop("truncate_directory", UNSET)

        restore_startup = d.pop("restore_startup", UNSET)

        def _parse_database_instance_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                database_instance_uuid_type_0 = UUID(data)

                return database_instance_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        database_instance_uuid = _parse_database_instance_uuid(d.pop("database_instance_uuid", UNSET))

        post_api_client_servers_server_backups_backup_restore_body = cls(
            truncate_directory=truncate_directory,
            restore_startup=restore_startup,
            database_instance_uuid=database_instance_uuid,
        )

        post_api_client_servers_server_backups_backup_restore_body.additional_properties = d
        return post_api_client_servers_server_backups_backup_restore_body

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
