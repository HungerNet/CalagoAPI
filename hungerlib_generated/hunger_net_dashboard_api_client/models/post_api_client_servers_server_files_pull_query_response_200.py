from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_client_servers_server_files_pull_query_response_200_query_result import (
        PostApiClientServersServerFilesPullQueryResponse200QueryResult,
    )


T = TypeVar("T", bound="PostApiClientServersServerFilesPullQueryResponse200")


@_attrs_define
class PostApiClientServersServerFilesPullQueryResponse200:
    """
    Attributes:
        query_result (PostApiClientServersServerFilesPullQueryResponse200QueryResult):
    """

    query_result: PostApiClientServersServerFilesPullQueryResponse200QueryResult
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_result = self.query_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query_result": query_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_client_servers_server_files_pull_query_response_200_query_result import (
            PostApiClientServersServerFilesPullQueryResponse200QueryResult,  # noqa: PLC0415
        )

        d = dict(src_dict)
        query_result = PostApiClientServersServerFilesPullQueryResponse200QueryResult.from_dict(d.pop("query_result"))

        post_api_client_servers_server_files_pull_query_response_200 = cls(
            query_result=query_result,
        )

        post_api_client_servers_server_files_pull_query_response_200.additional_properties = d
        return post_api_client_servers_server_files_pull_query_response_200

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
