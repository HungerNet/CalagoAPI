from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_client_servers_server_files_copy_many_body_files_item import (
        PostApiClientServersServerFilesCopyManyBodyFilesItem,
    )


T = TypeVar("T", bound="PostApiClientServersServerFilesCopyManyBody")


@_attrs_define
class PostApiClientServersServerFilesCopyManyBody:
    """
    Attributes:
        files (list[PostApiClientServersServerFilesCopyManyBodyFilesItem]):
        root (str | Unset):  Default: '/'.
        overwrite (bool | Unset):
        foreground (bool | Unset):
    """

    files: list[PostApiClientServersServerFilesCopyManyBodyFilesItem]
    root: str | Unset = "/"
    overwrite: bool | Unset = UNSET
    foreground: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        root = self.root

        overwrite = self.overwrite

        foreground = self.foreground

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
            }
        )
        if root is not UNSET:
            field_dict["root"] = root
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_client_servers_server_files_copy_many_body_files_item import (
            PostApiClientServersServerFilesCopyManyBodyFilesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = PostApiClientServersServerFilesCopyManyBodyFilesItem.from_dict(files_item_data)

            files.append(files_item)

        root = d.pop("root", UNSET)

        overwrite = d.pop("overwrite", UNSET)

        foreground = d.pop("foreground", UNSET)

        post_api_client_servers_server_files_copy_many_body = cls(
            files=files,
            root=root,
            overwrite=overwrite,
            foreground=foreground,
        )

        post_api_client_servers_server_files_copy_many_body.additional_properties = d
        return post_api_client_servers_server_files_copy_many_body

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
