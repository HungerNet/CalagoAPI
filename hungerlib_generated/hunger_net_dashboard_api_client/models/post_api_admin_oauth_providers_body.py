from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_admin_oauth_providers_body_info_urls import PostApiAdminOauthProvidersBodyInfoUrls


T = TypeVar("T", bound="PostApiAdminOauthProvidersBody")


@_attrs_define
class PostApiAdminOauthProvidersBody:
    """
    Attributes:
        name (str):
        enabled (bool):
        login_only (bool):
        login_bypass_two_factor (bool):
        link_viewable (bool):
        user_manageable (bool):
        basic_auth (bool):
        client_id (str):
        auth_url (str):
        token_url (str):
        info_url (str):
        scopes (list[str]):
        identifier_path (str):
        description (None | str | Unset):
        pkce (bool | Unset):
        client_secret (None | str | Unset):
        info_urls (PostApiAdminOauthProvidersBodyInfoUrls | Unset):
        email_path (None | str | Unset):
        username_path (None | str | Unset):
        name_first_path (None | str | Unset):
        name_last_path (None | str | Unset):
        avatar_url_template (None | str | Unset):
        avatar_overwrite (bool | Unset):
    """

    name: str
    enabled: bool
    login_only: bool
    login_bypass_two_factor: bool
    link_viewable: bool
    user_manageable: bool
    basic_auth: bool
    client_id: str
    auth_url: str
    token_url: str
    info_url: str
    scopes: list[str]
    identifier_path: str
    description: None | str | Unset = UNSET
    pkce: bool | Unset = UNSET
    client_secret: None | str | Unset = UNSET
    info_urls: PostApiAdminOauthProvidersBodyInfoUrls | Unset = UNSET
    email_path: None | str | Unset = UNSET
    username_path: None | str | Unset = UNSET
    name_first_path: None | str | Unset = UNSET
    name_last_path: None | str | Unset = UNSET
    avatar_url_template: None | str | Unset = UNSET
    avatar_overwrite: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        login_only = self.login_only

        login_bypass_two_factor = self.login_bypass_two_factor

        link_viewable = self.link_viewable

        user_manageable = self.user_manageable

        basic_auth = self.basic_auth

        client_id = self.client_id

        auth_url = self.auth_url

        token_url = self.token_url

        info_url = self.info_url

        scopes = self.scopes

        identifier_path = self.identifier_path

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        pkce = self.pkce

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        info_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.info_urls, Unset):
            info_urls = self.info_urls.to_dict()

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

        avatar_overwrite = self.avatar_overwrite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "enabled": enabled,
                "login_only": login_only,
                "login_bypass_two_factor": login_bypass_two_factor,
                "link_viewable": link_viewable,
                "user_manageable": user_manageable,
                "basic_auth": basic_auth,
                "client_id": client_id,
                "auth_url": auth_url,
                "token_url": token_url,
                "info_url": info_url,
                "scopes": scopes,
                "identifier_path": identifier_path,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if pkce is not UNSET:
            field_dict["pkce"] = pkce
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if info_urls is not UNSET:
            field_dict["info_urls"] = info_urls
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
        if avatar_overwrite is not UNSET:
            field_dict["avatar_overwrite"] = avatar_overwrite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_admin_oauth_providers_body_info_urls import PostApiAdminOauthProvidersBodyInfoUrls  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        enabled = d.pop("enabled")

        login_only = d.pop("login_only")

        login_bypass_two_factor = d.pop("login_bypass_two_factor")

        link_viewable = d.pop("link_viewable")

        user_manageable = d.pop("user_manageable")

        basic_auth = d.pop("basic_auth")

        client_id = d.pop("client_id")

        auth_url = d.pop("auth_url")

        token_url = d.pop("token_url")

        info_url = d.pop("info_url")

        scopes = cast(list[str], d.pop("scopes"))

        identifier_path = d.pop("identifier_path")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        pkce = d.pop("pkce", UNSET)

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        _info_urls = d.pop("info_urls", UNSET)
        info_urls: PostApiAdminOauthProvidersBodyInfoUrls | Unset
        if isinstance(_info_urls, Unset):
            info_urls = UNSET
        else:
            info_urls = PostApiAdminOauthProvidersBodyInfoUrls.from_dict(_info_urls)

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

        avatar_overwrite = d.pop("avatar_overwrite", UNSET)

        post_api_admin_oauth_providers_body = cls(
            name=name,
            enabled=enabled,
            login_only=login_only,
            login_bypass_two_factor=login_bypass_two_factor,
            link_viewable=link_viewable,
            user_manageable=user_manageable,
            basic_auth=basic_auth,
            client_id=client_id,
            auth_url=auth_url,
            token_url=token_url,
            info_url=info_url,
            scopes=scopes,
            identifier_path=identifier_path,
            description=description,
            pkce=pkce,
            client_secret=client_secret,
            info_urls=info_urls,
            email_path=email_path,
            username_path=username_path,
            name_first_path=name_first_path,
            name_last_path=name_last_path,
            avatar_url_template=avatar_url_template,
            avatar_overwrite=avatar_overwrite,
        )

        post_api_admin_oauth_providers_body.additional_properties = d
        return post_api_admin_oauth_providers_body

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
