from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TundraStatus")


@_attrs_define
class TundraStatus:
    """What a node reports about the tundra mesh daemon it manages. Hand-written rather than
    generated because the panel drives these routes directly, not through the shim.

        Attributes:
            supported (bool): False covers both a node that cannot run the mesh and one with it turned off.
            connected (bool):
            epoch (int | None | Unset):
    """

    supported: bool
    connected: bool
    epoch: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        supported = self.supported

        connected = self.connected

        epoch: int | None | Unset
        if isinstance(self.epoch, Unset):
            epoch = UNSET
        else:
            epoch = self.epoch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supported": supported,
                "connected": connected,
            }
        )
        if epoch is not UNSET:
            field_dict["epoch"] = epoch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supported = d.pop("supported")

        connected = d.pop("connected")

        def _parse_epoch(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        epoch = _parse_epoch(d.pop("epoch", UNSET))

        tundra_status = cls(
            supported=supported,
            connected=connected,
            epoch=epoch,
        )

        tundra_status.additional_properties = d
        return tundra_status

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
