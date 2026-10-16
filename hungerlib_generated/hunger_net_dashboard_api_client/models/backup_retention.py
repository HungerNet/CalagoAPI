from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupRetention")


@_attrs_define
class BackupRetention:
    """
    Attributes:
        count (int | Unset):  Default: 0.
        days (int | Unset):  Default: 0.
        daily (int | Unset):  Default: 0.
        weekly (int | Unset):  Default: 0.
        monthly (int | Unset):  Default: 0.
        yearly (int | Unset):  Default: 0.
    """

    count: int | Unset = 0
    days: int | Unset = 0
    daily: int | Unset = 0
    weekly: int | Unset = 0
    monthly: int | Unset = 0
    yearly: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        days = self.days

        daily = self.daily

        weekly = self.weekly

        monthly = self.monthly

        yearly = self.yearly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if days is not UNSET:
            field_dict["days"] = days
        if daily is not UNSET:
            field_dict["daily"] = daily
        if weekly is not UNSET:
            field_dict["weekly"] = weekly
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if yearly is not UNSET:
            field_dict["yearly"] = yearly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        days = d.pop("days", UNSET)

        daily = d.pop("daily", UNSET)

        weekly = d.pop("weekly", UNSET)

        monthly = d.pop("monthly", UNSET)

        yearly = d.pop("yearly", UNSET)

        backup_retention = cls(
            count=count,
            days=days,
            daily=daily,
            weekly=weekly,
            monthly=monthly,
            yearly=yearly,
        )

        backup_retention.additional_properties = d
        return backup_retention

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
