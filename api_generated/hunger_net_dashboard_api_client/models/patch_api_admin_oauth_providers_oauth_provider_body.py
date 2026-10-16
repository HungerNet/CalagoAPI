from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_admin_oauth_providers_oauth_provider_body_info_urls_type_0 import (
        PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0,
    )


T = TypeVar("T", bound="PatchApiAdminOauthProvidersOauthProviderBody")


@_attrs_define
class PatchApiAdminOauthProvidersOauthProviderBody:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        enabled (bool | None | Unset):
        login_only (bool | None | Unset):
        login_bypass_two_factor (bool | None | Unset):
        link_viewable (bool | None | Unset):
        user_manageable (bool | None | Unset):
        basic_auth (bool | None | Unset):
        pkce (bool | None | Unset):
        client_id (None | str | Unset):
        client_secret (None | str | Unset):
        auth_url (None | str | Unset):
        token_url (None | str | Unset):
        info_url (None | str | Unset):
        info_urls (None | PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0 | Unset):
        scopes (list[str] | None | Unset):
        identifier_path (None | str | Unset):
        email_path (None | str | Unset):
        username_path (None | str | Unset):
        name_first_path (None | str | Unset):
        name_last_path (None | str | Unset):
        avatar_url_template (None | str | Unset):
        avatar_overwrite (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    login_only: bool | None | Unset = UNSET
    login_bypass_two_factor: bool | None | Unset = UNSET
    link_viewable: bool | None | Unset = UNSET
    user_manageable: bool | None | Unset = UNSET
    basic_auth: bool | None | Unset = UNSET
    pkce: bool | None | Unset = UNSET
    client_id: None | str | Unset = UNSET
    client_secret: None | str | Unset = UNSET
    auth_url: None | str | Unset = UNSET
    token_url: None | str | Unset = UNSET
    info_url: None | str | Unset = UNSET
    info_urls: None | PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0 | Unset = UNSET
    scopes: list[str] | None | Unset = UNSET
    identifier_path: None | str | Unset = UNSET
    email_path: None | str | Unset = UNSET
    username_path: None | str | Unset = UNSET
    name_first_path: None | str | Unset = UNSET
    name_last_path: None | str | Unset = UNSET
    avatar_url_template: None | str | Unset = UNSET
    avatar_overwrite: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_api_admin_oauth_providers_oauth_provider_body_info_urls_type_0 import (
            PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0,  # noqa: PLC0415
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        login_only: bool | None | Unset
        if isinstance(self.login_only, Unset):
            login_only = UNSET
        else:
            login_only = self.login_only

        login_bypass_two_factor: bool | None | Unset
        if isinstance(self.login_bypass_two_factor, Unset):
            login_bypass_two_factor = UNSET
        else:
            login_bypass_two_factor = self.login_bypass_two_factor

        link_viewable: bool | None | Unset
        if isinstance(self.link_viewable, Unset):
            link_viewable = UNSET
        else:
            link_viewable = self.link_viewable

        user_manageable: bool | None | Unset
        if isinstance(self.user_manageable, Unset):
            user_manageable = UNSET
        else:
            user_manageable = self.user_manageable

        basic_auth: bool | None | Unset
        if isinstance(self.basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = self.basic_auth

        pkce: bool | None | Unset
        if isinstance(self.pkce, Unset):
            pkce = UNSET
        else:
            pkce = self.pkce

        client_id: None | str | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        auth_url: None | str | Unset
        if isinstance(self.auth_url, Unset):
            auth_url = UNSET
        else:
            auth_url = self.auth_url

        token_url: None | str | Unset
        if isinstance(self.token_url, Unset):
            token_url = UNSET
        else:
            token_url = self.token_url

        info_url: None | str | Unset
        if isinstance(self.info_url, Unset):
            info_url = UNSET
        else:
            info_url = self.info_url

        info_urls: dict[str, Any] | None | Unset
        if isinstance(self.info_urls, Unset):
            info_urls = UNSET
        elif isinstance(self.info_urls, PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0):
            info_urls = self.info_urls.to_dict()
        else:
            info_urls = self.info_urls

        scopes: list[str] | None | Unset
        if isinstance(self.scopes, Unset):
            scopes = UNSET
        elif isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        identifier_path: None | str | Unset
        if isinstance(self.identifier_path, Unset):
            identifier_path = UNSET
        else:
            identifier_path = self.identifier_path

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

        avatar_overwrite: bool | None | Unset
        if isinstance(self.avatar_overwrite, Unset):
            avatar_overwrite = UNSET
        else:
            avatar_overwrite = self.avatar_overwrite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if login_only is not UNSET:
            field_dict["login_only"] = login_only
        if login_bypass_two_factor is not UNSET:
            field_dict["login_bypass_two_factor"] = login_bypass_two_factor
        if link_viewable is not UNSET:
            field_dict["link_viewable"] = link_viewable
        if user_manageable is not UNSET:
            field_dict["user_manageable"] = user_manageable
        if basic_auth is not UNSET:
            field_dict["basic_auth"] = basic_auth
        if pkce is not UNSET:
            field_dict["pkce"] = pkce
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if auth_url is not UNSET:
            field_dict["auth_url"] = auth_url
        if token_url is not UNSET:
            field_dict["token_url"] = token_url
        if info_url is not UNSET:
            field_dict["info_url"] = info_url
        if info_urls is not UNSET:
            field_dict["info_urls"] = info_urls
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if identifier_path is not UNSET:
            field_dict["identifier_path"] = identifier_path
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
        from ..models.patch_api_admin_oauth_providers_oauth_provider_body_info_urls_type_0 import (
            PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_login_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        login_only = _parse_login_only(d.pop("login_only", UNSET))

        def _parse_login_bypass_two_factor(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        login_bypass_two_factor = _parse_login_bypass_two_factor(d.pop("login_bypass_two_factor", UNSET))

        def _parse_link_viewable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        link_viewable = _parse_link_viewable(d.pop("link_viewable", UNSET))

        def _parse_user_manageable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_manageable = _parse_user_manageable(d.pop("user_manageable", UNSET))

        def _parse_basic_auth(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        basic_auth = _parse_basic_auth(d.pop("basic_auth", UNSET))

        def _parse_pkce(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        pkce = _parse_pkce(d.pop("pkce", UNSET))

        def _parse_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))

        def _parse_auth_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_url = _parse_auth_url(d.pop("auth_url", UNSET))

        def _parse_token_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token_url = _parse_token_url(d.pop("token_url", UNSET))

        def _parse_info_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        info_url = _parse_info_url(d.pop("info_url", UNSET))

        def _parse_info_urls(data: object) -> None | PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                info_urls_type_0 = PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0.from_dict(data)

                return info_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminOauthProvidersOauthProviderBodyInfoUrlsType0 | Unset, data)

        info_urls = _parse_info_urls(d.pop("info_urls", UNSET))

        def _parse_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scopes = _parse_scopes(d.pop("scopes", UNSET))

        def _parse_identifier_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier_path = _parse_identifier_path(d.pop("identifier_path", UNSET))

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

        def _parse_avatar_overwrite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        avatar_overwrite = _parse_avatar_overwrite(d.pop("avatar_overwrite", UNSET))

        patch_api_admin_oauth_providers_oauth_provider_body = cls(
            name=name,
            description=description,
            enabled=enabled,
            login_only=login_only,
            login_bypass_two_factor=login_bypass_two_factor,
            link_viewable=link_viewable,
            user_manageable=user_manageable,
            basic_auth=basic_auth,
            pkce=pkce,
            client_id=client_id,
            client_secret=client_secret,
            auth_url=auth_url,
            token_url=token_url,
            info_url=info_url,
            info_urls=info_urls,
            scopes=scopes,
            identifier_path=identifier_path,
            email_path=email_path,
            username_path=username_path,
            name_first_path=name_first_path,
            name_last_path=name_last_path,
            avatar_url_template=avatar_url_template,
            avatar_overwrite=avatar_overwrite,
        )

        patch_api_admin_oauth_providers_oauth_provider_body.additional_properties = d
        return patch_api_admin_oauth_providers_oauth_provider_body

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
