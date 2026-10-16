from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserApiKey")


@_attrs_define
class UserApiKey:
    """
    Attributes:
        uuid (UUID):
        name (str):
        key_start (str):
        allowed_ips (list[str]):
        enabled (bool):
        user_permissions (list[str]):
        admin_permissions (list[str]):
        server_permissions (list[str]):
        created (datetime.datetime):
        last_used (datetime.datetime | None | Unset):
        expires (datetime.datetime | None | Unset):
    """

    uuid: UUID
    name: str
    key_start: str
    allowed_ips: list[str]
    enabled: bool
    user_permissions: list[str]
    admin_permissions: list[str]
    server_permissions: list[str]
    created: datetime.datetime
    last_used: datetime.datetime | None | Unset = UNSET
    expires: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        key_start = self.key_start

        allowed_ips = self.allowed_ips

        enabled = self.enabled

        user_permissions = self.user_permissions

        admin_permissions = self.admin_permissions

        server_permissions = self.server_permissions

        created = self.created.isoformat()

        last_used: None | str | Unset
        if isinstance(self.last_used, Unset):
            last_used = UNSET
        elif isinstance(self.last_used, datetime.datetime):
            last_used = self.last_used.isoformat()
        else:
            last_used = self.last_used

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
                "uuid": uuid,
                "name": name,
                "key_start": key_start,
                "allowed_ips": allowed_ips,
                "enabled": enabled,
                "user_permissions": user_permissions,
                "admin_permissions": admin_permissions,
                "server_permissions": server_permissions,
                "created": created,
            }
        )
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        key_start = d.pop("key_start")

        allowed_ips = cast(list[str], d.pop("allowed_ips"))

        enabled = d.pop("enabled")

        user_permissions = cast(list[str], d.pop("user_permissions"))

        admin_permissions = cast(list[str], d.pop("admin_permissions"))

        server_permissions = cast(list[str], d.pop("server_permissions"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_last_used(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used = _parse_last_used(d.pop("last_used", UNSET))

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

        user_api_key = cls(
            uuid=uuid,
            name=name,
            key_start=key_start,
            allowed_ips=allowed_ips,
            enabled=enabled,
            user_permissions=user_permissions,
            admin_permissions=admin_permissions,
            server_permissions=server_permissions,
            created=created,
            last_used=last_used,
            expires=expires,
        )

        user_api_key.additional_properties = d
        return user_api_key

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
