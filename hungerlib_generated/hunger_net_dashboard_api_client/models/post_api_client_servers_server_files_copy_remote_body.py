from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_client_servers_server_files_copy_remote_body_files_item import (
        PostApiClientServersServerFilesCopyRemoteBodyFilesItem,
    )


T = TypeVar("T", bound="PostApiClientServersServerFilesCopyRemoteBody")


@_attrs_define
class PostApiClientServersServerFilesCopyRemoteBody:
    """
    Attributes:
        files (list[PostApiClientServersServerFilesCopyRemoteBodyFilesItem]):
        destination (str):
        destination_server (str):  Example: 123e4567-e89b-12d3-a456-426614174000.
        root (str | Unset):  Default: '/'.
        foreground (bool | Unset):
    """

    files: list[PostApiClientServersServerFilesCopyRemoteBodyFilesItem]
    destination: str
    destination_server: str
    root: str | Unset = "/"
    foreground: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        destination = self.destination

        destination_server = self.destination_server

        root = self.root

        foreground = self.foreground

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "destination": destination,
                "destination_server": destination_server,
            }
        )
        if root is not UNSET:
            field_dict["root"] = root
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_client_servers_server_files_copy_remote_body_files_item import (
            PostApiClientServersServerFilesCopyRemoteBodyFilesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = PostApiClientServersServerFilesCopyRemoteBodyFilesItem.from_dict(files_item_data)

            files.append(files_item)

        destination = d.pop("destination")

        destination_server = d.pop("destination_server")

        root = d.pop("root", UNSET)

        foreground = d.pop("foreground", UNSET)

        post_api_client_servers_server_files_copy_remote_body = cls(
            files=files,
            destination=destination,
            destination_server=destination_server,
            root=root,
            foreground=foreground,
        )

        post_api_client_servers_server_files_copy_remote_body.additional_properties = d
        return post_api_client_servers_server_files_copy_remote_body

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
