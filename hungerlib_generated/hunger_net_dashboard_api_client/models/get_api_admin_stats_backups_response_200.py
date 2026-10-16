from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_stats_backups_response_200_all_time import GetApiAdminStatsBackupsResponse200AllTime
    from ..models.get_api_admin_stats_backups_response_200_month import GetApiAdminStatsBackupsResponse200Month
    from ..models.get_api_admin_stats_backups_response_200_today import GetApiAdminStatsBackupsResponse200Today
    from ..models.get_api_admin_stats_backups_response_200_week import GetApiAdminStatsBackupsResponse200Week


T = TypeVar("T", bound="GetApiAdminStatsBackupsResponse200")


@_attrs_define
class GetApiAdminStatsBackupsResponse200:
    """
    Attributes:
        all_time (GetApiAdminStatsBackupsResponse200AllTime):
        today (GetApiAdminStatsBackupsResponse200Today):
        week (GetApiAdminStatsBackupsResponse200Week):
        month (GetApiAdminStatsBackupsResponse200Month):
    """

    all_time: GetApiAdminStatsBackupsResponse200AllTime
    today: GetApiAdminStatsBackupsResponse200Today
    week: GetApiAdminStatsBackupsResponse200Week
    month: GetApiAdminStatsBackupsResponse200Month
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_time = self.all_time.to_dict()

        today = self.today.to_dict()

        week = self.week.to_dict()

        month = self.month.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "all_time": all_time,
                "today": today,
                "week": week,
                "month": month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_stats_backups_response_200_all_time import GetApiAdminStatsBackupsResponse200AllTime  # noqa: PLC0415
        from ..models.get_api_admin_stats_backups_response_200_month import GetApiAdminStatsBackupsResponse200Month  # noqa: PLC0415
        from ..models.get_api_admin_stats_backups_response_200_today import GetApiAdminStatsBackupsResponse200Today  # noqa: PLC0415
        from ..models.get_api_admin_stats_backups_response_200_week import GetApiAdminStatsBackupsResponse200Week  # noqa: PLC0415

        d = dict(src_dict)
        all_time = GetApiAdminStatsBackupsResponse200AllTime.from_dict(d.pop("all_time"))

        today = GetApiAdminStatsBackupsResponse200Today.from_dict(d.pop("today"))

        week = GetApiAdminStatsBackupsResponse200Week.from_dict(d.pop("week"))

        month = GetApiAdminStatsBackupsResponse200Month.from_dict(d.pop("month"))

        get_api_admin_stats_backups_response_200 = cls(
            all_time=all_time,
            today=today,
            week=week,
            month=month,
        )

        get_api_admin_stats_backups_response_200.additional_properties = d
        return get_api_admin_stats_backups_response_200

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
