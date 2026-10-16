from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_backup_kind import ServerBackupKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiRemoteServersServerBackupsBody")


@_attrs_define
class PatchApiRemoteServersServerBackupsBody:
    """
    Attributes:
        schedule_uuid (None | Unset | UUID):
        backup_uuid (None | Unset | UUID):
        backup_name (None | str | Unset):
        backup_group_uuid (None | Unset | UUID):
        oldest (bool | Unset):
        kind (None | ServerBackupKind | Unset):
        database_instance_uuid (None | Unset | UUID):
        target_backup_group_uuid (None | Unset | UUID):
    """

    schedule_uuid: None | Unset | UUID = UNSET
    backup_uuid: None | Unset | UUID = UNSET
    backup_name: None | str | Unset = UNSET
    backup_group_uuid: None | Unset | UUID = UNSET
    oldest: bool | Unset = UNSET
    kind: None | ServerBackupKind | Unset = UNSET
    database_instance_uuid: None | Unset | UUID = UNSET
    target_backup_group_uuid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, ServerBackupKind):
            kind = self.kind.value
        else:
            kind = self.kind

        database_instance_uuid: None | str | Unset
        if isinstance(self.database_instance_uuid, Unset):
            database_instance_uuid = UNSET
        elif isinstance(self.database_instance_uuid, UUID):
            database_instance_uuid = str(self.database_instance_uuid)
        else:
            database_instance_uuid = self.database_instance_uuid

        target_backup_group_uuid: None | str | Unset
        if isinstance(self.target_backup_group_uuid, Unset):
            target_backup_group_uuid = UNSET
        elif isinstance(self.target_backup_group_uuid, UUID):
            target_backup_group_uuid = str(self.target_backup_group_uuid)
        else:
            target_backup_group_uuid = self.target_backup_group_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if kind is not UNSET:
            field_dict["kind"] = kind
        if database_instance_uuid is not UNSET:
            field_dict["database_instance_uuid"] = database_instance_uuid
        if target_backup_group_uuid is not UNSET:
            field_dict["target_backup_group_uuid"] = target_backup_group_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_kind(data: object) -> None | ServerBackupKind | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_1 = ServerBackupKind(data)

                return kind_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerBackupKind | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

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

        def _parse_target_backup_group_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_backup_group_uuid_type_0 = UUID(data)

                return target_backup_group_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        target_backup_group_uuid = _parse_target_backup_group_uuid(d.pop("target_backup_group_uuid", UNSET))

        patch_api_remote_servers_server_backups_body = cls(
            schedule_uuid=schedule_uuid,
            backup_uuid=backup_uuid,
            backup_name=backup_name,
            backup_group_uuid=backup_group_uuid,
            oldest=oldest,
            kind=kind,
            database_instance_uuid=database_instance_uuid,
            target_backup_group_uuid=target_backup_group_uuid,
        )

        patch_api_remote_servers_server_backups_body.additional_properties = d
        return patch_api_remote_servers_server_backups_body

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
