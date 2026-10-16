from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsNetwork")


@_attrs_define
class GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemStatsResponse200StatsNetwork:
    """
    Attributes:
        received (int):
        received_packets (int):
        receiving_rate (float):
        received_packets_rate (float):
        sent (int):
        sent_packets (int):
        sending_rate (float):
        sending_packets_rate (float):
    """

    received: int
    received_packets: int
    receiving_rate: float
    received_packets_rate: float
    sent: int
    sent_packets: int
    sending_rate: float
    sending_packets_rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        received = self.received

        received_packets = self.received_packets

        receiving_rate = self.receiving_rate

        received_packets_rate = self.received_packets_rate

        sent = self.sent

        sent_packets = self.sent_packets

        sending_rate = self.sending_rate

        sending_packets_rate = self.sending_packets_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "received": received,
                "received_packets": received_packets,
                "receiving_rate": receiving_rate,
                "received_packets_rate": received_packets_rate,
                "sent": sent,
                "sent_packets": sent_packets,
                "sending_rate": sending_rate,
                "sending_packets_rate": sending_packets_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        received = d.pop("received")

        received_packets = d.pop("received_packets")

        receiving_rate = d.pop("receiving_rate")

        received_packets_rate = d.pop("received_packets_rate")

        sent = d.pop("sent")

        sent_packets = d.pop("sent_packets")

        sending_rate = d.pop("sending_rate")

        sending_packets_rate = d.pop("sending_packets_rate")

        get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_network = cls(
            received=received,
            received_packets=received_packets,
            receiving_rate=receiving_rate,
            received_packets_rate=received_packets_rate,
            sent=sent,
            sent_packets=sent_packets,
            sending_rate=sending_rate,
            sending_packets_rate=sending_packets_rate,
        )

        get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_network.additional_properties = d
        return get_api_admin_database_agent_hosts_database_agent_host_system_stats_response_200_stats_network

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
