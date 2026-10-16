from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiAdminUsersUserBody")


@_attrs_define
class PatchApiAdminUsersUserBody:
    """
    Attributes:
        role_uuid (None | Unset | UUID):
        external_id (None | str | Unset):
        username (None | str | Unset):
        email (None | str | Unset):
        name_first (None | str | Unset):
        name_last (None | str | Unset):
        password (None | str | Unset):
        admin (bool | None | Unset):
        frozen (bool | None | Unset):
        suspended (bool | None | Unset):
        language (None | str | Unset):
    """

    role_uuid: None | Unset | UUID = UNSET
    external_id: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    name_first: None | str | Unset = UNSET
    name_last: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    admin: bool | None | Unset = UNSET
    frozen: bool | None | Unset = UNSET
    suspended: bool | None | Unset = UNSET
    language: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

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

        admin: bool | None | Unset
        if isinstance(self.admin, Unset):
            admin = UNSET
        else:
            admin = self.admin

        frozen: bool | None | Unset
        if isinstance(self.frozen, Unset):
            frozen = UNSET
        else:
            frozen = self.frozen

        suspended: bool | None | Unset
        if isinstance(self.suspended, Unset):
            suspended = UNSET
        else:
            suspended = self.suspended

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_uuid is not UNSET:
            field_dict["role_uuid"] = role_uuid
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if name_first is not UNSET:
            field_dict["name_first"] = name_first
        if name_last is not UNSET:
            field_dict["name_last"] = name_last
        if password is not UNSET:
            field_dict["password"] = password
        if admin is not UNSET:
            field_dict["admin"] = admin
        if frozen is not UNSET:
            field_dict["frozen"] = frozen
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

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

        def _parse_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        admin = _parse_admin(d.pop("admin", UNSET))

        def _parse_frozen(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        frozen = _parse_frozen(d.pop("frozen", UNSET))

        def _parse_suspended(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        suspended = _parse_suspended(d.pop("suspended", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        patch_api_admin_users_user_body = cls(
            role_uuid=role_uuid,
            external_id=external_id,
            username=username,
            email=email,
            name_first=name_first,
            name_last=name_last,
            password=password,
            admin=admin,
            frozen=frozen,
            suspended=suspended,
            language=language,
        )

        patch_api_admin_users_user_body.additional_properties = d
        return patch_api_admin_users_user_body

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
