from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domain import Domain


T = TypeVar("T", bound="GetApiClientServersServerSubdomainsDomainsResponse200")


@_attrs_define
class GetApiClientServersServerSubdomainsDomainsResponse200:
    """
    Attributes:
        domains (list[Domain]):
    """

    domains: list[Domain]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domains = []
        for domains_item_data in self.domains:
            domains_item = domains_item_data.to_dict()
            domains.append(domains_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domains": domains,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain import Domain  # noqa: PLC0415

        d = dict(src_dict)
        domains = []
        _domains = d.pop("domains")
        for domains_item_data in _domains:
            domains_item = Domain.from_dict(domains_item_data)

            domains.append(domains_item)

        get_api_client_servers_server_subdomains_domains_response_200 = cls(
            domains=domains,
        )

        get_api_client_servers_server_subdomains_domains_response_200.additional_properties = d
        return get_api_client_servers_server_subdomains_domains_response_200

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
