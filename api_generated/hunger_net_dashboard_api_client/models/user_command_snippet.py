from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserCommandSnippet")


@_attrs_define
class UserCommandSnippet:
    """
    Attributes:
        uuid (UUID):
        name (str):
        eggs (list[UUID]):
        command (str):
        created (datetime.datetime):
    """

    uuid: UUID
    name: str
    eggs: list[UUID]
    command: str
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        eggs = []
        for eggs_item_data in self.eggs:
            eggs_item = str(eggs_item_data)
            eggs.append(eggs_item)

        command = self.command

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "eggs": eggs,
                "command": command,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        eggs = []
        _eggs = d.pop("eggs")
        for eggs_item_data in _eggs:
            eggs_item = UUID(eggs_item_data)

            eggs.append(eggs_item)

        command = d.pop("command")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        user_command_snippet = cls(
            uuid=uuid,
            name=name,
            eggs=eggs,
            command=command,
            created=created,
        )

        user_command_snippet.additional_properties = d
        return user_command_snippet

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
