from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveredOAuthProvider")


@_attrs_define
class DiscoveredOAuthProvider:
    """
    Attributes:
        name (str):
        auth_url (str):
        token_url (str):
        info_url (str):
        scopes (list[str]):
        identifier_path (str):
        basic_auth (bool):
        pkce (bool):
        email_path (None | str | Unset):
        username_path (None | str | Unset):
        name_first_path (None | str | Unset):
        name_last_path (None | str | Unset):
        avatar_url_template (None | str | Unset):
    """

    name: str
    auth_url: str
    token_url: str
    info_url: str
    scopes: list[str]
    identifier_path: str
    basic_auth: bool
    pkce: bool
    email_path: None | str | Unset = UNSET
    username_path: None | str | Unset = UNSET
    name_first_path: None | str | Unset = UNSET
    name_last_path: None | str | Unset = UNSET
    avatar_url_template: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        auth_url = self.auth_url

        token_url = self.token_url

        info_url = self.info_url

        scopes = self.scopes

        identifier_path = self.identifier_path

        basic_auth = self.basic_auth

        pkce = self.pkce

        email_path: None | str | Unset
        if isinstance(self.email_path, Unset):
            email_path = UNSET
        else:
            email_path = self.email_path

        username_path: None | str | Unset
        if isinstance(self.username_path, Unset):
            username_path = UNSET
        else:
            username_path = self.username_path

        name_first_path: None | str | Unset
        if isinstance(self.name_first_path, Unset):
            name_first_path = UNSET
        else:
            name_first_path = self.name_first_path

        name_last_path: None | str | Unset
        if isinstance(self.name_last_path, Unset):
            name_last_path = UNSET
        else:
            name_last_path = self.name_last_path

        avatar_url_template: None | str | Unset
        if isinstance(self.avatar_url_template, Unset):
            avatar_url_template = UNSET
        else:
            avatar_url_template = self.avatar_url_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "auth_url": auth_url,
                "token_url": token_url,
                "info_url": info_url,
                "scopes": scopes,
                "identifier_path": identifier_path,
                "basic_auth": basic_auth,
                "pkce": pkce,
            }
        )
        if email_path is not UNSET:
            field_dict["email_path"] = email_path
        if username_path is not UNSET:
            field_dict["username_path"] = username_path
        if name_first_path is not UNSET:
            field_dict["name_first_path"] = name_first_path
        if name_last_path is not UNSET:
            field_dict["name_last_path"] = name_last_path
        if avatar_url_template is not UNSET:
            field_dict["avatar_url_template"] = avatar_url_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        auth_url = d.pop("auth_url")

        token_url = d.pop("token_url")

        info_url = d.pop("info_url")

        scopes = cast(list[str], d.pop("scopes"))

        identifier_path = d.pop("identifier_path")

        basic_auth = d.pop("basic_auth")

        pkce = d.pop("pkce")

        def _parse_email_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_path = _parse_email_path(d.pop("email_path", UNSET))

        def _parse_username_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username_path = _parse_username_path(d.pop("username_path", UNSET))

        def _parse_name_first_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_first_path = _parse_name_first_path(d.pop("name_first_path", UNSET))

        def _parse_name_last_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_last_path = _parse_name_last_path(d.pop("name_last_path", UNSET))

        def _parse_avatar_url_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url_template = _parse_avatar_url_template(d.pop("avatar_url_template", UNSET))

        discovered_o_auth_provider = cls(
            name=name,
            auth_url=auth_url,
            token_url=token_url,
            info_url=info_url,
            scopes=scopes,
            identifier_path=identifier_path,
            basic_auth=basic_auth,
            pkce=pkce,
            email_path=email_path,
            username_path=username_path,
            name_first_path=name_first_path,
            name_last_path=name_last_path,
            avatar_url_template=avatar_url_template,
        )

        discovered_o_auth_provider.additional_properties = d
        return discovered_o_auth_provider

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
