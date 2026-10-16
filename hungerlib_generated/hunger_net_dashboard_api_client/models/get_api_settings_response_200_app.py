from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.two_factor_method import TwoFactorMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiSettingsResponse200App")


@_attrs_define
class GetApiSettingsResponse200App:
    """
    Attributes:
        url (str):
        additional_urls (list[str]):
        icon (str):
        name (str):
        language (str):
        registration_enabled (bool):
        password_login_enabled (bool):
        email_two_factor_enabled (bool):
        email_verification_required (bool):
        two_factor_accepted_methods (list[TwoFactorMethod]):
        debug (bool):
        icon_light (None | str | Unset):
        banner (None | str | Unset):
        banner_light (None | str | Unset):
    """

    url: str
    additional_urls: list[str]
    icon: str
    name: str
    language: str
    registration_enabled: bool
    password_login_enabled: bool
    email_two_factor_enabled: bool
    email_verification_required: bool
    two_factor_accepted_methods: list[TwoFactorMethod]
    debug: bool
    icon_light: None | str | Unset = UNSET
    banner: None | str | Unset = UNSET
    banner_light: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        additional_urls = self.additional_urls

        icon = self.icon

        name = self.name

        language = self.language

        registration_enabled = self.registration_enabled

        password_login_enabled = self.password_login_enabled

        email_two_factor_enabled = self.email_two_factor_enabled

        email_verification_required = self.email_verification_required

        two_factor_accepted_methods = []
        for two_factor_accepted_methods_item_data in self.two_factor_accepted_methods:
            two_factor_accepted_methods_item = two_factor_accepted_methods_item_data.value
            two_factor_accepted_methods.append(two_factor_accepted_methods_item)

        debug = self.debug

        icon_light: None | str | Unset
        if isinstance(self.icon_light, Unset):
            icon_light = UNSET
        else:
            icon_light = self.icon_light

        banner: None | str | Unset
        if isinstance(self.banner, Unset):
            banner = UNSET
        else:
            banner = self.banner

        banner_light: None | str | Unset
        if isinstance(self.banner_light, Unset):
            banner_light = UNSET
        else:
            banner_light = self.banner_light

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "additional_urls": additional_urls,
                "icon": icon,
                "name": name,
                "language": language,
                "registration_enabled": registration_enabled,
                "password_login_enabled": password_login_enabled,
                "email_two_factor_enabled": email_two_factor_enabled,
                "email_verification_required": email_verification_required,
                "two_factor_accepted_methods": two_factor_accepted_methods,
                "debug": debug,
            }
        )
        if icon_light is not UNSET:
            field_dict["icon_light"] = icon_light
        if banner is not UNSET:
            field_dict["banner"] = banner
        if banner_light is not UNSET:
            field_dict["banner_light"] = banner_light

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        additional_urls = cast(list[str], d.pop("additional_urls"))

        icon = d.pop("icon")

        name = d.pop("name")

        language = d.pop("language")

        registration_enabled = d.pop("registration_enabled")

        password_login_enabled = d.pop("password_login_enabled")

        email_two_factor_enabled = d.pop("email_two_factor_enabled")

        email_verification_required = d.pop("email_verification_required")

        two_factor_accepted_methods = []
        _two_factor_accepted_methods = d.pop("two_factor_accepted_methods")
        for two_factor_accepted_methods_item_data in _two_factor_accepted_methods:
            two_factor_accepted_methods_item = TwoFactorMethod(two_factor_accepted_methods_item_data)

            two_factor_accepted_methods.append(two_factor_accepted_methods_item)

        debug = d.pop("debug")

        def _parse_icon_light(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_light = _parse_icon_light(d.pop("icon_light", UNSET))

        def _parse_banner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        banner = _parse_banner(d.pop("banner", UNSET))

        def _parse_banner_light(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        banner_light = _parse_banner_light(d.pop("banner_light", UNSET))

        get_api_settings_response_200_app = cls(
            url=url,
            additional_urls=additional_urls,
            icon=icon,
            name=name,
            language=language,
            registration_enabled=registration_enabled,
            password_login_enabled=password_login_enabled,
            email_two_factor_enabled=email_two_factor_enabled,
            email_verification_required=email_verification_required,
            two_factor_accepted_methods=two_factor_accepted_methods,
            debug=debug,
            icon_light=icon_light,
            banner=banner,
            banner_light=banner_light,
        )

        get_api_settings_response_200_app.additional_properties = d
        return get_api_settings_response_200_app

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
