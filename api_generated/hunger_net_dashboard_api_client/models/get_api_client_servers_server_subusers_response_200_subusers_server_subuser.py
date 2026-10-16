from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="GetApiClientServersServerSubusersResponse200SubusersServerSubuser")


@_attrs_define
class GetApiClientServersServerSubusersResponse200SubusersServerSubuser:
    """
    Attributes:
        user (User):
        permissions (list[str]):
        ignored_files (list[str]):
        created (datetime.datetime):
    """

    user: User
    permissions: list[str]
    ignored_files: list[str]
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        permissions = self.permissions

        ignored_files = self.ignored_files

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "permissions": permissions,
                "ignored_files": ignored_files,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User  # noqa: PLC0415

        d = dict(src_dict)
        user = User.from_dict(d.pop("user"))

        permissions = cast(list[str], d.pop("permissions"))

        ignored_files = cast(list[str], d.pop("ignored_files"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        get_api_client_servers_server_subusers_response_200_subusers_server_subuser = cls(
            user=user,
            permissions=permissions,
            ignored_files=ignored_files,
            created=created,
        )

        get_api_client_servers_server_subusers_response_200_subusers_server_subuser.additional_properties = d
        return get_api_client_servers_server_subusers_response_200_subusers_server_subuser

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
