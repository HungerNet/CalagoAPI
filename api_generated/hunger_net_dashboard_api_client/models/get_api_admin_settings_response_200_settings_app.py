from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.two_factor_method import TwoFactorMethod
from ..models.two_factor_requirement import TwoFactorRequirement
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiAdminSettingsResponse200SettingsApp")


@_attrs_define
class GetApiAdminSettingsResponse200SettingsApp:
    """
    Attributes:
        name (str):
        icon (str):
        url (str):
        additional_urls (list[str]):
        language (str):
        two_factor_requirement (TwoFactorRequirement):
        email_two_factor_enabled (bool):
        two_factor_accepted_methods (list[TwoFactorMethod]):
        email_verification_required (bool):
        session_cookie (str):
        session_duration_seconds (int):
        telemetry_enabled (bool):
        registration_enabled (bool):
        password_login_enabled (bool):
        icon_light (None | str | Unset):
        banner (None | str | Unset):
        banner_light (None | str | Unset):
    """

    name: str
    icon: str
    url: str
    additional_urls: list[str]
    language: str
    two_factor_requirement: TwoFactorRequirement
    email_two_factor_enabled: bool
    two_factor_accepted_methods: list[TwoFactorMethod]
    email_verification_required: bool
    session_cookie: str
    session_duration_seconds: int
    telemetry_enabled: bool
    registration_enabled: bool
    password_login_enabled: bool
    icon_light: None | str | Unset = UNSET
    banner: None | str | Unset = UNSET
    banner_light: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        icon = self.icon

        url = self.url

        additional_urls = self.additional_urls

        language = self.language

        two_factor_requirement = self.two_factor_requirement.value

        email_two_factor_enabled = self.email_two_factor_enabled

        two_factor_accepted_methods = []
        for two_factor_accepted_methods_item_data in self.two_factor_accepted_methods:
            two_factor_accepted_methods_item = two_factor_accepted_methods_item_data.value
            two_factor_accepted_methods.append(two_factor_accepted_methods_item)

        email_verification_required = self.email_verification_required

        session_cookie = self.session_cookie

        session_duration_seconds = self.session_duration_seconds

        telemetry_enabled = self.telemetry_enabled

        registration_enabled = self.registration_enabled

        password_login_enabled = self.password_login_enabled

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
                "name": name,
                "icon": icon,
                "url": url,
                "additional_urls": additional_urls,
                "language": language,
                "two_factor_requirement": two_factor_requirement,
                "email_two_factor_enabled": email_two_factor_enabled,
                "two_factor_accepted_methods": two_factor_accepted_methods,
                "email_verification_required": email_verification_required,
                "session_cookie": session_cookie,
                "session_duration_seconds": session_duration_seconds,
                "telemetry_enabled": telemetry_enabled,
                "registration_enabled": registration_enabled,
                "password_login_enabled": password_login_enabled,
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
        name = d.pop("name")

        icon = d.pop("icon")

        url = d.pop("url")

        additional_urls = cast(list[str], d.pop("additional_urls"))

        language = d.pop("language")

        two_factor_requirement = TwoFactorRequirement(d.pop("two_factor_requirement"))

        email_two_factor_enabled = d.pop("email_two_factor_enabled")

        two_factor_accepted_methods = []
        _two_factor_accepted_methods = d.pop("two_factor_accepted_methods")
        for two_factor_accepted_methods_item_data in _two_factor_accepted_methods:
            two_factor_accepted_methods_item = TwoFactorMethod(two_factor_accepted_methods_item_data)

            two_factor_accepted_methods.append(two_factor_accepted_methods_item)

        email_verification_required = d.pop("email_verification_required")

        session_cookie = d.pop("session_cookie")

        session_duration_seconds = d.pop("session_duration_seconds")

        telemetry_enabled = d.pop("telemetry_enabled")

        registration_enabled = d.pop("registration_enabled")

        password_login_enabled = d.pop("password_login_enabled")

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

        get_api_admin_settings_response_200_settings_app = cls(
            name=name,
            icon=icon,
            url=url,
            additional_urls=additional_urls,
            language=language,
            two_factor_requirement=two_factor_requirement,
            email_two_factor_enabled=email_two_factor_enabled,
            two_factor_accepted_methods=two_factor_accepted_methods,
            email_verification_required=email_verification_required,
            session_cookie=session_cookie,
            session_duration_seconds=session_duration_seconds,
            telemetry_enabled=telemetry_enabled,
            registration_enabled=registration_enabled,
            password_login_enabled=password_login_enabled,
            icon_light=icon_light,
            banner=banner,
            banner_light=banner_light,
        )

        get_api_admin_settings_response_200_settings_app.additional_properties = d
        return get_api_admin_settings_response_200_settings_app

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
