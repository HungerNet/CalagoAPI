from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_settings_response_200_app import GetApiSettingsResponse200App
    from ..models.get_api_settings_response_200_captcha_provider_type_0 import (
        GetApiSettingsResponse200CaptchaProviderType0,
    )
    from ..models.get_api_settings_response_200_captcha_provider_type_1 import (
        GetApiSettingsResponse200CaptchaProviderType1,
    )
    from ..models.get_api_settings_response_200_captcha_provider_type_2 import (
        GetApiSettingsResponse200CaptchaProviderType2,
    )
    from ..models.get_api_settings_response_200_captcha_provider_type_3 import (
        GetApiSettingsResponse200CaptchaProviderType3,
    )
    from ..models.get_api_settings_response_200_captcha_provider_type_4 import (
        GetApiSettingsResponse200CaptchaProviderType4,
    )
    from ..models.get_api_settings_response_200_captcha_provider_type_5 import (
        GetApiSettingsResponse200CaptchaProviderType5,
    )
    from ..models.get_api_settings_response_200_server import GetApiSettingsResponse200Server
    from ..models.get_api_settings_response_200_user import GetApiSettingsResponse200User
    from ..models.get_api_settings_response_200_webauthn import GetApiSettingsResponse200Webauthn


T = TypeVar("T", bound="GetApiSettingsResponse200")


