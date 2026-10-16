from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_status_errors import ScheduleStatusErrors


T = TypeVar("T", bound="ScheduleStatus")


@_attrs_define
class ScheduleStatus:
    """
    Attributes:
        running (bool):
        errors (ScheduleStatusErrors):
        step (None | Unset | UUID):
    """

    running: bool
    errors: ScheduleStatusErrors
    step: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        running = self.running

        errors = self.errors.to_dict()

        step: None | str | Unset
        if isinstance(self.step, Unset):
            step = UNSET
        elif isinstance(self.step, UUID):
            step = str(self.step)
        else:
            step = self.step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "running": running,
                "errors": errors,
            }
        )
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_status_errors import ScheduleStatusErrors  # noqa: PLC0415

        d = dict(src_dict)
        running = d.pop("running")

        errors = ScheduleStatusErrors.from_dict(d.pop("errors"))

        def _parse_step(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                step_type_0 = UUID(data)

                return step_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        step = _parse_step(d.pop("step", UNSET))

        schedule_status = cls(
            running=running,
            errors=errors,
            step=step,
        )

        schedule_status.additional_properties = d
        return schedule_status

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
