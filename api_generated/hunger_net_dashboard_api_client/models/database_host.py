from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_type import DatabaseType

T = TypeVar("T", bound="DatabaseHost")


@_attrs_define
class DatabaseHost:
    """
    Attributes:
        uuid (UUID):
        name (str):
        maintenance_enabled (bool):
        type_ (DatabaseType):
        host (str):
        port (int):
    """

    uuid: UUID
    name: str
    maintenance_enabled: bool
    type_: DatabaseType
    host: str
    port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        maintenance_enabled = self.maintenance_enabled

        type_ = self.type_.value

        host = self.host

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "maintenance_enabled": maintenance_enabled,
                "type": type_,
                "host": host,
                "port": port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        maintenance_enabled = d.pop("maintenance_enabled")

        type_ = DatabaseType(d.pop("type"))

        host = d.pop("host")

        port = d.pop("port")

        database_host = cls(
            uuid=uuid,
            name=name,
            maintenance_enabled=maintenance_enabled,
            type_=type_,
            host=host,
            port=port,
        )

        database_host.additional_properties = d
        return database_host

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
