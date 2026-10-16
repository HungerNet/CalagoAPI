from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.location import Location


T = TypeVar("T", bound="SystemBackupPolicyLocation")


@_attrs_define
class SystemBackupPolicyLocation:
    """
    Attributes:
        location (Location):
        created (datetime.datetime):
    """

    location: Location
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location.to_dict()

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location  # noqa: PLC0415

        d = dict(src_dict)
        location = Location.from_dict(d.pop("location"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        system_backup_policy_location = cls(
            location=location,
            created=created,
        )

        system_backup_policy_location.additional_properties = d
        return system_backup_policy_location

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
