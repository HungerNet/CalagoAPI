from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.two_factor_method import TwoFactorMethod
from ..models.two_factor_requirement import TwoFactorRequirement
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiAdminSettingsBodyAppType1")


@_attrs_define
class PutApiAdminSettingsBodyAppType1:
    """
    Attributes:
        name (None | str | Unset):
        icon (None | str | Unset):
        icon_light (None | str | Unset):
        banner (None | str | Unset):
        banner_light (None | str | Unset):
        url (None | str | Unset):
        additional_urls (list[str] | None | Unset):
        language (None | str | Unset):
        two_factor_requirement (None | TwoFactorRequirement | Unset):
        email_two_factor_enabled (bool | None | Unset):
        two_factor_accepted_methods (list[TwoFactorMethod] | None | Unset):
        email_verification_required (bool | None | Unset):
        session_cookie (None | str | Unset):
        session_duration_seconds (int | None | Unset):
        telemetry_enabled (bool | None | Unset):
        registration_enabled (bool | None | Unset):
        password_login_enabled (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    icon_light: None | str | Unset = UNSET
    banner: None | str | Unset = UNSET
    banner_light: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_urls: list[str] | None | Unset = UNSET
    language: None | str | Unset = UNSET
    two_factor_requirement: None | TwoFactorRequirement | Unset = UNSET
    email_two_factor_enabled: bool | None | Unset = UNSET
    two_factor_accepted_methods: list[TwoFactorMethod] | None | Unset = UNSET
    email_verification_required: bool | None | Unset = UNSET
    session_cookie: None | str | Unset = UNSET
    session_duration_seconds: int | None | Unset = UNSET
    telemetry_enabled: bool | None | Unset = UNSET
    registration_enabled: bool | None | Unset = UNSET
    password_login_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

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

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        additional_urls: list[str] | None | Unset
        if isinstance(self.additional_urls, Unset):
            additional_urls = UNSET
        elif isinstance(self.additional_urls, list):
            additional_urls = self.additional_urls

        else:
            additional_urls = self.additional_urls

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        two_factor_requirement: None | str | Unset
        if isinstance(self.two_factor_requirement, Unset):
            two_factor_requirement = UNSET
        elif isinstance(self.two_factor_requirement, TwoFactorRequirement):
            two_factor_requirement = self.two_factor_requirement.value
        else:
            two_factor_requirement = self.two_factor_requirement

        email_two_factor_enabled: bool | None | Unset
        if isinstance(self.email_two_factor_enabled, Unset):
            email_two_factor_enabled = UNSET
        else:
            email_two_factor_enabled = self.email_two_factor_enabled

        two_factor_accepted_methods: list[str] | None | Unset
        if isinstance(self.two_factor_accepted_methods, Unset):
            two_factor_accepted_methods = UNSET
        elif isinstance(self.two_factor_accepted_methods, list):
            two_factor_accepted_methods = []
            for two_factor_accepted_methods_type_0_item_data in self.two_factor_accepted_methods:
                two_factor_accepted_methods_type_0_item = two_factor_accepted_methods_type_0_item_data.value
                two_factor_accepted_methods.append(two_factor_accepted_methods_type_0_item)

        else:
            two_factor_accepted_methods = self.two_factor_accepted_methods

        email_verification_required: bool | None | Unset
        if isinstance(self.email_verification_required, Unset):
            email_verification_required = UNSET
        else:
            email_verification_required = self.email_verification_required

        session_cookie: None | str | Unset
        if isinstance(self.session_cookie, Unset):
            session_cookie = UNSET
        else:
            session_cookie = self.session_cookie

        session_duration_seconds: int | None | Unset
        if isinstance(self.session_duration_seconds, Unset):
            session_duration_seconds = UNSET
        else:
            session_duration_seconds = self.session_duration_seconds

        telemetry_enabled: bool | None | Unset
        if isinstance(self.telemetry_enabled, Unset):
            telemetry_enabled = UNSET
        else:
            telemetry_enabled = self.telemetry_enabled

        registration_enabled: bool | None | Unset
        if isinstance(self.registration_enabled, Unset):
            registration_enabled = UNSET
        else:
            registration_enabled = self.registration_enabled

        password_login_enabled: bool | None | Unset
        if isinstance(self.password_login_enabled, Unset):
            password_login_enabled = UNSET
        else:
            password_login_enabled = self.password_login_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_light is not UNSET:
            field_dict["icon_light"] = icon_light
        if banner is not UNSET:
            field_dict["banner"] = banner
        if banner_light is not UNSET:
            field_dict["banner_light"] = banner_light
        if url is not UNSET:
            field_dict["url"] = url
        if additional_urls is not UNSET:
            field_dict["additional_urls"] = additional_urls
        if language is not UNSET:
            field_dict["language"] = language
        if two_factor_requirement is not UNSET:
            field_dict["two_factor_requirement"] = two_factor_requirement
        if email_two_factor_enabled is not UNSET:
            field_dict["email_two_factor_enabled"] = email_two_factor_enabled
        if two_factor_accepted_methods is not UNSET:
            field_dict["two_factor_accepted_methods"] = two_factor_accepted_methods
        if email_verification_required is not UNSET:
            field_dict["email_verification_required"] = email_verification_required
        if session_cookie is not UNSET:
            field_dict["session_cookie"] = session_cookie
        if session_duration_seconds is not UNSET:
            field_dict["session_duration_seconds"] = session_duration_seconds
        if telemetry_enabled is not UNSET:
            field_dict["telemetry_enabled"] = telemetry_enabled
        if registration_enabled is not UNSET:
            field_dict["registration_enabled"] = registration_enabled
        if password_login_enabled is not UNSET:
            field_dict["password_login_enabled"] = password_login_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

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

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_additional_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_urls_type_0 = cast(list[str], data)

                return additional_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        additional_urls = _parse_additional_urls(d.pop("additional_urls", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_two_factor_requirement(data: object) -> None | TwoFactorRequirement | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                two_factor_requirement_type_1 = TwoFactorRequirement(data)

                return two_factor_requirement_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TwoFactorRequirement | Unset, data)

        two_factor_requirement = _parse_two_factor_requirement(d.pop("two_factor_requirement", UNSET))

        def _parse_email_two_factor_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        email_two_factor_enabled = _parse_email_two_factor_enabled(d.pop("email_two_factor_enabled", UNSET))

        def _parse_two_factor_accepted_methods(data: object) -> list[TwoFactorMethod] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                two_factor_accepted_methods_type_0 = []
                _two_factor_accepted_methods_type_0 = data
                for two_factor_accepted_methods_type_0_item_data in _two_factor_accepted_methods_type_0:
                    two_factor_accepted_methods_type_0_item = TwoFactorMethod(
                        two_factor_accepted_methods_type_0_item_data
                    )

                    two_factor_accepted_methods_type_0.append(two_factor_accepted_methods_type_0_item)

                return two_factor_accepted_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TwoFactorMethod] | None | Unset, data)

        two_factor_accepted_methods = _parse_two_factor_accepted_methods(d.pop("two_factor_accepted_methods", UNSET))

        def _parse_email_verification_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        email_verification_required = _parse_email_verification_required(d.pop("email_verification_required", UNSET))

        def _parse_session_cookie(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_cookie = _parse_session_cookie(d.pop("session_cookie", UNSET))

        def _parse_session_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        session_duration_seconds = _parse_session_duration_seconds(d.pop("session_duration_seconds", UNSET))

        def _parse_telemetry_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        telemetry_enabled = _parse_telemetry_enabled(d.pop("telemetry_enabled", UNSET))

        def _parse_registration_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        registration_enabled = _parse_registration_enabled(d.pop("registration_enabled", UNSET))

        def _parse_password_login_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        password_login_enabled = _parse_password_login_enabled(d.pop("password_login_enabled", UNSET))

        put_api_admin_settings_body_app_type_1 = cls(
            name=name,
            icon=icon,
            icon_light=icon_light,
            banner=banner,
            banner_light=banner_light,
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
        )

        put_api_admin_settings_body_app_type_1.additional_properties = d
        return put_api_admin_settings_body_app_type_1

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
