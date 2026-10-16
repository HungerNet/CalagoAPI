from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiRemoteSftpAuthResponse200")


@_attrs_define
class PostApiRemoteSftpAuthResponse200:
    """
    Attributes:
        user (UUID):
        server (UUID):
        permissions (list[str]):
        ignored_files (list[str]):
    """

    user: UUID
    server: UUID
    permissions: list[str]
    ignored_files: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = str(self.user)

        server = str(self.server)

        permissions = self.permissions

        ignored_files = self.ignored_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "server": server,
                "permissions": permissions,
                "ignored_files": ignored_files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = UUID(d.pop("user"))

        server = UUID(d.pop("server"))

        permissions = cast(list[str], d.pop("permissions"))

        ignored_files = cast(list[str], d.pop("ignored_files"))

        post_api_remote_sftp_auth_response_200 = cls(
            user=user,
            server=server,
            permissions=permissions,
            ignored_files=ignored_files,
        )

        post_api_remote_sftp_auth_response_200.additional_properties = d
        return post_api_remote_sftp_auth_response_200

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