@_attrs_define
class GetApiSettingsResponse200:
    """
    Attributes:
        time (datetime.datetime):
        disabled_extensions (list[str]):
        captcha_provider (GetApiSettingsResponse200CaptchaProviderType0 | GetApiSettingsResponse200CaptchaProviderType1
            | GetApiSettingsResponse200CaptchaProviderType2 | GetApiSettingsResponse200CaptchaProviderType3 |
            GetApiSettingsResponse200CaptchaProviderType4 | GetApiSettingsResponse200CaptchaProviderType5):
        app (GetApiSettingsResponse200App):
        webauthn (GetApiSettingsResponse200Webauthn):
        server (GetApiSettingsResponse200Server):
        user (GetApiSettingsResponse200User):
        oobe_step (None | str | Unset):
    """

    time: datetime.datetime
    disabled_extensions: list[str]
    captcha_provider: (
        GetApiSettingsResponse200CaptchaProviderType0
        | GetApiSettingsResponse200CaptchaProviderType1
        | GetApiSettingsResponse200CaptchaProviderType2
        | GetApiSettingsResponse200CaptchaProviderType3
        | GetApiSettingsResponse200CaptchaProviderType4
        | GetApiSettingsResponse200CaptchaProviderType5
    )
    app: GetApiSettingsResponse200App
    webauthn: GetApiSettingsResponse200Webauthn
    server: GetApiSettingsResponse200Server
    user: GetApiSettingsResponse200User
    oobe_step: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_api_settings_response_200_captcha_provider_type_0 import (
            GetApiSettingsResponse200CaptchaProviderType0,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_1 import (
            GetApiSettingsResponse200CaptchaProviderType1,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_2 import (
            GetApiSettingsResponse200CaptchaProviderType2,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_3 import (
            GetApiSettingsResponse200CaptchaProviderType3,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_4 import (
            GetApiSettingsResponse200CaptchaProviderType4,  # noqa: PLC0415
        )

        time = self.time.isoformat()

        disabled_extensions = self.disabled_extensions

        captcha_provider: dict[str, Any]
        if isinstance(self.captcha_provider, GetApiSettingsResponse200CaptchaProviderType0):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, GetApiSettingsResponse200CaptchaProviderType1):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, GetApiSettingsResponse200CaptchaProviderType2):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, GetApiSettingsResponse200CaptchaProviderType3):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, GetApiSettingsResponse200CaptchaProviderType4):
            captcha_provider = self.captcha_provider.to_dict()
        else:
            captcha_provider = self.captcha_provider.to_dict()

        app = self.app.to_dict()

        webauthn = self.webauthn.to_dict()

        server = self.server.to_dict()

        user = self.user.to_dict()

        oobe_step: None | str | Unset
        if isinstance(self.oobe_step, Unset):
            oobe_step = UNSET
        else:
            oobe_step = self.oobe_step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "disabled_extensions": disabled_extensions,
                "captcha_provider": captcha_provider,
                "app": app,
                "webauthn": webauthn,
                "server": server,
                "user": user,
            }
        )
        if oobe_step is not UNSET:
            field_dict["oobe_step"] = oobe_step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_settings_response_200_app import GetApiSettingsResponse200App  # noqa: PLC0415
        from ..models.get_api_settings_response_200_captcha_provider_type_0 import (
            GetApiSettingsResponse200CaptchaProviderType0,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_1 import (
            GetApiSettingsResponse200CaptchaProviderType1,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_2 import (
            GetApiSettingsResponse200CaptchaProviderType2,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_3 import (
            GetApiSettingsResponse200CaptchaProviderType3,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_4 import (
            GetApiSettingsResponse200CaptchaProviderType4,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_captcha_provider_type_5 import (
            GetApiSettingsResponse200CaptchaProviderType5,  # noqa: PLC0415
        )
        from ..models.get_api_settings_response_200_server import GetApiSettingsResponse200Server  # noqa: PLC0415
        from ..models.get_api_settings_response_200_user import GetApiSettingsResponse200User  # noqa: PLC0415
        from ..models.get_api_settings_response_200_webauthn import GetApiSettingsResponse200Webauthn  # noqa: PLC0415

        d = dict(src_dict)
        time = datetime.datetime.fromisoformat(d.pop("time"))

        disabled_extensions = cast(list[str], d.pop("disabled_extensions"))

        def _parse_captcha_provider(
            data: object,
        ) -> (
            GetApiSettingsResponse200CaptchaProviderType0
            | GetApiSettingsResponse200CaptchaProviderType1
            | GetApiSettingsResponse200CaptchaProviderType2
            | GetApiSettingsResponse200CaptchaProviderType3
            | GetApiSettingsResponse200CaptchaProviderType4
            | GetApiSettingsResponse200CaptchaProviderType5
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                captcha_provider_type_0 = GetApiSettingsResponse200CaptchaProviderType0.from_dict(data)

                return captcha_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                captcha_provider_type_1 = GetApiSettingsResponse200CaptchaProviderType1.from_dict(data)

                return captcha_provider_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                captcha_provider_type_2 = GetApiSettingsResponse200CaptchaProviderType2.from_dict(data)

                return captcha_provider_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                captcha_provider_type_3 = GetApiSettingsResponse200CaptchaProviderType3.from_dict(data)

                return captcha_provider_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                captcha_provider_type_4 = GetApiSettingsResponse200CaptchaProviderType4.from_dict(data)

                return captcha_provider_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            captcha_provider_type_5 = GetApiSettingsResponse200CaptchaProviderType5.from_dict(data)

            return captcha_provider_type_5

        captcha_provider = _parse_captcha_provider(d.pop("captcha_provider"))

        app = GetApiSettingsResponse200App.from_dict(d.pop("app"))

        webauthn = GetApiSettingsResponse200Webauthn.from_dict(d.pop("webauthn"))

        server = GetApiSettingsResponse200Server.from_dict(d.pop("server"))

        user = GetApiSettingsResponse200User.from_dict(d.pop("user"))

        def _parse_oobe_step(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oobe_step = _parse_oobe_step(d.pop("oobe_step", UNSET))

        get_api_settings_response_200 = cls(
            time=time,
            disabled_extensions=disabled_extensions,
            captcha_provider=captcha_provider,
            app=app,
            webauthn=webauthn,
            server=server,
            user=user,
            oobe_step=oobe_step,
        )

        get_api_settings_response_200.additional_properties = d
        return get_api_settings_response_200

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
