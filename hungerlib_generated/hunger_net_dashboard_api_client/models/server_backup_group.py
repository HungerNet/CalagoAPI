from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.backup_retention import BackupRetention


T = TypeVar("T", bound="ServerBackupGroup")


@_attrs_define
class ServerBackupGroup:
    """
    Attributes:
        uuid (UUID):
        name (str):
        order (int):
        retention (BackupRetention):
        total_backups (int):
        usable_backups (int):
        usable_unlocked_backups (int):
        created (datetime.datetime):
    """

    uuid: UUID
    name: str
    order: int
    retention: BackupRetention
    total_backups: int
    usable_backups: int
    usable_unlocked_backups: int
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        order = self.order

        retention = self.retention.to_dict()

        total_backups = self.total_backups

        usable_backups = self.usable_backups

        usable_unlocked_backups = self.usable_unlocked_backups

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "order": order,
                "retention": retention,
                "total_backups": total_backups,
                "usable_backups": usable_backups,
                "usable_unlocked_backups": usable_unlocked_backups,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_retention import BackupRetention  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        order = d.pop("order")

        retention = BackupRetention.from_dict(d.pop("retention"))

        total_backups = d.pop("total_backups")

        usable_backups = d.pop("usable_backups")

        usable_unlocked_backups = d.pop("usable_unlocked_backups")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        server_backup_group = cls(
            uuid=uuid,
            name=name,
            order=order,
            retention=retention,
            total_backups=total_backups,
            usable_backups=usable_backups,
            usable_unlocked_backups=usable_unlocked_backups,
            created=created,
        )

        server_backup_group.additional_properties = d
        return server_backup_group

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
