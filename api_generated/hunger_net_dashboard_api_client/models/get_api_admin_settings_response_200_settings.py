from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

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
    from ..models.get_api_admin_settings_response_200_settings_activity import (
        GetApiAdminSettingsResponse200SettingsActivity,
    )
    from ..models.get_api_admin_settings_response_200_settings_app import GetApiAdminSettingsResponse200SettingsApp
    from ..models.get_api_admin_settings_response_200_settings_metadata import (
        GetApiAdminSettingsResponse200SettingsMetadata,
    )
    from ..models.get_api_admin_settings_response_200_settings_ratelimits import (
        GetApiAdminSettingsResponse200SettingsRatelimits,
    )
    from ..models.get_api_admin_settings_response_200_settings_server import (
        GetApiAdminSettingsResponse200SettingsServer,
    )
    from ..models.get_api_admin_settings_response_200_settings_user import GetApiAdminSettingsResponse200SettingsUser
    from ..models.get_api_admin_settings_response_200_settings_webauthn import (
        GetApiAdminSettingsResponse200SettingsWebauthn,
    )
    from ..models.mail_mode_type_0 import MailModeType0
    from ..models.mail_mode_type_1 import MailModeType1
    from ..models.mail_mode_type_2 import MailModeType2
    from ..models.mail_mode_type_3 import MailModeType3
    from ..models.storage_driver_type_0 import StorageDriverType0
    from ..models.storage_driver_type_1 import StorageDriverType1


T = TypeVar("T", bound="GetApiAdminSettingsResponse200Settings")


