from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.two_factor_method import TwoFactorMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role import Role


T = TypeVar("T", bound="GetApiAdminRolesRoleUsersResponse200UsersAdminUser")


@_attrs_define
class GetApiAdminRolesRoleUsersResponse200UsersAdminUser:
    """
    Attributes:
        uuid (UUID):
        username (str):
        email (str):
        admin (bool):
        frozen (bool):
        suspended (bool):
        totp_enabled (bool):
        email_two_factor_enabled (bool):
        two_factor_methods (list[TwoFactorMethod]):
        require_two_factor (bool):
        two_factor_satisfied (bool):
        email_verified (bool):
        require_email_verification (bool):
        password_login_disabled (bool):
        language (str):
        has_password (bool):
        created (datetime.datetime):
        external_id (None | str | Unset):
        role (None | Role | Unset):
        avatar (None | str | Unset):
        name_first (None | str | Unset):
        name_last (None | str | Unset):
        totp_last_used (datetime.datetime | None | Unset):
    """

    uuid: UUID
    username: str
    email: str
    admin: bool
    frozen: bool
    suspended: bool
    totp_enabled: bool
    email_two_factor_enabled: bool
    two_factor_methods: list[TwoFactorMethod]
    require_two_factor: bool
    two_factor_satisfied: bool
    email_verified: bool
    require_email_verification: bool
    password_login_disabled: bool
    language: str
    has_password: bool
    created: datetime.datetime
    external_id: None | str | Unset = UNSET
    role: None | Role | Unset = UNSET
    avatar: None | str | Unset = UNSET
    name_first: None | str | Unset = UNSET
    name_last: None | str | Unset = UNSET
    totp_last_used: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.role import Role  # noqa: PLC0415

        uuid = str(self.uuid)

        username = self.username

        email = self.email

        admin = self.admin

        frozen = self.frozen

        suspended = self.suspended

        totp_enabled = self.totp_enabled

        email_two_factor_enabled = self.email_two_factor_enabled

        two_factor_methods = []
        for two_factor_methods_item_data in self.two_factor_methods:
            two_factor_methods_item = two_factor_methods_item_data.value
            two_factor_methods.append(two_factor_methods_item)

        require_two_factor = self.require_two_factor

        two_factor_satisfied = self.two_factor_satisfied

        email_verified = self.email_verified

        require_email_verification = self.require_email_verification

        password_login_disabled = self.password_login_disabled

        language = self.language

        has_password = self.has_password

        created = self.created.isoformat()

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        role: dict[str, Any] | None | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, Role):
            role = self.role.to_dict()
        else:
            role = self.role

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

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

        totp_last_used: None | str | Unset
        if isinstance(self.totp_last_used, Unset):
            totp_last_used = UNSET
        elif isinstance(self.totp_last_used, datetime.datetime):
            totp_last_used = self.totp_last_used.isoformat()
        else:
            totp_last_used = self.totp_last_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "username": username,
                "email": email,
                "admin": admin,
                "frozen": frozen,
                "suspended": suspended,
                "totp_enabled": totp_enabled,
                "email_two_factor_enabled": email_two_factor_enabled,
                "two_factor_methods": two_factor_methods,
                "require_two_factor": require_two_factor,
                "two_factor_satisfied": two_factor_satisfied,
                "email_verified": email_verified,
                "require_email_verification": require_email_verification,
                "password_login_disabled": password_login_disabled,
                "language": language,
                "has_password": has_password,
                "created": created,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if role is not UNSET:
            field_dict["role"] = role
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if name_first is not UNSET:
            field_dict["name_first"] = name_first
        if name_last is not UNSET:
            field_dict["name_last"] = name_last
        if totp_last_used is not UNSET:
            field_dict["totp_last_used"] = totp_last_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role import Role  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        username = d.pop("username")

        email = d.pop("email")

        admin = d.pop("admin")

        frozen = d.pop("frozen")

        suspended = d.pop("suspended")

        totp_enabled = d.pop("totp_enabled")

        email_two_factor_enabled = d.pop("email_two_factor_enabled")

        two_factor_methods = []
        _two_factor_methods = d.pop("two_factor_methods")
        for two_factor_methods_item_data in _two_factor_methods:
            two_factor_methods_item = TwoFactorMethod(two_factor_methods_item_data)

            two_factor_methods.append(two_factor_methods_item)

        require_two_factor = d.pop("require_two_factor")

        two_factor_satisfied = d.pop("two_factor_satisfied")

        email_verified = d.pop("email_verified")

        require_email_verification = d.pop("require_email_verification")

        password_login_disabled = d.pop("password_login_disabled")

        language = d.pop("language")

        has_password = d.pop("has_password")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_role(data: object) -> None | Role | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1 = Role.from_dict(data)

                return role_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Role | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

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

        def _parse_totp_last_used(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                totp_last_used_type_0 = datetime.datetime.fromisoformat(data)

                return totp_last_used_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        totp_last_used = _parse_totp_last_used(d.pop("totp_last_used", UNSET))

        get_api_admin_roles_role_users_response_200_users_admin_user = cls(
            uuid=uuid,
            username=username,
            email=email,
            admin=admin,
            frozen=frozen,
            suspended=suspended,
            totp_enabled=totp_enabled,
            email_two_factor_enabled=email_two_factor_enabled,
            two_factor_methods=two_factor_methods,
            require_two_factor=require_two_factor,
            two_factor_satisfied=two_factor_satisfied,
            email_verified=email_verified,
            require_email_verification=require_email_verification,
            password_login_disabled=password_login_disabled,
            language=language,
            has_password=has_password,
            created=created,
            external_id=external_id,
            role=role,
            avatar=avatar,
            name_first=name_first,
            name_last=name_last,
            totp_last_used=totp_last_used,
        )

        get_api_admin_roles_role_users_response_200_users_admin_user.additional_properties = d
        return get_api_admin_roles_role_users_response_200_users_admin_user

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
