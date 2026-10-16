from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_type import DatabaseType

if TYPE_CHECKING:
    from ..models.admin_database_host import AdminDatabaseHost


T = TypeVar("T", bound="GetApiAdminServersServerDatabasesResponse200DatabasesAdminServerServerDatabase")


@_attrs_define
class GetApiAdminServersServerDatabasesResponse200DatabasesAdminServerServerDatabase:
    """
    Attributes:
        uuid (UUID):
        database_host (AdminDatabaseHost):
        type_ (DatabaseType):
        host (str):
        port (int):
        name (str):
        is_locked (bool):
        username (str):
        password (str):
        created (datetime.datetime):
    """

    uuid: UUID
    database_host: AdminDatabaseHost
    type_: DatabaseType
    host: str
    port: int
    name: str
    is_locked: bool
    username: str
    password: str
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        database_host = self.database_host.to_dict()

        type_ = self.type_.value

        host = self.host

        port = self.port

        name = self.name

        is_locked = self.is_locked

        username = self.username

        password = self.password

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "database_host": database_host,
                "type": type_,
                "host": host,
                "port": port,
                "name": name,
                "is_locked": is_locked,
                "username": username,
                "password": password,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_database_host import AdminDatabaseHost  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        database_host = AdminDatabaseHost.from_dict(d.pop("database_host"))

        type_ = DatabaseType(d.pop("type"))

        host = d.pop("host")

        port = d.pop("port")

        name = d.pop("name")

        is_locked = d.pop("is_locked")

        username = d.pop("username")

        password = d.pop("password")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        get_api_admin_servers_server_databases_response_200_databases_admin_server_server_database = cls(
            uuid=uuid,
            database_host=database_host,
            type_=type_,
            host=host,
            port=port,
            name=name,
            is_locked=is_locked,
            username=username,
            password=password,
            created=created,
        )

        get_api_admin_servers_server_databases_response_200_databases_admin_server_server_database.additional_properties = d
        return get_api_admin_servers_server_databases_response_200_databases_admin_server_server_database

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
