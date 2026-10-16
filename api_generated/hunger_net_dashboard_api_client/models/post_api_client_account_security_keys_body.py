from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientAccountSecurityKeysBody")


@_attrs_define
class PostApiClientAccountSecurityKeysBody:
    """
    Attributes:
        name (str):
        password (str):
        allow_usernameless_login (bool | Unset):
    """

    name: str
    password: str
    allow_usernameless_login: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        password = self.password

        allow_usernameless_login = self.allow_usernameless_login

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "password": password,
            }
        )
        if allow_usernameless_login is not UNSET:
            field_dict["allow_usernameless_login"] = allow_usernameless_login

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        password = d.pop("password")

        allow_usernameless_login = d.pop("allow_usernameless_login", UNSET)

        post_api_client_account_security_keys_body = cls(
            name=name,
            password=password,
            allow_usernameless_login=allow_usernameless_login,
        )

        post_api_client_account_security_keys_body.additional_properties = d
        return post_api_client_account_security_keys_body

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
