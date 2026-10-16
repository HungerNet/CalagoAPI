from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchApiClientServersServerSubdomainsSubdomainBody")


@_attrs_define
class PatchApiClientServersServerSubdomainsSubdomainBody:
    """
    Attributes:
        allocation_uuid (UUID):
    """

    allocation_uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocation_uuid = str(self.allocation_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allocation_uuid": allocation_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allocation_uuid = UUID(d.pop("allocation_uuid"))

        patch_api_client_servers_server_subdomains_subdomain_body = cls(
            allocation_uuid=allocation_uuid,
        )

        patch_api_client_servers_server_subdomains_subdomain_body.additional_properties = d
        return patch_api_client_servers_server_subdomains_subdomain_body

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
