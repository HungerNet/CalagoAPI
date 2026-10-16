from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.archive_format import ArchiveFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerFilesCompressBody")


@_attrs_define
class PostApiClientServersServerFilesCompressBody:
    """
    Attributes:
        format_ (ArchiveFormat):
        files (list[str]):
        name (None | str | Unset):
        root (str | Unset):  Default: '/'.
        foreground (bool | Unset):
    """

    format_: ArchiveFormat
    files: list[str]
    name: None | str | Unset = UNSET
    root: str | Unset = "/"
    foreground: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        files = self.files

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        root = self.root

        foreground = self.foreground

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "files": files,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if root is not UNSET:
            field_dict["root"] = root
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = ArchiveFormat(d.pop("format"))

        files = cast(list[str], d.pop("files"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        root = d.pop("root", UNSET)

        foreground = d.pop("foreground", UNSET)

        post_api_client_servers_server_files_compress_body = cls(
            format_=format_,
            files=files,
            name=name,
            root=root,
            foreground=foreground,
        )

        post_api_client_servers_server_files_compress_body.additional_properties = d
        return post_api_client_servers_server_files_compress_body

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
