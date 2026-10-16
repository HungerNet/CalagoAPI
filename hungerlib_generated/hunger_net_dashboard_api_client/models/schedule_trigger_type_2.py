from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_trigger_type_2_type import ScheduleTriggerType2Type
from ..models.server_state import ServerState

T = TypeVar("T", bound="ScheduleTriggerType2")


@_attrs_define
class ScheduleTriggerType2:
    """
    Attributes:
        state (ServerState):
        type_ (ScheduleTriggerType2Type):
    """

    state: ServerState
    type_: ScheduleTriggerType2Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = ServerState(d.pop("state"))

        type_ = ScheduleTriggerType2Type(d.pop("type"))

        schedule_trigger_type_2 = cls(
            state=state,
            type_=type_,
        )

        schedule_trigger_type_2.additional_properties = d
        return schedule_trigger_type_2

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
