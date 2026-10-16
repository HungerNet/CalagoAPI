from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schedule_variable import ScheduleVariable


T = TypeVar("T", bound="ScheduleHttpHeader")


@_attrs_define
class ScheduleHttpHeader:
    """
    Attributes:
        name (str):
        value (ScheduleVariable | str):
    """

    name: str
    value: ScheduleVariable | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_variable import ScheduleVariable  # noqa: PLC0415

        name = self.name

        value: dict[str, Any] | str
        if isinstance(self.value, ScheduleVariable):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_variable import ScheduleVariable  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_value(data: object) -> ScheduleVariable | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_dynamic_parameter_type_1 = ScheduleVariable.from_dict(data)

                return componentsschemas_schedule_dynamic_parameter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ScheduleVariable | str, data)

        value = _parse_value(d.pop("value"))

        schedule_http_header = cls(
            name=name,
            value=value,
        )

        schedule_http_header.additional_properties = d
        return schedule_http_header

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
