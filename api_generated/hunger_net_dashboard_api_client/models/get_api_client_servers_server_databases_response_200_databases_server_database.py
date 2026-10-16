from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_type import DatabaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiClientServersServerDatabasesResponse200DatabasesServerDatabase")


@_attrs_define
class GetApiClientServersServerDatabasesResponse200DatabasesServerDatabase:
    """
    Attributes:
        uuid (UUID):
        type_ (DatabaseType):
        host (str):
        port (int):
        name (str):
        is_locked (bool):
        username (str):
        created (datetime.datetime):
        password (None | str | Unset):
    """

    uuid: UUID
    type_: DatabaseType
    host: str
    port: int
    name: str
    is_locked: bool
    username: str
    created: datetime.datetime
    password: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        type_ = self.type_.value

        host = self.host

        port = self.port

        name = self.name

        is_locked = self.is_locked

        username = self.username

        created = self.created.isoformat()

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "type": type_,
                "host": host,
                "port": port,
                "name": name,
                "is_locked": is_locked,
                "username": username,
                "created": created,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        type_ = DatabaseType(d.pop("type"))

        host = d.pop("host")

        port = d.pop("port")

        name = d.pop("name")

        is_locked = d.pop("is_locked")

        username = d.pop("username")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        get_api_client_servers_server_databases_response_200_databases_server_database = cls(
            uuid=uuid,
            type_=type_,
            host=host,
            port=port,
            name=name,
            is_locked=is_locked,
            username=username,
            created=created,
            password=password,
        )

        get_api_client_servers_server_databases_response_200_databases_server_database.additional_properties = d
        return get_api_client_servers_server_databases_response_200_databases_server_database

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
