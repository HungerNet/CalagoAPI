from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_trigger_type_7_type import ScheduleTriggerType7Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_variable import ScheduleVariable


T = TypeVar("T", bound="ScheduleTriggerType7")


@_attrs_define
class ScheduleTriggerType7:
    """
    Attributes:
        contains (str):
        type_ (ScheduleTriggerType7Type):
        case_insensitive (bool | Unset):
        output_into (None | ScheduleVariable | Unset):
    """

    contains: str
    type_: ScheduleTriggerType7Type
    case_insensitive: bool | Unset = UNSET
    output_into: None | ScheduleVariable | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_variable import ScheduleVariable  # noqa: PLC0415

        contains = self.contains

        type_ = self.type_.value

        case_insensitive = self.case_insensitive

        output_into: dict[str, Any] | None | Unset
        if isinstance(self.output_into, Unset):
            output_into = UNSET
        elif isinstance(self.output_into, ScheduleVariable):
            output_into = self.output_into.to_dict()
        else:
            output_into = self.output_into

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contains": contains,
                "type": type_,
            }
        )
        if case_insensitive is not UNSET:
            field_dict["case_insensitive"] = case_insensitive
        if output_into is not UNSET:
            field_dict["output_into"] = output_into

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_variable import ScheduleVariable  # noqa: PLC0415

        d = dict(src_dict)
        contains = d.pop("contains")

        type_ = ScheduleTriggerType7Type(d.pop("type"))

        case_insensitive = d.pop("case_insensitive", UNSET)

        def _parse_output_into(data: object) -> None | ScheduleVariable | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_into_type_1 = ScheduleVariable.from_dict(data)

                return output_into_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScheduleVariable | Unset, data)

        output_into = _parse_output_into(d.pop("output_into", UNSET))

        schedule_trigger_type_7 = cls(
            contains=contains,
            type_=type_,
            case_insensitive=case_insensitive,
            output_into=output_into,
        )

        schedule_trigger_type_7.additional_properties = d
        return schedule_trigger_type_7

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
