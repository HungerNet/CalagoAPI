from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_o_auth_provider import AdminOAuthProvider


T = TypeVar("T", bound="PostApiAdminOauthProvidersOauthProviderDuplicateResponse200")


@_attrs_define
class PostApiAdminOauthProvidersOauthProviderDuplicateResponse200:
    """
    Attributes:
        oauth_provider (AdminOAuthProvider):
    """

    oauth_provider: AdminOAuthProvider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oauth_provider = self.oauth_provider.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oauth_provider": oauth_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_o_auth_provider import AdminOAuthProvider  # noqa: PLC0415

        d = dict(src_dict)
        oauth_provider = AdminOAuthProvider.from_dict(d.pop("oauth_provider"))

        post_api_admin_oauth_providers_oauth_provider_duplicate_response_200 = cls(
            oauth_provider=oauth_provider,
        )

        post_api_admin_oauth_providers_oauth_provider_duplicate_response_200.additional_properties = d
        return post_api_admin_oauth_providers_oauth_provider_duplicate_response_200

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
