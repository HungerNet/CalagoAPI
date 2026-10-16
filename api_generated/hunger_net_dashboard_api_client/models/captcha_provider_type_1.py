from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.captcha_provider_type_1_type import CaptchaProviderType1Type

T = TypeVar("T", bound="CaptchaProviderType1")


@_attrs_define
class CaptchaProviderType1:
    """
    Attributes:
        site_key (str):
        secret_key (str):
        type_ (CaptchaProviderType1Type):
    """

    site_key: str
    secret_key: str
    type_: CaptchaProviderType1Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_key = self.site_key

        secret_key = self.secret_key

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site_key": site_key,
                "secret_key": secret_key,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_key = d.pop("site_key")

        secret_key = d.pop("secret_key")

        type_ = CaptchaProviderType1Type(d.pop("type"))

        captcha_provider_type_1 = cls(
            site_key=site_key,
            secret_key=secret_key,
            type_=type_,
        )

        captcha_provider_type_1.additional_properties = d
        return captcha_provider_type_1

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
