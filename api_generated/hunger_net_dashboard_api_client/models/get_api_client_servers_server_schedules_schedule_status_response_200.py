from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_status import ScheduleStatus


T = TypeVar("T", bound="GetApiClientServersServerSchedulesScheduleStatusResponse200")


@_attrs_define
class GetApiClientServersServerSchedulesScheduleStatusResponse200:
    """
    Attributes:
        status (ScheduleStatus):
    """

    status: ScheduleStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_status import ScheduleStatus  # noqa: PLC0415

        d = dict(src_dict)
        status = ScheduleStatus.from_dict(d.pop("status"))

        get_api_client_servers_server_schedules_schedule_status_response_200 = cls(
            status=status,
        )

        get_api_client_servers_server_schedules_schedule_status_response_200.additional_properties = d
        return get_api_client_servers_server_schedules_schedule_status_response_200

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
