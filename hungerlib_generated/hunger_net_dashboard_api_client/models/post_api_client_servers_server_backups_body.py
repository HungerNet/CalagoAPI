from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerBackupsBody")


@_attrs_define
class PostApiClientServersServerBackupsBody:
    """
    Attributes:
        ignored_files (list[str]):
        name (None | str | Unset):
        backup_group_uuid (None | Unset | UUID):
        database_instance_uuid (None | Unset | UUID):
    """

    ignored_files: list[str]
    name: None | str | Unset = UNSET
    backup_group_uuid: None | Unset | UUID = UNSET
    database_instance_uuid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignored_files = self.ignored_files

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        backup_group_uuid: None | str | Unset
        if isinstance(self.backup_group_uuid, Unset):
            backup_group_uuid = UNSET
        elif isinstance(self.backup_group_uuid, UUID):
            backup_group_uuid = str(self.backup_group_uuid)
        else:
            backup_group_uuid = self.backup_group_uuid

        database_instance_uuid: None | str | Unset
        if isinstance(self.database_instance_uuid, Unset):
            database_instance_uuid = UNSET
        elif isinstance(self.database_instance_uuid, UUID):
            database_instance_uuid = str(self.database_instance_uuid)
        else:
            database_instance_uuid = self.database_instance_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ignored_files": ignored_files,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if backup_group_uuid is not UNSET:
            field_dict["backup_group_uuid"] = backup_group_uuid
        if database_instance_uuid is not UNSET:
            field_dict["database_instance_uuid"] = database_instance_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignored_files = cast(list[str], d.pop("ignored_files"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        post_api_client_servers_server_backups_body = cls(
            ignored_files=ignored_files,
            name=name,
            backup_group_uuid=backup_group_uuid,
            database_instance_uuid=database_instance_uuid,
        )

        post_api_client_servers_server_backups_body.additional_properties = d
        return post_api_client_servers_server_backups_body

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
