from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminSystemHealthGeneralResponse200MigrationsExtensionsAdditionalProperty")


@_attrs_define
class GetApiAdminSystemHealthGeneralResponse200MigrationsExtensionsAdditionalProperty:
    """
    Attributes:
        total (int):
        applied (int):
    """

    total: int
    applied: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        applied = self.applied

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "applied": applied,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        applied = d.pop("applied")

        get_api_admin_system_health_general_response_200_migrations_extensions_additional_property = cls(
            total=total,
            applied=applied,
        )

        get_api_admin_system_health_general_response_200_migrations_extensions_additional_property.additional_properties = d
        return get_api_admin_system_health_general_response_200_migrations_extensions_additional_property

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
