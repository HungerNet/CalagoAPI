from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminStatsGeneralResponse200Stats")


@_attrs_define
class GetApiAdminStatsGeneralResponse200Stats:
    """
    Attributes:
        users (int):
        servers (int):
        locations (int):
        nodes (int):
        nest_eggs (int):
        database_hosts (int):
        backup_configurations (int):
        roles (int):
    """

    users: int
    servers: int
    locations: int
    nodes: int
    nest_eggs: int
    database_hosts: int
    backup_configurations: int
    roles: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = self.users

        servers = self.servers

        locations = self.locations

        nodes = self.nodes

        nest_eggs = self.nest_eggs

        database_hosts = self.database_hosts

        backup_configurations = self.backup_configurations

        roles = self.roles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "servers": servers,
                "locations": locations,
                "nodes": nodes,
                "nest_eggs": nest_eggs,
                "database_hosts": database_hosts,
                "backup_configurations": backup_configurations,
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        users = d.pop("users")

        servers = d.pop("servers")

        locations = d.pop("locations")

        nodes = d.pop("nodes")

        nest_eggs = d.pop("nest_eggs")

        database_hosts = d.pop("database_hosts")

        backup_configurations = d.pop("backup_configurations")

        roles = d.pop("roles")

        get_api_admin_stats_general_response_200_stats = cls(
            users=users,
            servers=servers,
            locations=locations,
            nodes=nodes,
            nest_eggs=nest_eggs,
            database_hosts=database_hosts,
            backup_configurations=backup_configurations,
            roles=roles,
        )

        get_api_admin_stats_general_response_200_stats.additional_properties = d
        return get_api_admin_stats_general_response_200_stats

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
