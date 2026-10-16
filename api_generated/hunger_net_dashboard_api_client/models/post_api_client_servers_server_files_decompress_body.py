from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerFilesDecompressBody")


@_attrs_define
class PostApiClientServersServerFilesDecompressBody:
    """
    Attributes:
        file (str):
        root (str | Unset):  Default: '/'.
        foreground (bool | Unset):
    """

    file: str
    root: str | Unset = "/"
    foreground: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        root = self.root

        foreground = self.foreground

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if root is not UNSET:
            field_dict["root"] = root
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        root = d.pop("root", UNSET)

        foreground = d.pop("foreground", UNSET)

        post_api_client_servers_server_files_decompress_body = cls(
            file=file,
            root=root,
            foreground=foreground,
        )

        post_api_client_servers_server_files_decompress_body.additional_properties = d
        return post_api_client_servers_server_files_decompress_body

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
