from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_client_servers_server_files_copy_remote_many_body_files_item import (
        PostApiClientServersServerFilesCopyRemoteManyBodyFilesItem,
    )


T = TypeVar("T", bound="PostApiClientServersServerFilesCopyRemoteManyBody")


@_attrs_define
class PostApiClientServersServerFilesCopyRemoteManyBody:
    """
    Attributes:
        files (list[PostApiClientServersServerFilesCopyRemoteManyBodyFilesItem]):
        destination (str):
        destination_servers (list[UUID]):
        root (str | Unset):  Default: '/'.
    """

    files: list[PostApiClientServersServerFilesCopyRemoteManyBodyFilesItem]
    destination: str
    destination_servers: list[UUID]
    root: str | Unset = "/"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        destination = self.destination

        destination_servers = []
        for destination_servers_item_data in self.destination_servers:
            destination_servers_item = str(destination_servers_item_data)
            destination_servers.append(destination_servers_item)

        root = self.root

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "destination": destination,
                "destination_servers": destination_servers,
            }
        )
        if root is not UNSET:
            field_dict["root"] = root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_client_servers_server_files_copy_remote_many_body_files_item import (
            PostApiClientServersServerFilesCopyRemoteManyBodyFilesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = PostApiClientServersServerFilesCopyRemoteManyBodyFilesItem.from_dict(files_item_data)

            files.append(files_item)

        destination = d.pop("destination")

        destination_servers = []
        _destination_servers = d.pop("destination_servers")
        for destination_servers_item_data in _destination_servers:
            destination_servers_item = UUID(destination_servers_item_data)

            destination_servers.append(destination_servers_item)

        root = d.pop("root", UNSET)

        post_api_client_servers_server_files_copy_remote_many_body = cls(
            files=files,
            destination=destination,
            destination_servers=destination_servers,
            root=root,
        )

        post_api_client_servers_server_files_copy_remote_many_body.additional_properties = d
        return post_api_client_servers_server_files_copy_remote_many_body

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
