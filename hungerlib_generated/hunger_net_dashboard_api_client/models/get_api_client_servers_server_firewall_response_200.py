from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_rule import FirewallRule


T = TypeVar("T", bound="GetApiClientServersServerFirewallResponse200")


@_attrs_define
class GetApiClientServersServerFirewallResponse200:
    """
    Attributes:
        allocation_ports (list[int]):
        rules (list[FirewallRule]):
        supported (bool | None | Unset):
    """

    allocation_ports: list[int]
    rules: list[FirewallRule]
    supported: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocation_ports = self.allocation_ports

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        supported: bool | None | Unset
        if isinstance(self.supported, Unset):
            supported = UNSET
        else:
            supported = self.supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allocation_ports": allocation_ports,
                "rules": rules,
            }
        )
        if supported is not UNSET:
            field_dict["supported"] = supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_rule import FirewallRule  # noqa: PLC0415

        d = dict(src_dict)
        allocation_ports = cast(list[int], d.pop("allocation_ports"))

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = FirewallRule.from_dict(rules_item_data)

            rules.append(rules_item)

        def _parse_supported(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supported = _parse_supported(d.pop("supported", UNSET))

        get_api_client_servers_server_firewall_response_200 = cls(
            allocation_ports=allocation_ports,
            rules=rules,
            supported=supported,
        )

        get_api_client_servers_server_firewall_response_200.additional_properties = d
        return get_api_client_servers_server_firewall_response_200

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
