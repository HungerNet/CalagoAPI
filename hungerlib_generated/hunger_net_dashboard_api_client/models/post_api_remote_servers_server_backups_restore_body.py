from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiRemoteServersServerBackupsRestoreBody")


@_attrs_define
class PostApiRemoteServersServerBackupsRestoreBody:
    """
    Attributes:
        truncate_directory (bool):
        schedule_uuid (None | Unset | UUID):
        backup_uuid (None | Unset | UUID):
        backup_name (None | str | Unset):
        backup_group_uuid (None | Unset | UUID):
        oldest (bool | Unset):
        restore_startup (bool | Unset):
    """

    truncate_directory: bool
    schedule_uuid: None | Unset | UUID = UNSET
    backup_uuid: None | Unset | UUID = UNSET
    backup_name: None | str | Unset = UNSET
    backup_group_uuid: None | Unset | UUID = UNSET
    oldest: bool | Unset = UNSET
    restore_startup: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        truncate_directory = self.truncate_directory

        schedule_uuid: None | str | Unset
        if isinstance(self.schedule_uuid, Unset):
            schedule_uuid = UNSET
        elif isinstance(self.schedule_uuid, UUID):
            schedule_uuid = str(self.schedule_uuid)
        else:
            schedule_uuid = self.schedule_uuid

        backup_uuid: None | str | Unset
        if isinstance(self.backup_uuid, Unset):
            backup_uuid = UNSET
        elif isinstance(self.backup_uuid, UUID):
            backup_uuid = str(self.backup_uuid)
        else:
            backup_uuid = self.backup_uuid

        backup_name: None | str | Unset
        if isinstance(self.backup_name, Unset):
            backup_name = UNSET
        else:
            backup_name = self.backup_name

        backup_group_uuid: None | str | Unset
        if isinstance(self.backup_group_uuid, Unset):
            backup_group_uuid = UNSET
        elif isinstance(self.backup_group_uuid, UUID):
            backup_group_uuid = str(self.backup_group_uuid)
        else:
            backup_group_uuid = self.backup_group_uuid

        oldest = self.oldest

        restore_startup = self.restore_startup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "truncate_directory": truncate_directory,
            }
        )
        if schedule_uuid is not UNSET:
            field_dict["schedule_uuid"] = schedule_uuid
        if backup_uuid is not UNSET:
            field_dict["backup_uuid"] = backup_uuid
        if backup_name is not UNSET:
            field_dict["backup_name"] = backup_name
        if backup_group_uuid is not UNSET:
            field_dict["backup_group_uuid"] = backup_group_uuid
        if oldest is not UNSET:
            field_dict["oldest"] = oldest
        if restore_startup is not UNSET:
            field_dict["restore_startup"] = restore_startup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        truncate_directory = d.pop("truncate_directory")

        def _parse_schedule_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                schedule_uuid_type_0 = UUID(data)

                return schedule_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        schedule_uuid = _parse_schedule_uuid(d.pop("schedule_uuid", UNSET))

        def _parse_backup_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_uuid_type_0 = UUID(data)

                return backup_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_uuid = _parse_backup_uuid(d.pop("backup_uuid", UNSET))

        def _parse_backup_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_name = _parse_backup_name(d.pop("backup_name", UNSET))

        def _parse_backup_group_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_group_uuid_type_0 = UUID(data)

                return backup_group_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_group_uuid = _parse_backup_group_uuid(d.pop("backup_group_uuid", UNSET))

        oldest = d.pop("oldest", UNSET)

        restore_startup = d.pop("restore_startup", UNSET)

        post_api_remote_servers_server_backups_restore_body = cls(
            truncate_directory=truncate_directory,
            schedule_uuid=schedule_uuid,
            backup_uuid=backup_uuid,
            backup_name=backup_name,
            backup_group_uuid=backup_group_uuid,
            oldest=oldest,
            restore_startup=restore_startup,
        )

        post_api_remote_servers_server_backups_restore_body.additional_properties = d
        return post_api_remote_servers_server_backups_restore_body

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
