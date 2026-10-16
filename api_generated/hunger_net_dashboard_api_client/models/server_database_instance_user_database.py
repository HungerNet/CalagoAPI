from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_permission import DatabasePermission

T = TypeVar("T", bound="ServerDatabaseInstanceUserDatabase")


@_attrs_define
class ServerDatabaseInstanceUserDatabase:
    """
    Attributes:
        database_uuid (UUID):
        permission (DatabasePermission):
        created (datetime.datetime):
    """

    database_uuid: UUID
    permission: DatabasePermission
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_uuid = str(self.database_uuid)

        permission = self.permission.value

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database_uuid": database_uuid,
                "permission": permission,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database_uuid = UUID(d.pop("database_uuid"))

        permission = DatabasePermission(d.pop("permission"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        server_database_instance_user_database = cls(
            database_uuid=database_uuid,
            permission=permission,
            created=created,
        )

        server_database_instance_user_database.additional_properties = d
        return server_database_instance_user_database

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
