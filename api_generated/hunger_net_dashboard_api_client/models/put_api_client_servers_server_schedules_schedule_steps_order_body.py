from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutApiClientServersServerSchedulesScheduleStepsOrderBody")


@_attrs_define
class PutApiClientServersServerSchedulesScheduleStepsOrderBody:
    """
    Attributes:
        schedule_step_order (list[UUID]):
    """

    schedule_step_order: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_step_order = []
        for schedule_step_order_item_data in self.schedule_step_order:
            schedule_step_order_item = str(schedule_step_order_item_data)
            schedule_step_order.append(schedule_step_order_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_step_order": schedule_step_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_step_order = []
        _schedule_step_order = d.pop("schedule_step_order")
        for schedule_step_order_item_data in _schedule_step_order:
            schedule_step_order_item = UUID(schedule_step_order_item_data)

            schedule_step_order.append(schedule_step_order_item)

        put_api_client_servers_server_schedules_schedule_steps_order_body = cls(
            schedule_step_order=schedule_step_order,
        )

        put_api_client_servers_server_schedules_schedule_steps_order_body.additional_properties = d
        return put_api_client_servers_server_schedules_schedule_steps_order_body

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
