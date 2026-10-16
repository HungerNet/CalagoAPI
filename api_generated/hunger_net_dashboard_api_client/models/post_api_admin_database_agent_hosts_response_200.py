from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.database_agent_host import DatabaseAgentHost


T = TypeVar("T", bound="PostApiAdminDatabaseAgentHostsResponse200")


@_attrs_define
class PostApiAdminDatabaseAgentHostsResponse200:
    """
    Attributes:
        database_agent_host (DatabaseAgentHost):
    """

    database_agent_host: DatabaseAgentHost
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_agent_host = self.database_agent_host.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database_agent_host": database_agent_host,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_agent_host import DatabaseAgentHost  # noqa: PLC0415

        d = dict(src_dict)
        database_agent_host = DatabaseAgentHost.from_dict(d.pop("database_agent_host"))

        post_api_admin_database_agent_hosts_response_200 = cls(
            database_agent_host=database_agent_host,
        )

        post_api_admin_database_agent_hosts_response_200.additional_properties = d
        return post_api_admin_database_agent_hosts_response_200

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
