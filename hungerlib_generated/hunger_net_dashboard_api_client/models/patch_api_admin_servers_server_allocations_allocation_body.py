from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiAdminServersServerAllocationsAllocationBody")


@_attrs_define
class PatchApiAdminServersServerAllocationsAllocationBody:
    """
    Attributes:
        notes (None | str | Unset):
        primary (bool | None | Unset):
    """

    notes: None | str | Unset = UNSET
    primary: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        primary: bool | None | Unset
        if isinstance(self.primary, Unset):
            primary = UNSET
        else:
            primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notes is not UNSET:
            field_dict["notes"] = notes
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_primary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        primary = _parse_primary(d.pop("primary", UNSET))

        patch_api_admin_servers_server_allocations_allocation_body = cls(
            notes=notes,
            primary=primary,
        )

        patch_api_admin_servers_server_allocations_allocation_body.additional_properties = d
        return patch_api_admin_servers_server_allocations_allocation_body

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
