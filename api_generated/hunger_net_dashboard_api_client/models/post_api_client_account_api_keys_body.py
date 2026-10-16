from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientAccountApiKeysBody")


@_attrs_define
class PostApiClientAccountApiKeysBody:
    """
    Attributes:
        name (str):
        allowed_ips (list[str]):
        user_permissions (list[str]):
        admin_permissions (list[str]):
        server_permissions (list[str]):
        enabled (bool | Unset):
        expires (datetime.datetime | None | Unset):
    """

    name: str
    allowed_ips: list[str]
    user_permissions: list[str]
    admin_permissions: list[str]
    server_permissions: list[str]
    enabled: bool | Unset = UNSET
    expires: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        allowed_ips = self.allowed_ips

        user_permissions = self.user_permissions

        admin_permissions = self.admin_permissions

        server_permissions = self.server_permissions

        enabled = self.enabled

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "allowed_ips": allowed_ips,
                "user_permissions": user_permissions,
                "admin_permissions": admin_permissions,
                "server_permissions": server_permissions,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        allowed_ips = cast(list[str], d.pop("allowed_ips"))

        user_permissions = cast(list[str], d.pop("user_permissions"))

        admin_permissions = cast(list[str], d.pop("admin_permissions"))

        server_permissions = cast(list[str], d.pop("server_permissions"))

        enabled = d.pop("enabled", UNSET)

        def _parse_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = datetime.datetime.fromisoformat(data)

                return expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))

        post_api_client_account_api_keys_body = cls(
            name=name,
            allowed_ips=allowed_ips,
            user_permissions=user_permissions,
            admin_permissions=admin_permissions,
            server_permissions=server_permissions,
            enabled=enabled,
            expires=expires,
        )

        post_api_client_account_api_keys_body.additional_properties = d
        return post_api_client_account_api_keys_body

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
