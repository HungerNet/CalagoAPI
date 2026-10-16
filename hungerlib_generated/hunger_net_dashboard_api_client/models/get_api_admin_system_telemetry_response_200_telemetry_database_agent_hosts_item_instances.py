from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemInstances")


@_attrs_define
class GetApiAdminSystemTelemetryResponse200TelemetryDatabaseAgentHostsItemInstances:
    """
    Attributes:
        total (int):
        online (int):
        offline (int):
    """

    total: int
    online: int
    offline: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        online = self.online

        offline = self.offline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "online": online,
                "offline": offline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        online = d.pop("online")

        offline = d.pop("offline")

        get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item_instances = cls(
            total=total,
            online=online,
            offline=offline,
        )

        get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item_instances.additional_properties = d
        return get_api_admin_system_telemetry_response_200_telemetry_database_agent_hosts_item_instances

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
