from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.two_factor_method import TwoFactorMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthLoginCheckpointBody")


@_attrs_define
class PostApiAuthLoginCheckpointBody:
    """
    Attributes:
        code (str):
        confirmation_token (str):
        method (None | TwoFactorMethod | Unset):
    """

    code: str
    confirmation_token: str
    method: None | TwoFactorMethod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        confirmation_token = self.confirmation_token

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        elif isinstance(self.method, TwoFactorMethod):
            method = self.method.value
        else:
            method = self.method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "confirmation_token": confirmation_token,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        confirmation_token = d.pop("confirmation_token")

        def _parse_method(data: object) -> None | TwoFactorMethod | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_type_1 = TwoFactorMethod(data)

                return method_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TwoFactorMethod | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        post_api_auth_login_checkpoint_body = cls(
            code=code,
            confirmation_token=confirmation_token,
            method=method,
        )

        post_api_auth_login_checkpoint_body.additional_properties = d
        return post_api_auth_login_checkpoint_body

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
