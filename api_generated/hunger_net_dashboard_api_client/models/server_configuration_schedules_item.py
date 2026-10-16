from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerConfigurationSchedulesItem")


@_attrs_define
class ServerConfigurationSchedulesItem:
    """
    Attributes:
        uuid (UUID):
        triggers (Any):
        condition (Any):
        actions (list[Any]):
    """

    uuid: UUID
    triggers: Any
    condition: Any
    actions: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        triggers = self.triggers

        condition = self.condition

        actions = self.actions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "triggers": triggers,
                "condition": condition,
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        triggers = d.pop("triggers")

        condition = d.pop("condition")

        actions = cast(list[Any], d.pop("actions"))

        server_configuration_schedules_item = cls(
            uuid=uuid,
            triggers=triggers,
            condition=condition,
            actions=actions,
        )

        server_configuration_schedules_item.additional_properties = d
        return server_configuration_schedules_item

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