@_attrs_define
class GetApiAdminSettingsResponse200Settings:
    """
    Attributes:
        storage_driver (StorageDriverType0 | StorageDriverType1):
        mail_mode (MailModeType0 | MailModeType1 | MailModeType2 | MailModeType3):
        captcha_provider (CaptchaProviderType0 | CaptchaProviderType1 | CaptchaProviderType2 | CaptchaProviderType3 |
            CaptchaProviderType4 | CaptchaProviderType5):
        app (GetApiAdminSettingsResponse200SettingsApp):
        metadata (GetApiAdminSettingsResponse200SettingsMetadata):
        webauthn (GetApiAdminSettingsResponse200SettingsWebauthn):
        server (GetApiAdminSettingsResponse200SettingsServer):
        user (GetApiAdminSettingsResponse200SettingsUser):
        activity (GetApiAdminSettingsResponse200SettingsActivity):
        ratelimits (GetApiAdminSettingsResponse200SettingsRatelimits):
        telemetry_uuid (None | Unset | UUID):
        telemetry_cron_schedule (None | str | Unset):
        oobe_step (None | str | Unset):
    """

    storage_driver: StorageDriverType0 | StorageDriverType1
    mail_mode: MailModeType0 | MailModeType1 | MailModeType2 | MailModeType3
    captcha_provider: (
        CaptchaProviderType0
        | CaptchaProviderType1
        | CaptchaProviderType2
        | CaptchaProviderType3
        | CaptchaProviderType4
        | CaptchaProviderType5
    )
    app: GetApiAdminSettingsResponse200SettingsApp
    metadata: GetApiAdminSettingsResponse200SettingsMetadata
    webauthn: GetApiAdminSettingsResponse200SettingsWebauthn
    server: GetApiAdminSettingsResponse200SettingsServer
    user: GetApiAdminSettingsResponse200SettingsUser
    activity: GetApiAdminSettingsResponse200SettingsActivity
    ratelimits: GetApiAdminSettingsResponse200SettingsRatelimits
    telemetry_uuid: None | Unset | UUID = UNSET
    telemetry_cron_schedule: None | str | Unset = UNSET
    oobe_step: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.captcha_provider_type_0 import CaptchaProviderType0  # noqa: PLC0415
        from ..models.captcha_provider_type_1 import CaptchaProviderType1  # noqa: PLC0415
        from ..models.captcha_provider_type_2 import CaptchaProviderType2  # noqa: PLC0415
        from ..models.captcha_provider_type_3 import CaptchaProviderType3  # noqa: PLC0415
        from ..models.captcha_provider_type_4 import CaptchaProviderType4  # noqa: PLC0415
        from ..models.mail_mode_type_0 import MailModeType0  # noqa: PLC0415
        from ..models.mail_mode_type_1 import MailModeType1  # noqa: PLC0415
        from ..models.mail_mode_type_2 import MailModeType2  # noqa: PLC0415
        from ..models.storage_driver_type_0 import StorageDriverType0  # noqa: PLC0415

        storage_driver: dict[str, Any]
        if isinstance(self.storage_driver, StorageDriverType0):
            storage_driver = self.storage_driver.to_dict()
        else:
            storage_driver = self.storage_driver.to_dict()

        mail_mode: dict[str, Any]
        if isinstance(self.mail_mode, MailModeType0):
            mail_mode = self.mail_mode.to_dict()
        elif isinstance(self.mail_mode, MailModeType1):
            mail_mode = self.mail_mode.to_dict()
        elif isinstance(self.mail_mode, MailModeType2):
            mail_mode = self.mail_mode.to_dict()
        else:
            mail_mode = self.mail_mode.to_dict()

        captcha_provider: dict[str, Any]
        if isinstance(self.captcha_provider, CaptchaProviderType0):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType1):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType2):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType3):
            captcha_provider = self.captcha_provider.to_dict()
        elif isinstance(self.captcha_provider, CaptchaProviderType4):
            captcha_provider = self.captcha_provider.to_dict()
        else:
            captcha_provider = self.captcha_provider.to_dict()

        app = self.app.to_dict()

        metadata = self.metadata.to_dict()

        webauthn = self.webauthn.to_dict()

        server = self.server.to_dict()

        user = self.user.to_dict()

        activity = self.activity.to_dict()

        ratelimits = self.ratelimits.to_dict()

        telemetry_uuid: None | str | Unset
        if isinstance(self.telemetry_uuid, Unset):
            telemetry_uuid = UNSET
        elif isinstance(self.telemetry_uuid, UUID):
            telemetry_uuid = str(self.telemetry_uuid)
        else:
            telemetry_uuid = self.telemetry_uuid

        telemetry_cron_schedule: None | str | Unset
        if isinstance(self.telemetry_cron_schedule, Unset):
            telemetry_cron_schedule = UNSET
        else:
            telemetry_cron_schedule = self.telemetry_cron_schedule

        oobe_step: None | str | Unset
        if isinstance(self.oobe_step, Unset):
            oobe_step = UNSET
        else:
            oobe_step = self.oobe_step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage_driver": storage_driver,
                "mail_mode": mail_mode,
                "captcha_provider": captcha_provider,
                "app": app,
                "metadata": metadata,
                "webauthn": webauthn,
                "server": server,
                "user": user,
                "activity": activity,
                "ratelimits": ratelimits,
            }
        )
        if telemetry_uuid is not UNSET:
            field_dict["telemetry_uuid"] = telemetry_uuid
        if telemetry_cron_schedule is not UNSET:
            field_dict["telemetry_cron_schedule"] = telemetry_cron_schedule
        if oobe_step is not UNSET:
            field_dict["oobe_step"] = oobe_step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.captcha_provider_type_0 import CaptchaProviderType0  # noqa: PLC0415
        from ..models.captcha_provider_type_1 import CaptchaProviderType1  # noqa: PLC0415
        from ..models.captcha_provider_type_2 import CaptchaProviderType2  # noqa: PLC0415
        from ..models.captcha_provider_type_3 import CaptchaProviderType3  # noqa: PLC0415
        from ..models.captcha_provider_type_4 import CaptchaProviderType4  # noqa: PLC0415
        from ..models.captcha_provider_type_5 import CaptchaProviderType5  # noqa: PLC0415
        from ..models.get_api_admin_settings_response_200_settings_activity import (
            GetApiAdminSettingsResponse200SettingsActivity,  # noqa: PLC0415
        )
        from ..models.get_api_admin_settings_response_200_settings_app import GetApiAdminSettingsResponse200SettingsApp  # noqa: PLC0415
        from ..models.get_api_admin_settings_response_200_settings_metadata import (
            GetApiAdminSettingsResponse200SettingsMetadata,  # noqa: PLC0415
        )
        from ..models.get_api_admin_settings_response_200_settings_ratelimits import (
            GetApiAdminSettingsResponse200SettingsRatelimits,  # noqa: PLC0415
        )
        from ..models.get_api_admin_settings_response_200_settings_server import (
            GetApiAdminSettingsResponse200SettingsServer,  # noqa: PLC0415
        )
        from ..models.get_api_admin_settings_response_200_settings_user import (
            GetApiAdminSettingsResponse200SettingsUser,  # noqa: PLC0415
        )
        from ..models.get_api_admin_settings_response_200_settings_webauthn import (
            GetApiAdminSettingsResponse200SettingsWebauthn,  # noqa: PLC0415
        )
        from ..models.mail_mode_type_0 import MailModeType0  # noqa: PLC0415
        from ..models.mail_mode_type_1 import MailModeType1  # noqa: PLC0415
        from ..models.mail_mode_type_2 import MailModeType2  # noqa: PLC0415
        from ..models.mail_mode_type_3 import MailModeType3  # noqa: PLC0415
        from ..models.storage_driver_type_0 import StorageDriverType0  # noqa: PLC0415
        from ..models.storage_driver_type_1 import StorageDriverType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_storage_driver(data: object) -> StorageDriverType0 | StorageDriverType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_storage_driver_type_0 = StorageDriverType0.from_dict(data)

                return componentsschemas_storage_driver_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_storage_driver_type_1 = StorageDriverType1.from_dict(data)

            return componentsschemas_storage_driver_type_1

        storage_driver = _parse_storage_driver(d.pop("storage_driver"))

        def _parse_mail_mode(data: object) -> MailModeType0 | MailModeType1 | MailModeType2 | MailModeType3:
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
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_mail_mode_type_3 = MailModeType3.from_dict(data)

            return componentsschemas_mail_mode_type_3

        mail_mode = _parse_mail_mode(d.pop("mail_mode"))

        def _parse_captcha_provider(
            data: object,
        ) -> (
            CaptchaProviderType0
            | CaptchaProviderType1
            | CaptchaProviderType2
            | CaptchaProviderType3
            | CaptchaProviderType4
            | CaptchaProviderType5
        ):
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
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_captcha_provider_type_5 = CaptchaProviderType5.from_dict(data)

            return componentsschemas_captcha_provider_type_5

        captcha_provider = _parse_captcha_provider(d.pop("captcha_provider"))

        app = GetApiAdminSettingsResponse200SettingsApp.from_dict(d.pop("app"))

        metadata = GetApiAdminSettingsResponse200SettingsMetadata.from_dict(d.pop("metadata"))

        webauthn = GetApiAdminSettingsResponse200SettingsWebauthn.from_dict(d.pop("webauthn"))

        server = GetApiAdminSettingsResponse200SettingsServer.from_dict(d.pop("server"))

        user = GetApiAdminSettingsResponse200SettingsUser.from_dict(d.pop("user"))

        activity = GetApiAdminSettingsResponse200SettingsActivity.from_dict(d.pop("activity"))

        ratelimits = GetApiAdminSettingsResponse200SettingsRatelimits.from_dict(d.pop("ratelimits"))

        def _parse_telemetry_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                telemetry_uuid_type_0 = UUID(data)

                return telemetry_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        telemetry_uuid = _parse_telemetry_uuid(d.pop("telemetry_uuid", UNSET))

        def _parse_telemetry_cron_schedule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telemetry_cron_schedule = _parse_telemetry_cron_schedule(d.pop("telemetry_cron_schedule", UNSET))

        def _parse_oobe_step(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oobe_step = _parse_oobe_step(d.pop("oobe_step", UNSET))

        get_api_admin_settings_response_200_settings = cls(
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
            telemetry_uuid=telemetry_uuid,
            telemetry_cron_schedule=telemetry_cron_schedule,
            oobe_step=oobe_step,
        )

        get_api_admin_settings_response_200_settings.additional_properties = d
        return get_api_admin_settings_response_200_settings

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
