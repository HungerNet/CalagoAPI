from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiClientAccountBody")


@_attrs_define
class PatchApiClientAccountBody:
    """
    Attributes:
        username (None | str | Unset):
        name_first (None | str | Unset):
        name_last (None | str | Unset):
        language (None | str | Unset):
    """

    username: None | str | Unset = UNSET
    name_first: None | str | Unset = UNSET
    name_last: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        name_first: None | str | Unset
        if isinstance(self.name_first, Unset):
            name_first = UNSET
        else:
            name_first = self.name_first

        name_last: None | str | Unset
        if isinstance(self.name_last, Unset):
            name_last = UNSET
        else:
            name_last = self.name_last

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if name_first is not UNSET:
            field_dict["name_first"] = name_first
        if name_last is not UNSET:
            field_dict["name_last"] = name_last
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_name_first(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_first = _parse_name_first(d.pop("name_first", UNSET))

        def _parse_name_last(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_last = _parse_name_last(d.pop("name_last", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        patch_api_client_account_body = cls(
            username=username,
            name_first=name_first,
            name_last=name_last,
            language=language,
        )

        patch_api_client_account_body.additional_properties = d
        return patch_api_client_account_body

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
