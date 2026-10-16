from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_security_key import UserSecurityKey


T = TypeVar("T", bound="PostApiClientAccountSecurityKeysResponse200")


@_attrs_define
class PostApiClientAccountSecurityKeysResponse200:
    """
    Attributes:
        security_key (UserSecurityKey):
        options (Any):
    """

    security_key: UserSecurityKey
    options: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_key = self.security_key.to_dict()

        options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "security_key": security_key,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_security_key import UserSecurityKey  # noqa: PLC0415

        d = dict(src_dict)
        security_key = UserSecurityKey.from_dict(d.pop("security_key"))

        options = d.pop("options")

        post_api_client_account_security_keys_response_200 = cls(
            security_key=security_key,
            options=options,
        )

        post_api_client_account_security_keys_response_200.additional_properties = d
        return post_api_client_account_security_keys_response_200

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
