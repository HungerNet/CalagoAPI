from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.database_agent_host import DatabaseAgentHost


T = TypeVar("T", bound="SystemBackupPolicyDatabaseAgentHost")


@_attrs_define
class SystemBackupPolicyDatabaseAgentHost:
    """
    Attributes:
        database_agent_host (DatabaseAgentHost):
        created (datetime.datetime):
    """

    database_agent_host: DatabaseAgentHost
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_agent_host = self.database_agent_host.to_dict()

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database_agent_host": database_agent_host,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_agent_host import DatabaseAgentHost  # noqa: PLC0415

        d = dict(src_dict)
        database_agent_host = DatabaseAgentHost.from_dict(d.pop("database_agent_host"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        system_backup_policy_database_agent_host = cls(
            database_agent_host=database_agent_host,
            created=created,
        )

        system_backup_policy_database_agent_host.additional_properties = d
        return system_backup_policy_database_agent_host

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
