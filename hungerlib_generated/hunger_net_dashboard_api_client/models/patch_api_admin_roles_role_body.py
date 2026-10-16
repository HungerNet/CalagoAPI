from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiAdminRolesRoleBody")


@_attrs_define
class PatchApiAdminRolesRoleBody:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        require_two_factor (bool | None | Unset):
        admin_permissions (list[str] | None | Unset):
        server_permissions (list[str] | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    require_two_factor: bool | None | Unset = UNSET
    admin_permissions: list[str] | None | Unset = UNSET
    server_permissions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        require_two_factor: bool | None | Unset
        if isinstance(self.require_two_factor, Unset):
            require_two_factor = UNSET
        else:
            require_two_factor = self.require_two_factor

        admin_permissions: list[str] | None | Unset
        if isinstance(self.admin_permissions, Unset):
            admin_permissions = UNSET
        elif isinstance(self.admin_permissions, list):
            admin_permissions = self.admin_permissions

        else:
            admin_permissions = self.admin_permissions

        server_permissions: list[str] | None | Unset
        if isinstance(self.server_permissions, Unset):
            server_permissions = UNSET
        elif isinstance(self.server_permissions, list):
            server_permissions = self.server_permissions

        else:
            server_permissions = self.server_permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if require_two_factor is not UNSET:
            field_dict["require_two_factor"] = require_two_factor
        if admin_permissions is not UNSET:
            field_dict["admin_permissions"] = admin_permissions
        if server_permissions is not UNSET:
            field_dict["server_permissions"] = server_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_require_two_factor(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        require_two_factor = _parse_require_two_factor(d.pop("require_two_factor", UNSET))

        def _parse_admin_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                admin_permissions_type_0 = cast(list[str], data)

                return admin_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        admin_permissions = _parse_admin_permissions(d.pop("admin_permissions", UNSET))

        def _parse_server_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                server_permissions_type_0 = cast(list[str], data)

                return server_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        server_permissions = _parse_server_permissions(d.pop("server_permissions", UNSET))

        patch_api_admin_roles_role_body = cls(
            name=name,
            description=description,
            require_two_factor=require_two_factor,
            admin_permissions=admin_permissions,
            server_permissions=server_permissions,
        )

        patch_api_admin_roles_role_body.additional_properties = d
        return patch_api_admin_roles_role_body

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
