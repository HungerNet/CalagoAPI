from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiAdminDatabaseAgentHostsConfigBody")


@_attrs_define
class PatchApiAdminDatabaseAgentHostsConfigBody:
    """
    Attributes:
        database_agent_host_uuids (list[UUID]):
        config (Any):
    """

    database_agent_host_uuids: list[UUID]
    config: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_agent_host_uuids = []
        for database_agent_host_uuids_item_data in self.database_agent_host_uuids:
            database_agent_host_uuids_item = str(database_agent_host_uuids_item_data)
            database_agent_host_uuids.append(database_agent_host_uuids_item)

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database_agent_host_uuids": database_agent_host_uuids,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database_agent_host_uuids = []
        _database_agent_host_uuids = d.pop("database_agent_host_uuids")
        for database_agent_host_uuids_item_data in _database_agent_host_uuids:
            database_agent_host_uuids_item = UUID(database_agent_host_uuids_item_data)

            database_agent_host_uuids.append(database_agent_host_uuids_item)

        config = d.pop("config")

        patch_api_admin_database_agent_hosts_config_body = cls(
            database_agent_host_uuids=database_agent_host_uuids,
            config=config,
        )

        patch_api_admin_database_agent_hosts_config_body.additional_properties = d
        return patch_api_admin_database_agent_hosts_config_body

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
