from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseExplorerQueryBody")


@_attrs_define
class PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseExplorerQueryBody:
    """
    Attributes:
        query (str):
        rows (int | Unset):
        read_only (bool | Unset):
    """

    query: str
    rows: int | Unset = UNSET
    read_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        rows = self.rows

        read_only = self.read_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if rows is not UNSET:
            field_dict["rows"] = rows
        if read_only is not UNSET:
            field_dict["read_only"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        rows = d.pop("rows", UNSET)

        read_only = d.pop("read_only", UNSET)

        post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_query_body = (
            cls(
                query=query,
                rows=rows,
                read_only=read_only,
            )
        )

        post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_query_body.additional_properties = d
        return (
            post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_query_body
        )

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
