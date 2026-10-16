from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider import Provider
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsDomainBody")


@_attrs_define
class PatchApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsDomainBody:
    """
    Attributes:
        provider (None | Provider | Unset):
        domain (None | str | Unset):
        eggs (list[UUID] | None | Unset):
        disallowed_subdomains_regexes (list[str] | None | Unset):
        provider_config (Any | Unset):
    """

    provider: None | Provider | Unset = UNSET
    domain: None | str | Unset = UNSET
    eggs: list[UUID] | None | Unset = UNSET
    disallowed_subdomains_regexes: list[str] | None | Unset = UNSET
    provider_config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, Provider):
            provider = self.provider.value
        else:
            provider = self.provider

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        eggs: list[str] | None | Unset
        if isinstance(self.eggs, Unset):
            eggs = UNSET
        elif isinstance(self.eggs, list):
            eggs = []
            for eggs_type_0_item_data in self.eggs:
                eggs_type_0_item = str(eggs_type_0_item_data)
                eggs.append(eggs_type_0_item)

        else:
            eggs = self.eggs

        disallowed_subdomains_regexes: list[str] | None | Unset
        if isinstance(self.disallowed_subdomains_regexes, Unset):
            disallowed_subdomains_regexes = UNSET
        elif isinstance(self.disallowed_subdomains_regexes, list):
            disallowed_subdomains_regexes = self.disallowed_subdomains_regexes

        else:
            disallowed_subdomains_regexes = self.disallowed_subdomains_regexes

        provider_config = self.provider_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if domain is not UNSET:
            field_dict["domain"] = domain
        if eggs is not UNSET:
            field_dict["eggs"] = eggs
        if disallowed_subdomains_regexes is not UNSET:
            field_dict["disallowed_subdomains_regexes"] = disallowed_subdomains_regexes
        if provider_config is not UNSET:
            field_dict["provider_config"] = provider_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_provider(data: object) -> None | Provider | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_type_1 = Provider(data)

                return provider_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Provider | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_eggs(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                eggs_type_0 = []
                _eggs_type_0 = data
                for eggs_type_0_item_data in _eggs_type_0:
                    eggs_type_0_item = UUID(eggs_type_0_item_data)

                    eggs_type_0.append(eggs_type_0_item)

                return eggs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        eggs = _parse_eggs(d.pop("eggs", UNSET))

        def _parse_disallowed_subdomains_regexes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disallowed_subdomains_regexes_type_0 = cast(list[str], data)

                return disallowed_subdomains_regexes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        disallowed_subdomains_regexes = _parse_disallowed_subdomains_regexes(
            d.pop("disallowed_subdomains_regexes", UNSET)
        )

        provider_config = d.pop("provider_config", UNSET)

        patch_api_admin_extensions_dev_0x7d8_subdomainmanager_domains_domain_body = cls(
            provider=provider,
            domain=domain,
            eggs=eggs,
            disallowed_subdomains_regexes=disallowed_subdomains_regexes,
            provider_config=provider_config,
        )

        patch_api_admin_extensions_dev_0x7d8_subdomainmanager_domains_domain_body.additional_properties = d
        return patch_api_admin_extensions_dev_0x7d8_subdomainmanager_domains_domain_body

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
