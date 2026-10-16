from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_client_servers_server_files_search_body_content_filter_type_1 import (
        PostApiClientServersServerFilesSearchBodyContentFilterType1,
    )
    from ..models.post_api_client_servers_server_files_search_body_match_context_type_1 import (
        PostApiClientServersServerFilesSearchBodyMatchContextType1,
    )
    from ..models.post_api_client_servers_server_files_search_body_path_filter_type_1 import (
        PostApiClientServersServerFilesSearchBodyPathFilterType1,
    )
    from ..models.post_api_client_servers_server_files_search_body_size_filter_type_1 import (
        PostApiClientServersServerFilesSearchBodySizeFilterType1,
    )


T = TypeVar("T", bound="PostApiClientServersServerFilesSearchBody")


@_attrs_define
class PostApiClientServersServerFilesSearchBody:
    """
    Attributes:
        root (str | Unset):
        path_filter (None | PostApiClientServersServerFilesSearchBodyPathFilterType1 | Unset):
        size_filter (None | PostApiClientServersServerFilesSearchBodySizeFilterType1 | Unset):
        content_filter (None | PostApiClientServersServerFilesSearchBodyContentFilterType1 | Unset):
        match_context (None | PostApiClientServersServerFilesSearchBodyMatchContextType1 | Unset):
    """

    root: str | Unset = UNSET
    path_filter: None | PostApiClientServersServerFilesSearchBodyPathFilterType1 | Unset = UNSET
    size_filter: None | PostApiClientServersServerFilesSearchBodySizeFilterType1 | Unset = UNSET
    content_filter: None | PostApiClientServersServerFilesSearchBodyContentFilterType1 | Unset = UNSET
    match_context: None | PostApiClientServersServerFilesSearchBodyMatchContextType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_api_client_servers_server_files_search_body_content_filter_type_1 import (
            PostApiClientServersServerFilesSearchBodyContentFilterType1,  # noqa: PLC0415
        )
        from ..models.post_api_client_servers_server_files_search_body_match_context_type_1 import (
            PostApiClientServersServerFilesSearchBodyMatchContextType1,  # noqa: PLC0415
        )
        from ..models.post_api_client_servers_server_files_search_body_path_filter_type_1 import (
            PostApiClientServersServerFilesSearchBodyPathFilterType1,  # noqa: PLC0415
        )
        from ..models.post_api_client_servers_server_files_search_body_size_filter_type_1 import (
            PostApiClientServersServerFilesSearchBodySizeFilterType1,  # noqa: PLC0415
        )

        root = self.root

        path_filter: dict[str, Any] | None | Unset
        if isinstance(self.path_filter, Unset):
            path_filter = UNSET
        elif isinstance(self.path_filter, PostApiClientServersServerFilesSearchBodyPathFilterType1):
            path_filter = self.path_filter.to_dict()
        else:
            path_filter = self.path_filter

        size_filter: dict[str, Any] | None | Unset
        if isinstance(self.size_filter, Unset):
            size_filter = UNSET
        elif isinstance(self.size_filter, PostApiClientServersServerFilesSearchBodySizeFilterType1):
            size_filter = self.size_filter.to_dict()
        else:
            size_filter = self.size_filter

        content_filter: dict[str, Any] | None | Unset
        if isinstance(self.content_filter, Unset):
            content_filter = UNSET
        elif isinstance(self.content_filter, PostApiClientServersServerFilesSearchBodyContentFilterType1):
            content_filter = self.content_filter.to_dict()
        else:
            content_filter = self.content_filter

        match_context: dict[str, Any] | None | Unset
        if isinstance(self.match_context, Unset):
            match_context = UNSET
        elif isinstance(self.match_context, PostApiClientServersServerFilesSearchBodyMatchContextType1):
            match_context = self.match_context.to_dict()
        else:
            match_context = self.match_context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if root is not UNSET:
            field_dict["root"] = root
        if path_filter is not UNSET:
            field_dict["path_filter"] = path_filter
        if size_filter is not UNSET:
            field_dict["size_filter"] = size_filter
        if content_filter is not UNSET:
            field_dict["content_filter"] = content_filter
        if match_context is not UNSET:
            field_dict["match_context"] = match_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_client_servers_server_files_search_body_content_filter_type_1 import (
            PostApiClientServersServerFilesSearchBodyContentFilterType1,  # noqa: PLC0415
        )
        from ..models.post_api_client_servers_server_files_search_body_match_context_type_1 import (
            PostApiClientServersServerFilesSearchBodyMatchContextType1,  # noqa: PLC0415
        )
        from ..models.post_api_client_servers_server_files_search_body_path_filter_type_1 import (
            PostApiClientServersServerFilesSearchBodyPathFilterType1,  # noqa: PLC0415
        )
        from ..models.post_api_client_servers_server_files_search_body_size_filter_type_1 import (
            PostApiClientServersServerFilesSearchBodySizeFilterType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        root = d.pop("root", UNSET)

        def _parse_path_filter(data: object) -> None | PostApiClientServersServerFilesSearchBodyPathFilterType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                path_filter_type_1 = PostApiClientServersServerFilesSearchBodyPathFilterType1.from_dict(data)

                return path_filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostApiClientServersServerFilesSearchBodyPathFilterType1 | Unset, data)

        path_filter = _parse_path_filter(d.pop("path_filter", UNSET))

        def _parse_size_filter(data: object) -> None | PostApiClientServersServerFilesSearchBodySizeFilterType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                size_filter_type_1 = PostApiClientServersServerFilesSearchBodySizeFilterType1.from_dict(data)

                return size_filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostApiClientServersServerFilesSearchBodySizeFilterType1 | Unset, data)

        size_filter = _parse_size_filter(d.pop("size_filter", UNSET))

        def _parse_content_filter(
            data: object,
        ) -> None | PostApiClientServersServerFilesSearchBodyContentFilterType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_filter_type_1 = PostApiClientServersServerFilesSearchBodyContentFilterType1.from_dict(data)

                return content_filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostApiClientServersServerFilesSearchBodyContentFilterType1 | Unset, data)

        content_filter = _parse_content_filter(d.pop("content_filter", UNSET))

        def _parse_match_context(
            data: object,
        ) -> None | PostApiClientServersServerFilesSearchBodyMatchContextType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                match_context_type_1 = PostApiClientServersServerFilesSearchBodyMatchContextType1.from_dict(data)

                return match_context_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostApiClientServersServerFilesSearchBodyMatchContextType1 | Unset, data)

        match_context = _parse_match_context(d.pop("match_context", UNSET))

        post_api_client_servers_server_files_search_body = cls(
            root=root,
            path_filter=path_filter,
            size_filter=size_filter,
            content_filter=content_filter,
            match_context=match_context,
        )

        post_api_client_servers_server_files_search_body.additional_properties = d
        return post_api_client_servers_server_files_search_body

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
