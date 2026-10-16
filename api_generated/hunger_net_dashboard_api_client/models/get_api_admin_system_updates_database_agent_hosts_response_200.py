from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_updates_database_agent_hosts_response_200_outdated_database_agent_hosts import (
        GetApiAdminSystemUpdatesDatabaseAgentHostsResponse200OutdatedDatabaseAgentHosts,
    )


T = TypeVar("T", bound="GetApiAdminSystemUpdatesDatabaseAgentHostsResponse200")


@_attrs_define
class GetApiAdminSystemUpdatesDatabaseAgentHostsResponse200:
    """
    Attributes:
        outdated_database_agent_hosts (GetApiAdminSystemUpdatesDatabaseAgentHostsResponse200OutdatedDatabaseAgentHosts):
        failed_database_agent_hosts (int):
    """

    outdated_database_agent_hosts: GetApiAdminSystemUpdatesDatabaseAgentHostsResponse200OutdatedDatabaseAgentHosts
    failed_database_agent_hosts: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outdated_database_agent_hosts = self.outdated_database_agent_hosts.to_dict()

        failed_database_agent_hosts = self.failed_database_agent_hosts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outdated_database_agent_hosts": outdated_database_agent_hosts,
                "failed_database_agent_hosts": failed_database_agent_hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_updates_database_agent_hosts_response_200_outdated_database_agent_hosts import (
            GetApiAdminSystemUpdatesDatabaseAgentHostsResponse200OutdatedDatabaseAgentHosts,  # noqa: PLC0415
        )

        d = dict(src_dict)
        outdated_database_agent_hosts = (
            GetApiAdminSystemUpdatesDatabaseAgentHostsResponse200OutdatedDatabaseAgentHosts.from_dict(
                d.pop("outdated_database_agent_hosts")
            )
        )

        failed_database_agent_hosts = d.pop("failed_database_agent_hosts")

        get_api_admin_system_updates_database_agent_hosts_response_200 = cls(
            outdated_database_agent_hosts=outdated_database_agent_hosts,
            failed_database_agent_hosts=failed_database_agent_hosts,
        )

        get_api_admin_system_updates_database_agent_hosts_response_200.additional_properties = d
        return get_api_admin_system_updates_database_agent_hosts_response_200

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
