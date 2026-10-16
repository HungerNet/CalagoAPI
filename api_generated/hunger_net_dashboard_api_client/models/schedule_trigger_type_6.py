from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_condition_comparator import ScheduleConditionComparator
from ..models.schedule_resource_metric import ScheduleResourceMetric
from ..models.schedule_trigger_type_6_type import ScheduleTriggerType6Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleTriggerType6")


@_attrs_define
class ScheduleTriggerType6:
    """
    Attributes:
        metric (ScheduleResourceMetric):
        comparator (ScheduleConditionComparator):
        value (float):
        type_ (ScheduleTriggerType6Type):
        for_seconds (int | Unset):
    """

    metric: ScheduleResourceMetric
    comparator: ScheduleConditionComparator
    value: float
    type_: ScheduleTriggerType6Type
    for_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric.value

        comparator = self.comparator.value

        value = self.value

        type_ = self.type_.value

        for_seconds = self.for_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "comparator": comparator,
                "value": value,
                "type": type_,
            }
        )
        if for_seconds is not UNSET:
            field_dict["for_seconds"] = for_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric = ScheduleResourceMetric(d.pop("metric"))

        comparator = ScheduleConditionComparator(d.pop("comparator"))

        value = d.pop("value")

        type_ = ScheduleTriggerType6Type(d.pop("type"))

        for_seconds = d.pop("for_seconds", UNSET)

        schedule_trigger_type_6 = cls(
            metric=metric,
            comparator=comparator,
            value=value,
            type_=type_,
            for_seconds=for_seconds,
        )

        schedule_trigger_type_6.additional_properties = d
        return schedule_trigger_type_6

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
