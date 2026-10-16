from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_o_auth_link import UserOAuthLink


T = TypeVar("T", bound="GetApiClientAccountOauthLinksOauthLinkResponse200")


@_attrs_define
class GetApiClientAccountOauthLinksOauthLinkResponse200:
    """
    Attributes:
        oauth_link (UserOAuthLink):
    """

    oauth_link: UserOAuthLink
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oauth_link = self.oauth_link.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oauth_link": oauth_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_o_auth_link import UserOAuthLink  # noqa: PLC0415

        d = dict(src_dict)
        oauth_link = UserOAuthLink.from_dict(d.pop("oauth_link"))

        get_api_client_account_oauth_links_oauth_link_response_200 = cls(
            oauth_link=oauth_link,
        )

        get_api_client_account_oauth_links_oauth_link_response_200.additional_properties = d
        return get_api_client_account_oauth_links_oauth_link_response_200

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
