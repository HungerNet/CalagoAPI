from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_database_instance_user_database import ServerDatabaseInstanceUserDatabase


T = TypeVar(
    "T", bound="PutApiClientServersServerDatabasesInstancesDatabaseInstanceUsersUserDatabasesDatabaseResponse200"
)


@_attrs_define
class PutApiClientServersServerDatabasesInstancesDatabaseInstanceUsersUserDatabasesDatabaseResponse200:
    """
    Attributes:
        database (None | ServerDatabaseInstanceUserDatabase | Unset):
    """

    database: None | ServerDatabaseInstanceUserDatabase | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_database_instance_user_database import ServerDatabaseInstanceUserDatabase  # noqa: PLC0415

        database: dict[str, Any] | None | Unset
        if isinstance(self.database, Unset):
            database = UNSET
        elif isinstance(self.database, ServerDatabaseInstanceUserDatabase):
            database = self.database.to_dict()
        else:
            database = self.database

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database is not UNSET:
            field_dict["database"] = database

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_database_instance_user_database import ServerDatabaseInstanceUserDatabase  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_database(data: object) -> None | ServerDatabaseInstanceUserDatabase | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                database_type_1 = ServerDatabaseInstanceUserDatabase.from_dict(data)

                return database_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerDatabaseInstanceUserDatabase | Unset, data)

        database = _parse_database(d.pop("database", UNSET))

        put_api_client_servers_server_databases_instances_database_instance_users_user_databases_database_response_200 = cls(
            database=database,
        )

        put_api_client_servers_server_databases_instances_database_instance_users_user_databases_database_response_200.additional_properties = d
        return put_api_client_servers_server_databases_instances_database_instance_users_user_databases_database_response_200

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
