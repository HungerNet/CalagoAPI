from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_provider_mapping_type_type_0_type import OAuthProviderMappingTypeType0Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthProviderMappingTypeType0")


@_attrs_define
class OAuthProviderMappingTypeType0:
    """
    Attributes:
        role_uuid (UUID):
        type_ (OAuthProviderMappingTypeType0Type):
        revoke_unmatched (bool | Unset):
    """

    role_uuid: UUID
    type_: OAuthProviderMappingTypeType0Type
    revoke_unmatched: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_uuid = str(self.role_uuid)

        type_ = self.type_.value

        revoke_unmatched = self.revoke_unmatched

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_uuid": role_uuid,
                "type": type_,
            }
        )
        if revoke_unmatched is not UNSET:
            field_dict["revoke_unmatched"] = revoke_unmatched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role_uuid = UUID(d.pop("role_uuid"))

        type_ = OAuthProviderMappingTypeType0Type(d.pop("type"))

        revoke_unmatched = d.pop("revoke_unmatched", UNSET)

        o_auth_provider_mapping_type_type_0 = cls(
            role_uuid=role_uuid,
            type_=type_,
            revoke_unmatched=revoke_unmatched,
        )

        o_auth_provider_mapping_type_type_0.additional_properties = d
        return o_auth_provider_mapping_type_type_0

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
