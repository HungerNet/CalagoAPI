from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiClientAccountApiKeysApiKeyBody")


@_attrs_define
class PatchApiClientAccountApiKeysApiKeyBody:
    """
    Attributes:
        allowed_ips (list[str]):
        name (None | str | Unset):
        enabled (bool | None | Unset):
        user_permissions (list[str] | None | Unset):
        admin_permissions (list[str] | None | Unset):
        server_permissions (list[str] | None | Unset):
        expires (datetime.datetime | None | Unset):
    """

    allowed_ips: list[str]
    name: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    user_permissions: list[str] | None | Unset = UNSET
    admin_permissions: list[str] | None | Unset = UNSET
    server_permissions: list[str] | None | Unset = UNSET
    expires: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_ips = self.allowed_ips

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        user_permissions: list[str] | None | Unset
        if isinstance(self.user_permissions, Unset):
            user_permissions = UNSET
        elif isinstance(self.user_permissions, list):
            user_permissions = self.user_permissions

        else:
            user_permissions = self.user_permissions

        admin_permissions: list[str] | None | Unset
        if isinstance(self.admin_permissions, Unset):
            admin_permissions = UNSET
        elif isinstance(self.admin_permissions, list):
            admin_permissions = self.admin_permissions

        else:
            admin_permissions = self.admin_permissions

        server_permissions: list[str] | None | Unset
        if isinstance(self.server_permissions, Unset):
            server_permissions = UNSET
        elif isinstance(self.server_permissions, list):
            server_permissions = self.server_permissions

        else:
            server_permissions = self.server_permissions

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
                "allowed_ips": allowed_ips,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if user_permissions is not UNSET:
            field_dict["user_permissions"] = user_permissions
        if admin_permissions is not UNSET:
            field_dict["admin_permissions"] = admin_permissions
        if server_permissions is not UNSET:
            field_dict["server_permissions"] = server_permissions
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_ips = cast(list[str], d.pop("allowed_ips"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_user_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_permissions_type_0 = cast(list[str], data)

                return user_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        user_permissions = _parse_user_permissions(d.pop("user_permissions", UNSET))

        def _parse_admin_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                admin_permissions_type_0 = cast(list[str], data)

                return admin_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        admin_permissions = _parse_admin_permissions(d.pop("admin_permissions", UNSET))

        def _parse_server_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                server_permissions_type_0 = cast(list[str], data)

                return server_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        server_permissions = _parse_server_permissions(d.pop("server_permissions", UNSET))

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

        patch_api_client_account_api_keys_api_key_body = cls(
            allowed_ips=allowed_ips,
            name=name,
            enabled=enabled,
            user_permissions=user_permissions,
            admin_permissions=admin_permissions,
            server_permissions=server_permissions,
            expires=expires,
        )

        patch_api_client_account_api_keys_api_key_body.additional_properties = d
        return patch_api_client_account_api_keys_api_key_body

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
