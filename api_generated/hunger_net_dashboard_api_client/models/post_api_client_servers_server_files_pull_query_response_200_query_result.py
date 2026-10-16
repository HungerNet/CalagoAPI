from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_client_servers_server_files_pull_query_response_200_query_result_headers import (
        PostApiClientServersServerFilesPullQueryResponse200QueryResultHeaders,
    )


T = TypeVar("T", bound="PostApiClientServersServerFilesPullQueryResponse200QueryResult")


@_attrs_define
class PostApiClientServersServerFilesPullQueryResponse200QueryResult:
    """
    Attributes:
        final_url (str):
        headers (PostApiClientServersServerFilesPullQueryResponse200QueryResultHeaders):
        file_name (None | str | Unset):
        file_size (int | None | Unset):
    """

    final_url: str
    headers: PostApiClientServersServerFilesPullQueryResponse200QueryResultHeaders
    file_name: None | str | Unset = UNSET
    file_size: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        final_url = self.final_url

        headers = self.headers.to_dict()

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_size: int | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "final_url": final_url,
                "headers": headers,
            }
        )
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_client_servers_server_files_pull_query_response_200_query_result_headers import (
            PostApiClientServersServerFilesPullQueryResponse200QueryResultHeaders,  # noqa: PLC0415
        )

        d = dict(src_dict)
        final_url = d.pop("final_url")

        headers = PostApiClientServersServerFilesPullQueryResponse200QueryResultHeaders.from_dict(d.pop("headers"))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_file_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        post_api_client_servers_server_files_pull_query_response_200_query_result = cls(
            final_url=final_url,
            headers=headers,
            file_name=file_name,
            file_size=file_size,
        )

        post_api_client_servers_server_files_pull_query_response_200_query_result.additional_properties = d
        return post_api_client_servers_server_files_pull_query_response_200_query_result

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
