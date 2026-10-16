from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_rule_action import FirewallRuleAction
from ..models.firewall_rule_protocol import FirewallRuleProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallRule")


@_attrs_define
class FirewallRule:
    """
    Attributes:
        action (FirewallRuleAction):
        protocols (list[FirewallRuleProtocol] | Unset):
        sources (list[str] | Unset):
        ports (list[int] | None | Unset):
        source_file (None | str | Unset):
    """

    action: FirewallRuleAction
    protocols: list[FirewallRuleProtocol] | Unset = UNSET
    sources: list[str] | Unset = UNSET
    ports: list[int] | None | Unset = UNSET
    source_file: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        protocols: list[str] | Unset = UNSET
        if not isinstance(self.protocols, Unset):
            protocols = []
            for protocols_item_data in self.protocols:
                protocols_item = protocols_item_data.value
                protocols.append(protocols_item)

        sources: list[str] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources

        ports: list[int] | None | Unset
        if isinstance(self.ports, Unset):
            ports = UNSET
        elif isinstance(self.ports, list):
            ports = self.ports

        else:
            ports = self.ports

        source_file: None | str | Unset
        if isinstance(self.source_file, Unset):
            source_file = UNSET
        else:
            source_file = self.source_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if protocols is not UNSET:
            field_dict["protocols"] = protocols
        if sources is not UNSET:
            field_dict["sources"] = sources
        if ports is not UNSET:
            field_dict["ports"] = ports
        if source_file is not UNSET:
            field_dict["source_file"] = source_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = FirewallRuleAction(d.pop("action"))

        _protocols = d.pop("protocols", UNSET)
        protocols: list[FirewallRuleProtocol] | Unset = UNSET
        if _protocols is not UNSET:
            protocols = []
            for protocols_item_data in _protocols:
                protocols_item = FirewallRuleProtocol(protocols_item_data)

                protocols.append(protocols_item)

        sources = cast(list[str], d.pop("sources", UNSET))

        def _parse_ports(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ports_type_0 = cast(list[int], data)

                return ports_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        ports = _parse_ports(d.pop("ports", UNSET))

        def _parse_source_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_file = _parse_source_file(d.pop("source_file", UNSET))

        firewall_rule = cls(
            action=action,
            protocols=protocols,
            sources=sources,
            ports=ports,
            source_file=source_file,
        )

        firewall_rule.additional_properties = d
        return firewall_rule

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
