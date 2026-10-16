from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminUsersBody")


@_attrs_define
class PostApiAdminUsersBody:
    """
    Attributes:
        username (str):
        email (str):
        admin (bool):
        language (str):
        role_uuid (None | Unset | UUID):
        external_id (None | str | Unset):
        name_first (None | str | Unset):
        name_last (None | str | Unset):
        password (None | str | Unset):
        frozen (bool | Unset):
        suspended (bool | Unset):
        verify_email (bool | Unset):
        send_email (bool | Unset):
    """

    username: str
    email: str
    admin: bool
    language: str
    role_uuid: None | Unset | UUID = UNSET
    external_id: None | str | Unset = UNSET
    name_first: None | str | Unset = UNSET
    name_last: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    frozen: bool | Unset = UNSET
    suspended: bool | Unset = UNSET
    verify_email: bool | Unset = UNSET
    send_email: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        admin = self.admin

        language = self.language

        role_uuid: None | str | Unset
        if isinstance(self.role_uuid, Unset):
            role_uuid = UNSET
        elif isinstance(self.role_uuid, UUID):
            role_uuid = str(self.role_uuid)
        else:
            role_uuid = self.role_uuid

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

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

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        frozen = self.frozen

        suspended = self.suspended

        verify_email = self.verify_email

        send_email = self.send_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "email": email,
                "admin": admin,
                "language": language,
            }
        )
        if role_uuid is not UNSET:
            field_dict["role_uuid"] = role_uuid
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if name_first is not UNSET:
            field_dict["name_first"] = name_first
        if name_last is not UNSET:
            field_dict["name_last"] = name_last
        if password is not UNSET:
            field_dict["password"] = password
        if frozen is not UNSET:
            field_dict["frozen"] = frozen
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if verify_email is not UNSET:
            field_dict["verify_email"] = verify_email
        if send_email is not UNSET:
            field_dict["send_email"] = send_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        email = d.pop("email")

        admin = d.pop("admin")

        language = d.pop("language")

        def _parse_role_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_uuid_type_0 = UUID(data)

                return role_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        role_uuid = _parse_role_uuid(d.pop("role_uuid", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

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

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        frozen = d.pop("frozen", UNSET)

        suspended = d.pop("suspended", UNSET)

        verify_email = d.pop("verify_email", UNSET)

        send_email = d.pop("send_email", UNSET)

        post_api_admin_users_body = cls(
            username=username,
            email=email,
            admin=admin,
            language=language,
            role_uuid=role_uuid,
            external_id=external_id,
            name_first=name_first,
            name_last=name_last,
            password=password,
            frozen=frozen,
            suspended=suspended,
            verify_email=verify_email,
            send_email=send_email,
        )

        post_api_admin_users_body.additional_properties = d
        return post_api_admin_users_body

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
