from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteApiAdminExtensionsManageExtensionBody")


@_attrs_define
class DeleteApiAdminExtensionsManageExtensionBody:
    """
    Attributes:
        remove_migrations (bool):
    """

    remove_migrations: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remove_migrations = self.remove_migrations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remove_migrations": remove_migrations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        remove_migrations = d.pop("remove_migrations")

        delete_api_admin_extensions_manage_extension_body = cls(
            remove_migrations=remove_migrations,
        )

        delete_api_admin_extensions_manage_extension_body.additional_properties = d
        return delete_api_admin_extensions_manage_extension_body

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
