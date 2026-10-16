from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerSubusersBody")


@_attrs_define
class PostApiClientServersServerSubusersBody:
    """
    Attributes:
        email (str):
        permissions (list[str]):
        ignored_files (list[str]):
        captcha (None | str | Unset):
    """

    email: str
    permissions: list[str]
    ignored_files: list[str]
    captcha: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        permissions = self.permissions

        ignored_files = self.ignored_files

        captcha: None | str | Unset
        if isinstance(self.captcha, Unset):
            captcha = UNSET
        else:
            captcha = self.captcha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "permissions": permissions,
                "ignored_files": ignored_files,
            }
        )
        if captcha is not UNSET:
            field_dict["captcha"] = captcha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        permissions = cast(list[str], d.pop("permissions"))

        ignored_files = cast(list[str], d.pop("ignored_files"))

        def _parse_captcha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        captcha = _parse_captcha(d.pop("captcha", UNSET))

        post_api_client_servers_server_subusers_body = cls(
            email=email,
            permissions=permissions,
            ignored_files=ignored_files,
            captcha=captcha,
        )

        post_api_client_servers_server_subusers_body.additional_properties = d
        return post_api_client_servers_server_subusers_body

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
