from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiClientAccountSecurityKeysSecurityKeyChallengeResponse200")


@_attrs_define
class PostApiClientAccountSecurityKeysSecurityKeyChallengeResponse200:
    """
    Attributes:
        credential_id (str):
    """

    credential_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credential_id": credential_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_id = d.pop("credential_id")

        post_api_client_account_security_keys_security_key_challenge_response_200 = cls(
            credential_id=credential_id,
        )

        post_api_client_account_security_keys_security_key_challenge_response_200.additional_properties = d
        return post_api_client_account_security_keys_security_key_challenge_response_200

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
