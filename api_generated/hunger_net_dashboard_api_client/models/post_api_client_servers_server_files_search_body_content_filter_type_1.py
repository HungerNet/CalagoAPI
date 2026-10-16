from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiClientServersServerFilesSearchBodyContentFilterType1")


@_attrs_define
class PostApiClientServersServerFilesSearchBodyContentFilterType1:
    """
    Attributes:
        query (str):
        max_search_size (int):
        include_unmatched (bool):
        case_insensitive (bool):
    """

    query: str
    max_search_size: int
    include_unmatched: bool
    case_insensitive: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        max_search_size = self.max_search_size

        include_unmatched = self.include_unmatched

        case_insensitive = self.case_insensitive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "max_search_size": max_search_size,
                "include_unmatched": include_unmatched,
                "case_insensitive": case_insensitive,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        max_search_size = d.pop("max_search_size")

        include_unmatched = d.pop("include_unmatched")

        case_insensitive = d.pop("case_insensitive")

        post_api_client_servers_server_files_search_body_content_filter_type_1 = cls(
            query=query,
            max_search_size=max_search_size,
            include_unmatched=include_unmatched,
            case_insensitive=case_insensitive,
        )

        post_api_client_servers_server_files_search_body_content_filter_type_1.additional_properties = d
        return post_api_client_servers_server_files_search_body_content_filter_type_1

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
