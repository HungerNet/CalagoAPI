from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiClientServersServerSubdomainsBody")


@_attrs_define
class PostApiClientServersServerSubdomainsBody:
    """
    Attributes:
        domain_uuid (UUID):
        allocation_uuid (UUID):
        subdomain (str):
    """

    domain_uuid: UUID
    allocation_uuid: UUID
    subdomain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_uuid = str(self.domain_uuid)

        allocation_uuid = str(self.allocation_uuid)

        subdomain = self.subdomain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_uuid": domain_uuid,
                "allocation_uuid": allocation_uuid,
                "subdomain": subdomain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_uuid = UUID(d.pop("domain_uuid"))

        allocation_uuid = UUID(d.pop("allocation_uuid"))

        subdomain = d.pop("subdomain")

        post_api_client_servers_server_subdomains_body = cls(
            domain_uuid=domain_uuid,
            allocation_uuid=allocation_uuid,
            subdomain=subdomain,
        )

        post_api_client_servers_server_subdomains_body.additional_properties = d
        return post_api_client_servers_server_subdomains_body

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
