from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiAdminSettingsBodyWebauthnType1")


@_attrs_define
class PutApiAdminSettingsBodyWebauthnType1:
    """
    Attributes:
        enabled (bool | None | Unset):
        allow_discoverable (bool | None | Unset):
        rp_id (None | str | Unset):
        rp_origin (None | str | Unset):
        authentication_timeout_seconds (int | None | Unset):
        registration_timeout_seconds (int | None | Unset):
    """

    enabled: bool | None | Unset = UNSET
    allow_discoverable: bool | None | Unset = UNSET
    rp_id: None | str | Unset = UNSET
    rp_origin: None | str | Unset = UNSET
    authentication_timeout_seconds: int | None | Unset = UNSET
    registration_timeout_seconds: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        allow_discoverable: bool | None | Unset
        if isinstance(self.allow_discoverable, Unset):
            allow_discoverable = UNSET
        else:
            allow_discoverable = self.allow_discoverable

        rp_id: None | str | Unset
        if isinstance(self.rp_id, Unset):
            rp_id = UNSET
        else:
            rp_id = self.rp_id

        rp_origin: None | str | Unset
        if isinstance(self.rp_origin, Unset):
            rp_origin = UNSET
        else:
            rp_origin = self.rp_origin

        authentication_timeout_seconds: int | None | Unset
        if isinstance(self.authentication_timeout_seconds, Unset):
            authentication_timeout_seconds = UNSET
        else:
            authentication_timeout_seconds = self.authentication_timeout_seconds

        registration_timeout_seconds: int | None | Unset
        if isinstance(self.registration_timeout_seconds, Unset):
            registration_timeout_seconds = UNSET
        else:
            registration_timeout_seconds = self.registration_timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if allow_discoverable is not UNSET:
            field_dict["allow_discoverable"] = allow_discoverable
        if rp_id is not UNSET:
            field_dict["rp_id"] = rp_id
        if rp_origin is not UNSET:
            field_dict["rp_origin"] = rp_origin
        if authentication_timeout_seconds is not UNSET:
            field_dict["authentication_timeout_seconds"] = authentication_timeout_seconds
        if registration_timeout_seconds is not UNSET:
            field_dict["registration_timeout_seconds"] = registration_timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_allow_discoverable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_discoverable = _parse_allow_discoverable(d.pop("allow_discoverable", UNSET))

        def _parse_rp_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rp_id = _parse_rp_id(d.pop("rp_id", UNSET))

        def _parse_rp_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rp_origin = _parse_rp_origin(d.pop("rp_origin", UNSET))

        def _parse_authentication_timeout_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        authentication_timeout_seconds = _parse_authentication_timeout_seconds(
            d.pop("authentication_timeout_seconds", UNSET)
        )

        def _parse_registration_timeout_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        registration_timeout_seconds = _parse_registration_timeout_seconds(d.pop("registration_timeout_seconds", UNSET))

        put_api_admin_settings_body_webauthn_type_1 = cls(
            enabled=enabled,
            allow_discoverable=allow_discoverable,
            rp_id=rp_id,
            rp_origin=rp_origin,
            authentication_timeout_seconds=authentication_timeout_seconds,
            registration_timeout_seconds=registration_timeout_seconds,
        )

        put_api_admin_settings_body_webauthn_type_1.additional_properties = d
        return put_api_admin_settings_body_webauthn_type_1

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
