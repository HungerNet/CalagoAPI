from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_remote_servers_server_transfer_success_body_backup_migrations import (
        PostApiRemoteServersServerTransferSuccessBodyBackupMigrations,
    )


T = TypeVar("T", bound="PostApiRemoteServersServerTransferSuccessBody")


@_attrs_define
class PostApiRemoteServersServerTransferSuccessBody:
    """
    Attributes:
        backups (list[UUID]):
        backup_migrations (PostApiRemoteServersServerTransferSuccessBodyBackupMigrations | Unset):
    """

    backups: list[UUID]
    backup_migrations: PostApiRemoteServersServerTransferSuccessBodyBackupMigrations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backups = []
        for backups_item_data in self.backups:
            backups_item = str(backups_item_data)
            backups.append(backups_item)

        backup_migrations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_migrations, Unset):
            backup_migrations = self.backup_migrations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backups": backups,
            }
        )
        if backup_migrations is not UNSET:
            field_dict["backup_migrations"] = backup_migrations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_remote_servers_server_transfer_success_body_backup_migrations import (
            PostApiRemoteServersServerTransferSuccessBodyBackupMigrations,  # noqa: PLC0415
        )

        d = dict(src_dict)
        backups = []
        _backups = d.pop("backups")
        for backups_item_data in _backups:
            backups_item = UUID(backups_item_data)

            backups.append(backups_item)

        _backup_migrations = d.pop("backup_migrations", UNSET)
        backup_migrations: PostApiRemoteServersServerTransferSuccessBodyBackupMigrations | Unset
        if isinstance(_backup_migrations, Unset):
            backup_migrations = UNSET
        else:
            backup_migrations = PostApiRemoteServersServerTransferSuccessBodyBackupMigrations.from_dict(
                _backup_migrations
            )

        post_api_remote_servers_server_transfer_success_body = cls(
            backups=backups,
            backup_migrations=backup_migrations,
        )

        post_api_remote_servers_server_transfer_success_body.additional_properties = d
        return post_api_remote_servers_server_transfer_success_body

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
