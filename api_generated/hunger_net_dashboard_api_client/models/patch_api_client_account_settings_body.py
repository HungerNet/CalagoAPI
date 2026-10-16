from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_api_client_account_settings_body_settings import PatchApiClientAccountSettingsBodySettings


T = TypeVar("T", bound="PatchApiClientAccountSettingsBody")


@_attrs_define
class PatchApiClientAccountSettingsBody:
    """
    Attributes:
        settings (PatchApiClientAccountSettingsBodySettings):
    """

    settings: PatchApiClientAccountSettingsBodySettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_api_client_account_settings_body_settings import PatchApiClientAccountSettingsBodySettings  # noqa: PLC0415

        d = dict(src_dict)
        settings = PatchApiClientAccountSettingsBodySettings.from_dict(d.pop("settings"))

        patch_api_client_account_settings_body = cls(
            settings=settings,
        )

        patch_api_client_account_settings_body.additional_properties = d
        return patch_api_client_account_settings_body

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
