from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiRemoteBackupsBackupDatabaseRestoreBody")


@_attrs_define
class PostApiRemoteBackupsBackupDatabaseRestoreBody:
    """
    Attributes:
        successful (bool):
        database_instance (None | Unset | UUID):
    """

    successful: bool
    database_instance: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        successful = self.successful

        database_instance: None | str | Unset
        if isinstance(self.database_instance, Unset):
            database_instance = UNSET
        elif isinstance(self.database_instance, UUID):
            database_instance = str(self.database_instance)
        else:
            database_instance = self.database_instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "successful": successful,
            }
        )
        if database_instance is not UNSET:
            field_dict["database_instance"] = database_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        successful = d.pop("successful")

        def _parse_database_instance(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                database_instance_type_0 = UUID(data)

                return database_instance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        database_instance = _parse_database_instance(d.pop("database_instance", UNSET))

        post_api_remote_backups_backup_database_restore_body = cls(
            successful=successful,
            database_instance=database_instance,
        )

        post_api_remote_backups_backup_database_restore_body.additional_properties = d
        return post_api_remote_backups_backup_database_restore_body

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
