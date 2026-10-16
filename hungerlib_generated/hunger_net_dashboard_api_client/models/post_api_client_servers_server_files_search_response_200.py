from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_matches import ContentMatches
    from ..models.directory_entry import DirectoryEntry


T = TypeVar("T", bound="PostApiClientServersServerFilesSearchResponse200")


@_attrs_define
class PostApiClientServersServerFilesSearchResponse200:
    """
    Attributes:
        entries (list[DirectoryEntry]):
        content_matches (list[ContentMatches] | None | Unset):
    """

    entries: list[DirectoryEntry]
    content_matches: list[ContentMatches] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        content_matches: list[dict[str, Any]] | None | Unset
        if isinstance(self.content_matches, Unset):
            content_matches = UNSET
        elif isinstance(self.content_matches, list):
            content_matches = []
            for content_matches_type_0_item_data in self.content_matches:
                content_matches_type_0_item = content_matches_type_0_item_data.to_dict()
                content_matches.append(content_matches_type_0_item)

        else:
            content_matches = self.content_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
            }
        )
        if content_matches is not UNSET:
            field_dict["content_matches"] = content_matches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_matches import ContentMatches  # noqa: PLC0415
        from ..models.directory_entry import DirectoryEntry  # noqa: PLC0415

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = DirectoryEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        def _parse_content_matches(data: object) -> list[ContentMatches] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_matches_type_0 = []
                _content_matches_type_0 = data
                for content_matches_type_0_item_data in _content_matches_type_0:
                    content_matches_type_0_item = ContentMatches.from_dict(content_matches_type_0_item_data)

                    content_matches_type_0.append(content_matches_type_0_item)

                return content_matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContentMatches] | None | Unset, data)

        content_matches = _parse_content_matches(d.pop("content_matches", UNSET))

        post_api_client_servers_server_files_search_response_200 = cls(
            entries=entries,
            content_matches=content_matches,
        )

        post_api_client_servers_server_files_search_response_200.additional_properties = d
        return post_api_client_servers_server_files_search_response_200

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
