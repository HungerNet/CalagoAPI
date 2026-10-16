from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiSettingsResponse200Server")


@_attrs_define
class GetApiSettingsResponse200Server:
    """
    Attributes:
        max_file_manager_view_size (int):
        max_file_manager_content_search_size (int):
        max_file_manager_search_results (int):
        max_subuser_count (int):
        max_schedule_step_count (int):
        max_backup_group_count (int):
        max_firewall_rule_count (int):
        max_firewall_rule_source_count (int):
        max_tunnel_connection_count (int):
        max_tunnel_port_count (int):
        max_database_instance_database_count (int):
        max_database_instance_user_count (int):
        allow_overwriting_custom_docker_image (bool):
        allow_acknowledging_installation_failure (bool):
        container_prelude (str):
    """

    max_file_manager_view_size: int
    max_file_manager_content_search_size: int
    max_file_manager_search_results: int
    max_subuser_count: int
    max_schedule_step_count: int
    max_backup_group_count: int
    max_firewall_rule_count: int
    max_firewall_rule_source_count: int
    max_tunnel_connection_count: int
    max_tunnel_port_count: int
    max_database_instance_database_count: int
    max_database_instance_user_count: int
    allow_overwriting_custom_docker_image: bool
    allow_acknowledging_installation_failure: bool
    container_prelude: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_file_manager_view_size = self.max_file_manager_view_size

        max_file_manager_content_search_size = self.max_file_manager_content_search_size

        max_file_manager_search_results = self.max_file_manager_search_results

        max_subuser_count = self.max_subuser_count

        max_schedule_step_count = self.max_schedule_step_count

        max_backup_group_count = self.max_backup_group_count

        max_firewall_rule_count = self.max_firewall_rule_count

        max_firewall_rule_source_count = self.max_firewall_rule_source_count

        max_tunnel_connection_count = self.max_tunnel_connection_count

        max_tunnel_port_count = self.max_tunnel_port_count

        max_database_instance_database_count = self.max_database_instance_database_count

        max_database_instance_user_count = self.max_database_instance_user_count

        allow_overwriting_custom_docker_image = self.allow_overwriting_custom_docker_image

        allow_acknowledging_installation_failure = self.allow_acknowledging_installation_failure

        container_prelude = self.container_prelude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_file_manager_view_size": max_file_manager_view_size,
                "max_file_manager_content_search_size": max_file_manager_content_search_size,
                "max_file_manager_search_results": max_file_manager_search_results,
                "max_subuser_count": max_subuser_count,
                "max_schedule_step_count": max_schedule_step_count,
                "max_backup_group_count": max_backup_group_count,
                "max_firewall_rule_count": max_firewall_rule_count,
                "max_firewall_rule_source_count": max_firewall_rule_source_count,
                "max_tunnel_connection_count": max_tunnel_connection_count,
                "max_tunnel_port_count": max_tunnel_port_count,
                "max_database_instance_database_count": max_database_instance_database_count,
                "max_database_instance_user_count": max_database_instance_user_count,
                "allow_overwriting_custom_docker_image": allow_overwriting_custom_docker_image,
                "allow_acknowledging_installation_failure": allow_acknowledging_installation_failure,
                "container_prelude": container_prelude,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_file_manager_view_size = d.pop("max_file_manager_view_size")

        max_file_manager_content_search_size = d.pop("max_file_manager_content_search_size")

        max_file_manager_search_results = d.pop("max_file_manager_search_results")

        max_subuser_count = d.pop("max_subuser_count")

        max_schedule_step_count = d.pop("max_schedule_step_count")

        max_backup_group_count = d.pop("max_backup_group_count")

        max_firewall_rule_count = d.pop("max_firewall_rule_count")

        max_firewall_rule_source_count = d.pop("max_firewall_rule_source_count")

        max_tunnel_connection_count = d.pop("max_tunnel_connection_count")

        max_tunnel_port_count = d.pop("max_tunnel_port_count")

        max_database_instance_database_count = d.pop("max_database_instance_database_count")

        max_database_instance_user_count = d.pop("max_database_instance_user_count")

        allow_overwriting_custom_docker_image = d.pop("allow_overwriting_custom_docker_image")

        allow_acknowledging_installation_failure = d.pop("allow_acknowledging_installation_failure")

        container_prelude = d.pop("container_prelude")

        get_api_settings_response_200_server = cls(
            max_file_manager_view_size=max_file_manager_view_size,
            max_file_manager_content_search_size=max_file_manager_content_search_size,
            max_file_manager_search_results=max_file_manager_search_results,
            max_subuser_count=max_subuser_count,
            max_schedule_step_count=max_schedule_step_count,
            max_backup_group_count=max_backup_group_count,
            max_firewall_rule_count=max_firewall_rule_count,
            max_firewall_rule_source_count=max_firewall_rule_source_count,
            max_tunnel_connection_count=max_tunnel_connection_count,
            max_tunnel_port_count=max_tunnel_port_count,
            max_database_instance_database_count=max_database_instance_database_count,
            max_database_instance_user_count=max_database_instance_user_count,
            allow_overwriting_custom_docker_image=allow_overwriting_custom_docker_image,
            allow_acknowledging_installation_failure=allow_acknowledging_installation_failure,
            container_prelude=container_prelude,
        )

        get_api_settings_response_200_server.additional_properties = d
        return get_api_settings_response_200_server

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
