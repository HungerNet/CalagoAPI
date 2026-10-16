from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AllocationFilter")


@_attrs_define
class AllocationFilter:
    """
    Attributes:
        search (None | str | Unset):
        ip (None | str | Unset):
        port_from (int | None | Unset):
        port_to (int | None | Unset):
        assigned (bool | None | Unset):
    """

    search: None | str | Unset = UNSET
    ip: None | str | Unset = UNSET
    port_from: int | None | Unset = UNSET
    port_to: int | None | Unset = UNSET
    assigned: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        port_from: int | None | Unset
        if isinstance(self.port_from, Unset):
            port_from = UNSET
        else:
            port_from = self.port_from

        port_to: int | None | Unset
        if isinstance(self.port_to, Unset):
            port_to = UNSET
        else:
            port_to = self.port_to

        assigned: bool | None | Unset
        if isinstance(self.assigned, Unset):
            assigned = UNSET
        else:
            assigned = self.assigned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search is not UNSET:
            field_dict["search"] = search
        if ip is not UNSET:
            field_dict["ip"] = ip
        if port_from is not UNSET:
            field_dict["port_from"] = port_from
        if port_to is not UNSET:
            field_dict["port_to"] = port_to
        if assigned is not UNSET:
            field_dict["assigned"] = assigned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        def _parse_port_from(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port_from = _parse_port_from(d.pop("port_from", UNSET))

        def _parse_port_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port_to = _parse_port_to(d.pop("port_to", UNSET))

        def _parse_assigned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        assigned = _parse_assigned(d.pop("assigned", UNSET))

        allocation_filter = cls(
            search=search,
            ip=ip,
            port_from=port_from,
            port_to=port_to,
            assigned=assigned,
        )

        allocation_filter.additional_properties = d
        return allocation_filter

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
