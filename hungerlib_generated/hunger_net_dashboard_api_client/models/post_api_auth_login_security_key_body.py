from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAuthLoginSecurityKeyBody")


@_attrs_define
class PostApiAuthLoginSecurityKeyBody:
    """
    Attributes:
        uuid (UUID):
        public_key_credential (Any):
    """

    uuid: UUID
    public_key_credential: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        public_key_credential = self.public_key_credential

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "public_key_credential": public_key_credential,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        public_key_credential = d.pop("public_key_credential")

        post_api_auth_login_security_key_body = cls(
            uuid=uuid,
            public_key_credential=public_key_credential,
        )

        post_api_auth_login_security_key_body.additional_properties = d
        return post_api_auth_login_security_key_body

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
