from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerFilesCopyBody")


@_attrs_define
class PostApiClientServersServerFilesCopyBody:
    """
    Attributes:
        path (str):
        destination (None | str | Unset):
        overwrite (bool | Unset):
        foreground (bool | Unset):
    """

    path: str
    destination: None | str | Unset = UNSET
    overwrite: bool | Unset = UNSET
    foreground: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        destination: None | str | Unset
        if isinstance(self.destination, Unset):
            destination = UNSET
        else:
            destination = self.destination

        overwrite = self.overwrite

        foreground = self.foreground

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if destination is not UNSET:
            field_dict["destination"] = destination
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        def _parse_destination(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination = _parse_destination(d.pop("destination", UNSET))

        overwrite = d.pop("overwrite", UNSET)

        foreground = d.pop("foreground", UNSET)

        post_api_client_servers_server_files_copy_body = cls(
            path=path,
            destination=destination,
            overwrite=overwrite,
            foreground=foreground,
        )

        post_api_client_servers_server_files_copy_body.additional_properties = d
        return post_api_client_servers_server_files_copy_body

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
