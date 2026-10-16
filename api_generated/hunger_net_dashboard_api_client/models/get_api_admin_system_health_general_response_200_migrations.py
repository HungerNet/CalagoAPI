from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_health_general_response_200_migrations_extensions import (
        GetApiAdminSystemHealthGeneralResponse200MigrationsExtensions,
    )


T = TypeVar("T", bound="GetApiAdminSystemHealthGeneralResponse200Migrations")


@_attrs_define
class GetApiAdminSystemHealthGeneralResponse200Migrations:
    """
    Attributes:
        total (int):
        applied (int):
        extensions (GetApiAdminSystemHealthGeneralResponse200MigrationsExtensions):
    """

    total: int
    applied: int
    extensions: GetApiAdminSystemHealthGeneralResponse200MigrationsExtensions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        applied = self.applied

        extensions = self.extensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "applied": applied,
                "extensions": extensions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_health_general_response_200_migrations_extensions import (
            GetApiAdminSystemHealthGeneralResponse200MigrationsExtensions,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total = d.pop("total")

        applied = d.pop("applied")

        extensions = GetApiAdminSystemHealthGeneralResponse200MigrationsExtensions.from_dict(d.pop("extensions"))

        get_api_admin_system_health_general_response_200_migrations = cls(
            total=total,
            applied=applied,
            extensions=extensions,
        )

        get_api_admin_system_health_general_response_200_migrations.additional_properties = d
        return get_api_admin_system_health_general_response_200_migrations

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
