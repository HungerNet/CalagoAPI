from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_backup_selector_type_1_mode import ScheduleBackupSelectorType1Mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleBackupSelectorType1")


@_attrs_define
class ScheduleBackupSelectorType1:
    """
    Attributes:
        mode (ScheduleBackupSelectorType1Mode):
        backup_group_uuid (None | Unset | UUID):
    """

    mode: ScheduleBackupSelectorType1Mode
    backup_group_uuid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        backup_group_uuid: None | str | Unset
        if isinstance(self.backup_group_uuid, Unset):
            backup_group_uuid = UNSET
        elif isinstance(self.backup_group_uuid, UUID):
            backup_group_uuid = str(self.backup_group_uuid)
        else:
            backup_group_uuid = self.backup_group_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if backup_group_uuid is not UNSET:
            field_dict["backup_group_uuid"] = backup_group_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = ScheduleBackupSelectorType1Mode(d.pop("mode"))

        def _parse_backup_group_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_group_uuid_type_0 = UUID(data)

                return backup_group_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_group_uuid = _parse_backup_group_uuid(d.pop("backup_group_uuid", UNSET))

        schedule_backup_selector_type_1 = cls(
            mode=mode,
            backup_group_uuid=backup_group_uuid,
        )

        schedule_backup_selector_type_1.additional_properties = d
        return schedule_backup_selector_type_1

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
