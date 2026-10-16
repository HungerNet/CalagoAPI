from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiClientServersServerFilesSearchBodyMatchContextType1")


@_attrs_define
class PostApiClientServersServerFilesSearchBodyMatchContextType1:
    """
    Attributes:
        before (int):
        after (int):
        max_matches (int):
    """

    before: int
    after: int
    max_matches: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        before = self.before

        after = self.after

        max_matches = self.max_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "before": before,
                "after": after,
                "max_matches": max_matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        before = d.pop("before")

        after = d.pop("after")

        max_matches = d.pop("max_matches")

        post_api_client_servers_server_files_search_body_match_context_type_1 = cls(
            before=before,
            after=after,
            max_matches=max_matches,
        )

        post_api_client_servers_server_files_search_body_match_context_type_1.additional_properties = d
        return post_api_client_servers_server_files_search_body_match_context_type_1

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
