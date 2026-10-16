from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiClientAccountCommandSnippetsCommandSnippetBody")


@_attrs_define
class PatchApiClientAccountCommandSnippetsCommandSnippetBody:
    """
    Attributes:
        name (str):
        eggs (list[UUID] | None | Unset):
        command (None | str | Unset):
    """

    name: str
    eggs: list[UUID] | None | Unset = UNSET
    command: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        eggs: list[str] | None | Unset
        if isinstance(self.eggs, Unset):
            eggs = UNSET
        elif isinstance(self.eggs, list):
            eggs = []
            for eggs_type_0_item_data in self.eggs:
                eggs_type_0_item = str(eggs_type_0_item_data)
                eggs.append(eggs_type_0_item)

        else:
            eggs = self.eggs

        command: None | str | Unset
        if isinstance(self.command, Unset):
            command = UNSET
        else:
            command = self.command

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if eggs is not UNSET:
            field_dict["eggs"] = eggs
        if command is not UNSET:
            field_dict["command"] = command

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_eggs(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                eggs_type_0 = []
                _eggs_type_0 = data
                for eggs_type_0_item_data in _eggs_type_0:
                    eggs_type_0_item = UUID(eggs_type_0_item_data)

                    eggs_type_0.append(eggs_type_0_item)

                return eggs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        eggs = _parse_eggs(d.pop("eggs", UNSET))

        def _parse_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command = _parse_command(d.pop("command", UNSET))

        patch_api_client_account_command_snippets_command_snippet_body = cls(
            name=name,
            eggs=eggs,
            command=command,
        )

        patch_api_client_account_command_snippets_command_snippet_body.additional_properties = d
        return patch_api_client_account_command_snippets_command_snippet_body

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
