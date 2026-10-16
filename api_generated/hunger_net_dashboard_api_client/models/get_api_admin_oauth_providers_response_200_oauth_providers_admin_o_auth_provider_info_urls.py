from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminOauthProvidersResponse200OauthProvidersAdminOAuthProviderInfoUrls")


@_attrs_define
class GetApiAdminOauthProvidersResponse200OauthProvidersAdminOAuthProviderInfoUrls:
    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_api_admin_oauth_providers_response_200_oauth_providers_admin_o_auth_provider_info_urls = cls()

        get_api_admin_oauth_providers_response_200_oauth_providers_admin_o_auth_provider_info_urls.additional_properties = d
        return get_api_admin_oauth_providers_response_200_oauth_providers_admin_o_auth_provider_info_urls

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
