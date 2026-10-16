from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_ip_hiding import ActivityIpHiding
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiAdminSettingsBodyActivityType1")


@_attrs_define
class PutApiAdminSettingsBodyActivityType1:
    """
    Attributes:
        admin_log_retention_days (int | None | Unset):
        admin_log_retention_count (int | None | Unset):
        user_log_retention_days (int | None | Unset):
        user_log_retention_count (int | None | Unset):
        server_log_retention_days (int | None | Unset):
        server_log_retention_count (int | None | Unset):
        server_log_admin_activity (bool | None | Unset):
        server_log_schedule_activity (bool | None | Unset):
        server_hide_activity_ips (ActivityIpHiding | None | Unset):
    """

    admin_log_retention_days: int | None | Unset = UNSET
    admin_log_retention_count: int | None | Unset = UNSET
    user_log_retention_days: int | None | Unset = UNSET
    user_log_retention_count: int | None | Unset = UNSET
    server_log_retention_days: int | None | Unset = UNSET
    server_log_retention_count: int | None | Unset = UNSET
    server_log_admin_activity: bool | None | Unset = UNSET
    server_log_schedule_activity: bool | None | Unset = UNSET
    server_hide_activity_ips: ActivityIpHiding | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_log_retention_days: int | None | Unset
        if isinstance(self.admin_log_retention_days, Unset):
            admin_log_retention_days = UNSET
        else:
            admin_log_retention_days = self.admin_log_retention_days

        admin_log_retention_count: int | None | Unset
        if isinstance(self.admin_log_retention_count, Unset):
            admin_log_retention_count = UNSET
        else:
            admin_log_retention_count = self.admin_log_retention_count

        user_log_retention_days: int | None | Unset
        if isinstance(self.user_log_retention_days, Unset):
            user_log_retention_days = UNSET
        else:
            user_log_retention_days = self.user_log_retention_days

        user_log_retention_count: int | None | Unset
        if isinstance(self.user_log_retention_count, Unset):
            user_log_retention_count = UNSET
        else:
            user_log_retention_count = self.user_log_retention_count

        server_log_retention_days: int | None | Unset
        if isinstance(self.server_log_retention_days, Unset):
            server_log_retention_days = UNSET
        else:
            server_log_retention_days = self.server_log_retention_days

        server_log_retention_count: int | None | Unset
        if isinstance(self.server_log_retention_count, Unset):
            server_log_retention_count = UNSET
        else:
            server_log_retention_count = self.server_log_retention_count

        server_log_admin_activity: bool | None | Unset
        if isinstance(self.server_log_admin_activity, Unset):
            server_log_admin_activity = UNSET
        else:
            server_log_admin_activity = self.server_log_admin_activity

        server_log_schedule_activity: bool | None | Unset
        if isinstance(self.server_log_schedule_activity, Unset):
            server_log_schedule_activity = UNSET
        else:
            server_log_schedule_activity = self.server_log_schedule_activity

        server_hide_activity_ips: None | str | Unset
        if isinstance(self.server_hide_activity_ips, Unset):
            server_hide_activity_ips = UNSET
        elif isinstance(self.server_hide_activity_ips, ActivityIpHiding):
            server_hide_activity_ips = self.server_hide_activity_ips.value
        else:
            server_hide_activity_ips = self.server_hide_activity_ips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_log_retention_days is not UNSET:
            field_dict["admin_log_retention_days"] = admin_log_retention_days
        if admin_log_retention_count is not UNSET:
            field_dict["admin_log_retention_count"] = admin_log_retention_count
        if user_log_retention_days is not UNSET:
            field_dict["user_log_retention_days"] = user_log_retention_days
        if user_log_retention_count is not UNSET:
            field_dict["user_log_retention_count"] = user_log_retention_count
        if server_log_retention_days is not UNSET:
            field_dict["server_log_retention_days"] = server_log_retention_days
        if server_log_retention_count is not UNSET:
            field_dict["server_log_retention_count"] = server_log_retention_count
        if server_log_admin_activity is not UNSET:
            field_dict["server_log_admin_activity"] = server_log_admin_activity
        if server_log_schedule_activity is not UNSET:
            field_dict["server_log_schedule_activity"] = server_log_schedule_activity
        if server_hide_activity_ips is not UNSET:
            field_dict["server_hide_activity_ips"] = server_hide_activity_ips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_admin_log_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        admin_log_retention_days = _parse_admin_log_retention_days(d.pop("admin_log_retention_days", UNSET))

        def _parse_admin_log_retention_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        admin_log_retention_count = _parse_admin_log_retention_count(d.pop("admin_log_retention_count", UNSET))

        def _parse_user_log_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_log_retention_days = _parse_user_log_retention_days(d.pop("user_log_retention_days", UNSET))

        def _parse_user_log_retention_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_log_retention_count = _parse_user_log_retention_count(d.pop("user_log_retention_count", UNSET))

        def _parse_server_log_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        server_log_retention_days = _parse_server_log_retention_days(d.pop("server_log_retention_days", UNSET))

        def _parse_server_log_retention_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        server_log_retention_count = _parse_server_log_retention_count(d.pop("server_log_retention_count", UNSET))

        def _parse_server_log_admin_activity(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        server_log_admin_activity = _parse_server_log_admin_activity(d.pop("server_log_admin_activity", UNSET))

        def _parse_server_log_schedule_activity(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        server_log_schedule_activity = _parse_server_log_schedule_activity(d.pop("server_log_schedule_activity", UNSET))

        def _parse_server_hide_activity_ips(data: object) -> ActivityIpHiding | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                server_hide_activity_ips_type_1 = ActivityIpHiding(data)

                return server_hide_activity_ips_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivityIpHiding | None | Unset, data)

        server_hide_activity_ips = _parse_server_hide_activity_ips(d.pop("server_hide_activity_ips", UNSET))

        put_api_admin_settings_body_activity_type_1 = cls(
            admin_log_retention_days=admin_log_retention_days,
            admin_log_retention_count=admin_log_retention_count,
            user_log_retention_days=user_log_retention_days,
            user_log_retention_count=user_log_retention_count,
            server_log_retention_days=server_log_retention_days,
            server_log_retention_count=server_log_retention_count,
            server_log_admin_activity=server_log_admin_activity,
            server_log_schedule_activity=server_log_schedule_activity,
            server_hide_activity_ips=server_hide_activity_ips,
        )

        put_api_admin_settings_body_activity_type_1.additional_properties = d
        return put_api_admin_settings_body_activity_type_1

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
