from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerFilesCreateSymlinkBody")


@_attrs_define
class PostApiClientServersServerFilesCreateSymlinkBody:
    """
    Attributes:
        link (str):
        target (str):
        root (str | Unset):  Default: '/'.
    """

    link: str
    target: str
    root: str | Unset = "/"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link = self.link

        target = self.target

        root = self.root

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
                "target": target,
            }
        )
        if root is not UNSET:
            field_dict["root"] = root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        link = d.pop("link")

        target = d.pop("target")

        root = d.pop("root", UNSET)

        post_api_client_servers_server_files_create_symlink_body = cls(
            link=link,
            target=target,
            root=root,
        )

        post_api_client_servers_server_files_create_symlink_body.additional_properties = d
        return post_api_client_servers_server_files_create_symlink_body

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
