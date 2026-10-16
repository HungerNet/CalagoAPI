from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthRegisterBody")


@_attrs_define
class PostApiAuthRegisterBody:
    """
    Attributes:
        username (str):
        email (str):
        password (str):
        name_first (None | str | Unset):
        name_last (None | str | Unset):
        language (None | str | Unset):
        captcha (None | str | Unset):
    """

    username: str
    email: str
    password: str
    name_first: None | str | Unset = UNSET
    name_last: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    captcha: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        password = self.password

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

        captcha: None | str | Unset
        if isinstance(self.captcha, Unset):
            captcha = UNSET
        else:
            captcha = self.captcha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "email": email,
                "password": password,
            }
        )
        if name_first is not UNSET:
            field_dict["name_first"] = name_first
        if name_last is not UNSET:
            field_dict["name_last"] = name_last
        if language is not UNSET:
            field_dict["language"] = language
        if captcha is not UNSET:
            field_dict["captcha"] = captcha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        email = d.pop("email")

        password = d.pop("password")

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

        def _parse_captcha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        captcha = _parse_captcha(d.pop("captcha", UNSET))

        post_api_auth_register_body = cls(
            username=username,
            email=email,
            password=password,
            name_first=name_first,
            name_last=name_last,
            language=language,
            captcha=captcha,
        )

        post_api_auth_register_body.additional_properties = d
        return post_api_auth_register_body

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
