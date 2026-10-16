from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_auth_login_response_200_type_0_type import PostApiAuthLoginResponse200Type0Type

if TYPE_CHECKING:
    from ..models.full_user import FullUser


T = TypeVar("T", bound="PostApiAuthLoginResponse200Type0")


@_attrs_define
class PostApiAuthLoginResponse200Type0:
    """
    Attributes:
        user (FullUser):
        type_ (PostApiAuthLoginResponse200Type0Type):
    """

    user: FullUser
    type_: PostApiAuthLoginResponse200Type0Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.full_user import FullUser  # noqa: PLC0415

        d = dict(src_dict)
        user = FullUser.from_dict(d.pop("user"))

        type_ = PostApiAuthLoginResponse200Type0Type(d.pop("type"))

        post_api_auth_login_response_200_type_0 = cls(
            user=user,
            type_=type_,
        )

        post_api_auth_login_response_200_type_0.additional_properties = d
        return post_api_auth_login_response_200_type_0

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
