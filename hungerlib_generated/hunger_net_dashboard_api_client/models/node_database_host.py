from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_database_host import AdminDatabaseHost


T = TypeVar("T", bound="NodeDatabaseHost")


@_attrs_define
class NodeDatabaseHost:
    """
    Attributes:
        database_host (AdminDatabaseHost):
        created (datetime.datetime):
    """

    database_host: AdminDatabaseHost
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_host = self.database_host.to_dict()

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database_host": database_host,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_database_host import AdminDatabaseHost  # noqa: PLC0415

        d = dict(src_dict)
        database_host = AdminDatabaseHost.from_dict(d.pop("database_host"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        node_database_host = cls(
            database_host=database_host,
            created=created,
        )

        node_database_host.additional_properties = d
        return node_database_host

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
