from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminRolesBody")


@_attrs_define
class PostApiAdminRolesBody:
    """
    Attributes:
        name (str):
        require_two_factor (bool):
        admin_permissions (list[str]):
        server_permissions (list[str]):
        description (None | str | Unset):
    """

    name: str
    require_two_factor: bool
    admin_permissions: list[str]
    server_permissions: list[str]
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        require_two_factor = self.require_two_factor

        admin_permissions = self.admin_permissions

        server_permissions = self.server_permissions

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "require_two_factor": require_two_factor,
                "admin_permissions": admin_permissions,
                "server_permissions": server_permissions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        require_two_factor = d.pop("require_two_factor")

        admin_permissions = cast(list[str], d.pop("admin_permissions"))

        server_permissions = cast(list[str], d.pop("server_permissions"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        post_api_admin_roles_body = cls(
            name=name,
            require_two_factor=require_two_factor,
            admin_permissions=admin_permissions,
            server_permissions=server_permissions,
            description=description,
        )

        post_api_admin_roles_body.additional_properties = d
        return post_api_admin_roles_body

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
