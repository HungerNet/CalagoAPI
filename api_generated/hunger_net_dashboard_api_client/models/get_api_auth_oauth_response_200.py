from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.o_auth_provider import OAuthProvider


T = TypeVar("T", bound="GetApiAuthOauthResponse200")


@_attrs_define
class GetApiAuthOauthResponse200:
    """
    Attributes:
        oauth_providers (list[OAuthProvider]):
    """

    oauth_providers: list[OAuthProvider]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oauth_providers = []
        for oauth_providers_item_data in self.oauth_providers:
            oauth_providers_item = oauth_providers_item_data.to_dict()
            oauth_providers.append(oauth_providers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oauth_providers": oauth_providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_provider import OAuthProvider  # noqa: PLC0415

        d = dict(src_dict)
        oauth_providers = []
        _oauth_providers = d.pop("oauth_providers")
        for oauth_providers_item_data in _oauth_providers:
            oauth_providers_item = OAuthProvider.from_dict(oauth_providers_item_data)

            oauth_providers.append(oauth_providers_item)

        get_api_auth_oauth_response_200 = cls(
            oauth_providers=oauth_providers,
        )

        get_api_auth_oauth_response_200.additional_properties = d
        return get_api_auth_oauth_response_200

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
