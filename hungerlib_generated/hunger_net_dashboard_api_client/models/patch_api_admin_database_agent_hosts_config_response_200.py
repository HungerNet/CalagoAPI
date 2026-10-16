from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiAdminDatabaseAgentHostsConfigResponse200")


@_attrs_define
class PatchApiAdminDatabaseAgentHostsConfigResponse200:
    """
    Attributes:
        applied (int):
        ignored_paths (list[str]):
    """

    applied: int
    ignored_paths: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        ignored_paths = self.ignored_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "ignored_paths": ignored_paths,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied = d.pop("applied")

        ignored_paths = cast(list[str], d.pop("ignored_paths"))

        patch_api_admin_database_agent_hosts_config_response_200 = cls(
            applied=applied,
            ignored_paths=ignored_paths,
        )

        patch_api_admin_database_agent_hosts_config_response_200.additional_properties = d
        return patch_api_admin_database_agent_hosts_config_response_200

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
