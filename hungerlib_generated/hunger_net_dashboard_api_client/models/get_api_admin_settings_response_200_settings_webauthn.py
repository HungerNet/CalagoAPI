from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminSettingsResponse200SettingsWebauthn")


@_attrs_define
class GetApiAdminSettingsResponse200SettingsWebauthn:
    """
    Attributes:
        enabled (bool):
        allow_discoverable (bool):
        rp_id (str):
        rp_origin (str):
        authentication_timeout_seconds (int):
        registration_timeout_seconds (int):
    """

    enabled: bool
    allow_discoverable: bool
    rp_id: str
    rp_origin: str
    authentication_timeout_seconds: int
    registration_timeout_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        allow_discoverable = self.allow_discoverable

        rp_id = self.rp_id

        rp_origin = self.rp_origin

        authentication_timeout_seconds = self.authentication_timeout_seconds

        registration_timeout_seconds = self.registration_timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "allow_discoverable": allow_discoverable,
                "rp_id": rp_id,
                "rp_origin": rp_origin,
                "authentication_timeout_seconds": authentication_timeout_seconds,
                "registration_timeout_seconds": registration_timeout_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        allow_discoverable = d.pop("allow_discoverable")

        rp_id = d.pop("rp_id")

        rp_origin = d.pop("rp_origin")

        authentication_timeout_seconds = d.pop("authentication_timeout_seconds")

        registration_timeout_seconds = d.pop("registration_timeout_seconds")

        get_api_admin_settings_response_200_settings_webauthn = cls(
            enabled=enabled,
            allow_discoverable=allow_discoverable,
            rp_id=rp_id,
            rp_origin=rp_origin,
            authentication_timeout_seconds=authentication_timeout_seconds,
            registration_timeout_seconds=registration_timeout_seconds,
        )

        get_api_admin_settings_response_200_settings_webauthn.additional_properties = d
        return get_api_admin_settings_response_200_settings_webauthn

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
