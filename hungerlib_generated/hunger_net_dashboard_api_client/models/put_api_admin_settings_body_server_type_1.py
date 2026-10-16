from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiAdminSettingsBodyServerType1")


@_attrs_define
class PutApiAdminSettingsBodyServerType1:
    """
    Attributes:
        max_file_manager_view_size (int | None | Unset):
        max_file_manager_content_search_size (int | None | Unset):
        max_file_manager_search_results (int | None | Unset):
        max_subuser_count (int | None | Unset):
        max_schedule_step_count (int | None | Unset):
        max_backup_group_count (int | None | Unset):
        max_firewall_rule_count (int | None | Unset):
        max_firewall_rule_source_count (int | None | Unset):
        max_tunnel_connection_count (int | None | Unset):
        max_tunnel_port_count (int | None | Unset):
        max_database_instance_database_count (int | None | Unset):
        max_database_instance_user_count (int | None | Unset):
        allow_overwriting_custom_docker_image (bool | None | Unset):
        allow_viewing_installation_logs (bool | None | Unset):
        allow_acknowledging_installation_failure (bool | None | Unset):
        allow_viewing_transfer_progress (bool | None | Unset):
        container_prelude (None | str | Unset):
    """

    max_file_manager_view_size: int | None | Unset = UNSET
    max_file_manager_content_search_size: int | None | Unset = UNSET
    max_file_manager_search_results: int | None | Unset = UNSET
    max_subuser_count: int | None | Unset = UNSET
    max_schedule_step_count: int | None | Unset = UNSET
    max_backup_group_count: int | None | Unset = UNSET
    max_firewall_rule_count: int | None | Unset = UNSET
    max_firewall_rule_source_count: int | None | Unset = UNSET
    max_tunnel_connection_count: int | None | Unset = UNSET
    max_tunnel_port_count: int | None | Unset = UNSET
    max_database_instance_database_count: int | None | Unset = UNSET
    max_database_instance_user_count: int | None | Unset = UNSET
    allow_overwriting_custom_docker_image: bool | None | Unset = UNSET
    allow_viewing_installation_logs: bool | None | Unset = UNSET
    allow_acknowledging_installation_failure: bool | None | Unset = UNSET
    allow_viewing_transfer_progress: bool | None | Unset = UNSET
    container_prelude: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_file_manager_view_size: int | None | Unset
        if isinstance(self.max_file_manager_view_size, Unset):
            max_file_manager_view_size = UNSET
        else:
            max_file_manager_view_size = self.max_file_manager_view_size

        max_file_manager_content_search_size: int | None | Unset
        if isinstance(self.max_file_manager_content_search_size, Unset):
            max_file_manager_content_search_size = UNSET
        else:
            max_file_manager_content_search_size = self.max_file_manager_content_search_size

        max_file_manager_search_results: int | None | Unset
        if isinstance(self.max_file_manager_search_results, Unset):
            max_file_manager_search_results = UNSET
        else:
            max_file_manager_search_results = self.max_file_manager_search_results

        max_subuser_count: int | None | Unset
        if isinstance(self.max_subuser_count, Unset):
            max_subuser_count = UNSET
        else:
            max_subuser_count = self.max_subuser_count

        max_schedule_step_count: int | None | Unset
        if isinstance(self.max_schedule_step_count, Unset):
            max_schedule_step_count = UNSET
        else:
            max_schedule_step_count = self.max_schedule_step_count

        max_backup_group_count: int | None | Unset
        if isinstance(self.max_backup_group_count, Unset):
            max_backup_group_count = UNSET
        else:
            max_backup_group_count = self.max_backup_group_count

        max_firewall_rule_count: int | None | Unset
        if isinstance(self.max_firewall_rule_count, Unset):
            max_firewall_rule_count = UNSET
        else:
            max_firewall_rule_count = self.max_firewall_rule_count

        max_firewall_rule_source_count: int | None | Unset
        if isinstance(self.max_firewall_rule_source_count, Unset):
            max_firewall_rule_source_count = UNSET
        else:
            max_firewall_rule_source_count = self.max_firewall_rule_source_count

        max_tunnel_connection_count: int | None | Unset
        if isinstance(self.max_tunnel_connection_count, Unset):
            max_tunnel_connection_count = UNSET
        else:
            max_tunnel_connection_count = self.max_tunnel_connection_count

        max_tunnel_port_count: int | None | Unset
        if isinstance(self.max_tunnel_port_count, Unset):
            max_tunnel_port_count = UNSET
        else:
            max_tunnel_port_count = self.max_tunnel_port_count

        max_database_instance_database_count: int | None | Unset
        if isinstance(self.max_database_instance_database_count, Unset):
            max_database_instance_database_count = UNSET
        else:
            max_database_instance_database_count = self.max_database_instance_database_count

        max_database_instance_user_count: int | None | Unset
        if isinstance(self.max_database_instance_user_count, Unset):
            max_database_instance_user_count = UNSET
        else:
            max_database_instance_user_count = self.max_database_instance_user_count

        allow_overwriting_custom_docker_image: bool | None | Unset
        if isinstance(self.allow_overwriting_custom_docker_image, Unset):
            allow_overwriting_custom_docker_image = UNSET
        else:
            allow_overwriting_custom_docker_image = self.allow_overwriting_custom_docker_image

        allow_viewing_installation_logs: bool | None | Unset
        if isinstance(self.allow_viewing_installation_logs, Unset):
            allow_viewing_installation_logs = UNSET
        else:
            allow_viewing_installation_logs = self.allow_viewing_installation_logs

        allow_acknowledging_installation_failure: bool | None | Unset
        if isinstance(self.allow_acknowledging_installation_failure, Unset):
            allow_acknowledging_installation_failure = UNSET
        else:
            allow_acknowledging_installation_failure = self.allow_acknowledging_installation_failure

        allow_viewing_transfer_progress: bool | None | Unset
        if isinstance(self.allow_viewing_transfer_progress, Unset):
            allow_viewing_transfer_progress = UNSET
        else:
            allow_viewing_transfer_progress = self.allow_viewing_transfer_progress

        container_prelude: None | str | Unset
        if isinstance(self.container_prelude, Unset):
            container_prelude = UNSET
        else:
            container_prelude = self.container_prelude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_file_manager_view_size is not UNSET:
            field_dict["max_file_manager_view_size"] = max_file_manager_view_size
        if max_file_manager_content_search_size is not UNSET:
            field_dict["max_file_manager_content_search_size"] = max_file_manager_content_search_size
        if max_file_manager_search_results is not UNSET:
            field_dict["max_file_manager_search_results"] = max_file_manager_search_results
        if max_subuser_count is not UNSET:
            field_dict["max_subuser_count"] = max_subuser_count
        if max_schedule_step_count is not UNSET:
            field_dict["max_schedule_step_count"] = max_schedule_step_count
        if max_backup_group_count is not UNSET:
            field_dict["max_backup_group_count"] = max_backup_group_count
        if max_firewall_rule_count is not UNSET:
            field_dict["max_firewall_rule_count"] = max_firewall_rule_count
        if max_firewall_rule_source_count is not UNSET:
            field_dict["max_firewall_rule_source_count"] = max_firewall_rule_source_count
        if max_tunnel_connection_count is not UNSET:
            field_dict["max_tunnel_connection_count"] = max_tunnel_connection_count
        if max_tunnel_port_count is not UNSET:
            field_dict["max_tunnel_port_count"] = max_tunnel_port_count
        if max_database_instance_database_count is not UNSET:
            field_dict["max_database_instance_database_count"] = max_database_instance_database_count
        if max_database_instance_user_count is not UNSET:
            field_dict["max_database_instance_user_count"] = max_database_instance_user_count
        if allow_overwriting_custom_docker_image is not UNSET:
            field_dict["allow_overwriting_custom_docker_image"] = allow_overwriting_custom_docker_image
        if allow_viewing_installation_logs is not UNSET:
            field_dict["allow_viewing_installation_logs"] = allow_viewing_installation_logs
        if allow_acknowledging_installation_failure is not UNSET:
            field_dict["allow_acknowledging_installation_failure"] = allow_acknowledging_installation_failure
        if allow_viewing_transfer_progress is not UNSET:
            field_dict["allow_viewing_transfer_progress"] = allow_viewing_transfer_progress
        if container_prelude is not UNSET:
            field_dict["container_prelude"] = container_prelude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_max_file_manager_view_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_file_manager_view_size = _parse_max_file_manager_view_size(d.pop("max_file_manager_view_size", UNSET))

        def _parse_max_file_manager_content_search_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_file_manager_content_search_size = _parse_max_file_manager_content_search_size(
            d.pop("max_file_manager_content_search_size", UNSET)
        )

        def _parse_max_file_manager_search_results(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_file_manager_search_results = _parse_max_file_manager_search_results(
            d.pop("max_file_manager_search_results", UNSET)
        )

        def _parse_max_subuser_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_subuser_count = _parse_max_subuser_count(d.pop("max_subuser_count", UNSET))

        def _parse_max_schedule_step_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_schedule_step_count = _parse_max_schedule_step_count(d.pop("max_schedule_step_count", UNSET))

        def _parse_max_backup_group_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_backup_group_count = _parse_max_backup_group_count(d.pop("max_backup_group_count", UNSET))

        def _parse_max_firewall_rule_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_firewall_rule_count = _parse_max_firewall_rule_count(d.pop("max_firewall_rule_count", UNSET))

        def _parse_max_firewall_rule_source_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_firewall_rule_source_count = _parse_max_firewall_rule_source_count(
            d.pop("max_firewall_rule_source_count", UNSET)
        )

        def _parse_max_tunnel_connection_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tunnel_connection_count = _parse_max_tunnel_connection_count(d.pop("max_tunnel_connection_count", UNSET))

        def _parse_max_tunnel_port_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tunnel_port_count = _parse_max_tunnel_port_count(d.pop("max_tunnel_port_count", UNSET))

        def _parse_max_database_instance_database_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_database_instance_database_count = _parse_max_database_instance_database_count(
            d.pop("max_database_instance_database_count", UNSET)
        )

        def _parse_max_database_instance_user_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_database_instance_user_count = _parse_max_database_instance_user_count(
            d.pop("max_database_instance_user_count", UNSET)
        )

        def _parse_allow_overwriting_custom_docker_image(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_overwriting_custom_docker_image = _parse_allow_overwriting_custom_docker_image(
            d.pop("allow_overwriting_custom_docker_image", UNSET)
        )

        def _parse_allow_viewing_installation_logs(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_viewing_installation_logs = _parse_allow_viewing_installation_logs(
            d.pop("allow_viewing_installation_logs", UNSET)
        )

        def _parse_allow_acknowledging_installation_failure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_acknowledging_installation_failure = _parse_allow_acknowledging_installation_failure(
            d.pop("allow_acknowledging_installation_failure", UNSET)
        )

        def _parse_allow_viewing_transfer_progress(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_viewing_transfer_progress = _parse_allow_viewing_transfer_progress(
            d.pop("allow_viewing_transfer_progress", UNSET)
        )

        def _parse_container_prelude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container_prelude = _parse_container_prelude(d.pop("container_prelude", UNSET))

        put_api_admin_settings_body_server_type_1 = cls(
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
            allow_viewing_installation_logs=allow_viewing_installation_logs,
            allow_acknowledging_installation_failure=allow_acknowledging_installation_failure,
            allow_viewing_transfer_progress=allow_viewing_transfer_progress,
            container_prelude=container_prelude,
        )

        put_api_admin_settings_body_server_type_1.additional_properties = d
        return put_api_admin_settings_body_server_type_1

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
