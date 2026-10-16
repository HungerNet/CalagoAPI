from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_trigger_type_3_type import ScheduleTriggerType3Type
from ..models.server_backup_status import ServerBackupStatus

T = TypeVar("T", bound="ScheduleTriggerType3")


@_attrs_define
class ScheduleTriggerType3:
    """
    Attributes:
        status (ServerBackupStatus):
        type_ (ScheduleTriggerType3Type):
    """

    status: ServerBackupStatus
    type_: ScheduleTriggerType3Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ServerBackupStatus(d.pop("status"))

        type_ = ScheduleTriggerType3Type(d.pop("type"))

        schedule_trigger_type_3 = cls(
            status=status,
            type_=type_,
        )

        schedule_trigger_type_3.additional_properties = d
        return schedule_trigger_type_3

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
