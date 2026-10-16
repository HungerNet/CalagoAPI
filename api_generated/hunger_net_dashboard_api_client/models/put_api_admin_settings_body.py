from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.captcha_provider_type_0 import CaptchaProviderType0
    from ..models.captcha_provider_type_1 import CaptchaProviderType1
    from ..models.captcha_provider_type_2 import CaptchaProviderType2
    from ..models.captcha_provider_type_3 import CaptchaProviderType3
    from ..models.captcha_provider_type_4 import CaptchaProviderType4
    from ..models.captcha_provider_type_5 import CaptchaProviderType5
    from ..models.mail_mode_type_0 import MailModeType0
    from ..models.mail_mode_type_1 import MailModeType1
    from ..models.mail_mode_type_2 import MailModeType2
    from ..models.mail_mode_type_3 import MailModeType3
    from ..models.put_api_admin_settings_body_activity_type_1 import PutApiAdminSettingsBodyActivityType1
    from ..models.put_api_admin_settings_body_app_type_1 import PutApiAdminSettingsBodyAppType1
    from ..models.put_api_admin_settings_body_metadata_type_1 import PutApiAdminSettingsBodyMetadataType1
    from ..models.put_api_admin_settings_body_ratelimits_type_1 import PutApiAdminSettingsBodyRatelimitsType1
    from ..models.put_api_admin_settings_body_server_type_1 import PutApiAdminSettingsBodyServerType1
    from ..models.put_api_admin_settings_body_user_type_1 import PutApiAdminSettingsBodyUserType1
    from ..models.put_api_admin_settings_body_webauthn_type_1 import PutApiAdminSettingsBodyWebauthnType1
    from ..models.storage_driver_type_0 import StorageDriverType0
    from ..models.storage_driver_type_1 import StorageDriverType1


T = TypeVar("T", bound="PutApiAdminSettingsBody")


