from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerFilesPullBody")


@_attrs_define
class PostApiClientServersServerFilesPullBody:
    """
    Attributes:
        url (str):
        root (str | Unset):  Default: '/'.
        name (None | str | Unset):
        use_header (bool | Unset):
        foreground (bool | Unset):
    """

    url: str
    root: str | Unset = "/"
    name: None | str | Unset = UNSET
    use_header: bool | Unset = UNSET
    foreground: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        root = self.root

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        use_header = self.use_header

        foreground = self.foreground

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if root is not UNSET:
            field_dict["root"] = root
        if name is not UNSET:
            field_dict["name"] = name
        if use_header is not UNSET:
            field_dict["use_header"] = use_header
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        root = d.pop("root", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        use_header = d.pop("use_header", UNSET)

        foreground = d.pop("foreground", UNSET)

        post_api_client_servers_server_files_pull_body = cls(
            url=url,
            root=root,
            name=name,
            use_header=use_header,
            foreground=foreground,
        )

        post_api_client_servers_server_files_pull_body.additional_properties = d
        return post_api_client_servers_server_files_pull_body

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
