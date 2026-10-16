from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_command_snippet import UserCommandSnippet


T = TypeVar("T", bound="GetApiClientServersEggsEggCommandSnippetsResponse200")


@_attrs_define
class GetApiClientServersEggsEggCommandSnippetsResponse200:
    """
    Attributes:
        command_snippets (list[UserCommandSnippet]):
    """

    command_snippets: list[UserCommandSnippet]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command_snippets = []
        for command_snippets_item_data in self.command_snippets:
            command_snippets_item = command_snippets_item_data.to_dict()
            command_snippets.append(command_snippets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command_snippets": command_snippets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_command_snippet import UserCommandSnippet  # noqa: PLC0415

        d = dict(src_dict)
        command_snippets = []
        _command_snippets = d.pop("command_snippets")
        for command_snippets_item_data in _command_snippets:
            command_snippets_item = UserCommandSnippet.from_dict(command_snippets_item_data)

            command_snippets.append(command_snippets_item)

        get_api_client_servers_eggs_egg_command_snippets_response_200 = cls(
            command_snippets=command_snippets,
        )

        get_api_client_servers_eggs_egg_command_snippets_response_200.additional_properties = d
        return get_api_client_servers_eggs_egg_command_snippets_response_200

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
