from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerSchedulesScheduleTriggerBody")


@_attrs_define
class PostApiClientServersServerSchedulesScheduleTriggerBody:
    """
    Attributes:
        skip_condition (bool | Unset):
    """

    skip_condition: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip_condition = self.skip_condition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skip_condition is not UNSET:
            field_dict["skip_condition"] = skip_condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        skip_condition = d.pop("skip_condition", UNSET)

        post_api_client_servers_server_schedules_schedule_trigger_body = cls(
            skip_condition=skip_condition,
        )

        post_api_client_servers_server_schedules_schedule_trigger_body.additional_properties = d
        return post_api_client_servers_server_schedules_schedule_trigger_body

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
