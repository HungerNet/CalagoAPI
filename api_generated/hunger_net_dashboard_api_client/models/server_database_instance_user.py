from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_database_instance_user_database import ServerDatabaseInstanceUserDatabase


T = TypeVar("T", bound="ServerDatabaseInstanceUser")


@_attrs_define
class ServerDatabaseInstanceUser:
    """
    Attributes:
        uuid (UUID):
        username (str):
        password (str):
        databases (list[ServerDatabaseInstanceUserDatabase]):
    """

    uuid: UUID
    username: str
    password: str
    databases: list[ServerDatabaseInstanceUserDatabase]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        username = self.username

        password = self.password

        databases = []
        for databases_item_data in self.databases:
            databases_item = databases_item_data.to_dict()
            databases.append(databases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "username": username,
                "password": password,
                "databases": databases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_database_instance_user_database import ServerDatabaseInstanceUserDatabase  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        username = d.pop("username")

        password = d.pop("password")

        databases = []
        _databases = d.pop("databases")
        for databases_item_data in _databases:
            databases_item = ServerDatabaseInstanceUserDatabase.from_dict(databases_item_data)

            databases.append(databases_item)

        server_database_instance_user = cls(
            uuid=uuid,
            username=username,
            password=password,
            databases=databases,
        )

        server_database_instance_user.additional_properties = d
        return server_database_instance_user

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
