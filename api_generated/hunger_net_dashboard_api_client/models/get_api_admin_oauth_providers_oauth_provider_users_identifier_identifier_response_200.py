from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_user_o_auth_link import AdminUserOAuthLink


T = TypeVar("T", bound="GetApiAdminOauthProvidersOauthProviderUsersIdentifierIdentifierResponse200")


@_attrs_define
class GetApiAdminOauthProvidersOauthProviderUsersIdentifierIdentifierResponse200:
    """
    Attributes:
        user_oauth_link (AdminUserOAuthLink):
    """

    user_oauth_link: AdminUserOAuthLink
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_oauth_link = self.user_oauth_link.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_oauth_link": user_oauth_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_user_o_auth_link import AdminUserOAuthLink  # noqa: PLC0415

        d = dict(src_dict)
        user_oauth_link = AdminUserOAuthLink.from_dict(d.pop("user_oauth_link"))

        get_api_admin_oauth_providers_oauth_provider_users_identifier_identifier_response_200 = cls(
            user_oauth_link=user_oauth_link,
        )

        get_api_admin_oauth_providers_oauth_provider_users_identifier_identifier_response_200.additional_properties = d
        return get_api_admin_oauth_providers_oauth_provider_users_identifier_identifier_response_200

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
