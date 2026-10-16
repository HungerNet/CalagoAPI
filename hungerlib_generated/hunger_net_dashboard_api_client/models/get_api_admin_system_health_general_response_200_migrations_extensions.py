from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_health_general_response_200_migrations_extensions_additional_property import (
        GetApiAdminSystemHealthGeneralResponse200MigrationsExtensionsAdditionalProperty,
    )


T = TypeVar("T", bound="GetApiAdminSystemHealthGeneralResponse200MigrationsExtensions")


@_attrs_define
class GetApiAdminSystemHealthGeneralResponse200MigrationsExtensions:
    additional_properties: dict[
        str, GetApiAdminSystemHealthGeneralResponse200MigrationsExtensionsAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_health_general_response_200_migrations_extensions_additional_property import (
            GetApiAdminSystemHealthGeneralResponse200MigrationsExtensionsAdditionalProperty,  # noqa: PLC0415
        )

        d = dict(src_dict)
        get_api_admin_system_health_general_response_200_migrations_extensions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                GetApiAdminSystemHealthGeneralResponse200MigrationsExtensionsAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        get_api_admin_system_health_general_response_200_migrations_extensions.additional_properties = (
            additional_properties
        )
        return get_api_admin_system_health_general_response_200_migrations_extensions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GetApiAdminSystemHealthGeneralResponse200MigrationsExtensionsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: GetApiAdminSystemHealthGeneralResponse200MigrationsExtensionsAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
