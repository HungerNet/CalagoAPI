from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_o_auth_provider_info_urls import AdminOAuthProviderInfoUrls


T = TypeVar("T", bound="AdminOAuthProvider")


@_attrs_define
class AdminOAuthProvider:
    """
    Attributes:
        uuid (UUID):
        name (str):
        client_id (str):
        auth_url (str):
        token_url (str):
        info_url (str):
        info_urls (AdminOAuthProviderInfoUrls):
        scopes (list[str]):
        identifier_path (str):
        avatar_overwrite (bool):
        enabled (bool):
        login_only (bool):
        login_bypass_two_factor (bool):
        link_viewable (bool):
        user_manageable (bool):
        basic_auth (bool):
        pkce (bool):
        created (datetime.datetime):
        description (None | str | Unset):
        client_secret (None | str | Unset):
        email_path (None | str | Unset):
        username_path (None | str | Unset):
        name_first_path (None | str | Unset):
        name_last_path (None | str | Unset):
        avatar_url_template (None | str | Unset):
    """

    uuid: UUID
    name: str
    client_id: str
    auth_url: str
    token_url: str
    info_url: str
    info_urls: AdminOAuthProviderInfoUrls
    scopes: list[str]
    identifier_path: str
    avatar_overwrite: bool
    enabled: bool
    login_only: bool
    login_bypass_two_factor: bool
    link_viewable: bool
    user_manageable: bool
    basic_auth: bool
    pkce: bool
    created: datetime.datetime
    description: None | str | Unset = UNSET
    client_secret: None | str | Unset = UNSET
    email_path: None | str | Unset = UNSET
    username_path: None | str | Unset = UNSET
    name_first_path: None | str | Unset = UNSET
    name_last_path: None | str | Unset = UNSET
    avatar_url_template: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        client_id = self.client_id

        auth_url = self.auth_url

        token_url = self.token_url

        info_url = self.info_url

        info_urls = self.info_urls.to_dict()

        scopes = self.scopes

        identifier_path = self.identifier_path

        avatar_overwrite = self.avatar_overwrite

        enabled = self.enabled

        login_only = self.login_only

        login_bypass_two_factor = self.login_bypass_two_factor

        link_viewable = self.link_viewable

        user_manageable = self.user_manageable

        basic_auth = self.basic_auth

        pkce = self.pkce

        created = self.created.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

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
                "uuid": uuid,
                "name": name,
                "client_id": client_id,
                "auth_url": auth_url,
                "token_url": token_url,
                "info_url": info_url,
                "info_urls": info_urls,
                "scopes": scopes,
                "identifier_path": identifier_path,
                "avatar_overwrite": avatar_overwrite,
                "enabled": enabled,
                "login_only": login_only,
                "login_bypass_two_factor": login_bypass_two_factor,
                "link_viewable": link_viewable,
                "user_manageable": user_manageable,
                "basic_auth": basic_auth,
                "pkce": pkce,
                "created": created,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
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
        from ..models.admin_o_auth_provider_info_urls import AdminOAuthProviderInfoUrls  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        client_id = d.pop("client_id")

        auth_url = d.pop("auth_url")

        token_url = d.pop("token_url")

        info_url = d.pop("info_url")

        info_urls = AdminOAuthProviderInfoUrls.from_dict(d.pop("info_urls"))

        scopes = cast(list[str], d.pop("scopes"))

        identifier_path = d.pop("identifier_path")

        avatar_overwrite = d.pop("avatar_overwrite")

        enabled = d.pop("enabled")

        login_only = d.pop("login_only")

        login_bypass_two_factor = d.pop("login_bypass_two_factor")

        link_viewable = d.pop("link_viewable")

        user_manageable = d.pop("user_manageable")

        basic_auth = d.pop("basic_auth")

        pkce = d.pop("pkce")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

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

        admin_o_auth_provider = cls(
            uuid=uuid,
            name=name,
            client_id=client_id,
            auth_url=auth_url,
            token_url=token_url,
            info_url=info_url,
            info_urls=info_urls,
            scopes=scopes,
            identifier_path=identifier_path,
            avatar_overwrite=avatar_overwrite,
            enabled=enabled,
            login_only=login_only,
            login_bypass_two_factor=login_bypass_two_factor,
            link_viewable=link_viewable,
            user_manageable=user_manageable,
            basic_auth=basic_auth,
            pkce=pkce,
            created=created,
            description=description,
            client_secret=client_secret,
            email_path=email_path,
            username_path=username_path,
            name_first_path=name_first_path,
            name_last_path=name_last_path,
            avatar_url_template=avatar_url_template,
        )

        admin_o_auth_provider.additional_properties = d
        return admin_o_auth_provider

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