@_attrs_define
class PutApiAdminSettingsBody:
    """
    Attributes:
        oobe_step (None | str | Unset):
        storage_driver (None | StorageDriverType0 | StorageDriverType1 | Unset):
        mail_mode (MailModeType0 | MailModeType1 | MailModeType2 | MailModeType3 | None | Unset):
        captcha_provider (CaptchaProviderType0 | CaptchaProviderType1 | CaptchaProviderType2 | CaptchaProviderType3 |
            CaptchaProviderType4 | CaptchaProviderType5 | None | Unset):
        app (None | PutApiAdminSettingsBodyAppType1 | Unset):
        metadata (None | PutApiAdminSettingsBodyMetadataType1 | Unset):
        webauthn (None | PutApiAdminSettingsBodyWebauthnType1 | Unset):
        server (None | PutApiAdminSettingsBodyServerType1 | Unset):
        user (None | PutApiAdminSettingsBodyUserType1 | Unset):
        activity (None | PutApiAdminSettingsBodyActivityType1 | Unset):
        ratelimits (None | PutApiAdminSettingsBodyRatelimitsType1 | Unset):
    """

    oobe_step: None | str | Unset = UNSET
    storage_driver: None | StorageDriverType0 | StorageDriverType1 | Unset = UNSET
    mail_mode: MailModeType0 | MailModeType1 | MailModeType2 | MailModeType3 | None | Unset = UNSET
    captcha_provider: (
        CaptchaProviderType0
        | CaptchaProviderType1
        | CaptchaProviderType2
        | CaptchaProviderType3
        | CaptchaProviderType4
        | CaptchaProviderType5
        | None
        | Unset
    ) = UNSET
    app: None | PutApiAdminSettingsBodyAppType1 | Unset = UNSET
    metadata: None | PutApiAdminSettingsBodyMetadataType1 | Unset = UNSET
    webauthn: None | PutApiAdminSettingsBodyWebauthnType1 | Unset = UNSET
    server: None | PutApiAdminSettingsBodyServerType1 | Unset = UNSET
    user: None | PutApiAdminSettingsBodyUserType1 | Unset = UNSET
    activity: None | PutApiAdminSettingsBodyActivityType1 | Unset = UNSET
    ratelimits: None | PutApiAdminSettingsBodyRatelimitsType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.captcha_provider_type_0 import CaptchaProviderType0  # noqa: PLC0415
        from ..models.captcha_provider_type_1 import CaptchaProviderType1  # noqa: PLC0415
        from ..models.captcha_provider_type_2 import CaptchaProviderType2  # noqa: PLC0415
        from ..models.captcha_provider_type_3 import CaptchaProviderType3  # noqa: PLC0415
        from ..models.captcha_provider_type_4 import CaptchaProviderType4  # noqa: PLC0415
        from ..models.captcha_provider_type_5 import CaptchaProviderType5  # noqa: PLC0415
        from ..models.mail_mode_type_0 import MailModeType0  # noqa: PLC0415
        from ..models.mail_mode_type_1 import MailModeType1  # noqa: PLC0415
        from ..models.mail_mode_type_2 import MailModeType2  # noqa: PLC0415
        from ..models.mail_mode_type_3 import MailModeType3  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_activity_type_1 import PutApiAdminSettingsBodyActivityType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_app_type_1 import PutApiAdminSettingsBodyAppType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_metadata_type_1 import PutApiAdminSettingsBodyMetadataType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_ratelimits_type_1 import PutApiAdminSettingsBodyRatelimitsType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_server_type_1 import PutApiAdminSettingsBodyServerType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_user_type_1 import PutApiAdminSettingsBodyUserType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_webauthn_type_1 import PutApiAdminSettingsBodyWebauthnType1  # noqa: PLC0415
        from ..models.storage_driver_type_0 import StorageDriverType0  # noqa: PLC0415
        from ..models.storage_driver_type_1 import StorageDriverType1  # noqa: PLC0415

        oobe_step: None | str | Unset
        if isinstance(self.oobe_step, Unset):
            oobe_step = UNSET
        else:
            oobe_step = self.oobe_step

        storage_driver: dict[str, Any] | None | Unset
        if isinstance(self.storage_driver, Unset):
            storage_driver = UNSET
        elif isinstance(self.storage_driver, StorageDriverType0):
            storage_driver = self.storage_driver.to_dict()
        elif isinstance(self.storage_driver, StorageDriverType1):
            storage_driver = self.storage_driver.to_dict()
        else:
            storage_driver = self.storage_driver

        mail_mode: dict[str, Any] | None | Unset
        if isinstance(self.mail_mode, Unset):
            mail_mode = UNSET
        elif isinstance(self.mail_mode, MailModeType0):
            mail_mode = self.mail_mode.to_dict()
        elif isinstance(self.mail_mode, MailModeType1):
            mail_mode = self.mail_mode.to_dict()
        elif isinstance(self.mail_mode, MailModeType2):
            mail_mode = self.mail_mode.to_dict()
        elif isinstance(self.mail_mode, MailModeType3):
            mail_mode = self.mail_mode.to_dict()
        else:
            mail_mode = self.mail_mode

        captcha_provider: dict[str, Any] | None | Unset
        if isinstance(self.captcha_provider, Unset):
            captcha_provider = UNSET
        elif isinstance(self.captcha_provider, CaptchaProviderType0):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType1):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType2):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType3):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType4):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType5):
            captcha_provider = self.captcha_provider.to_dict()
        else:
            captcha_provider = self.captcha_provider

        app: dict[str, Any] | None | Unset
        if isinstance(self.app, Unset):
            app = UNSET
        elif isinstance(self.app, PutApiAdminSettingsBodyAppType1):
            app = self.app.to_dict()
        else:
            app = self.app

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PutApiAdminSettingsBodyMetadataType1):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        webauthn: dict[str, Any] | None | Unset
        if isinstance(self.webauthn, Unset):
            webauthn = UNSET
        elif isinstance(self.webauthn, PutApiAdminSettingsBodyWebauthnType1):
            webauthn = self.webauthn.to_dict()
        else:
            webauthn = self.webauthn

        server: dict[str, Any] | None | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        elif isinstance(self.server, PutApiAdminSettingsBodyServerType1):
            server = self.server.to_dict()
        else:
            server = self.server

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, PutApiAdminSettingsBodyUserType1):
            user = self.user.to_dict()
        else:
            user = self.user

        activity: dict[str, Any] | None | Unset
        if isinstance(self.activity, Unset):
            activity = UNSET
        elif isinstance(self.activity, PutApiAdminSettingsBodyActivityType1):
            activity = self.activity.to_dict()
        else:
            activity = self.activity

        ratelimits: dict[str, Any] | None | Unset
        if isinstance(self.ratelimits, Unset):
            ratelimits = UNSET
        elif isinstance(self.ratelimits, PutApiAdminSettingsBodyRatelimitsType1):
            ratelimits = self.ratelimits.to_dict()
        else:
            ratelimits = self.ratelimits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oobe_step is not UNSET:
            field_dict["oobe_step"] = oobe_step
        if storage_driver is not UNSET:
            field_dict["storage_driver"] = storage_driver
        if mail_mode is not UNSET:
            field_dict["mail_mode"] = mail_mode
        if captcha_provider is not UNSET:
            field_dict["captcha_provider"] = captcha_provider
        if app is not UNSET:
            field_dict["app"] = app
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if webauthn is not UNSET:
            field_dict["webauthn"] = webauthn
        if server is not UNSET:
            field_dict["server"] = server
        if user is not UNSET:
            field_dict["user"] = user
        if activity is not UNSET:
            field_dict["activity"] = activity
        if ratelimits is not UNSET:
            field_dict["ratelimits"] = ratelimits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.captcha_provider_type_0 import CaptchaProviderType0  # noqa: PLC0415
        from ..models.captcha_provider_type_1 import CaptchaProviderType1  # noqa: PLC0415
        from ..models.captcha_provider_type_2 import CaptchaProviderType2  # noqa: PLC0415
        from ..models.captcha_provider_type_3 import CaptchaProviderType3  # noqa: PLC0415
        from ..models.captcha_provider_type_4 import CaptchaProviderType4  # noqa: PLC0415
        from ..models.captcha_provider_type_5 import CaptchaProviderType5  # noqa: PLC0415
        from ..models.mail_mode_type_0 import MailModeType0  # noqa: PLC0415
        from ..models.mail_mode_type_1 import MailModeType1  # noqa: PLC0415
        from ..models.mail_mode_type_2 import MailModeType2  # noqa: PLC0415
        from ..models.mail_mode_type_3 import MailModeType3  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_activity_type_1 import PutApiAdminSettingsBodyActivityType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_app_type_1 import PutApiAdminSettingsBodyAppType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_metadata_type_1 import PutApiAdminSettingsBodyMetadataType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_ratelimits_type_1 import PutApiAdminSettingsBodyRatelimitsType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_server_type_1 import PutApiAdminSettingsBodyServerType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_user_type_1 import PutApiAdminSettingsBodyUserType1  # noqa: PLC0415
        from ..models.put_api_admin_settings_body_webauthn_type_1 import PutApiAdminSettingsBodyWebauthnType1  # noqa: PLC0415
        from ..models.storage_driver_type_0 import StorageDriverType0  # noqa: PLC0415
        from ..models.storage_driver_type_1 import StorageDriverType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_oobe_step(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oobe_step = _parse_oobe_step(d.pop("oobe_step", UNSET))

        def _parse_storage_driver(data: object) -> None | StorageDriverType0 | StorageDriverType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_storage_driver_type_0 = StorageDriverType0.from_dict(data)

                return componentsschemas_storage_driver_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_storage_driver_type_1 = StorageDriverType1.from_dict(data)

                return componentsschemas_storage_driver_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageDriverType0 | StorageDriverType1 | Unset, data)

        storage_driver = _parse_storage_driver(d.pop("storage_driver", UNSET))

        def _parse_mail_mode(
            data: object,
        ) -> MailModeType0 | MailModeType1 | MailModeType2 | MailModeType3 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_mail_mode_type_0 = MailModeType0.from_dict(data)

                return componentsschemas_mail_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_mail_mode_type_1 = MailModeType1.from_dict(data)

                return componentsschemas_mail_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_mail_mode_type_2 = MailModeType2.from_dict(data)

                return componentsschemas_mail_mode_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_mail_mode_type_3 = MailModeType3.from_dict(data)

                return componentsschemas_mail_mode_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MailModeType0 | MailModeType1 | MailModeType2 | MailModeType3 | None | Unset, data)

        mail_mode = _parse_mail_mode(d.pop("mail_mode", UNSET))

        def _parse_captcha_provider(
            data: object,
        ) -> (
            CaptchaProviderType0
            | CaptchaProviderType1
            | CaptchaProviderType2
            | CaptchaProviderType3
            | CaptchaProviderType4
            | CaptchaProviderType5
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_captcha_provider_type_0 = CaptchaProviderType0.from_dict(data)

                return componentsschemas_captcha_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_captcha_provider_type_1 = CaptchaProviderType1.from_dict(data)

                return componentsschemas_captcha_provider_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_captcha_provider_type_2 = CaptchaProviderType2.from_dict(data)

                return componentsschemas_captcha_provider_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_captcha_provider_type_3 = CaptchaProviderType3.from_dict(data)

                return componentsschemas_captcha_provider_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_captcha_provider_type_4 = CaptchaProviderType4.from_dict(data)

                return componentsschemas_captcha_provider_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_captcha_provider_type_5 = CaptchaProviderType5.from_dict(data)

                return componentsschemas_captcha_provider_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CaptchaProviderType0
                | CaptchaProviderType1
                | CaptchaProviderType2
                | CaptchaProviderType3
                | CaptchaProviderType4
                | CaptchaProviderType5
                | None
                | Unset,
                data,
            )

        captcha_provider = _parse_captcha_provider(d.pop("captcha_provider", UNSET))

        def _parse_app(data: object) -> None | PutApiAdminSettingsBodyAppType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                app_type_1 = PutApiAdminSettingsBodyAppType1.from_dict(data)

                return app_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PutApiAdminSettingsBodyAppType1 | Unset, data)

        app = _parse_app(d.pop("app", UNSET))

        def _parse_metadata(data: object) -> None | PutApiAdminSettingsBodyMetadataType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = PutApiAdminSettingsBodyMetadataType1.from_dict(data)

                return metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PutApiAdminSettingsBodyMetadataType1 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_webauthn(data: object) -> None | PutApiAdminSettingsBodyWebauthnType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                webauthn_type_1 = PutApiAdminSettingsBodyWebauthnType1.from_dict(data)

                return webauthn_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PutApiAdminSettingsBodyWebauthnType1 | Unset, data)

        webauthn = _parse_webauthn(d.pop("webauthn", UNSET))

        def _parse_server(data: object) -> None | PutApiAdminSettingsBodyServerType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                server_type_1 = PutApiAdminSettingsBodyServerType1.from_dict(data)

                return server_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PutApiAdminSettingsBodyServerType1 | Unset, data)

        server = _parse_server(d.pop("server", UNSET))

        def _parse_user(data: object) -> None | PutApiAdminSettingsBodyUserType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = PutApiAdminSettingsBodyUserType1.from_dict(data)

                return user_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PutApiAdminSettingsBodyUserType1 | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_activity(data: object) -> None | PutApiAdminSettingsBodyActivityType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                activity_type_1 = PutApiAdminSettingsBodyActivityType1.from_dict(data)

                return activity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PutApiAdminSettingsBodyActivityType1 | Unset, data)

        activity = _parse_activity(d.pop("activity", UNSET))

        def _parse_ratelimits(data: object) -> None | PutApiAdminSettingsBodyRatelimitsType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ratelimits_type_1 = PutApiAdminSettingsBodyRatelimitsType1.from_dict(data)

                return ratelimits_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PutApiAdminSettingsBodyRatelimitsType1 | Unset, data)

        ratelimits = _parse_ratelimits(d.pop("ratelimits", UNSET))

        put_api_admin_settings_body = cls(
            oobe_step=oobe_step,
            storage_driver=storage_driver,
            mail_mode=mail_mode,
            captcha_provider=captcha_provider,
            app=app,
            metadata=metadata,
            webauthn=webauthn,
            server=server,
            user=user,
            activity=activity,
            ratelimits=ratelimits,
        )

        put_api_admin_settings_body.additional_properties = d
        return put_api_admin_settings_body

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
