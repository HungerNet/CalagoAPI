from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAdminUsersUserOauthLinksBody")


@_attrs_define
class PostApiAdminUsersUserOauthLinksBody:
    """
    Attributes:
        oauth_provider_uuid (UUID):
        identifier (str):
    """

    oauth_provider_uuid: UUID
    identifier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oauth_provider_uuid = str(self.oauth_provider_uuid)

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oauth_provider_uuid": oauth_provider_uuid,
                "identifier": identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        oauth_provider_uuid = UUID(d.pop("oauth_provider_uuid"))

        identifier = d.pop("identifier")

        post_api_admin_users_user_oauth_links_body = cls(
            oauth_provider_uuid=oauth_provider_uuid,
            identifier=identifier,
        )

        post_api_admin_users_user_oauth_links_body.additional_properties = d
        return post_api_admin_users_user_oauth_links_body

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
