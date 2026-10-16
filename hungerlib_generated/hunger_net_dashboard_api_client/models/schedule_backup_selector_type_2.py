from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_backup_selector_type_2_mode import ScheduleBackupSelectorType2Mode

if TYPE_CHECKING:
    from ..models.schedule_variable import ScheduleVariable


T = TypeVar("T", bound="ScheduleBackupSelectorType2")


@_attrs_define
class ScheduleBackupSelectorType2:
    """
    Attributes:
        uuid (ScheduleVariable | str):
        mode (ScheduleBackupSelectorType2Mode):
    """

    uuid: ScheduleVariable | str
    mode: ScheduleBackupSelectorType2Mode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_variable import ScheduleVariable  # noqa: PLC0415

        uuid: dict[str, Any] | str
        if isinstance(self.uuid, ScheduleVariable):
            uuid = self.uuid.to_dict()
        else:
            uuid = self.uuid

        mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_variable import ScheduleVariable  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_uuid(data: object) -> ScheduleVariable | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_dynamic_parameter_type_1 = ScheduleVariable.from_dict(data)

                return componentsschemas_schedule_dynamic_parameter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ScheduleVariable | str, data)

        uuid = _parse_uuid(d.pop("uuid"))

        mode = ScheduleBackupSelectorType2Mode(d.pop("mode"))

        schedule_backup_selector_type_2 = cls(
            uuid=uuid,
            mode=mode,
        )

        schedule_backup_selector_type_2.additional_properties = d
        return schedule_backup_selector_type_2

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
