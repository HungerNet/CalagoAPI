from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.captcha_provider_type_2_type import CaptchaProviderType2Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptchaProviderType2")


@_attrs_define
class CaptchaProviderType2:
    """
    Attributes:
        v3 (bool):
        site_key (str):
        secret_key (str):
        type_ (CaptchaProviderType2Type):
        threshold (float | Unset):
    """

    v3: bool
    site_key: str
    secret_key: str
    type_: CaptchaProviderType2Type
    threshold: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        v3 = self.v3

        site_key = self.site_key

        secret_key = self.secret_key

        type_ = self.type_.value

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "v3": v3,
                "site_key": site_key,
                "secret_key": secret_key,
                "type": type_,
            }
        )
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        v3 = d.pop("v3")

        site_key = d.pop("site_key")

        secret_key = d.pop("secret_key")

        type_ = CaptchaProviderType2Type(d.pop("type"))

        threshold = d.pop("threshold", UNSET)

        captcha_provider_type_2 = cls(
            v3=v3,
            site_key=site_key,
            secret_key=secret_key,
            type_=type_,
            threshold=threshold,
        )

        captcha_provider_type_2.additional_properties = d
        return captcha_provider_type_2

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
