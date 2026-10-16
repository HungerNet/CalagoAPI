from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiClientAccountTwoFactorResponse200")


@_attrs_define
class PostApiClientAccountTwoFactorResponse200:
    """
    Attributes:
        recovery_codes (list[str]):
    """

    recovery_codes: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recovery_codes = self.recovery_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recovery_codes": recovery_codes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recovery_codes = cast(list[str], d.pop("recovery_codes"))

        post_api_client_account_two_factor_response_200 = cls(
            recovery_codes=recovery_codes,
        )

        post_api_client_account_two_factor_response_200.additional_properties = d
        return post_api_client_account_two_factor_response_200

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
