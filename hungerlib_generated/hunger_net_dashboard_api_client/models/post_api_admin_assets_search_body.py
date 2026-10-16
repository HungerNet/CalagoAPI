from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminAssetsSearchBody")


@_attrs_define
class PostApiAdminAssetsSearchBody:
    """
    Attributes:
        search (str):
        per_page (int | Unset):
        directory (str | Unset):
    """

    search: str
    per_page: int | Unset = UNSET
    directory: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search = self.search

        per_page = self.per_page

        directory = self.directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "search": search,
            }
        )
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if directory is not UNSET:
            field_dict["directory"] = directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search = d.pop("search")

        per_page = d.pop("per_page", UNSET)

        directory = d.pop("directory", UNSET)

        post_api_admin_assets_search_body = cls(
            search=search,
            per_page=per_page,
            directory=directory,
        )

        post_api_admin_assets_search_body.additional_properties = d
        return post_api_admin_assets_search_body

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
